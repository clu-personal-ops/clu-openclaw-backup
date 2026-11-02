from pathlib import Path
import xml.etree.ElementTree as E,json,re
from html.parser import HTMLParser
p=Path(__file__).parent;ns={'a':'http://www.w3.org/2005/Atom'}
class Text(HTMLParser):
 def __init__(self):super().__init__();self.o=[]
 def handle_starttag(self,t,a):
  if t in ['p','li','pre','blockquote','br']:self.o.append('\n')
  if t=='a':self.o.append(' ['+dict(a).get('href','')+'] ')
 def handle_endtag(self,t):
  if t in ['p','li','pre','blockquote']:self.o.append('\n')
 def handle_data(self,d):self.o.append(d)
def txt(s):
 x=Text();x.feed(s or '');return re.sub('\n{3,}','\n\n',''.join(x.o)).strip()
cs=json.loads((p/'comment-corpus.json').read_text()) if (p/'comment-corpus.json').exists() else [];by={c['id']:c for c in cs}
for f in ['rss-response','rss-limit500.xml','rss-limit1000.xml','rss-old.xml','rss-new.xml','rss-controversial.xml','rss-top.xml','rss-confidence.xml']:
 if not (p/f).exists():continue
 try:es=E.fromstring((p/f).read_bytes()).findall('a:entry',ns)
 except E.ParseError:continue
 for order,e in enumerate(es):
  i=e.findtext('a:id',namespaces=ns)
  if i in by:
   by[i].setdefault('sources',[by[i].get('source')]);by[i]['sources']=list(dict.fromkeys(by[i]['sources']+[f]));continue
  s=e.findtext('a:content',namespaces=ns);d={'id':i,'ref':'OP' if i.startswith('t3_') else 'C%03d'%(len(cs)), 'author':(e.findtext('a:author/a:name',namespaces=ns) or '[unavailable]').removeprefix('/u/'),'permalink':e.find('a:link',ns).get('href'),'updated':e.findtext('a:updated',namespaces=ns),'body_html':s,'body':txt(s),'parent_id':None,'score':None,'source':f,'sources':[f],'first_feed_order':order};cs.append(d);by[i]=d
(p/'comment-corpus.json').write_text(json.dumps(cs,indent=2,ensure_ascii=False));(p/'comment-corpus.md').write_text('\n\n'.join('## '+d['ref']+' — '+d['author']+'\n'+d['permalink']+'\n\n'+d['body'] for d in cs))
print('Entries',len(cs),'comments',len(cs)-1,'deleted',sum(x['body']=='[deleted]' for x in cs),'removed',sum(x['body']=='[removed]' for x in cs))
