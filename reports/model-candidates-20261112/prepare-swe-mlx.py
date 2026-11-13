import pathlib,json,urllib.request,gc,hashlib,time,shutil
import mlx.core as mx
import mlx.nn as nn
from mlx.utils import tree_unflatten
from mlx_lm.utils import load,save
from mlx_lm.tuner.lora import LoRALinear
R=pathlib.Path(__file__).resolve().parent
LM=next(pathlib.Path.home().glob('.*/bin/lms')).parent.parent
rows=json.load(urllib.request.urlopen('http://127.0.0.1:1234/api/v1/models',timeout=10))['models']
if any(x['type']=='llm' and x['loaded_instances'] for x in rows):raise RuntimeError('Shared text model is loaded; defer offline fusion rather than competing')
base=next((LM/'models').glob('*/Qwen3.8-27B-MLX-4bit'))
out=LM/'models/clu-local/Qwen3.8-27B-SWE-superqwen-MLX-4bit'
staging=R/'swe-merged-staging'
if out.exists() or staging.exists():raise RuntimeError('Output/staging already exists; reconcile before retry')
source=R/'swe-adapter-source'
adapter_cfg=json.loads((source/'adapter_config.json').read_text());assert adapter_cfg['r']==16 and adapter_cfg['lora_alpha']==32 and not adapter_cfg['use_dora'] and not adapter_cfg['use_rslora']
weights=mx.load(str(source/'adapter_model.safetensors'));pairs={}
for name,w in weights.items():
 prefix='base_model.model.model.language_model.layers.'
 if not name.startswith(prefix):raise ValueError('Unexpected adapter tensor '+name)
 native='language_model.model.layers.'+name[len(prefix):];module,part=native.rsplit('.lora_',1);side,suffix=part.split('.')
 if side not in ['A','B'] or suffix!='weight':raise ValueError('Unexpected LoRA suffix '+name)
 pairs.setdefault(module,{})[side]=w
assert len(pairs)==400 and all(set(p)=={'A','B'} for p in pairs.values())
print('LOADING BASE LAZILY',flush=True);model,tokenizer,cfg=load(str(base),lazy=True,return_config=True,trust_remote_code=False);modules=dict(model.named_modules())
for name,pair in pairs.items():
 if name not in modules:raise ValueError('Missing base module '+name)
 layer=modules[name]
 if not isinstance(layer,nn.QuantizedLinear):raise ValueError('Expected quantized linear '+name)
 a,b=pair['A'],pair['B'];expected=(layer.weight.shape[0],layer.weight.shape[1]*32//layer.bits)
 if a.shape!=(16,expected[1]) or b.shape!=(expected[0],16):raise ValueError('Shape mismatch '+name)
print('ALL 400 ADAPTER MODULES MATCH',flush=True)
checks=[]
for i,(name,pair) in enumerate(sorted(pairs.items())):
 layer=modules.pop(name);lora=LoRALinear.from_base(layer,r=16,scale=2.0,dropout=0.0);lora.lora_a=pair['A'].T;lora.lora_b=pair['B'].T
 fused=lora.fuse();mx.eval(fused.parameters())
 changed=bool(mx.any(fused.weight!=layer.weight).item());checks.append({'module':name,'packed_weights_changed':changed})
 model.update_modules(tree_unflatten([(name,fused)]));del layer,lora,fused;gc.collect();mx.clear_cache()
 if (i+1)%25==0:print('FUSED',i+1,'/400',flush=True)
assert all(x['packed_weights_changed'] for x in checks)
cfg['language_model_only']=True
print('SAVING SEPARATE QUANTIZED CHECKPOINT',flush=True);save(staging,str(base),model,tokenizer,cfg,donate_model=True)
# Preserve the fine-tune tokenizer/template rather than inventing a prompt format.
for name in ['tokenizer.json','tokenizer_config.json','chat_template.jinja']:shutil.copyfile(source/name,staging/name)
receipt={'source_repo':'superqwen/qwen3.8-27b-swe-lora','source_revision':'c26577ac18d6f0ba37d728aee6ca5fc1b6d5f09a','adapter_sha256':hashlib.sha256((source/'adapter_model.safetensors').read_bytes()).hexdigest(),'base_path':str(base),'base_config_sha256':hashlib.sha256((base/'config.json').read_bytes()).hexdigest(),'method':'native MLX LoRALinear fuse: W_quant_base + (alpha/r) B A, requantized 4bit affine group64; not a BF16 merge','adapter_modules':len(checks),'all_modules_changed':True,'checks':checks,'inference_performed':False,'peak_memory_bytes':mx.get_peak_memory()}
(staging/'PREPARATION_PROVENANCE.json').write_text(json.dumps(receipt,indent=2))
out.parent.mkdir(parents=True,exist_ok=True);staging.rename(out);(R/'swe-merge-receipt.json').write_text(json.dumps(receipt,indent=2));print('SWE PREPARATION COMPLETE',out,flush=True)
