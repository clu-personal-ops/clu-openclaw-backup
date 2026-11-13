import pathlib,json,urllib.request,urllib.parse,subprocess,hashlib,shutil
R=pathlib.Path(__file__).resolve().parent
LM=next(pathlib.Path.home().glob('.*/bin/lms')).parent.parent
SPECS=[('superqwen/qwen3.8-27b-swe-lora',R/'swe-adapter-source',{'adapter_config.json','adapter_model.safetensors','tokenizer.json','tokenizer_config.json','chat_template.jinja','README.md'}),('jason-schulz/Gemma-4-26B-A4B-Hermes-VLM-MLX',LM/'models/jason-schulz/Gemma-4-26B-A4B-Hermes-VLM-MLX',None)]
records=[]
for repo,dest,allow in SPECS:
 try:
  meta=json.load(urllib.request.urlopen('https://huggingface.co/api/models/'+repo+'?blobs=true',timeout=30));(R/(repo.replace('/','--')+'.json')).write_text(json.dumps(meta,indent=2))
  files=[x for x in meta['siblings'] if x['rfilename'] in allow] if allow else [x for x in meta['siblings'] if '/' not in x['rfilename'] and (x['rfilename'].endswith(('.json','.safetensors','.jinja','.model')) or x['rfilename'] in ['README.md','LICENSE'])]
  total=sum(x['size'] for x in files);print('START',repo,total,flush=True)
  if shutil.disk_usage(LM).free<total+60*1024**3:raise RuntimeError('insufficient disk reserve for expanded preparation')
  dest.mkdir(parents=True,exist_ok=True)
  for item in files:
   name=item['rfilename'];p=dest/name;part=dest/(name+'.part');rec={'repo':repo,'revision':meta['sha'],'filename':name,'size_bytes':item['size'],'path':str(p),'status':'pending'};records.append(rec)
   if not p.exists():
    url='https://huggingface.co/'+repo+'/resolve/'+meta['sha']+'/'+urllib.parse.quote(name)
    subprocess.run(['curl','--fail','--location','--silent','--show-error','--retry','3','--retry-delay','5','--connect-timeout','30','--max-time','3600','--continue-at','-','--output',str(part),url],check=True);target=part
   else:target=p
   if target.stat().st_size!=item['size']:raise RuntimeError('size mismatch '+name)
   h=hashlib.sha256()
   with target.open('rb') as f:
    for chunk in iter(lambda:f.read(8*1024*1024),b''):h.update(chunk)
   expected=item.get('lfs',{}).get('sha256')
   if expected and h.hexdigest()!=expected:raise RuntimeError('SHA256 mismatch '+name)
   if target==part:part.rename(p)
   rec.update(status='verified',sha256=h.hexdigest(),expected_sha256=expected);(R/'expanded-downloads.json').write_text(json.dumps(records,indent=2));print('VERIFIED',repo,name,flush=True)
 except Exception as e:records.append({'repo':repo,'status':'failed','error':str(e)});print('FAILED',repo,str(e),flush=True)
 (R/'expanded-downloads.json').write_text(json.dumps(records,indent=2))
print('EXPANDED DOWNLOADS FINISHED',flush=True)
