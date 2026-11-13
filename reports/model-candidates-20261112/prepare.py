import pathlib,json,hashlib,shutil
R=pathlib.Path(__file__).resolve().parent
source=pathlib.Path('/Users/clu/.openclaw/media/inbound/pasted-text-1794537447773---8e80600d-2f03-488b-9ca8-9338f27c5969.txt')
shutil.copyfile(source,R/'OWNER_HANDOFF.txt')
(R/'source-receipt.json').write_text(json.dumps({'source_filename':source.name,'bytes':source.stat().st_size,'sha256':hashlib.sha256(source.read_bytes()).hexdigest()},indent=2)+chr(10))
baseline=json.loads((R/'baseline-inventory.json').read_text());saved=json.loads((R/'baseline-saved-settings.json').read_text())
models=[]
for row in baseline:
 if row['type']!='llm':continue
 fields=saved[row['modelKey']+'.json']['load']['fields'];ctx=next(x['value'] for x in fields if x['key']=='llm.load.contextLength')
 models.append({'role':'baseline','model_key':row['modelKey'],'format':row['format'],'quantization':row['quantization']['name'],'size_bytes':row['sizeBytes'],'advertised_context':row['maxContextLength'],'saved_load_context':ctx,'proposed_role_fit_context':ctx,'common_short_context':8192,'runtime_verified':False})
for repo,filename,base,ctx,sampling,origin in [
 ('ClankLabs/Wrench-9B-Q4_K_M-GGUF','Wrench-9B-Q4_K_M-GGUF .gguf','qwen/qwen3.5-9b',8192,{'temperature':0.4,'top_k':20,'top_p':0.95,'min_p':0,'presence_penalty':1.5},'publisher card'),
 ('samuelcardillo/Carnice-Qwen3.6-MoE-35B-A3B-GGUF','Carnice-Qwen3.6-MoE-35B-A3B-Q4_K_M.gguf','qwen/qwen3.6-35b-a3b',32768,{'temperature':0.3,'top_p':0.9},'owner handoff hypothesis; not a publisher sampling recommendation'),
 ('fesalfayed/gpt-oss-20b-hermes_agent-tool-finetune_gguf','gpt-oss-20b-hermes.Q4_K_M.gguf','openai/gpt-oss-20b',32768,{'temperature':0.7,'top_p':0.95,'min_p':0.1,'repetition_penalty':1.0},'publisher card; strict-task temperature 0.2 is a separate labeled profile')]:
 meta=json.loads((R/(repo.replace('/','--')+'.json')).read_text());item=next(x for x in meta['siblings'] if x['rfilename']==filename)
 models.append({'role':'candidate','repo':repo,'revision':meta['sha'],'filename':filename,'provisional_model_key':repo+'/'+filename,'resolved_lms_model_key':None,'baseline':base,'format':'gguf','quantization':'Q4_K_M','size_bytes':item['size'],'expected_sha256':item['lfs']['sha256'],'license':meta['cardData']['license'],'proposed_role_fit_context':ctx,'common_short_context':8192,'context_status':'Wrench card explicitly specifies 8192; others require runtime/long-context qualification, not guaranteed by architecture','sampling':sampling,'sampling_provenance':origin,'reasoning_requested':'low' if 'gpt-oss' in repo else 'off_if_supported','runtime_verified':False,'template_status':'preserve embedded native Qwen/Harmony template; verify rendered roles and parser before scoring','install_status':'consult downloads.json'})
manifest={'schema':1,'status':'prepared-not-runtime-qualified','scope':'download and standalone profiles only; no model loading, inference, routing or active config changes','models':models,'evaluation_policy':{'short_context':8192,'output_cap_initial':4096,'context_accounting':'tokenize rendered prompt; include tools/history/reasoning/output reserve; do not truncate silently','controlled_track':{'temperature':0,'purpose':'reproduce existing deterministic worker baseline; not sole suitability verdict'},'tuned_track':'publisher/reasonable per-model sampling; equivalent task, attempts, wall-time and output budgets; record seeds/repeats, do not claim bitwise determinism','long_context':'separate role-fit track; do not reduce all models to smallest context or push Wrench beyond its documented 8K','runtime_preflight_required':True,'tools':'no real side effects; keep deterministic executor authority','constraints':'formats/quantizers/backends differ from installed baselines; rankings describe deployed configurations, not isolated fine-tune gains'}}
(R/'trial-profiles.json').write_text(json.dumps(manifest,indent=2)+chr(10))
print('Prepared',len(models),'model profiles; no active settings changed')
