'use client';
import {createContext,useContext,useEffect,useState,useCallback,useRef} from 'react';
import {createClient,type SupabaseClient} from '@supabase/supabase-js';
export type Attempt={id:string;type:'quiz'|'finance'|'case'|'interview';topic:string;score:number;answer:string;at:string;details?:unknown};
export type Progress={completed:string[];attempts:Attempt[];notes:Record<string,string>;days:number[]};
const empty:Progress={completed:[],attempts:[],notes:{},days:[]};
const Context=createContext<{data:Progress;ready:boolean;save:(a:Attempt)=>void;complete:(id:string)=>void;note:(id:string,text:string)=>void;day:(n:number)=>void;status:string;login:(email:string)=>Promise<string>;exportData:()=>void}>({data:empty,ready:false,save:()=>{},complete:()=>{},note:()=>{},day:()=>{},status:'Loading',login:async()=>'',exportData:()=>{}});
const storage='acq-academy-progress-v1';
export function ProgressProvider({children}:{children:React.ReactNode}){
 const [data,setData]=useState<Progress>(empty),[ready,setReady]=useState(false),[status,setStatus]=useState('Saved on this device');const client=useRef<SupabaseClient|null>(null);const userId=useRef<string|null>(null);
 useEffect(()=>{try{const stored=JSON.parse(localStorage.getItem(storage)||'null');if(stored&&Array.isArray(stored.completed)&&Array.isArray(stored.attempts)&&Array.isArray(stored.days)&&typeof stored.notes==='object')setData(stored);}catch{setStatus('Saved data could not be read; export future practice as a backup.');}setReady(true);
 const url=process.env.NEXT_PUBLIC_SUPABASE_URL,key=process.env.NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY;if(url&&key){client.current=createClient(url,key);const {data:{subscription}}=client.current.auth.onAuthStateChange((_,session)=>{userId.current=session?.user.id??null;if(session){setStatus('Connecting cloud progress…');setTimeout(async()=>{const {data:row,error}=await client.current!.from('academy_progress').select('data').eq('user_id',session.user.id).maybeSingle();if(error){setStatus('Cloud sync unavailable; saved on this device.');return;}if(row?.data)setData(row.data as Progress);setStatus('Cloud sync connected');},0);}else setStatus('Saved on this device');});return ()=>subscription.unsubscribe();}
 },[]);
 useEffect(()=>{if(!ready)return;try{localStorage.setItem(storage,JSON.stringify(data));}catch{setStatus('Device storage unavailable. Export progress to keep a backup.');}if(client.current&&userId.current){const timer=setTimeout(()=>{client.current!.from('academy_progress').upsert({user_id:userId.current,data,updated_at:new Date().toISOString()}).then(({error})=>setStatus(error?'Cloud save failed; saved on this device.':'Cloud sync connected'));},700);return ()=>clearTimeout(timer);}},[data,ready]);
 const save=useCallback((a:Attempt)=>setData(p=>({...p,attempts:[...p.attempts,a]})),[]);
 const complete=useCallback((id:string)=>setData(p=>({...p,completed:[...new Set([...p.completed,id])]})),[]);
 const note=useCallback((id:string,text:string)=>setData(p=>({...p,notes:{...p.notes,[id]:text}})),[]);
 const day=useCallback((n:number)=>setData(p=>({...p,days:p.days.includes(n)?p.days.filter(x=>x!==n):[...p.days,n]})),[]);
 const login=async(email:string)=>{if(!client.current)return 'Cloud sign-in is not configured. Device progress works now.';const {error}=await client.current.auth.signInWithOtp({email,options:{emailRedirectTo:window.location.origin}});return error?error.message:'Check your email for the sign-in link.';};
 const exportData=()=>{const blob=new Blob([JSON.stringify(data,null,2)],{type:'application/json'});const url=URL.createObjectURL(blob);const a=document.createElement('a');a.href=url;a.download='acq-academy-progress.json';a.click();URL.revokeObjectURL(url);};
 return <Context.Provider value={{data,ready,save,complete,note,day,status,login,exportData}}>{children}</Context.Provider>
}
export const useProgress=()=>useContext(Context);
