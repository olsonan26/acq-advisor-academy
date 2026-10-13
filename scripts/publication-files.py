import json,subprocess,sys,base64
from pathlib import Path
root=Path(__file__).resolve().parents[1]
if len(sys.argv)>1:
 name=sys.argv[1];offset=int(sys.argv[2]);size=int(sys.argv[3]);data=(root/name).read_bytes()[offset:offset+size]
 print(base64.b64encode(data).decode());sys.exit()
entries=[]
for line in subprocess.check_output(['git','ls-tree','-r','HEAD'],cwd=root).decode().splitlines():
 meta,path=line.split('\t',1);mode,kind,sha=meta.split()
 if path.endswith('.png'):
  entries.append({'path':path,'mode':mode,'binary':True,'size':(root/path).stat().st_size})
 else:
  content=subprocess.check_output(['git','cat-file','blob',sha],cwd=root).decode('utf8')
  entries.append({'path':path,'mode':mode,'binary':False,'content':content})
print(json.dumps(entries,ensure_ascii=True))
