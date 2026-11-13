import fs from 'node:fs';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
export const ROOT='/Users/clu/.openclaw/workspace';
export const JOB='0691547a-cc3e-4b7a-a928-f37ea96800f9';
const NODE='/Users/clu/.openclaw/tools/node-v24.22.1/bin/node';
const CLI='/Users/clu/.openclaw/tools/node-v24.22.1/lib/node_modules/openclaw/openclaw.mjs';
const SELF=fileURLToPath(import.meta.url);
const STATE=ROOT+'/state/usage-monitor.json';
const REMINDER='openai-usage-expiration:'+JOB;
export function cli(args){return JSON.parse(execFileSync(NODE,[CLI,...args],{encoding:'utf8',timeout:35000,maxBuffer:1024*1024,stdio:['ignore','pipe','pipe']}));}
export function observe(raw,now=Date.now(),minimum=now-90000){
 if(!raw || !Number.isFinite(raw.updatedAt) || raw.updatedAt<minimum || raw.updatedAt>now+5000) throw Error('Provider snapshot is missing or stale');
 const p=raw.providers?.find(p=>p.provider==='openai');
 if(!p || p.error || !Array.isArray(p.windows) || !p.windows.length) throw Error('OpenAI usage retrieval failed');
 if(p.windows.some(w=>typeof w.usedPercent!=='number'||!Number.isFinite(w.usedPercent)||w.usedPercent<0||w.usedPercent>100||typeof w.label!=='string')) throw Error('Malformed provider usage windows');
 // Require both normal Codex windows: a partial response cannot establish availability.
 const week=p.windows.filter(w=>/^week$/i.test(w.label));
 const short=p.windows.filter(w=>/^\d+h$/.test(w.label));
 if(week.length!==1||short.length!==1) throw Error('Expected short-term and weekly usage windows are unavailable');
 const exhausted=p.windows.filter(w=>w.usedPercent>=100);
 const known=exhausted.length>0 && exhausted.every(w=>Number.isFinite(w.resetAt)&&w.resetAt>now);
 return {phase:exhausted.length?'cooldown':'available',resetAt:known?Math.max(...exhausted.map(w=>w.resetAt)):null,weeklyRemaining:100-week[0].usedPercent,updatedAt:raw.updatedAt};
}
const when=t=>new Date(t).toLocaleString('en-US',{timeZone:'America/New_York',year:'numeric',month:'short',day:'numeric',hour:'2-digit',minute:'2-digit',second:'2-digit',timeZoneName:'short'})+' ('+new Date(t).toISOString()+')';
export function transition(previous,sample,{expired=false,now=Date.now()}={}){
 const s={...previous,lastCheckedAt:now}; const messages=[];
 if(sample.error){
  if(!s.retrievalError) messages.push('OpenAI usage check failed: reliable current usage could not be retrieved. Availability, recovery time and weekly remaining are unknown; no reset is assumed.');
  s.retrievalError=true; return {state:s,messages};
 }
 if(s.retrievalError) messages.push('OpenAI usage retrieval is working again.');
 s.retrievalError=false;
 const changed=s.phase!==sample.phase||s.resetAt!==sample.resetAt;
 if(sample.phase==='cooldown' && changed) messages.push('OpenAI usage is in cooldown. '+(sample.resetAt?'Provider-reported recovery time: '+when(sample.resetAt)+'.':'Exact recovery time is not available.')+' Weekly usage remaining: '+sample.weeklyRemaining+'%.');
 if(sample.phase==='available'&&s.phase==='cooldown') messages.push('OpenAI usage is available again (including an early/manual reset if applicable). Weekly usage remaining: '+sample.weeklyRemaining+'%.');
 if(expired&&sample.phase==='cooldown'&&!changed) messages.push('The expected OpenAI cooldown expiration has arrived, but the provider still reports exhausted usage. Recovery is not yet confirmed. Weekly usage remaining: '+sample.weeklyRemaining+'%.');
 Object.assign(s,sample); return {state:s,messages};
}
export async function fetchUsage(minimum,call=cli){
 const started=Date.now();
 while(true){
  try {const raw=call(['gateway','call','usage.status','--json']); return observe(raw,Date.now(),Math.max(Date.now()-90000,minimum||0));}
  catch(e){if(Date.now()-started>=70000) return {error:true};}
  await new Promise(r=>setTimeout(r,1500));
 }
}
export function syncReminder(state,call=cli,now=Date.now(),runningExpiration=null){
 const jobs=call(['automations','list','--all','--json']).jobs.filter(j=>j.declarationKey===REMINDER || j.declarationKey?.startsWith(REMINDER+':'));
 const desired=state.phase==='cooldown'&&state.resetAt>now ? state.resetAt : null;
 let keep=jobs.find(j=>j.enabled&&Date.parse(j.schedule?.at)===desired);
 for(const j of jobs) if(j!==keep && !(runningExpiration && Date.parse(j.schedule?.at)===runningExpiration)) call(['automations','rm',j.id]);
 if(desired&&!keep){
  keep=call(['automations','add','--name','openai-usage-expiration','--declaration-key',REMINDER+':'+desired,'--at',new Date(desired).toISOString(),'--delete-after-run','--session','isolated','--command-argv',JSON.stringify([NODE,SELF,'--expiration',String(desired)]),'--timeout-seconds','120','--announce','--channel','telegram','--to','telegram:9013562211','--account','default','--no-best-effort-deliver','--json']);
  keep=keep.job??keep;
  if(!keep.id) throw Error('Expiration scheduler returned no job identity');
 }
 return {...state,reminderId:keep?.id??null};
}
export async function run({expiration=null,load,save,fetch=fetchUsage,sync=syncReminder,now=()=>Date.now()}={}){
 const previous=load();
 // An old one-shot queued before a manual reset/reschedule must not announce.
 if(expiration && (previous.phase!=='cooldown'||previous.resetAt!==expiration)) return 'NO_REPLY';
 const sample=await fetch(expiration||0);
 const result=transition(previous,sample,{expired:!!expiration,now:now()});
 // A failed retrieval preserves the last confirmed cooldown and its reminder.
 let state=result.state;
 try {state=sync(state,undefined,now(),expiration);}catch(e){throw Error('Usage monitor could not synchronize its expiration reminder');}
 save(state);
 return result.messages.join('\n\n')||'NO_REPLY';
}
if(process.argv[1]===SELF){
 let locked=false;
 try{
  fs.mkdirSync(ROOT+'/state',{recursive:true});
  try{fs.mkdirSync(STATE+'.lock');locked=true;fs.writeFileSync(STATE+'.lock/pid',String(process.pid));}
  catch(e){
   const pid=Number(fs.readFileSync(STATE+'.lock/pid','utf8'));let alive=true;try{process.kill(pid,0);}catch{alive=false;}
   if(alive){console.log('NO_REPLY');process.exit(0);}
   fs.rmSync(STATE+'.lock',{recursive:true});fs.mkdirSync(STATE+'.lock');locked=true;fs.writeFileSync(STATE+'.lock/pid',String(process.pid));
  }
  const expiration=process.argv[2]==='--expiration'?Number(process.argv[3]):null;
  const output=await run({expiration,load:()=>fs.existsSync(STATE)?JSON.parse(fs.readFileSync(STATE,'utf8')):{},save:s=>{fs.writeFileSync(STATE+'.tmp',JSON.stringify(s,null,2)+'\n',{mode:0o600});fs.renameSync(STATE+'.tmp',STATE);}});
  console.log(output);
 }catch(e){console.error('Usage monitor failed: reliable usage check or reminder scheduling unavailable. Inspect job history; no availability was assumed.');process.exitCode=1;}
 finally{if(locked)fs.rmSync(STATE+'.lock',{recursive:true,force:true});}
}
