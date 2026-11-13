import pathlib,json,urllib.request,hashlib,struct,shutil,fcntl
import mlx.core as mx
from mlx_lm.utils import load,save
R=pathlib.Path(__file__).resolve().parent;LM=next(pathlib.Path.home().glob('.*/bin/lms')).parent.parent
source=LM/'models/jason-schulz/Gemma-4-26B-A4B-Hermes-VLM-MLX';out=LM/'models/clu-local/Gemma-4-26B-A4B-Hermes-TEXT-local-MLX';staging=R/'gemma-text-staging'
if out.exists() or staging.exists():raise RuntimeError('Output or staging exists; reconcile before retry')
meta=json.loads((R/'jason-schulz--Gemma-4-26B-A4B-Hermes-VLM-MLX.json').read_text());expected={x['rfilename'] for x in meta['siblings'] if x['rfilename'].endswith('.safetensors')}
verified={x.get('filename') for x in json.loads((R/'expanded-downloads.json').read_text()) if x.get('repo')==meta['id'] and x.get('status')=='verified'}
if not expected<=verified:raise RuntimeError('Source shards not all checksum-verified')
lockdir=pathlib.Path.home()/'.cache/clu-local-workers';lockdir.mkdir(parents=True,exist_ok=True);lock=(lockdir/'controller.lock').open('a');fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
rows=json.load(urllib.request.urlopen('http://127.0.0.1:1234/api/v1/models',timeout=10))['models']
if any(x['type']=='llm' and x['loaded_instances'] for x in rows):raise RuntimeError('Shared text model loaded; defer export')
print('LOADING PUBLIC GEMMA LANGUAGE TOWER ONLY',flush=True);model,tokenizer,cfg=load(str(source),lazy=True,return_config=True,trust_remote_code=False);cfg['language_model_only']=True;cfg.pop('vision_config',None);cfg['architectures']=['Gemma4ForCausalLM']
save(staging,str(source),model,tokenizer,cfg,donate_model=True)
for name in ['tokenizer.json','tokenizer_config.json','chat_template.jinja']:shutil.copyfile(source/name,staging/name)
def headers(folder):
 result={}
 for f in folder.glob('*.safetensors'):
  with f.open('rb') as h:n=struct.unpack('<Q',h.read(8))[0];header=json.loads(h.read(n))
  for name,spec in header.items():
   if name=='__metadata__':continue
   result[name]=(f,8+n,spec)
 return result
def digest(entry):
 f,offset,spec=entry;start,end=spec['data_offsets'];remaining=end-start;h=hashlib.sha256()
 with f.open('rb') as stream:
  stream.seek(offset+start)
  while remaining:
   chunk=stream.read(min(8*1024*1024,remaining))
   if not chunk:raise RuntimeError('Truncated tensor')
   h.update(chunk);remaining-=len(chunk)
 return h.hexdigest()
original=headers(source);exported=headers(staging);checks=[]
for name,entry in exported.items():
 if not name.startswith('language_model.') or name not in original:raise RuntimeError('Unexpected text export tensor '+name)
 if entry[2]['shape']!=original[name][2]['shape'] or entry[2]['dtype']!=original[name][2]['dtype']:raise RuntimeError('Tensor shape/type changed '+name)
 a,b=digest(entry),digest(original[name])
 if a!=b:raise RuntimeError('Language weight changed '+name)
 checks.append({'tensor':name,'sha256':a})
assert set(exported)=={k for k in original if k.startswith('language_model.')}
receipt={'source_repo':meta['id'],'source_revision':meta['sha'],'method':'text-only export of public VLM checkpoint; no weight changes or requantization','original_text_repo':'jason-schulz/Gemma-4-26B-A4B-Hermes-MLX','original_text_access':'HTTP 401; exact equivalence with inaccessible original not independently verifiable','all_exported_tensors_byte_identical':True,'tensor_count':len(checks),'tensor_hashes':checks,'inference_performed':False}
(staging/'PREPARATION_PROVENANCE.json').write_text(json.dumps(receipt,indent=2));out.parent.mkdir(parents=True,exist_ok=True);staging.rename(out);(R/'gemma-text-export-receipt.json').write_text(json.dumps(receipt,indent=2));print('GEMMA TEXT EXPORT COMPLETE',out,flush=True)
