import pathlib,json,urllib.request,subprocess,fcntl,uuid,time,sys
R=pathlib.Path(__file__).resolve().parent;LM=next(pathlib.Path.home().glob('.*/bin/lms')).parent.parent;cli=str(LM/'bin/lms')
def inventory():return json.load(urllib.request.urlopen('http://127.0.0.1:1234/api/v1/models',timeout=15))['models']
lockdir=pathlib.Path.home()/'.cache/clu-local-workers';lockdir.mkdir(parents=True,exist_ok=True);lock=(lockdir/'controller.lock').open('a');fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
recs=json.loads((R/'default-config-receipts.json').read_text());selected=set(sys.argv[1:]);results=[]
for rec in recs:
 if rec.get('model_key') not in selected:continue
 rows=inventory()
 if any(x['type']=='llm' and x['loaded_instances'] for x in rows):results.append({'model':rec['model_key'],'status':'resource-blocked-owner-text-present'});continue
 ident='clu-model-prep-'+uuid.uuid4().hex[:12];journal=R/'owned-readiness-instance.json';journal.write_text(json.dumps({'instance':ident,'model':rec['model_key'],'baseline_instances':[i['id'] for x in rows for i in x['loaded_instances']]}));result={'model':rec['model_key'],'identifier':ident,'requested_default_context':rec['context_length'],'inference_performed':False}
 try:
  proc=subprocess.run([cli,'load',rec['model_key'],'--identifier',ident,'--ttl','600','--yes'],capture_output=True,text=True,timeout=180);result['load_output']=(proc.stdout+proc.stderr)[-6000:]
  if proc.returncode:raise RuntimeError('Load failed')
  row=next(x for x in inventory() if x['key']==rec['model_key']);inst=next(i for i in row['loaded_instances'] if i['id']==ident);ctx=inst['config']['context_length'];result.update(observed_context=ctx,capabilities=row.get('capabilities'),status='load-and-default-context-verified' if ctx==rec['context_length'] else 'default-context-mismatch')
 except Exception as e:result.update(status='failed',error=str(e))
 finally:
  if any(i['id']==ident for x in inventory() for i in x['loaded_instances']):
   p=subprocess.run([cli,'unload',ident],capture_output=True,text=True,timeout=120);result['cleanup_output']=p.stdout+p.stderr
  if any(i['id']==ident for x in inventory() for i in x['loaded_instances']):raise RuntimeError('Owned instance cleanup failed; journal retained')
  journal.unlink();result['owned_instance_unloaded']=True
 results.append(result);(R/('readiness-'+rec['model_key'].replace('/','--')+'.json')).write_text(json.dumps(result,indent=2));print(json.dumps(result),flush=True)
print('READINESS CHECKS FINISHED',flush=True)
