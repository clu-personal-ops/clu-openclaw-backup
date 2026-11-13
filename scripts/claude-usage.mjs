import fs from 'node:fs';
import {pathToFileURL} from 'node:url';
const DIST='/Users/clu/.openclaw/tools/node-v24.22.1/lib/node_modules/openclaw/dist';
export function parseClaudeUsage(raw,now=Date.now()){
 const entries=[['5h',raw?.five_hour],['Week',raw?.seven_day]];
 for(const [label,value] of [['Sonnet',raw?.seven_day_sonnet]]) if(value!=null) entries.push([label,value]);
 for(const limit of Array.isArray(raw?.limits)?raw.limits:[]){
  const model=limit?.scope?.model;
  if(limit?.is_active===false||!model) continue;
  const name=String(model.id??model.display_name??'');
  if(/sonnet/i.test(name)) entries.push([name,{utilization:limit.percent,resets_at:limit.resets_at}]);
 }
 const windows=entries.map(([label,value])=>{
  if(typeof value?.utilization!=='number'||!Number.isFinite(value.utilization)||value.utilization<0||value.utilization>100) throw Error('Malformed Claude quota');
  const resetAt=typeof value.resets_at==='string'?Date.parse(value.resets_at):NaN;
  return {label,usedPercent:value.utilization,resetAt:Number.isFinite(resetAt)?resetAt:null};
 });
 const exhausted=windows.filter(w=>w.usedPercent===100);
 return {phase:exhausted.length?'cooldown':'available',weeklyRemaining:100-windows.find(w=>w.label==='Week').usedPercent,shortRemaining:100-windows[0].usedPercent,resetAt:exhausted.length&&exhausted.every(w=>w.resetAt>now)?Math.max(...exhausted.map(w=>w.resetAt)):null,weeklyResetAt:windows.find(w=>w.label==='Week').resetAt,updatedAt:now};
}
export async function fetchClaudeUsage(){
 try{
  const names=fs.readdirSync(DIST).filter(n=>/^provider-auth-[A-Za-z0-9_-]{8}\.mjs$/.test(n));
  if(names.length!==1) throw Error('Native credential reader unavailable');
  const {t:readCredentials}=await import(pathToFileURL(DIST+'/'+names[0]).href);
  const credential=readCredentials({allowKeychainPrompt:false})??readCredentials({tryKeychainWithoutPrompt:true});
  const token=credential?.access??credential?.token;
  if(!token||credential.expires<=Date.now()) return {error:true,reason:'credential_unavailable_or_expired'};
  const response=await fetch('https://api.anthropic.com/api/oauth/usage',{headers:{Authorization:`Bearer ${token}`,'User-Agent':'openclaw',Accept:'application/json','anthropic-version':'2023-06-01','anthropic-beta':'oauth-2025-04-20'},signal:AbortSignal.timeout(12000)});
  if(!response.ok) return {error:true,reason:'http_'+response.status};
  return parseClaudeUsage(await response.json());
 }catch{return {error:true,reason:'retrieval_or_schema_failure'};}
}
