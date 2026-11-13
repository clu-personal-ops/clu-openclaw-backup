import pathlib,json,urllib.parse,subprocess,hashlib,shutil,time
ROOT=pathlib.Path(__file__).resolve().parent
MODELS=pathlib.Path.home()/'.lmstudio/models'
SELECTION=[('ClankLabs/Wrench-9B-Q4_K_M-GGUF','Wrench-9B-Q4_K_M-GGUF .gguf'),('samuelcardillo/Carnice-Qwen3.6-MoE-35B-A3B-GGUF','Carnice-Qwen3.6-MoE-35B-A3B-Q4_K_M.gguf'),('fesalfayed/gpt-oss-20b-hermes_agent-tool-finetune_gguf','gpt-oss-20b-hermes.Q4_K_M.gguf')]
records=[]
for repo,name in SELECTION:
 rec={'repo':repo,'filename':name,'status':'pending'};records.append(rec)
 try:
  meta=json.loads((ROOT/(repo.replace('/','--')+'.json')).read_text());item=next(x for x in meta['siblings'] if x['rfilename']==name)
  expected=item['lfs']['sha256'];size=item['size'];rec.update(revision=meta['sha'],expected_sha256=expected,size_bytes=size)
  folder=MODELS/repo;folder.mkdir(parents=True,exist_ok=True);dest=folder/name;part=folder/(name+'.part')
  if not dest.exists():
   if shutil.disk_usage(folder).free < size+30*1024**3: raise RuntimeError('insufficient free disk with 30GiB reserve')
   url='https://huggingface.co/'+repo+'/resolve/'+meta['sha']+'/'+urllib.parse.quote(name)
   print('DOWNLOADING',repo,size,flush=True)
   subprocess.run(['curl','--fail','--location','--retry','3','--retry-delay','5','--connect-timeout','30','--max-time','3600','--continue-at','-','--output',str(part),url],check=True)
   target=part
  else: target=dest
  if target.stat().st_size!=size: raise RuntimeError('size mismatch')
  h=hashlib.sha256()
  with target.open('rb') as f:
   if f.read(4)!=b'GGUF': raise RuntimeError('not GGUF')
   f.seek(0)
   for chunk in iter(lambda:f.read(8*1024*1024),b''):h.update(chunk)
  if h.hexdigest()!=expected:raise RuntimeError('SHA256 mismatch')
  if target==part:part.rename(dest)
  rec.update(status='verified',path=str(dest),sha256=h.hexdigest());print('VERIFIED',repo,flush=True)
 except Exception as e:rec.update(status='failed',error=str(e));print('FAILED',repo,str(e),flush=True)
 (ROOT/'downloads.json').write_text(json.dumps(records,indent=2)+chr(10))
print('FINISHED',flush=True)
