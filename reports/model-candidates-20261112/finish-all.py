import pathlib,json,subprocess,select,os,time,sys,hashlib,traceback
R=pathlib.Path(__file__).resolve().parent;LM=next(pathlib.Path.home().glob('.*/bin/lms')).parent.parent;native=next(LM.glob('extensions/backends/vendor/_amphibian/app-mlx-generate-mac14-arm64@42/bin/python3'))
def run(args,name,timeout=1200):
 with (R/name).open('w') as log:
  p=subprocess.run([str(x) for x in args],stdout=log,stderr=subprocess.STDOUT,timeout=timeout)
 if p.returncode:raise RuntimeError('Step failed; inspect '+name)
def wait_processes(pids):
 kq=select.kqueue();pending=set()
 try:
  for pid in pids:
   try:kq.control([select.kevent(pid,filter=select.KQ_FILTER_PROC,flags=select.KQ_EV_ADD|select.KQ_EV_ENABLE|select.KQ_EV_ONESHOT,fflags=select.KQ_NOTE_EXIT)],0,0);pending.add(pid)
   except ProcessLookupError:pass
  print('Waiting event-driven for existing download processes',sorted(pending),flush=True);deadline=time.monotonic()+7200
  while pending:
   remaining=deadline-time.monotonic()
   if remaining<=0:raise TimeoutError('Download wait limit reached; preserve transfers and receipts')
   events=kq.control(None,len(pending),remaining)
   for event in events:pending.discard(event.ident);print('Observed download-process exit',event.ident,flush=True)
 finally:kq.close()
try:
 wait_processes([51965,53372])
 first=json.loads((R/'downloads.json').read_text());expanded=json.loads((R/'expanded-downloads.json').read_text())
 if len(first)!=3 or any(x['status']!='verified' for x in first):raise RuntimeError('Original candidate downloads incomplete or failed')
 if any(x['status']!='verified' for x in expanded):raise RuntimeError('Expanded downloads incomplete or failed')
 print('All remote files verified; preparing public Gemma text-only variant',flush=True)
 if not (R/'gemma-text-export-receipt.json').exists():run([native,R/'prepare-gemma-text.py'],'gemma-text-preparation.log',1800)
 run([sys.executable,R/'apply-defaults.py'],'final-default-application.log',120)
 rows=json.loads((R/'default-config-receipts.json').read_text());assert len(rows)==6 and all(x['status']=='defaults-persisted-readback-verified' for x in rows)
 needed=[]
 for row in rows:
  p=R/('readiness-'+row['model_key'].replace('/','--')+'.json')
  old=json.loads(p.read_text()) if p.exists() else {}
  if old.get('status')!='load-and-default-context-verified' or old.get('observed_context')!=row['context_length']:needed.append(row['model_key'])
 if needed:run([sys.executable,R/'verify-ready.py',*needed],'final-readiness.log',1800)
 run([sys.executable,R/'inspect_gguf.py'],'final-gguf-metadata.log',120)
 inventory=json.loads(subprocess.check_output([str(LM/'bin/lms'),'ls','--json']));(R/'final-inventory.json').write_text(json.dumps(inventory,indent=2))
 baseline=json.loads((R/'baseline-saved-settings.json').read_text());folder=LM/'.internal/user-concrete-model-default-config'
 assert all(json.loads((folder/k).read_text())==v for k,v in baseline.items()),'OG5 saved defaults changed externally; inspect, do not overwrite'
 result=[]
 for row in rows:
  p=R/('readiness-'+row['model_key'].replace('/','--')+'.json');ready=json.loads(p.read_text()) if p.exists() else {}
  result.append({'family':row['family'],'model_key':row['model_key'],'hardware_viable':True,'context_length':row['context_length'],'defaults_persisted':True,'readiness':ready.get('status','missing'),'owned_instance_unloaded':ready.get('owned_instance_unloaded',False),'source_provenance':'local text export from public VLM; original text repo inaccessible' if 'TEXT-local' in row['family'] else 'local quantized-base adapter merge' if 'SWE-superqwen' in row['family'] else 'pinned publisher checkpoint'})
 success=all(x['readiness']=='load-and-default-context-verified' and x['owned_instance_unloaded'] for x in result)
 summary={'status':'six-practical-variants-prepared' if success else 'readiness-blocked','families':result,'original_text_repository':'HTTP401; public-language-tower derivative is explicitly labeled, not claimed exact original','og5_saved_defaults_unchanged':True,'generation_or_benchmarking_performed':False,'pipeline_code_modified':False}
 (R/'FINAL_SUMMARY.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2),flush=True)
 if not success:sys.exit(2)
 print('MODEL PREPARATION FINISHED; return evidence-backed six-family result to owner',flush=True)
except BaseException as exc:
 (R/'completion-blocker.json').write_text(json.dumps({'error':str(exc),'next':'Inspect named log and existing effects before retry; preserve original downloads, model files and settings'},indent=2));traceback.print_exc();print('MODEL PREPARATION NEEDS FOLLOW-UP:',str(exc),flush=True);sys.exit(1)
