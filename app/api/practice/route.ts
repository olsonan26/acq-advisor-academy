import {NextResponse} from 'next/server';
import {cases} from '@/data/cases';
import {lessons,sps} from '@/data/curriculum';
import {askFounder} from '@/lib/case-engine';
import {assessCase} from '@/lib/assessment';
import {assessInterview} from '@/lib/interview-assessment';
import {interviewRounds} from '@/data/interview';
import {aiCoach} from '@/lib/ai-coach';
import {verifyAccess} from '@/lib/access';
export async function POST(req:Request){
 const secret=process.env.ACADEMY_ACCESS_PASSWORD;const token=(req.headers.get('cookie')||'').split(';').map(x=>x.trim()).find(x=>x.startsWith('academy-access='))?.slice('academy-access='.length)||'';
 if(secret&&!verifyAccess(token,secret))return NextResponse.json({error:'Sign in to the private academy.'},{status:401});
 if(!secret&&process.env.NODE_ENV==='production'&&process.env.ACADEMY_LOCAL_DEMO!=='true')return NextResponse.json({error:'Private academy access is not configured.'},{status:503});
 try{const raw=await req.text();if(raw.length>30000)return NextResponse.json({error:'Request too large.'},{status:413});const b=JSON.parse(raw);if(typeof b.mode!=='string')throw Error('Invalid practice mode');
 if(b.mode==='founder'){if(!cases.some(c=>c.id===b.caseId)||typeof b.question!=='string'||b.question.length>2000||!Array.isArray(b.revealed))throw Error('Invalid founder request');return NextResponse.json(askFounder(b.caseId,b.question,b.revealed.filter((x:unknown)=>typeof x==='string')));}
 if(b.mode==='case-assessment'){if(!cases.some(c=>c.id===b.caseId)||!Array.isArray(b.steps)||b.steps.length!==7||!b.steps.every((s:unknown)=>typeof s==='string'&&s.trim().length>=25&&s.length<=4000)||!Array.isArray(b.revealed)||b.revealed.length<2||typeof b.margin!=='string'||typeof b.cac!=='string'||!b.margin.trim()||!b.cac.trim())return NextResponse.json({error:'Complete all seven SPS steps, uncover two facts, and calculate operating margin and CAC before requesting the answer key.'},{status:400});const report=assessCase(b.caseId,b);const ai=await aiCoach({case:cases.find(c=>c.id===b.caseId),answerKey:report.answerKey,report,spsSource:'Business Re-Imagined slides 42–44; source pack supplied by user'},JSON.stringify({steps:b.steps,margin:b.margin,cac:b.cac}));return NextResponse.json({...report,aiFeedback:ai.text,aiStatus:ai.status});}
 if(b.mode==='interview'){if(!Number.isInteger(b.round)||b.round<0||b.round>=interviewRounds.length||typeof b.answer!=='string'||b.answer.trim().length<40||b.answer.length>12000)throw Error('Choose a valid round and provide at least 40 characters of reasoning.');const report=assessInterview(b.round,b.answer);const ai=await aiCoach({round:interviewRounds[b.round],report,sourceStatus:'Recruitment transcript timestamps approximate; not independently authenticated.'},b.answer);return NextResponse.json({...report,aiFeedback:ai.text,aiStatus:ai.status});}
 if(b.mode==='tutor'){if(typeof b.question!=='string'||b.question.length>2000)throw Error('Question must be under 2,000 characters.');const terms=b.question.toLowerCase().split(/\W+/).filter((x:string)=>x.length>3);const ranked=lessons.map(l=>({l,score:terms.reduce((n:number,x:string)=>n+Number(`${l.title} ${l.explanation}`.toLowerCase().includes(x)),0)})).sort((a,b)=>b.score-a.score);const selected=ranked.slice(0,3).map(x=>x.l);const ai=await aiCoach({lessons:selected,sps,sourceStatus:'Official course pages and titles only. Spoken teachings unverified. SPS sourced from original PowerPoint. Recruitment transcripts user-supplied, timings approximate.'},b.question);if(ai.text)return NextResponse.json({text:ai.text,mode:'Live AI professor'});const l=selected[0];return NextResponse.json({mode:'Guided curriculum tutor',text:`${ai.status}\n\nRelated lesson: ${l.title}\n\n${l.explanation}\n\nWorked example: ${l.example}\n${l.steps.join('\n')}\n\nCommon mistake: ${l.mistake}\n\nYour turn: ${l.question} Explain the reasoning before looking at the lesson answer.\n\nSource: ${l.source}`});}
 return NextResponse.json({error:'Unknown practice mode.'},{status:400});
 }catch(e){return NextResponse.json({error:e instanceof Error?e.message:'Could not process this practice request.'},{status:400})}
}
