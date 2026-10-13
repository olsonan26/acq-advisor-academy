from pathlib import Path
root=Path(__file__).resolve().parents[1]
p=root/'components/academy.tsx'
s=p.read_text(encoding='utf8')
s=s.replace("import Professor from './professor';", "import Professor from './professor';\nimport Review from './review';\nconst groundedCount=lessons.filter(l=>!l.source.toLowerCase().startsWith('supplemental')).length;")
s=s.replace("section==='progress'?<Performance/>:<Sources/>","section==='progress'?<Performance/>:section==='review'?<Review/>:<Sources/>")
anchor='<div className="section-heading"><h2>Your preparation plan</h2>'
block='''<Panel><div className="section-heading"><h2>What you are studying</h2><Link className="text-button" href="/sources">Inspect source evidence →</Link></div><div className="practice-grid"><div><Tag>SUPPLIED SOURCE MATERIAL</Tag><h3>{groundedCount} source-grounded lessons</h3><p>Core teaching cites the original SPS slides or supplied recruitment transcripts. Worked business examples may be supplemental. Transcript timing is approximate, not authenticated video.</p></div><div><Tag>SUPPLEMENTAL BUSINESS EDUCATION</Tag><h3>{lessons.length-groundedCount} supplemental lessons</h3><p>Original finance, operating, and practice explanations. Related official lesson links identify topics; they do not verify the video's teaching.</p></div><div><Tag>VIDEO TEACHING NOT VERIFIED</Tag><h3>{sources.length} official lessons awaiting transcripts</h3><p>Only pages, titles, sequence, and player references are verified. These videos are not represented as completed academy lessons or watched teaching.</p></div></div><Link className="button secondary" href="/review">See three completed demonstrations <ArrowRight size={16}/></Link></Panel>'''
if anchor in s:s=s.replace(anchor,block+anchor,1)
s=s.replace('<h3>{l.title}</h3><p>{l.explanation.slice', '<h3>{l.title}</h3><Tag>{l.source.toLowerCase().startsWith(\'supplemental\')?\'Supplemental teaching\':\'Supplied source teaching\'}</Tag><p>{l.explanation.slice')
p.write_text(s,encoding='utf8')
p=root/'app/(academy)/[section]/page.tsx';s=p.read_text(encoding='utf8').replace("'progress','sources'","'progress','sources','review'");p.write_text(s,encoding='utf8')
