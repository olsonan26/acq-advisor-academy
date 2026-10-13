from research import fetch,ROOT
import json,re,urllib.parse,concurrent.futures
rows=json.loads((ROOT/'data/sources.json').read_text())
def check(row):
 raw,p,e=fetch(row['url']);plain=raw.replace('\\"','"')
 videos=re.findall(r'"muxPlaybackId":"([^"]+)","title":"([^"]+)"',plain)
 candidates=[v for v in videos if v[1].lower()==row['title'].lower()]
 if not candidates and row['title']=='Start Here':candidates=[v for v in videos if 'start' in v[1].lower()]
 row['playerDetected']=bool(videos);row['captionAccess']='No matching public caption track located'
 if candidates:
  pid=candidates[0][0];row['playbackId']=pid
  manifest,_,err=fetch('https://stream.mux.com/'+pid+'.m3u8')
  row['captionAccess']=err or 'Public player manifest accessible; no subtitle track found'
  tracks=re.findall(r'#EXT-X-MEDIA:[^\n]*TYPE=SUBTITLES[^\n]*URI="([^"]+)"',manifest)
  row['captionTracks']=tracks
  if tracks:
   row['captionAccess']='Public subtitle track located; pending teaching analysis'
 return row
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:rows=list(pool.map(check,rows))
(ROOT/'data/sources.json').write_text(json.dumps(rows,indent=2),encoding='utf8')
print('Pages',len(rows),'players',sum(r['playerDetected'] for r in rows),'matching players',sum('playbackId' in r for r in rows),'caption tracks',sum(bool(r.get('captionTracks')) for r in rows))
