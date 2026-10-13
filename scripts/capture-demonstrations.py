import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
progress=json.loads(Path('C:/Users/olson/Downloads/acq-academy-progress.json').read_text(encoding='utf8'))
samples={kind:next(a for a in reversed(progress['attempts']) if a['type']==kind) for kind in ('finance','case','interview')}
assert samples['finance']['details']['drill']=='payback-1'
assert samples['finance']['score']==100
assert samples['case']['topic']=='hvac' and samples['case']['score']==97
assert samples['interview']['score']==95
out={'provenance':'Actual submissions completed through the running interface in an isolated local session. Demonstration scores are not the student’s personal results.','finance':samples['finance'],'case':samples['case'],'interview':samples['interview']}
(root/'data/demonstrations.json').write_text(json.dumps(out,indent=2,ensure_ascii=False),encoding='utf8')
lines=['# Completed practice demonstrations','',out['provenance'],'','Feedback mode: transparent guided checklist. No live AI response is claimed.','', '## Financial exercise','', 'CAC $600; monthly revenue $200; delivery cost $80.','',f"Submitted answer: {samples['finance']['answer']} months. Score: 100/100.",'','Worked solution: ($200 − $80) = $120 monthly gross profit; $600 ÷ $120 = 5 months. Collections timing is omitted.','', '## Seven-step SPS founder diagnosis','', 'Case: Northline Heating (fictional). Monthly revenue $180,000; direct costs $108,000; overhead $54,000 including $12,000 acquisition spend. 60 new customers.','', 'Questions asked: monthly capacity/bookings/backlog/callbacks; P&L and acquisition definitions; cash and customer complaints. Five evidence categories were released before submission.','',samples['case']['answer'],'',f"Score: {samples['case']['score']}/100.",'']
r=samples['case']['details']['report']
for c in r['categories']:lines.append(f"- {c['name']}: {c['earned']}/{c['weight']}")
lines+=['','Correct calculations: operating profit $18,000; margin 10%; acquisition CAC $200. Backlog increases by 15 jobs monthly.','','Feedback:']+[f'- {g}' for g in r['gaps']]+['','Stronger spoken answer:',r['stronger'],'','Source references:']+[f'- {c}' for c in r['citations']]
r=samples['interview']['details'];lines+=['','## Interview-practice evaluation','', 'Two-step mental-math round.','', 'Submitted response:',samples['interview']['answer'],'',f"Score: {samples['interview']['score']}/100.",'']+[f"- {c['name']}: {c['earned']}/{c['weight']}" for c in r['categories']]+['','Corrections:']+[f'- {g}' for g in r['gaps']]+['','Stronger answer:',r['stronger'],'','These scores are educational checklist outputs. They do not establish live communication, semantic validity of every claim, coachability, or official hiring readiness.']
(root/'DEMONSTRATIONS.md').write_text('\n'.join(lines)+'\n',encoding='utf8')
print('Captured three UI-completed demonstrations, including seven SPS fields and actual assessment responses.')
