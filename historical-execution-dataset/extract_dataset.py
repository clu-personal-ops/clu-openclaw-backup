#!/usr/bin/env python3
"""Read-only, metadata-only historical extractor. Python 3 + zstd CLI; no network."""
import argparse, collections, csv, datetime as dt, glob, hashlib, io, json, os, pathlib, re, sqlite3, subprocess, tarfile, tempfile
from zoneinfo import ZoneInfo
P=argparse.ArgumentParser();P.add_argument('--home',default=str(pathlib.Path.home()));P.add_argument('--output',default=str(pathlib.Path(__file__).resolve().parent));P.add_argument('--cutoff');P.add_argument('--validate-only',action='store_true');args=P.parse_args()
HOME=pathlib.Path(args.home);OUT=pathlib.Path(args.output);OUT.mkdir(parents=True,exist_ok=True)
UTC=dt.timezone.utc;LOCAL=ZoneInfo('America/New_York');CUTOFF=args.cutoff or dt.datetime.now(UTC).isoformat();WARN=[];SOURCES={};COUNTS=collections.Counter();RUNS={};ATT={};EVENTS={};TRACE=[];TRANS=[];ROLLOUT=[];DBS=[];TURN_RUN={};THREAD_SESSION={};CALL_RUN={};SESSION_KEYS={};CHILD_LINK=[];MODEL_RESPONSE={};SEEN_EVENTS=set();SEEN_ROLLOUT=set();METRICS=collections.Counter();LOG_RETRIES={};CRON_MAP={};ACCEPTANCE_KEYS=collections.Counter()
RUN_COLS='codex_version error_code error_type task_id task_type task_completion_status task_acceptance_criteria_recorded task_outcome_independently_verifiable task_verification_source_reference execution_outcome_evidence model_version model_quantization model_api configured_model_id configured_provider run_timeout_seconds fast_mode thinking_level reasoning_level harness_name harness_version node_version os_platform os_arch os_release configured_max_concurrent configured_subagent_max_concurrent recorded_numeric_metrics_json run_id parent_run_id session_id run_type start_time_utc end_time_utc duration_ms model_id provider status openclaw_version source_reference source_system original_status status_conflict observed_model_ids time_basis duration_basis lifecycle_scope tool_use_count input_tokens output_tokens cache_read_tokens cache_write_tokens reasoning_tokens total_tokens cost_total compaction_count time_to_first_token_ms'.split()
ATT_COLS='codex_version task_id parent_attempt_id task_completion_status source_selected_logging model_version model_quantization model_api context_utilization max_output_tokens temperature top_p top_k seed stream recorded_numeric_metrics_json attempt_id run_id session_id timestamp_utc operation_type tool_name model_id provider status error_code error_type duration_ms input_tokens output_tokens context_tokens context_limit_tokens concurrent_executions source_reference source_system original_status status_conflict linkage_basis duration_basis population source_failure_only cache_read_tokens cache_write_tokens reasoning_tokens total_tokens cost_total exit_code retry_index request_body_bytes response_body_bytes prompt_chars observed_prompt_chars time_to_first_token_ms tokens_per_second'.split()
def dump(p,o):
 with open(p,'w') as f:json.dump(o,f,indent=2,sort_keys=True)
 os.chmod(p,0o600)
def hid(kind,v):return kind+'_'+hashlib.sha256((kind+'\0'+str(v)).encode()).hexdigest()[:24] if v is not None and v!='' else None
def token(v):
 if isinstance(v,(int,float)):return str(v)
 return v if isinstance(v,str) and len(v)<=160 and re.fullmatch(r'[A-Za-z0-9_.:/+ -]+',v) and '@' not in v and not re.search(r'(?:sk-|Bearer |token=|key=)',v,re.I) else None
def num(v):return v if isinstance(v,(int,float)) and not isinstance(v,bool) and v>=0 else None
def timestamp(v,local=False):
 if v is None or v=='':return None
 try:
  if isinstance(v,(int,float)):
   if v<1000000000:return None
   t=dt.datetime.fromtimestamp(v/(1000 if v>100000000000 else 1),UTC)
  else:
   t=dt.datetime.fromisoformat(str(v).replace('Z','+00:00'))
   if t.tzinfo is None:t=t.replace(tzinfo=LOCAL if local else UTC)
   t=t.astimezone(UTC)
  return t.isoformat(timespec='milliseconds').replace('+00:00','Z')
 except (ValueError,OverflowError,TypeError):return None
CUT=timestamp(CUTOFF)
def eligible(t):return not t or t<=CUT
def msdiff(a,b):
 if not a or not b:return None
 x=round((dt.datetime.fromisoformat(b.replace('Z','+00:00'))-dt.datetime.fromisoformat(a.replace('Z','+00:00'))).total_seconds()*1000)
 return x if x>=0 else None
NORM={'success':'success','succeeded':'success','completed':'success','complete':'success','ok':'success','done':'success','failure':'failure','failed':'failure','errored':'failure','error':'failure','blocked':'failure','timeout':'timeout','timed_out':'timeout','timedout':'timeout','cancelled':'cancelled','canceled':'cancelled','killed':'cancelled','aborted':'interrupted','interrupted':'interrupted','inprogress':'unknown','running':'unknown','started':'unknown','pending':'unknown','skipped':'unknown','candidate_failed':'failure','candidate_succeeded':'success'}
def norm(x):return NORM.get(str(x).lower(),'unknown')
def source(k,path,kind,**kw):
 if k not in SOURCES:SOURCES[k]={'path':str(path).replace(str(HOME),'~'),'kind':kind,'records_read':0,'first_timestamp_utc':None,'last_timestamp_utc':None,**kw}
 return k
def observed(ref,t=None):
 k=ref.split(':',1)[0]
 if k not in SOURCES:return
 s=SOURCES[k];s['records_read']+=1
 if t and eligible(t):s['first_timestamp_utc']=min(t,s['first_timestamp_utc'] or t);s['last_timestamp_utc']=max(t,s['last_timestamp_utc'] or t)
def refadd(o,ref):o.setdefault('_refs',set()).add(ref)
def setstatus(o,s,ref,priority=1):
 if s is None:return
 safe=token(s)
 if safe:o.setdefault('_original',set()).add(ref.split(':')[0]+'='+safe)
 n=norm(s)
 if n!='unknown':
  o.setdefault('_statuses',set()).add(n)
  if priority>=o.get('_status_priority',-1):o['status']=n;o['_status_priority']=priority
 o.setdefault('status','unknown')
def run(raw,ref,**kw):
 if raw is None:return None
 rid=hid('run',raw);o=RUNS.setdefault(rid,{'run_id':rid,'status':'unknown','run_type':'agent','task_completion_status':'unknown','task_outcome_independently_verifiable':'unknown','_raw':raw})
 refadd(o,ref)
 for k,v in kw.items():
  if v is None:continue
  if k in ['model_id','provider']:
   v=token(v)
   if v:o.setdefault('_'+k,set()).add(v)
  elif k in ['start_time_utc','end_time_utc']:
   if eligible(v):
    if k=='start_time_utc':o[k]=min(v,o.get(k) or v)
    else:o[k]=max(v,o.get(k) or v)
  elif k not in o or o[k] in [None,'agent','unknown']:o[k]=v
 return o
def attempt(raw,ref,**kw):
 aid=hid('attempt',raw);o=ATT.setdefault(aid,{'attempt_id':aid,'status':'unknown','population':'openclaw_observed','source_failure_only':0,'source_selected_logging':0,'task_completion_status':'unknown'});refadd(o,ref)
 for k,v in kw.items():
  if v is not None and (k not in o or o[k] is None or k in ['status','population','linkage_basis','source_failure_only','source_selected_logging']):o[k]=v
 return o
def cdb(path,immutable=False):
 c=sqlite3.connect('file:'+str(path)+'?mode=ro'+('&immutable=1' if immutable else ''),uri=True);c.row_factory=sqlite3.Row;c.execute('PRAGMA query_only=ON');c.execute('BEGIN');return c
def tables(c):return {r[0] for r in c.execute("select name from sqlite_master where type='table'")}
def rows(c,t):return (dict(r) for r in c.execute('select * from "'+t+'"'))
def decode(b):return subprocess.run(['zstd','-dc'],input=b,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True).stdout

def numeric_tree(o,prefix='',depth=0):
 if depth>4 or not isinstance(o,dict):return {}
 out={}
 for k,v in o.items():
  if not re.fullmatch(r'[A-Za-z][A-Za-z0-9_.]{0,60}',str(k)):continue
  name=prefix+str(k)
  if isinstance(v,(int,float)) and not isinstance(v,bool):out[name]=v
  elif isinstance(v,dict):out.update(numeric_tree(v,name+'.',depth+1))
 return out

def record_metrics(target,data,fields):
 out=json.loads(target.get('recorded_numeric_metrics_json') or '{}')
 for k in fields:
  v=data.get(k)
  if isinstance(v,(int,float)) and not isinstance(v,bool):out[k]=v
  elif isinstance(v,dict):out.update(numeric_tree(v,k+'.'))
 if out:target['recorded_numeric_metrics_json']=json.dumps(out,sort_keys=True,separators=(',',':'))

def acceptance_presence(target,data):
 # Criterion presence only. Runtime success or self-report never verifies task success.
 if not isinstance(data,dict):return
 for k,v in data.items():
  if k in ['acceptanceCriteria','acceptance_criteria','completionCriteria','completion_criteria'] and v:
   target['task_acceptance_criteria_recorded']=1;ACCEPTANCE_KEYS[k]+=1
  if isinstance(v,dict) and k in ['verification','acceptance','task','detail','criteria']:acceptance_presence(target,v)

def add_event(o,sid,ref,trace=False):
 t=timestamp(o.get('ts') or o.get('timestamp'));observed(ref,t)
 if not eligible(t):return
 if trace:TRACE.append((o,ref));return
 key=(sid,o.get('id') or hashlib.sha256(json.dumps(o,sort_keys=True).encode()).hexdigest())
 if key in SEEN_EVENTS:COUNTS['deduplicated_transcript_events']+=1;return
 SEEN_EVENTS.add(key);TRANS.append((sid,o,ref))

def dbload(path,key,immutable=False):
 try:
  c=cdb(path,immutable);ts=tables(c)
 except sqlite3.Error as e:WARN.append({'source':key,'limitation':'database_unreadable','error_type':type(e).__name__});return
 source(key,path,'sqlite',tables_present=sorted(t for t in ts if any(z in t for z in ['run','goal','audit','trajectory','transcript','thread_turn','thread_item'])))
 if 'task_runs' in ts:
  for q in rows(c,'task_runs'):
   raw=q.get('run_id')
   if isinstance(raw,str) and raw.startswith('cron:'):
    parts=raw.split(':')
    if len(parts)==4:CRON_MAP[parts[-1]]=raw
 if 'audit_events' in ts:
  for r in rows(c,'audit_events'):
   t=timestamp(r['occurred_at']);ref=f"{key}:audit_events:sequence={r['sequence']}";observed(ref,t)
   if not eligible(t):continue
   rid=r.get('run_id');sid=r.get('session_id');kind=r.get('kind');a=r.get('action','');status=r.get('status')
   if kind=='agent_run' and rid:
    rr=run(rid,ref,session_id=hid('session',sid),source_system='openclaw',**({'start_time_utc':t} if a.endswith('started') else {'end_time_utc':t,'duration_ms':num(r.get('duration_ms'))}))
    rr['time_basis']='audit_lifecycle';setstatus(rr,status,ref,5)
   if kind=='tool_action' and r.get('tool_call_id'):
    call=r['tool_call_id'];CALL_RUN[call]=rid
    if rid:run(rid,ref,session_id=hid('session',sid),source_system='openclaw')
    ar=attempt('tool:'+call,ref,run_id=hid('run',rid),session_id=hid('session',sid),timestamp_utc=t,operation_type='tool',tool_name=token(r.get('tool_name')),source_system='openclaw',linkage_basis='explicit_tool_call_id',duration_ms=num(r.get('duration_ms')),error_code=token(r.get('error_code')))
    if a.endswith('started'):ar['timestamp_utc']=t;ar['_start']=t
    else:ar['_end']=t;setstatus(ar,status,ref,5)
 if 'task_runs' in ts:
  for r in rows(c,'task_runs'):
   raw=r.get('run_id') or 'task:'+r['task_id'];ref=f"{key}:task_runs:task={hid('task',r['task_id'])}";t=timestamp(r.get('started_at'));observed(ref,t)
   if not eligible(t):continue
   rr=run(raw,ref,run_type='scheduled_job' if r.get('runtime')=='cron' else 'subagent',start_time_utc=t,end_time_utc=timestamp(r.get('ended_at')),parent_run_id=hid('run','task:'+r['parent_task_id']) if r.get('parent_task_id') else None,tool_use_count=num(r.get('tool_use_count')),task_id=hid('task',r['task_id']),task_type=token(r.get('task_kind')),source_system='openclaw');setstatus(rr,r.get('status'),ref,4)
   try:detail=json.loads(r.get('detail_json') or '{}');acceptance_presence(rr,detail);record_metrics(rr,detail,['durationMs','runAtMs'])
   except ValueError:pass
 if 'cron_run_receipts' in ts:
  for r in rows(c,'cron_run_receipts'):
   raw=CRON_MAP.get(r['receipt_id']) or r.get('request_run_id') or 'cron_receipt:'+r['receipt_id'];ref=f"{key}:cron_run_receipts:receipt={hid('receipt',r['receipt_id'])}";t=timestamp(r.get('started_at_ms'));observed(ref,t)
   if not eligible(t):continue
   rr=run(raw,ref,run_type='scheduled_job',start_time_utc=t,end_time_utc=timestamp(r.get('finished_at_ms')),source_system='openclaw');setstatus(rr,r.get('status'),ref,3)
 if 'subagent_runs' in ts:
  for r in rows(c,'subagent_runs'):
   p=json.loads(r['payload_json']);ex=p.get('execution',{});out=ex.get('outcome') or {};ref=f"{key}:subagent_runs:run={hid('run',r['run_id'])}";t=timestamp(ex.get('startedAt') or p.get('sessionStartedAt'));observed(ref,t)
   if not eligible(t):continue
   sid=(p.get('childSessionIdentity') or {}).get('sessionId');rr=run(r['run_id'],ref,run_type='subagent',session_id=hid('session',sid),start_time_utc=t,end_time_utc=timestamp(ex.get('endedAt') or out.get('endedAt')),duration_ms=num(out.get('elapsedMs')),source_system='openclaw',task_id=hid('task',p.get('taskRunId')),configured_model_id=token(p.get('model')),run_timeout_seconds=num(p.get('runTimeoutSeconds')));setstatus(rr,out.get('status') or ex.get('status'),ref,6)
   if p.get('childSessionKey'):SESSION_KEYS[p['childSessionKey']]=sid
 if 'message_tool_run_outcomes' in ts:
  for r in rows(c,'message_tool_run_outcomes'):
   ref=f"{key}:message_tool_run_outcomes:id={r['id']}";t=timestamp(r['occurred_at']);observed(ref,t)
   if not eligible(t):continue
   rr=run(r['run_id'],ref,model_id=r.get('model'),provider=r.get('provider'),source_system='openclaw');setstatus(rr,r.get('run_status'),ref,3)
 if 'session_windows' in ts:
  for r in rows(c,'session_windows'):
   SESSION_KEYS[r['session_key']]=r['session_id']
   # Windows are session containers, not independently counted when runs exist.
 if 'trajectory_runtime_events' in ts:
  for r in rows(c,'trajectory_runtime_events'):
   try:o=json.loads(r['event_json']);add_event(o,r['session_id'],f"{key}:trajectory_runtime_events:session={hid('session',r['session_id'])}:seq={r['seq']}",True)
   except (ValueError,TypeError):COUNTS['malformed_trajectory_events']+=1
 if 'transcript_events' in ts:
  for r in rows(c,'transcript_events'):
   ref=f"{key}:transcript_events:session={hid('session',r['session_id'])}:seq={r['seq']}"
   try:
    raw=r.get('event_json') or decode(r['event_zstd']).decode();add_event(json.loads(raw),r['session_id'],ref)
   except Exception as e:COUNTS['unreadable_transcript_events']+=1
 for tb in ['session_transcript_archives','session_transcript_cold_archives']:
  if tb not in ts:continue
  for r in rows(c,tb):
   if not r.get('archive_blob'):continue
   try:
    raw=decode(r['archive_blob']) if r.get('encoding','zstd')=='zstd' else r['archive_blob']
    for n,line in enumerate(raw.splitlines(),1):add_event(json.loads(line),r['session_id'],f"{key}:{tb}:session={hid('session',r['session_id'])}:generation={hid('generation',r.get('generation'))}:line={n}")
   except Exception:COUNTS['unreadable_transcript_archives']+=1
 if 'thread_turns' in ts:
  for r in rows(c,'thread_turns'):
   ROLLOUT.append(('db_turn',r,f"{key}:thread_turns:turn={hid('turn',r['turn_id'])}"))
 if 'thread_items' in ts:
  for r in rows(c,'thread_items'):
   if r.get('item_type') in ['commandExecution','dynamicToolCall','fileChange']:
    ROLLOUT.append(('db_item',r,f"{key}:thread_items:item={hid('item',r['item_id'])}"))
 if 'thread_goals' in ts:
  for r in rows(c,'thread_goals'):
   ref=f"{key}:thread_goals:goal={hid('goal',r['goal_id'])}";t=timestamp(r['created_at_ms']);observed(ref,t)
   if eligible(t):
    rr=run('goal:'+r['goal_id'],ref,run_type='goal',task_id=hid('task','goal:'+r['goal_id']),start_time_utc=t,source_system='codex');setstatus(rr,r.get('status'),ref,2)
 if 'logs' in ts:
  # Diagnostic entries lack response/attempt IDs; inspect metadata, never manufacture attempts.
  SOURCES[key]['diagnostic_rows']=c.execute('select count(*) from logs').fetchone()[0]
  SOURCES[key]['diagnostic_levels']={r[0]:r[1] for r in c.execute('select level,count(*) from logs group by level')}
  SOURCES[key]['first_timestamp_utc']=timestamp(c.execute('select min(ts) from logs').fetchone()[0]);SOURCES[key]['last_timestamp_utc']=timestamp(c.execute('select max(ts) from logs').fetchone()[0])
  for r in c.execute('select id,ts,level,target,feedback_log_body from logs'):
   COUNTS['harness_diagnostic_records_scanned']+=1
   # Only attempt-identifying structured JSON is eligible; free-text warnings are not attempts.
   body=r['feedback_log_body'] or ''
   try:d=json.loads(body)
   except (ValueError,TypeError):continue
   if not isinstance(d,dict):continue
   # Transport log JSON is merely inspected; rollouts supply response identities and usage.
   COUNTS['harness_json_diagnostics_scanned']+=1
 if 'flow_runs' in ts:SOURCES[key]['flow_run_rows']=c.execute('select count(*) from flow_runs').fetchone()[0]
 if 'thread_goals' in ts:SOURCES[key]['goal_rows']=c.execute('select count(*) from thread_goals').fetchone()[0]
 c.rollback();c.close()

def traceprocess():
 seen=set()
 for o,ref in TRACE:
  key=(o.get('runId'),o.get('sessionId'),o.get('traceId'),o.get('seq'),o.get('type'))
  if key in seen:COUNTS['deduplicated_trajectory_events']+=1;continue
  seen.add(key);rid=o.get('runId');sid=o.get('sessionId');t=timestamp(o.get('ts'));d=o.get('data') or {};typ=o.get('type');
  if not rid:continue
  rr=run(rid,ref,session_id=hid('session',sid),model_id=o.get('modelId'),provider=o.get('provider'),source_system='openclaw',model_api=token(o.get('modelApi')))
  record_metrics(rr,d,['imagesCount','toolCount','compactionCount','itemLifecycle'])
  if d.get('threadId'):THREAD_SESSION[d['threadId']]=sid
  if d.get('turnId'):TURN_RUN[d['turnId']]=rid
  if typ=='session.started':rr['start_time_utc']=min(t,rr.get('start_time_utc') or t);rr['time_basis']='explicit_lifecycle'
  if typ=='session.ended':
   rr['end_time_utc']=max(t,rr.get('end_time_utc') or t);setstatus(rr,'timeout' if d.get('timedOut') else d.get('status'),ref,6)
  if typ=='trace.metadata':
   h=d.get('harness') or {}
   if 'openclaw' in str(h.get('name','')).lower():rr['openclaw_version']=token(h.get('version'))
   rr.update({k:v for k,v in {'harness_name':token(h.get('name')),'harness_version':token(h.get('version')),'node_version':token((h.get('runtime') or {}).get('node')),'os_platform':token((h.get('os') or {}).get('platform')),'os_arch':token((h.get('os') or {}).get('arch')),'os_release':token((h.get('os') or {}).get('release'))}.items() if v is not None})
   md=d.get('model') or {}
   for a,b in [('fastMode','fast_mode'),('thinkLevel','thinking_level'),('reasoningLevel','reasoning_level'),('version','model_version'),('quantization','model_quantization'),('api','model_api')]:
    v=md.get(a)
    if v is not None and isinstance(v,(bool,int,float,str)):rr[b]=int(v) if isinstance(v,bool) else token(v) if isinstance(v,str) else v
   cfg=((d.get('config') or {}).get('redacted') or {}).get('agents',{}).get('defaults',{})
   if num(cfg.get('maxConcurrent')) is not None:rr['configured_max_concurrent']=cfg['maxConcurrent']
   if num((cfg.get('subagents') or {}).get('maxConcurrent')) is not None:rr['configured_subagent_max_concurrent']=cfg['subagents']['maxConcurrent']
  if typ in ['model.completed','trace.artifacts']:
   usage=d.get('usage') or {}
   for a,b in [('input','input_tokens'),('output','output_tokens'),('cacheRead','cache_read_tokens'),('cacheWrite','cache_write_tokens'),('reasoningTokens','reasoning_tokens'),('total','total_tokens')]:
    if num(usage.get(a)) is not None:rr[b]=num(usage[a])
   cost=usage.get('cost') or {}
   if num(cost.get('total')) is not None:rr['cost_total']=cost['total']
   if num(d.get('compactionCount')) is not None:rr['compaction_count']=d['compactionCount']
   if typ=='trace.artifacts':setstatus(rr,'timeout' if d.get('timedOut') else 'interrupted' if d.get('aborted') else d.get('finalStatus'),ref,6)
  if typ in ['tool.call','tool.result'] and d.get('toolCallId'):
   call=d['toolCallId'];CALL_RUN[call]=rid
   ar=attempt('tool:'+call,ref,run_id=rr['run_id'],session_id=hid('session',sid),timestamp_utc=t,operation_type='tool',tool_name=token(d.get('name')),model_id=token(o.get('modelId')),provider=token(o.get('provider')),source_system='openclaw',linkage_basis='explicit_tool_call_id')
   if typ=='tool.call':ar['_start']=t;ar['timestamp_utc']=t
   else:
    ar['_end']=t;res=d.get('result') if isinstance(d.get('result'),dict) else {}
    ar['duration_ms']=num(res.get('durationMs')) if num(res.get('durationMs')) is not None else ar.get('duration_ms');ar['exit_code']=res.get('exitCode')
    if d.get('isError') is True:setstatus(ar,'failed',ref,7)
    elif d.get('isError') is False:setstatus(ar,d.get('status') or 'completed',ref,6)
    elif d.get('status'):setstatus(ar,d['status'],ref,6)
    # Parse only JSON tool envelopes, never export bodies.
    extract_spawn(d.get('result'),rid);extract_spawn(d.get('output'),rid)
  if typ=='turn.dynamic_tool_terminal_release' and d.get('toolCallId'):
   ar=attempt('tool:'+d['toolCallId'],ref,run_id=rr['run_id'],operation_type='tool');
   if ar.get('duration_ms') is None:ar['duration_ms']=num(d.get('durationMs'));ar['duration_basis']='explicit_terminal_release_duration'

def extract_spawn(body,parent):
 if isinstance(body,str):
  try:body=json.loads(body)
  except (ValueError,TypeError):return
 if isinstance(body,dict):
  if body.get('runId') and (body.get('childSessionKey') or body.get('sessionKey')):CHILD_LINK.append((body['runId'],parent))
  if body.get('childRunId'):CHILD_LINK.append((body['childRunId'],parent))
  for k in ['result','details','data']:
   if isinstance(body.get(k),(dict,str)):extract_spawn(body[k],parent)
  for x in body.get('content',[]) if isinstance(body.get('content'),list) else []:
   if isinstance(x,dict) and x.get('type')=='text':extract_spawn(x.get('text'),parent)

def rollread(raw,ref):
 try:o=json.loads(raw)
 except (ValueError,TypeError):COUNTS['malformed_rollout_records']+=1;return
 p=o.get('payload') or {};t=timestamp(o.get('timestamp'));observed(ref,t)
 if not eligible(t):return
 key=(p.get('id') if o.get('type')=='session_meta' else None,hashlib.sha256(json.dumps(o,sort_keys=True).encode()).hexdigest())
 if key in SEEN_ROLLOUT:COUNTS['deduplicated_rollout_records']+=1;return
 SEEN_ROLLOUT.add(key);ROLLOUT.append(('record',o,ref))

def rollprocess():
 # Per-file context is handled by stream identifiers; backup files use distinct refs.
 state={};context={};response_turn={}
 for typ,o,ref in ROLLOUT:
  stream=ref.rsplit(':line=',1)[0]
  if typ!='record':continue
  p=o.get('payload') or {};ty=o.get('type');t=timestamp(o.get('timestamp'));ctx=state.setdefault(stream,{})
  if ty=='session_meta':ctx.update(thread=p.get('id'),provider=p.get('model_provider'),codex_version=token(p.get('cli_version')))
  if ty=='turn_context':
   ctx.update(turn=p.get('turn_id'),model=p.get('model'));context[p.get('turn_id')]=dict(ctx)
  if ty=='event_msg' and p.get('type')=='task_started':ctx.pop('model',None);ctx['turn']=p.get('turn_id');ctx['context_limit']=num(p.get('model_context_window'));context.setdefault(ctx['turn'],dict(ctx))
  if ty=='token_usage_record':
   turn=p.get('turn_id');rid=TURN_RUN.get(turn) or 'codex_turn:'+turn;sid=THREAD_SESSION.get(p.get('thread_id') or ctx.get('thread'));rr=run(rid,ref,session_id=hid('session',sid),source_system='codex',model_id=ctx.get('model'),provider=ctx.get('provider'),codex_version=ctx.get('codex_version'),lifecycle_scope='turn')
   response=p.get('response_id')
   if not response:COUNTS['token_usage_without_response_id']+=1;continue
   u=p.get('usage') or {};ar=attempt('response:'+response,ref,run_id=rr['run_id'],session_id=hid('session',sid),timestamp_utc=t,operation_type='model_call',model_id=token(ctx.get('model')),provider=token(ctx.get('provider')),source_system='codex',codex_version=ctx.get('codex_version'),linkage_basis='explicit_turn_and_response_id',context_limit_tokens=ctx.get('context_limit'))
   # A token usage record is not, by itself, proof of successful completion.
   for a,b in [('input_tokens','input_tokens'),('output_tokens','output_tokens'),('cached_input_tokens','cache_read_tokens'),('cache_write_input_tokens','cache_write_tokens'),('reasoning_output_tokens','reasoning_tokens'),('total_tokens','total_tokens')]:
    if num(u.get(a)) is not None:ar[b]=u[a]
   MODEL_RESPONSE[response]=ar['attempt_id'];response_turn[response]=turn
  if ty=='event_msg' and p.get('type') in ['task_started','task_complete','turn_aborted']:
   turn=p.get('turn_id') or ctx.get('turn')
   if not turn:continue
   rid=TURN_RUN.get(turn) or 'codex_turn:'+turn;sid=THREAD_SESSION.get(ctx.get('thread'));start=timestamp(p.get('started_at'));end=timestamp(p.get('completed_at'))
   rr=run(rid,ref,session_id=hid('session',sid),start_time_utc=start,end_time_utc=end,duration_ms=num(p.get('duration_ms')),time_to_first_token_ms=num(p.get('time_to_first_token_ms')),model_id=ctx.get('model'),provider=ctx.get('provider'),codex_version=ctx.get('codex_version'),source_system='codex',lifecycle_scope='turn')
   if p['type']=='task_complete':setstatus(rr,'completed',ref,2)
   if p['type']=='turn_aborted':setstatus(rr,'interrupted',ref,2)
  if ty=='event_msg' and p.get('type')=='item_completed':
   it=p.get('item') or {};turn=p.get('turn_id');rid=TURN_RUN.get(turn) or ('codex_turn:'+turn if turn else None);item=it.get('id')
   if it.get('type') in ['dynamicToolCall','commandExecution','fileChange'] and item:
    call=it.get('callId') or it.get('call_id') or item
    # Native dynamic IDs are the same call IDs as trajectory/audit; use them when known.
    key='tool:'+call if call in CALL_RUN else 'codex_item:'+item
    ar=attempt(key,ref,run_id=hid('run',rid),session_id=hid('session',THREAD_SESSION.get(p.get('thread_id'))),timestamp_utc=timestamp(p.get('started_at_ms')) or t,operation_type='tool',tool_name=token(it.get('tool') or ('exec_command' if it.get('type')=='commandExecution' else 'apply_patch' if it.get('type')=='fileChange' else None)),source_system='codex',duration_ms=num(it.get('durationMs')),exit_code=it.get('exitCode'),linkage_basis='explicit_turn_and_item_id')
    ar['_start']=timestamp(p.get('started_at_ms'));ar['_end']=timestamp(p.get('completed_at_ms'));setstatus(ar,'failed' if it.get('success') is False else it.get('status'),ref,4)
 for typ,r,ref in ROLLOUT:
  if typ=='db_turn':
   t=timestamp(r.get('started_at'));observed(ref,t)
   if not eligible(t):continue
   rid=TURN_RUN.get(r['turn_id']) or 'codex_turn:'+r['turn_id'];ctx=context.get(r['turn_id'],{});rr=run(rid,ref,session_id=hid('session',THREAD_SESSION.get(r['thread_id'])),start_time_utc=t,end_time_utc=timestamp(r.get('completed_at')),duration_ms=num(r.get('duration_ms')),model_id=ctx.get('model'),provider=ctx.get('provider'),codex_version=ctx.get('codex_version'),source_system='codex',lifecycle_scope='turn');setstatus(rr,r.get('status'),ref,3)
   try:
    err=json.loads(r.get('error_json') or '{}')
    if token(err.get('codexErrorInfo')):rr['error_type']=token(err['codexErrorInfo'])
    if token(err.get('code')):rr['error_code']=token(err['code'])
   except ValueError:pass
  if typ=='db_item':
   t=timestamp(r.get('started_at_ms') or r.get('created_at_ms'));observed(ref,t)
   if not eligible(t):continue
   it=json.loads(r['item_json']);item=r['item_id'];call=it.get('callId') or it.get('call_id') or item;key='tool:'+call if call in CALL_RUN else 'codex_item:'+item;rid=TURN_RUN.get(r['turn_id']) or 'codex_turn:'+r['turn_id']
   ar=attempt(key,ref,run_id=hid('run',rid),session_id=hid('session',THREAD_SESSION.get(r['thread_id'])),timestamp_utc=t,operation_type='tool',tool_name=token(it.get('tool') or ('exec_command' if r.get('item_type')=='commandExecution' else 'apply_patch' if r.get('item_type')=='fileChange' else None)),duration_ms=num(it.get('durationMs')),exit_code=it.get('exitCode'),source_system='codex',linkage_basis='explicit_turn_and_item_id');ar['_start']=timestamp(r.get('started_at_ms'));ar['_end']=timestamp(r.get('completed_at_ms'));setstatus(ar,'failed' if it.get('success') is False else it.get('status'),ref,4)


def transcriptprocess():
 for sid,o,ref in TRANS:
  m=o.get('message') or {};role=m.get('role');t=timestamp(m.get('timestamp') or o.get('timestamp'));oc=m.get('__openclaw') or {};rid=oc.get('runId') or (o.get('details') or {}).get('runId')
  if role=='custom' and m.get('customType')=='openclaw.nested-tool.v1':
   d=m.get('details') or {};call=d.get('toolCallId');rawrun=d.get('runId')
   if call:
    if rawrun:run(rawrun,ref,session_id=hid('session',sid),source_system='openclaw')
    ar=attempt('tool:'+call,ref,run_id=hid('run',rawrun),session_id=hid('session',sid),timestamp_utc=timestamp(d.get('startedAt')),parent_attempt_id=hid('attempt','tool:'+d['parentToolCallId']) if d.get('parentToolCallId') else None,operation_type='tool',tool_name=token(d.get('toolName')),source_system='openclaw',linkage_basis='explicit_nested_tool_ids');ar['_start']=timestamp(d.get('startedAt'));ar['_end']=timestamp(d.get('timestamp'));setstatus(ar,'failed' if d.get('isError') else 'completed' if d.get('isError') is False else None,ref,6)
  if role=='assistant':
   for block in m.get('content',[]) if isinstance(m.get('content'),list) else []:
    if isinstance(block,dict) and block.get('type') in ['toolCall','tool_call']:
     call=block.get('id');ar=attempt('tool:'+call,ref,run_id=hid('run',rid or CALL_RUN.get(call)),session_id=hid('session',sid),timestamp_utc=t,operation_type='tool',tool_name=token(block.get('name')),source_system='openclaw',linkage_basis='explicit_tool_call_id') if call else None
   response=m.get('responseId');u=m.get('usage') or {};provider=m.get('provider');known_codex=sid in THREAD_SESSION.values()
   actual=bool(response) or (provider!='openclaw' and not known_codex and any(num(u.get(k)) not in [None,0] for k in ['input','output']) and not m.get('openclawDeliveryMirror'))
   if not actual:continue
   if not rid:
    rids={CALL_RUN.get(b.get('id')) for b in m.get('content',[]) if isinstance(b,dict) and b.get('type') in ['toolCall','tool_call'] and CALL_RUN.get(b.get('id'))}
    if len(rids)==1:rid=next(iter(rids))
   ar=attempt('response:'+response if response else 'native_message:'+sid+':'+o['id'],ref,run_id=hid('run',rid),session_id=hid('session',sid),timestamp_utc=t,operation_type='model_call',model_id=token(m.get('responseModel') or m.get('model')),provider=token(provider),source_system='openclaw',model_api=token(m.get('api')),linkage_basis='explicit_response_id' if response else 'native_assistant_usage_record')
   stop=m.get('stopReason');setstatus(ar,'interrupted' if stop=='aborted' else 'failed' if stop=='error' else 'completed' if stop in ['stop','toolUse','length'] else stop,ref,4)
   for a,b in [('input','input_tokens'),('output','output_tokens'),('cacheRead','cache_read_tokens'),('cacheWrite','cache_write_tokens'),('reasoningTokens','reasoning_tokens'),('totalTokens','total_tokens')]:
    if num(u.get(a)) is not None:ar[b]=u[a]
   cu=u.get('contextUsage') or {}
   if cu.get('state') not in ['unavailable','unknown']:ar['context_tokens']=num(cu.get('totalTokens') if cu.get('totalTokens') is not None else cu.get('promptTokens'))
   cost=u.get('cost') or {};ar['cost_total']=num(cost.get('total'))
   if response:MODEL_RESPONSE[response]=ar['attempt_id']
  if role=='toolResult' and m.get('toolCallId'):
   call=m['toolCallId'];rid=rid or CALL_RUN.get(call);ar=attempt('tool:'+call,ref,run_id=hid('run',rid),session_id=hid('session',sid),operation_type='tool',tool_name=token(m.get('toolName')),source_system='openclaw',linkage_basis='explicit_tool_call_id');ar['_end']=t
   if m.get('isError') is True:setstatus(ar,'failed',ref,6)
   elif m.get('isError') is False:setstatus(ar,'completed',ref,2)
   d=m.get('details') if isinstance(m.get('details'),dict) else {}
   if num(d.get('durationMs')) is not None:ar['duration_ms']=d['durationMs']
   if isinstance(d.get('exitCode'),int):ar['exit_code']=d['exitCode']
   if rid:
    extract_spawn(d,rid)
    for b in m.get('content',[]) if isinstance(m.get('content'),list) else []:
     if isinstance(b,dict) and b.get('type')=='text':extract_spawn(b.get('text'),rid)


def gatewayprocess(path,key):
 source(key,path,'gateway_log',failure_only=False);seen=set()
 for n,line in enumerate(open(path,errors='replace'),1):
  ref=f'{key}:line={n}';objs=[]
  try:
   o=json.loads(line);t=timestamp(o.get('time') or o.get('_meta',{}).get('date'));objs=[v for k,v in o.items() if isinstance(v,dict) and k!='_meta'];msg=o.get('message') or ' '.join(str(o[k]) for k in ['0','1'] if isinstance(o.get(k),str))
  except (ValueError,TypeError):
   m=re.match(r'^(\d{4}-\d\d-\d\dT\S+)\s+',line);t=timestamp(m[1]) if m else None;msg=line
  observed(ref,t)
  if not eligible(t):continue
  # Read only exact structured fields, not arbitrary text or exception previews.
  for d in objs:
   rid=d.get('runId');sid=d.get('sessionId') or d.get('session_id')
   if d.get('threadId') and sid:THREAD_SESSION[d['threadId']]=sid
   if rid and d.get('turnId'):TURN_RUN[d['turnId']]=rid
   if rid:
    rr=run(rid,ref,session_id=hid('session',sid),source_system='openclaw')
    if d.get('runStatus'):setstatus(rr,d['runStatus'],ref,2)
    record_metrics(rr,d,['totalMs','elapsedMs','spans','durationMs','consecutiveFailures'])
   if d.get('toolCallId'):
    call=d['toolCallId'];mapped=rid or TURN_RUN.get(d.get('turnId')) or CALL_RUN.get(call)
    ar=attempt('tool:'+call,ref,run_id=hid('run',mapped),timestamp_utc=t,operation_type='tool',tool_name=token(d.get('tool')),duration_ms=num(d.get('durationMs')),source_system='openclaw',linkage_basis='explicit_tool_call_id')
   if d.get('candidateModel') and d.get('attempt') is not None and (rid or sid):
    ident=(rid or sid,d.get('attempt'),d.get('candidateProvider'),d.get('candidateModel'));phase=d.get('status') or d.get('decision');event=d.get('event');
    # Routing probes/eligibility checks are not actual model-call attempts.
    if not (isinstance(event,str) and any(x in event.lower() for x in ['attempt','fallback'])):continue
    if d.get('decision') not in ['candidate_failed','candidate_succeeded']:continue
    ar=attempt('route_attempt:'+json.dumps(ident),ref,run_id=hid('run',rid),session_id=hid('session',sid),timestamp_utc=t,operation_type='model_route_attempt',model_id=token(d.get('candidateModel')),provider=token(d.get('candidateProvider')),error_code=token(d.get('code')),retry_index=num(d.get('attempt')),source_system='openclaw_gateway',source_failure_only=int(d.get('decision')=='candidate_failed'),source_selected_logging=1,population='gateway_route_diagnostics',linkage_basis='explicit_run_candidate_attempt');setstatus(ar,d.get('decision'),ref,2)
    if d.get('status') is not None:setstatus(ar,d['status'],ref,1)
    if isinstance(d.get('status'),int):ar['error_code']=str(d['status']) if d.get('decision')=='candidate_failed' else ar.get('error_code')
    if token(d.get('errorName')):ar['error_type']=token(d['errorName'])
   if d.get('errorName') and rid:
    rr=RUNS.get(hid('run',rid))
    if rr:rr.setdefault('_diagnostic_error_types',set()).add(token(d['errorName']))
  # Legacy text lifecycle messages with explicit run IDs; no lane-error synthetic attempts.
  match=re.search(r'\brunId=([A-Za-z0-9_-]{8,100})',msg)
  if match:
   rid=match[1];sidm=re.search(r'\bsessionId=([A-Za-z0-9_-]{8,100})',msg);rr=run(rid,ref,session_id=hid('session',sidm[1]) if sidm else None,source_system='openclaw')
   if re.search(r'embedded run (?:start|begin)\b',msg):run(rid,ref,start_time_utc=t)
   if re.search(r'embedded run (?:done|end)\b',msg):
    run(rid,ref,end_time_utc=t)
    for pat,k in [(r'\bdurationMs=(\d+)','duration_ms')]:
     v=re.search(pat,msg)
     if v:rr[k]=int(v[1])
    ab=re.search(r'\baborted=(true|false)',msg)
    if ab and ab[1]=='true':setstatus(rr,'interrupted',ref,1)
   if 'embedded run timeout' in msg:setstatus(rr,'timeout',ref,2)
   for pat,k in [(r'\bmodel=([A-Za-z0-9_./:+-]+)','model_id'),(r'\bprovider=([A-Za-z0-9_.-]+)','provider')]:
    v=re.search(pat,msg)
    if v:run(rid,ref,**{k:v[1]})


def lmprocess(path,key):
 source(key,path,'lm_studio_server_log',failure_only=False);blocks=[];cur=None
 for n,line in enumerate(open(path,errors='replace'),1):
  m=re.match(r'^\[(\d{4}-\d\d-\d\d \d\d:\d\d:\d\d(?:\.\d+)?)\]((?:\s*\[[^\]]*\])*)\s*(.*)',line)
  if m:
   if cur:blocks.append(cur)
   cur=[n,timestamp(m[1],True),m[2],m[3]+'\n']
  elif cur:cur[3]+=line
 if cur:blocks.append(cur)
 for n,t,labels,body in blocks:
  ref=f'{key}:line={n}';observed(ref,t)
  if not eligible(t):continue
  m=re.match(r'Received request:\s*POST\s+(?:to\s+)?(/[^\s?]+)\s+with body\s*',body)
  if m and m[1] in ['/v1/chat/completions','/v1/responses','/v1/embeddings','/api/v1/chat']:
   try:d,_=json.JSONDecoder().raw_decode(body[m.end():].lstrip())
   except ValueError:COUNTS['lm_unparseable_inference_request_bodies']+=1;continue
   # LM logs do not identify the OpenClaw client. Keep an explicitly separate population.
   model=token(d.get('model'));req=d.get('request_id') or d.get('requestId');raw='lm_request:'+str(req) if req else 'lm_request:'+key+':'+str(n)
   ar=attempt(raw,ref,timestamp_utc=t,operation_type='embedding_call' if m[1]=='/v1/embeddings' else 'model_call',model_id=model,provider='lmstudio',model_version=token(d.get('model_version')),model_quantization=token(d.get('quantization')),source_system='lm_studio',population='lm_studio_unattributed_requests',linkage_basis='explicit_request_id' if req else 'source_location_only',request_body_bytes=len(body[m.end():].encode()))
   for fld in ['temperature','top_p','top_k','seed']:
    if isinstance(d.get(fld),(int,float)) and not isinstance(d.get(fld),bool):ar[fld]=d[fld]
   ar['max_output_tokens']=num(d.get('max_completion_tokens') if d.get('max_completion_tokens') is not None else d.get('max_tokens'))
   if isinstance(d.get('stream'),bool):ar['stream']=int(d['stream'])
   if req:LOG_RETRIES[str(req)]=ar
  if body.startswith('Generated prediction:'):
   try:d,_=json.JSONDecoder().raw_decode(body.split(':',1)[1].lstrip())
   except ValueError:continue
   response=d.get('id');aid=MODEL_RESPONSE.get(response)
   if aid:
    ar=ATT[aid];refadd(ar,ref);u=d.get('usage') or {}
    for a,b in [('prompt_tokens','input_tokens'),('completion_tokens','output_tokens'),('total_tokens','total_tokens')]:
     if num(u.get(a)) is not None and ar.get(b) is None:ar[b]=u[a]
    COUNTS['lm_predictions_linked_by_response_id']+=1
   else:COUNTS['lm_unlinked_prediction_records_not_double_counted']+=1
  if body.startswith('Finished streaming response'):COUNTS['lm_unlinked_stream_completion_records']+=1
 # A completion without a shared request ID does not establish request status, duration, concurrency.


def finalize():
 for child,parent in CHILD_LINK:
  rr=RUNS.get(hid('run',child))
  if rr and child!=parent:rr['parent_run_id']=hid('run',parent)
 # Fill links only from explicit call/run and thread/session identity maps.
 for ar in ATT.values():
  if ar.get('run_id') and ar['run_id'] in RUNS:
   rr=RUNS[ar['run_id']]
   if rr.get('task_id'):ar['task_id']=rr['task_id']
   if rr.get('codex_version'):ar['codex_version']=rr['codex_version']
   for fld in ['model_id','provider','model_api','model_version','model_quantization']:
    vals=rr.get('_'+fld,set())
    if not ar.get(fld) and len(vals)==1:ar[fld]=next(iter(vals))
    elif not ar.get(fld) and rr.get(fld) is not None and fld not in ['model_id','provider']:ar[fld]=rr[fld]
   if not ar.get('session_id') and rr.get('session_id'):ar['session_id']=rr['session_id']
  if ar.get('duration_ms') is None:
   d=msdiff(ar.get('_start'),ar.get('_end'))
   if d is not None:ar['duration_ms']=d;ar['duration_basis']='paired_call_result_timestamps'
  elif not ar.get('duration_basis'):ar['duration_basis']='explicit_source_duration'
  if ar.get('_start'):ar['timestamp_utc']=ar['_start']
 for rr in RUNS.values():
  mods=sorted(rr.get('_model_id',set()));provs=sorted(rr.get('_provider',set()));rr['model_id']=mods[0] if len(mods)==1 else None;rr['provider']=provs[0] if len(provs)==1 else None
  rr['observed_model_ids']=json.dumps(mods,separators=(',',':')) if mods else None
  if rr.get('duration_ms') is None:
   d=msdiff(rr.get('start_time_utc'),rr.get('end_time_utc'))
   if d is not None:rr['duration_ms']=d;rr['duration_basis']='paired_lifecycle_timestamps'
  else:rr['duration_basis']='explicit_source_duration'
  rr['execution_outcome_evidence']='recorded_terminal_status' if rr.get('_statuses') else 'unknown'
  if rr.get('parent_run_id') not in RUNS:rr['parent_run_id']=None
 for store in [RUNS,ATT]:
  for o in store.values():
   o['source_reference']=';'.join(sorted(o.get('_refs',set())));o['original_status']=';'.join(sorted(o.get('_original',set()))) or None;o['status_conflict']=int(len(o.get('_statuses',set()))>1)
   # No negative, non-finite, or inferred numeric defaults.
   for k,v in list(o.items()):
    if not k.startswith('_') and isinstance(v,float) and (v!=v or abs(v)==float('inf')):o[k]=None
 # Detached attempt link may refer to an otherwise missing but explicitly observed run ID.
 for o in ATT.values():
  if o.get('parent_attempt_id') and o['parent_attempt_id'] not in ATT:o['parent_attempt_id']=None
  if o.get('run_id') and o['run_id'] not in RUNS:o['run_id']=None
 for name,store,cols in [('runs.csv',RUNS,RUN_COLS),('attempts.csv',ATT,ATT_COLS)]:
  with open(OUT/(name+'.tmp'),'w',newline='') as f:
   w=csv.DictWriter(f,fieldnames=cols,extrasaction='ignore');w.writeheader()
   for o in sorted(store.values(),key=lambda o:(o.get('start_time_utc') or o.get('timestamp_utc') or '',o.get('attempt_id') or o.get('run_id') or '')):w.writerow({k:o.get(k) for k in cols})
  os.chmod(OUT/(name+'.tmp'),0o600)
  os.replace(OUT/(name+'.tmp'),OUT/name)


def validate():
 rr=list(csv.DictReader(open(OUT/'runs.csv')));aa=list(csv.DictReader(open(OUT/'attempts.csv')));rids={r['run_id'] for r in rr};aids={r['attempt_id'] for r in aa};errs=[]
 if len(rids)!=len(rr):errs.append('duplicate_run_ids')
 if len(aids)!=len(aa):errs.append('duplicate_attempt_ids')
 for r in rr:
  if r['parent_run_id'] and r['parent_run_id'] not in rids:errs.append('dangling_parent')
  if r['parent_run_id']==r['run_id']:errs.append('self_parent')
  if r['start_time_utc'] and r['end_time_utc'] and r['end_time_utc']<r['start_time_utc']:errs.append('reversed_run_interval')
  if r.get('task_completion_status')!='unknown':errs.append('unverified_task_success')
 for a in aa:
  if a['run_id'] and a['run_id'] not in rids:errs.append('dangling_attempt_run')
  if a.get('parent_attempt_id') and a['parent_attempt_id'] not in aids:errs.append('dangling_parent_attempt')
  if a.get('task_completion_status')!='unknown':errs.append('unverified_task_status')
 numeric={'duration_ms','input_tokens','output_tokens','context_tokens','context_limit_tokens','concurrent_executions','cache_read_tokens','cache_write_tokens','reasoning_tokens','total_tokens','cost_total','retry_index','request_body_bytes','response_body_bytes','prompt_chars','observed_prompt_chars','time_to_first_token_ms','tokens_per_second','tool_use_count','compaction_count','max_output_tokens','top_k','context_utilization'}
 for rows_ in [rr,aa]:
  for row in rows_:
   for k in numeric & row.keys():
    if row[k] and (float(row[k])<0 or not float(row[k])<float('inf')):errs.append('invalid_numeric:'+k)
   if row['status'] not in set(NORM.values()):errs.append('invalid_status')
   for v in row.values():
    if re.search(r'(?:\bsk-[A-Za-z0-9_-]{12,}|Bearer\s+\S+|[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}|-----BEGIN .*PRIVATE KEY)',v):errs.append('sensitive_pattern')
 report={'checks_passed':not errs,'errors':dict(collections.Counter(errs)),'runs':len(rr),'attempts':len(aa),'linked_attempts':sum(bool(a['run_id']) for a in aa),'parent_linked_runs':sum(bool(r['parent_run_id']) for r in rr),'missingness':{name:{k:sum(not r[k] for r in rows_) for k in (rows_[0].keys() if rows_ else [])} for name,rows_ in [('runs',rr),('attempts',aa)]}}
 dump(OUT/'validation.json',report);return report


def main():
 if args.validate_only:print(json.dumps(validate()));return
 # All reads are bounded to this pass. No jobs, network, agents, or config mutations.
 live=[HOME/'.openclaw/state/openclaw.sqlite']+list((HOME/'.openclaw/agents').glob('*/agent/openclaw-agent.sqlite'))
 harness=list((HOME/'.openclaw/agents').glob('*/agent/codex-home'))
 for b in harness:
  live += [b/f for f in ['thread_history_1.sqlite','goals_1.sqlite','logs_2.sqlite'] if (b/f).exists()]
 for i,p in enumerate(live):dbload(p,'db_live_'+str(i),immutable=p.name=='goals_1.sqlite' and not pathlib.Path(str(p)+'-wal').exists())
 for i,p in enumerate(sorted((HOME/'.openclaw/agents').glob('*/sessions/*.zst'))):
  key=source('session_archive_'+str(i),p,'compressed_session_jsonl')
  try:
   raw=decode(p.read_bytes());sid=p.name.split('.jsonl')[0]
   for n,line in enumerate(raw.splitlines(),1):add_event(json.loads(line),sid,f'{key}:line={n}')
  except Exception as e:WARN.append({'source':key,'limitation':'archive_unreadable','error_type':type(e).__name__})
 # Include retained canonical historical backup without restoring or changing it.
 for ai,p in enumerate(sorted((HOME/'Clu-Backups').glob('**/*.tar.gz'))):
  source('backup_'+str(ai),p,'retained_backup_archive')
  with tarfile.open(p,'r:gz') as tf, tempfile.TemporaryDirectory(prefix='openclaw-metadata-read-') as tmp:
   members=tf.getmembers();selected={}
   for m in members:
    if not m.isfile():continue
    base=pathlib.PurePosixPath(m.name).name
    if base in ['openclaw.sqlite','openclaw-agent.sqlite','thread_history_1.sqlite','goals_1.sqlite','logs_2.sqlite'] or any(base==n+s for n in ['openclaw.sqlite','openclaw-agent.sqlite','thread_history_1.sqlite','goals_1.sqlite','logs_2.sqlite'] for s in ['-wal','-shm']):
     # Never use archive names as extraction paths.
     parent=hid('directory',str(pathlib.PurePosixPath(m.name).parent));dest=pathlib.Path(tmp)/parent;dest.mkdir(exist_ok=True);fp=dest/base;fp.write_bytes(tf.extractfile(m).read());selected[m.name]=fp
    if '.jsonl' in base and ('/sessions/' in m.name or '/cron/' in m.name):
     key=source(f'backup_{ai}_jsonl_{len(SOURCES)}',str(p)+'!'+m.name,'backup_jsonl');raw=tf.extractfile(m).read()
     if base.endswith('.zst'):raw=decode(raw)
     for n,line in enumerate(raw.splitlines(),1):
      try:o=json.loads(line)
      except (ValueError,TypeError):COUNTS['malformed_backup_jsonl']+=1;continue
      if '/codex-home/' in m.name:rollread(line,f'{key}:line={n}')
      elif o.get('type') in ['session','message','custom','custom_message','model_change','thinking_level_change']:
       sid=base.split('.jsonl')[0];add_event(o,sid,f'{key}:line={n}')
   for j,(name,fp) in enumerate(selected.items()):
    if fp.name.endswith('.sqlite'):
     key=f'backup_{ai}_db_{j}';dbload(fp,key,immutable=not pathlib.Path(str(fp)+'-wal').exists());
     if key in SOURCES:SOURCES[key]['path']=str(p).replace(str(HOME),'~')+'!'+name
 for i,p in enumerate(sorted(list(pathlib.Path('/tmp/openclaw').glob('*.log'))+list((HOME/'Library/Logs/openclaw').glob('*.log'))+list((HOME/'.openclaw/logs').glob('*.log')))):gatewayprocess(p,'gateway_'+str(i))
 traceprocess()
 for b in harness:
  files=sorted(list((b/'sessions').glob('**/*.jsonl'))+list((b/'archived_sessions').glob('**/*.jsonl')))
  for i,p in enumerate(files):
   key=source('rollout_'+str(i),p,'codex_rollout')
   for n,line in enumerate(open(p),1):rollread(line,f'{key}:line={n}')
 rollprocess();transcriptprocess()
 for i,p in enumerate(sorted((HOME/'.lmstudio/server-logs').glob('**/*.log'))):lmprocess(p,'lm_server_'+str(i))
 for i,p in enumerate(sorted((HOME/'Library/Logs/LM Studio').glob('*.log'))):
  key=source('lm_app_'+str(i),p,'lm_studio_app_log');
  for n,line in enumerate(open(p,errors='replace'),1):
   m=re.match(r'^\[(\d{4}-\d\d-\d\d \d\d:\d\d:\d\d\.\d+)\]',line);observed(f'{key}:line={n}',timestamp(m[1],True) if m else None)
  SOURCES[key]['limitation']='Application lifecycle diagnostics; no unambiguous inference attempt identities extracted.'
 try:list((HOME/'.Trash').iterdir())
 except PermissionError:WARN.append({'source':'~/.Trash','limitation':'macOS_permission_denied; deleted backups not accessible'})
 finalize();report=validate()
 manifest={'extractor_version':1,'cutoff_utc':CUT,'collection_finished_utc':timestamp(dt.datetime.now(UTC).isoformat()),'sources':SOURCES,'collection_counters':dict(COUNTS),'structured_acceptance_criteria_key_counts':dict(ACCEPTANCE_KEYS),'limitations':WARN,'validation':{k:v for k,v in report.items() if k!='missingness'}}
 dump(OUT/'source_manifest.json',manifest);write_dictionary(manifest,report)
 manifest['output_sha256']={n:hashlib.sha256((OUT/n).read_bytes()).hexdigest() for n in ['runs.csv','attempts.csv','data_dictionary.md','extract_dataset.py','validation.json']}
 dump(OUT/'source_manifest.json',manifest)
 print(json.dumps({'output':str(OUT),'runs':report['runs'],'attempts':report['attempts'],'linked_attempts':report['linked_attempts'],'parent_linked_runs':report['parent_linked_runs'],'checks_passed':report['checks_passed'],'source_count':len(SOURCES),'warnings':WARN}))


def write_dictionary(manifest,report):
 text='''# OpenClaw Historical Execution Dataset\n\n## Reproduction and collection boundary\n\nMetadata-only extraction; sources opened read-only, SQLite query_only transactions, no network or operational changes. Temporary backup database copies are read then removed; no raw conversation or logs are exported. Python 3 and the installed `zstd` CLI are required.\n\nRun `python3 extract_dataset.py --cutoff "'''+CUT+'''" --output /path/to/output` on the original host. Validate without collection: `python3 extract_dataset.py --validate-only`. IDs are deterministic SHA-256-derived pseudonyms (96 bits) scoped by entity type; these are not anonymization against a holder of original IDs. Paths below are local source aliases, not conversation identifiers.\n\nA fixed UTC cutoff excludes later timestamped events. SQLite snapshots are consistent within each connection, not atomically across databases or files. Sources are live and may be compacted, deleted, rotated or rewritten; identical reruns require the same source bytes/snapshots. Undated records and current lifecycle snapshots may reflect later state; no historical point-in-time state is reconstructed.\n\n## Files and linkage\n\n- `runs.csv`: one row per explicitly identifiable OpenClaw run, scheduled-job receipt/task execution, Codex turn not already mapped to an OpenClaw run, or Goal execution record. Session windows and jobs' current definitions are not executions and are not counted separately.\n- `attempts.csv`: tool-call IDs, canonical model response IDs/usage records, explicit routing-attempt records, and separately identified LM Studio inference/embedding request records.\n- `source_manifest.json`: source aliases, local paths/archive members, inspected counts, observed date coverage, exclusions and limitations. Source references use `alias:table:primary-key` or `alias:line=N`; pseudonymized table keys can be reproduced by this extractor.\n- `validation.json`: integrity checks, counts and per-column missing counts (not statistical analysis).\n- `extract_dataset.py`: extraction and validation implementation.\n\n`attempts.run_id` references `runs.run_id` when explicit evidence exists. It is null if the operation cannot be attributed. `session_id` is independently observed and does not prove a run association. `parent_run_id` uses explicit spawn result child-run to parent-call-run links only; no time-nearness parent guesses.\n\n## Required columns\n\n| Column | Table | Definition |\n|---|---|---|\n| run_id | both | Deterministic pseudonym of an explicit execution ID; fallback Codex turn/receipt IDs are namespaced. |\n| parent_run_id | runs | Explicit linked parent run; null when unavailable. |\n| session_id | both | Pseudonym of observed OpenClaw transcript/session ID; no chat/user identity. |\n| run_type | runs | agent, subagent, scheduled_job, or goal. |\n| start_time_utc, end_time_utc | runs | ISO-8601 UTC lifecycle timestamps. Missing start/end stays null. |\n| duration_ms | both | Observed source duration, else nonnegative difference of explicitly paired lifecycle/call-result timestamps. Never measured from absence, file mtime, or arbitrary first/last messages. |\n| model_id, provider | both | Execution-time observed model/provider, never current default configuration. Tools may carry invoking model metadata. LM provider identifies the server, not proven OpenClaw route. |\n| status | both | success, failure, timeout, cancelled, interrupted, unknown, as defined below. Technical completion only; no task-quality judgment. |\n| openclaw_version | runs | Only explicit execution-time OpenClaw harness version; never filled from installed/current version. |\n| source_reference | both | Semicolon-separated exact source locators; aliases resolved in manifest. |\n| attempt_id | attempts | Pseudonym of tool call, model response, source-local request, or explicit routing candidate attempt. Retries with distinct IDs remain distinct. |\n| timestamp_utc | attempts | Explicit call/request/start timestamp where observed; completion/usage-event timestamp if only completion was recorded. |\n| operation_type | attempts | tool, model_call, embedding_call, or model_route_attempt. Routing attempts can include provider preflight/dispatch, not necessarily a completed HTTP inference call. |\n| tool_name | attempts | Tool identifier only, no arguments or output. |\n| error_code, error_type | attempts | Allowlisted structured machine identifier only. Free-form messages and inferred causes are not exported. |\n| input_tokens, output_tokens | attempts | Provider-reported per-call tokens. No text-length token estimate, no division of run totals into attempts. |\n| context_tokens | attempts | Explicit contextUsage totalTokens (or promptTokens if total absent), only if reported as available. Not inferred from cumulative or input-token counts. |\n| context_limit_tokens | attempts | Explicit turn model-context-window value associated by exact turn ID. |\n| concurrent_executions | attempts | Null unless directly measured; no global concurrency invented from incomplete lifecycles. |\n\n## Optional columns\n\n| Column | Definition |\n|---|---|\n| source_system | openclaw, codex, openclaw_gateway, or lm_studio; first canonical source on a merged row. |\n| original_status | All observed allowlisted source status strings with source aliases. |\n| status_conflict | 1 if different normalized terminal statuses were observed, else 0. This is an observed disagreement flag, not a judgment. |\n| observed_model_ids | JSON list of explicit model IDs seen for a run; scalar model/provider null if more than one observed value. |\n| time_basis, duration_basis | Provenance of lifecycle timestamps and explicit or paired duration. |\n| lifecycle_scope | turn when a Codex turn supplies execution identity. |\n| linkage_basis | explicit tool-call/turn/response ID or source-local metadata; not probabilistic matching. |\n| population | openclaw_observed, gateway_route_diagnostics, or lm_studio_unattributed_requests. Do not pool these as independent executions/attempts. |\n| source_failure_only | 1 for failure-only candidate_failed diagnostic events; source_selected_logging also flags selected diagnostic logging. 0 does NOT prove complete success coverage. |\n| cache_read_tokens, cache_write_tokens, reasoning_tokens, total_tokens | Direct usage counters, including genuine observed zero values. |\n| cost_total | Direct source cost value; currency/unit not independently verified. Zero may be a source placeholder. |\n| exit_code | Explicit tool process exit code; nonzero exit is not automatically the same as tool transport failure. |\n| retry_index | Source's explicit routing-attempt ordinal; do not assume zero- or one-based without source inspection. |\n| request_body_bytes, response_body_bytes | Measured UTF-8 request log-body bytes or explicitly reported response size; request size is logged representation, not network bytes. |\n| prompt_chars, observed_prompt_chars | Optional direct prompt-size metadata; null if unavailable in exported attempts. |\n| time_to_first_token_ms, tokens_per_second | Explicit execution/resource metrics only, with original units named in field. |\n| tool_use_count, compaction_count | Run-level source counters, not inferred from exported rows. |\n| input_tokens, output_tokens, cache_read_tokens, cache_write_tokens, reasoning_tokens, total_tokens (runs) | Explicit run-level aggregate usage, not individual model attempts. Do not sum with attempt usage. |\n\n## Normalization and missingness\n\nCSV empty fields are null; no literal zero is substituted for missing values. Reported numeric zeros remain zero. `success/succeeded/completed/complete/ok/done` normalize to success; `failure/failed/errored/error/blocked` to failure; `timeout/timed_out/timedout` to timeout; `cancelled/canceled/killed` to cancelled; `aborted/interrupted` to interrupted. `running/inProgress/started/pending/skipped` and unrecognized statuses are unknown, not failures. Explicit isError true normalizes to failure; false normalizes to technical success when appropriate.\n\nSource precedence is encoded numerically in setstatus: explicit tool error (7), trajectory lifecycle/artifacts and subagent outcome (6), audit (5), task and tool projection (4), receipt/delivery and Codex turn projection (3), transcript completion/rollout turn (2), legacy text (1). Later processing wins ties; normalized disagreements are flagged. Run conflicts can represent different scope semantics, including intentional handoff interruption versus Gateway completion; original values remain available. Conflicts remain flagged and original statuses preserved. An ordinary retry is not a failed run; a failed individual attempt does not change its enclosing run's outcome. Missing completion never becomes failure. Aborted Codex turns may be expected handoffs/interruptions; do not equate them with failed tasks.\n\nNative mirrored OpenClaw assistant messages without a response ID are not counted as additional model calls when the session is explicitly mapped to a Codex thread. Canonical Codex token_usage_record response IDs supply per-call usage; usage alone does not prove successful completion, so attempt status is unknown unless explicit completion status is linked. Run-level model.completed usage is not treated as an individual call. Tool calls/results/audit records with the same call ID merge; response records sharing response ID merge; transcript and rollout event duplicates are suppressed.\n\nLM Studio log bodies may contain private prompts, credentials and responses. These are parsed only in process and never exported. Only timestamp, model, endpoint-derived operation category, byte size and explicit request ID enter attempts. Most requests lack request IDs shared with OpenClaw and completion logs: status, duration, usage, session and run linkage therefore stay unknown/null. Unlinked streaming completion or Generated prediction lines are NOT counted again as extra calls. Prediction response IDs matching native response IDs add source provenance/usage to the existing attempt. LM requests cannot be claimed to originate from OpenClaw, may overlap OpenClaw attempts, and must be analyzed as a separate population. Cross-source deduplication is exact where shared IDs exist; unresolved LM overlap cannot be deduplicated reliably.\n\nGateway lane errors, authentication warnings, generic errors and Codex diagnostic warning lines without identifiable individual attempts are inspected but do not manufacture runs or attempts. Failure-only/selected retry diagnostics cannot establish valid failure rates. Audit/trajectory/rollout sources contain both successful and unsuccessful records but retention, instrumentation changes, missing attempts and filtered technical records prevent a claim of a complete experimental denominator.\n\n## Coverage, limitations and integrity\n\n'''
 text += '### Execution outcomes versus task outcomes\n\n`status` is a technical execution outcome, never task success. `task_completion_status` is separate and is unknown for every exported observation: no structured criterion-linked verification sufficient to establish task completion was found. Self-reported success, an agent response, a passed shell command, or a terminated Goal does not verify the overall task. `task_acceptance_criteria_recorded` is 1 only for explicit structured criterion fields; otherwise null because criteria may exist in unexported private prose. `task_outcome_independently_verifiable` is unknown without criterion-linked independent evidence. `task_verification_source_reference` remains null without such evidence. No new task execution or acceptance checking was performed.\n\n`task_id` is a pseudonym of persisted task/Goal identity where explicitly available, not an invented one-task-per-run grouping. `task_type` copies recorded task_kind, not a semantic classification of user prompts. Missing task IDs make complete task-level denominators unavailable. Scheduled task/receipt rows merge using the exact recorded cron job/start/receipt composite execution identity. `execution_outcome_evidence` distinguishes a recorded terminal status from unknown.\n\n### Recorded explanatory fields\n\n`model_version` and `model_quantization` preserve explicit fields only, never a guess from a model family or current load. LM request values, if present, are requested settings rather than proof of an effective backend setting. `model_api` records the source API identifier. `configured_model_id` is a spawn/request setting, not proof that model executed. `configured_provider` is reserved for an explicit requested provider. `run_timeout_seconds`, `fast_mode`, `thinking_level`, `reasoning_level`, `configured_max_concurrent`, `configured_subagent_max_concurrent` are direct settings; configured limits are NOT measured concurrency. `harness_name`, `harness_version`, `node_version`, `os_platform`, `os_arch`, `os_release`, and `openclaw_version` are execution-time software/environment metadata only. `codex_version` is the CLI version explicitly recorded in the Codex session metadata and linked by its exact turn/thread identities, not the currently installed version. Run-level `error_type` and `error_code` preserve structured turn errors only; a failed turn is not automatically a failed individual model call.\n\nAttempt `temperature`, `top_p`, `top_k`, `seed`, `stream`, `max_output_tokens` are explicitly logged request parameters, not necessarily effective backend values. Missing parameters remain null. `context_utilization` is reserved for a directly recorded value, not computed from assumed context. `recorded_numeric_metrics_json` holds numeric metadata only: key names/units are preserved (e.g. spans.<name>Ms or itemLifecycle.<count>); no causal interpretation is added. This is a documented sparse extension for direct numeric metrics with source provenance. `parent_attempt_id` links explicitly nested tool operations to the invoking attempt. `source_selected_logging` flags selected/routing diagnostic instrumentation independently of whether a particular event is failure-only.\n\n'
 text+='Cutoff: `'+CUT+'`. Export: '+str(report['runs'])+' runs, '+str(report['attempts'])+' attempts; '+str(report['linked_attempts'])+' attempt-to-run links; '+str(report['parent_linked_runs'])+' explicit parent links.\n\n'
 text+='Current Goal database and flow-run row counts are in the manifest; zero rows mean no accessible persisted Goal executions in that source, not proof no Goals were ever used. Current scheduled job definitions are inspected through database schemas; receipts/tasks, not definitions, supply historical executions. Compressed deleted-session archives, database transcript archives and the retained recovery baseline backup are included. Trash is inaccessible under macOS privacy permissions. Backups/openclaw is empty. Historical record deletion, unavailable machines/cloud workers, unmounted stores, remote provider logs, expired rotations and records not persisted locally are outside observable coverage. No remedial access or restore was attempted.\n\n'
 text+='LM Studio timestamps omit timezone: interpreted using the host America/New_York zone, including DST. This is a documented timezone conversion assumption, not a measured offset in the log. UTC/offset timestamps elsewhere preserve their source offsets. Millisecond precision in normalized strings does not imply source precision; LM server timestamps are typically whole seconds.\n\n'
 text+='No EDA, hypothesis testing, root-cause labels, task-quality labels or remediation research was performed. This is an observational local-record census, not a randomized or complete sample of physical requests. Observed denominators are the exported rows within each instrumented population, including success, failure and unknown outcomes; no complete task-level denominator is asserted. Do not drop unknown outcomes silently, combine task/run/attempt levels, or pool LM and OpenClaw populations. No timestamp-nearness matching was used. Historical collection includes the current incomplete collection session when records precede the cutoff. Integrity checks cover identifier uniqueness, foreign keys, nonnegative numeric values, accepted status vocabulary and exported credential/email patterns. A schema allowlist excludes conversation text, prompts, arguments, tool output, free-form errors, auth profile IDs, owner/contact IDs, URLs, auth headers and config secrets.\n\n'
 text+='### Source coverage\n\n| Source alias | Kind | Observed first UTC | Observed last UTC | Records inspected |\n|---|---|---|---|---|\n'
 for k,s in sorted(SOURCES.items()):text+='| '+k+' | '+s['kind']+' | '+str(s.get('first_timestamp_utc') or '')+' | '+str(s.get('last_timestamp_utc') or '')+' | '+str(s.get('records_read',0))+' |\n'
 text+='\n### Missing-value counts\n\n| Table | Column | Missing | Rows |\n|---|---|---:|---:|\n'
 for name,cols in report['missingness'].items():
  for k,n in cols.items():text+=f'| {name} | {k} | {n} | {report[name]} |\n'
 if WARN:text+='\n### Collection warnings\n\n'+''.join('- '+json.dumps(w)+'\n' for w in WARN)
 (OUT/'data_dictionary.md').write_text(text);os.chmod(OUT/'data_dictionary.md',0o600)

if __name__=='__main__':main()
