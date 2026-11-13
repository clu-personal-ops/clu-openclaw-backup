import assert from 'node:assert/strict';
import {observe,transition,syncReminder,run} from './usage-monitor.mjs';
const now=Date.now(),reset=now+3600000;
const raw=(short=0,week=56)=>({updatedAt:now,providers:[{provider:'openai',windows:[{label:'5h',usedPercent:short,resetAt:reset},{label:'Week',usedPercent:week,resetAt:reset+86400000}]}]});
let checks=0;function check(name,fn){fn();checks++;console.log('PASS '+name);}
check('available is silent initially and repeatedly',()=>{let x=transition({},observe(raw(),now),{now});assert.deepEqual(x.messages,[]);assert.deepEqual(transition(x.state,observe(raw(),now),{now}).messages,[]);});
const cooldown=transition({},observe(raw(100),now),{now});
check('cooldown exact recovery and weekly remainder',()=>{assert.match(cooldown.messages[0],new RegExp(new Date(reset).toISOString().replace(/[.*+?^${}()|[\]\\]/g,'\\$&')));assert.match(cooldown.messages[0],/44%/);});
check('hourly cooldown dedup despite weekly consumption',()=>{assert.deepEqual(transition(cooldown.state,observe(raw(100,60),now),{now}).messages,[]);});
check('early manual recovery once',()=>{const recovered=transition(cooldown.state,observe(raw(0),now),{now});assert.match(recovered.messages[0],/available again/);assert.deepEqual(transition(recovered.state,observe(raw(),now),{now}).messages,[]);});
check('unknown reset never guessed',()=>{let r=raw(100);delete r.providers[0].windows[0].resetAt;assert.match(transition({},observe(r,now),{now}).messages[0],/not available/);});
check('both exhausted use latest reset',()=>{assert.equal(observe(raw(100,100),now).resetAt,reset+86400000);});
check('expired exhausted time not called restored',()=>{const x=transition(cooldown.state,observe({...raw(100),updatedAt:reset+1},reset+1),{now:reset+1,expired:true});assert.equal(x.state.phase,'cooldown');assert.equal(x.state.resetAt,null);assert.doesNotMatch(x.messages.join(' '),/available again/);});
check('partial, malformed, error and stale snapshots rejected',()=>{for(const r of [{}, {...raw(),updatedAt:now-100000}, {...raw(),providers:[]}, {updatedAt:now,providers:[{provider:'openai',error:'Timeout'}]}, {updatedAt:now,providers:[{provider:'openai',windows:[{label:'5h',usedPercent:0}]}]},raw(NaN),raw(-1),raw(101)]) assert.throws(()=>observe(r,now));});
check('retrieval failure reported once, cooldown remembered, retrieval recovery reported',()=>{const x=transition(cooldown.state,{error:true},{now});assert.equal(x.messages.length,1);assert.equal(x.state.phase,'cooldown');assert.equal(x.state.resetAt,reset);const y=transition(x.state,{error:true},{now});assert.equal(y.messages.length,0);assert.match(transition(y.state,observe(raw(),now),{now}).messages.join(' '),/available again/);});
const reminder={id:'r1',declarationKey:'openai-usage-expiration:0691547a-cc3e-4b7a-a928-f37ea96800f9',enabled:true,schedule:{kind:'at',at:new Date(reset).toISOString()}};
function scheduler(jobs=[]){const calls=[];return {calls,call(args){calls.push(args);if(args[1]==='list')return {jobs};if(args[1]==='add')return {created:true,job:{id:'created'}};return {ok:true};}};}
check('one expiration scheduled, native delivery exact route',()=>{const f=scheduler();const s=syncReminder(cooldown.state,f.call,now);assert.equal(s.reminderId,'created');const a=f.calls.find(a=>a[1]==='add');assert(a.includes('--delete-after-run'));assert(a.includes('telegram:9013562211'));assert(a.includes('--command-argv'));assert.equal(a[a.indexOf('--at')+1],new Date(reset).toISOString());});
check('existing identical reminder not duplicated',()=>{const f=scheduler([reminder]);assert.equal(syncReminder(cooldown.state,f.call,now).reminderId,'r1');assert.equal(f.calls.length,1);});
check('early recovery cancels outdated reminder',()=>{const f=scheduler([reminder]);syncReminder({phase:'available'},f.call,now);assert.deepEqual(f.calls.at(-1),['automations','rm','r1']);});
check('reset change replaces one-shot, no duplicate',()=>{const f=scheduler([reminder]);syncReminder({...cooldown.state,resetAt:reset+10000},f.call,now);assert.deepEqual(f.calls.map(a=>a[1]),['list','rm','add']);});
check('running expiration does not cancel its own native notification',()=>{const f=scheduler([reminder]);syncReminder({phase:'available'},f.call,reset+1,reset);assert.equal(f.calls.length,1);});
check('executing old expiration can schedule new reset under a new key',()=>{const f=scheduler([reminder]);syncReminder({...cooldown.state,resetAt:reset+10000},f.call,now,reset);assert.deepEqual(f.calls.map(a=>a[1]),['list','add']);const a=f.calls[1];assert.equal(a[a.indexOf('--declaration-key')+1],reminder.declarationKey+':'+(reset+10000));});
let fetched=false;
assert.equal(await run({expiration:reset,load:()=>({phase:'available'}),fetch:async()=>{fetched=true;}}),'NO_REPLY');assert.equal(fetched,false);console.log('PASS stale queued expiration silent');checks++;
let saved;
const output=await run({load:()=>cooldown.state,save:s=>saved=s,fetch:async()=>observe(raw(),now),sync:s=>s,now:()=>now});assert.match(output,/available again/);assert.equal(saved.phase,'available');console.log('PASS end-to-end reducer run, no external notification');checks++;
let expirationSaved;const expirationResult=await run({expiration:reset,load:()=>cooldown.state,save:s=>expirationSaved=s,fetch:async minimum=>{assert.equal(minimum,reset);return observe({...raw(),updatedAt:reset+1},reset+1);},sync:s=>s,now:()=>reset+1});assert.match(expirationResult,/available again/);assert.equal(expirationSaved.phase,'available');console.log('PASS expiration verifies actual restoration');checks++;
console.log(`${checks} scenarios passed; scheduler fixtures only, no fake notifications.`);
