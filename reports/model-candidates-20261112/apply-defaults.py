import pathlib,json,subprocess,hashlib,time,sys
R=pathlib.Path(__file__).resolve().parent
LM=next(pathlib.Path.home().glob('.*/bin/lms')).parent.parent
rows=json.loads(subprocess.check_output([str(LM/'bin/lms'),'ls','--json']))
SPECS=[('Wrench-9B-Q4_K_M-GGUF',32768,0.4,0.95,20,0,1.5,False,8192),('Carnice-Qwen3.6-MoE-35B-A3B-GGUF',32768,0.3,0.9,20,0,0,False,8192),('gpt-oss-20b-hermes_agent-tool-finetune_gguf',32768,0.7,0.95,40,0.1,0,None,8192),('Qwen3.8-27B-SWE-superqwen-MLX-4bit',32768,0.0,0.95,20,0,0,True,8192),('Gemma-4-26B-A4B-Hermes-VLM-MLX',32768,0.5,0.9,40,0,0,False,8192),('Gemma-4-26B-A4B-Hermes-TEXT-local-MLX',32768,0.5,0.9,40,0,0,False,8192)]
records=[]
backup=R/'defaults-backups';backup.mkdir(exist_ok=True)
for suffix,ctx,temp,top_p,top_k,min_p,presence,thinking,maxout in SPECS:
 matches=[row for row in rows if suffix in row.get('path','') and row['type']=='llm']
 if len(matches)!=1:records.append({'family':suffix,'status':'waiting-for-complete-indexed-checkpoint','matches':len(matches)});continue
 row=matches[0];identity=row['indexedModelIdentifier'];p=LM/'.internal/user-concrete-model-default-config'/(identity+'.json')
 existed=p.exists();old=p.read_text() if existed else None;safe=hashlib.sha256(identity.encode()).hexdigest()
 receipt=backup/(safe+'.json')
 if not receipt.exists():receipt.write_text(json.dumps({'path':str(p),'existed':existed,'original_content':old},indent=2))
 d=json.loads(old) if old else {'preset':'','operation':{'fields':[]},'load':{'fields':[]}}
 def merge(section,updates):
  fields=d.setdefault(section,{}).setdefault('fields',[]);index={x['key']:i for i,x in enumerate(fields)}
  for k,v in updates.items():
   field={'key':k,'value':v}
   if k in index:fields[index[k]]=field
   else:fields.append(field)
 checked=lambda value:{'checked':True,'value':value}
 merge('load',{'llm.load.contextLength':ctx,'llm.load.numParallelSessions':1})
 op={'llm.prediction.temperature':temp,'llm.prediction.topPSampling':checked(top_p),'llm.prediction.topKSampling':top_k,'llm.prediction.minPSampling':{'checked':min_p>0,'value':min_p},'llm.prediction.repeatPenalty':{'checked':False,'value':1.0},'llm.prediction.maxPredictedTokens':checked(maxout),'llm.prediction.contextOverflowPolicy':'stopAtLimit'}
 if row['format']=='gguf':op['llm.prediction.llama.presencePenalty']={'checked':presence!=0,'value':presence}
 if thinking is not None:op['llm.prediction.reasoning.enableThinking']=thinking
 merge('operation',op);p.parent.mkdir(parents=True,exist_ok=True);tmp=p.with_suffix('.json.tmp');tmp.write_text(json.dumps(d,indent=2));tmp.replace(p)
 assert json.loads(p.read_text())==d
 records.append({'family':suffix,'status':'defaults-persisted-readback-verified','model_key':row['modelKey'],'indexed_identity':identity,'path':str(p),'context_length':ctx,'max_output_tokens':maxout,'thinking':thinking,'default_config':d,'runtime_effective_verified':False})
(R/'default-config-receipts.json').write_text(json.dumps(records,indent=2));print(json.dumps([{k:v for k,v in rec.items() if k!='default_config'} for rec in records],indent=2))
