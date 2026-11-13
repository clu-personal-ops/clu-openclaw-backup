import struct,json,pathlib,hashlib
R=pathlib.Path(__file__).resolve().parent
def metadata(path):
 with path.open('rb') as f:
  def number(fmt):
   n=struct.calcsize('<'+fmt);raw=f.read(n)
   if len(raw)!=n:raise ValueError('truncated metadata')
   return struct.unpack('<'+fmt,raw)[0]
  def string():
   n=number('Q')
   if n>16000000:raise ValueError('metadata string exceeds cap')
   v=f.read(n)
   if len(v)!=n:raise ValueError('truncated string')
   return v.decode('utf-8',errors='replace')
  def value(t):
   if t==8:return string()
   if t==9:
    subtype=number('I');count=number('Q')
    if count>1000000:raise ValueError('metadata array exceeds cap')
    for _ in range(count):value(subtype)
    return {'array_items':count,'type':subtype}
   return number({0:'B',1:'b',2:'H',3:'h',4:'I',5:'i',6:'f',7:'?',10:'Q',11:'q',12:'d'}[t])
  if f.read(4)!=b'GGUF':raise ValueError('not GGUF')
  version=number('I');tensors=number('Q');count=number('Q')
  if version not in (2,3) or count>100000:raise ValueError('unsupported GGUF header')
  out={'version':version,'tensors':tensors,'metadata_items':count}
  for _ in range(count):
   key=string();v=value(number('I'))
   if key.startswith('general.') or 'context_length' in key or 'rope.' in key or 'chat_template' in key:out[key]=v
  out['metadata_bytes']=f.tell()
  return out
if __name__=='__main__':
 rows=[]
 for rec in json.loads((R/'downloads.json').read_text()):
  if rec['status']!='verified':continue
  row={'repo':rec['repo'],'metadata':metadata(pathlib.Path(rec['path']))};rows.append(row)
 (R/'gguf-metadata.json').write_text(json.dumps(rows,indent=2))
 print(json.dumps([{**r,'metadata':{k:(str(v)[:160]+'...' if 'chat_template' in k else v) for k,v in r['metadata'].items()}} for r in rows],indent=2))
