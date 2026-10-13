import urllib.request, urllib.parse, json, re, concurrent.futures
from html.parser import HTMLParser
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
 def __init__(self):
  super().__init__(); self.links=[]; self.current=None; self.text=[]; self.media=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='a': self.current=[a.get('href',''),'']
  if tag in ('iframe','video','track','source'): self.media.append({'tag':tag,**a})
 def handle_data(self,data):
  self.text.append(data)
  if self.current: self.current[1]+=data
 def handle_endtag(self,tag):
  if tag=='a' and self.current: self.links.append(self.current); self.current=None
def fetch(url):
 try:
  raw=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=30).read().decode()
  p=Page();p.feed(raw);return raw,p,None
 except Exception as e:return '',Page(),str(e)
courses={'Business Scaling':'https://www.acquisition.com/training/scalingstart','$100M Offers':'https://www.acquisition.com/training/offers','$100M Leads':'https://www.acquisition.com/training/leads','$100M Money Models':'https://www.acquisition.com/training/money/context'}
ledger=[]
for course,start in courses.items():
 raw,p,error=fetch(start)
 (ROOT/'research').mkdir(exist_ok=True)
 (ROOT/'research'/ (re.sub(r'[^a-z]+','-',course.lower()).strip('-')+'.html')).write_text(raw,encoding='utf8')
 links=[(start,'Context' if 'Leads' in course or 'Money' in course else 'Start Here')]
 for href,title in p.links:
  url=urllib.parse.urljoin(start,href);title=' '.join(title.split())
  keep=('/training/money/' in url if 'Money' in course else bool(re.search(r'/training/offers(?:\d+|freebonus)?$',url)) if 'Offers' in course else bool(re.search(r'/training/leads(?:\d+|freebonus)?$',url)) if 'Leads' in course else '/training/' in url and not any(x in url for x in ['/offers','/leads','/money/']))
  if keep and '#' not in url and title not in ('Education','Scaling Course') and url not in [x[0] for x in links]:links.append((url,title))
 if not links:links=[(start,'Context')]
 def inspect(item):
  url,title=item;r,q,e=fetch(url)
  downloads=[{'url':urllib.parse.urljoin(url,h),'title':' '.join(t.split())} for h,t in q.links if re.search(r'\.pdf|download|worksheet|transcript',h,re.I)]
  players=[m for m in q.media if any(x in str(m).lower() for x in ['wistia','vimeo','youtube','video','track'])]
  ids=list(dict.fromkeys(re.findall(r'(?:wistia_async_|hashedId["\s:]+)([a-z0-9]{10})',r)))
  return {'course':course,'title':title,'url':url,'accessed':'Public HTML and navigation only' if not e else 'Page request failed','status':'Teaching unverified; transcript needed','duration':None,'timestamps':[],'media':players,'wistiaIds':ids,'resources':downloads,'error':e,'keyPoints':[],'confidence':'High for observed menu title and URL; no confidence assigned to unaccessed teaching'}
 with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool: rows=list(pool.map(inspect,links))
 for i,row in enumerate(rows):row['order']=i+1
 ledger+=rows
 print(course,len(rows),flush=True)
(ROOT/'data').mkdir(exist_ok=True)
(ROOT/'data'/'sources.json').write_text(json.dumps(ledger,indent=2),encoding='utf8')
print('Inventory written:',len(ledger))
