from pathlib import Path
import zipfile,xml.etree.ElementTree as ET,json,re,hashlib
root=Path(__file__).resolve().parents[1];src=root/'references/source-pack'
ns={'a':'http://schemas.openxmlformats.org/drawingml/2006/main','p':'http://schemas.openxmlformats.org/presentationml/2006/main'}
z=zipfile.ZipFile(src/'03_Business_Re-Imagined_Original.pptx');slides=[]
for i in range(1,88):
 e=ET.fromstring(z.read(f'ppt/slides/slide{i}.xml'))
 text='\n'.join(x.text or '' for x in e.findall('.//a:t',ns))
 slides.append({'number':i,'hidden':e.attrib.get('show')=='0','text':text,'pictures':len(e.findall('.//p:pic',ns)),'shapes':len(e.findall('.//p:sp',ns))})
(root/'data/slides.json').write_text(json.dumps(slides,indent=2),encoding='utf8')
print('PowerPoint:',len(slides),'slides;',sum(not s['hidden'] for s in slides),'visible;',sum(s['hidden'] for s in slides),'hidden')
for i in [32,47,48,67,70]:print('Visual-only slide',i,slides[i-1]['pictures'],'pictures;',slides[i-1]['shapes'],'shapes')
print('Transcripts:',*[p.name for p in src.glob('*.txt')])
