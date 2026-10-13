import {notFound} from 'next/navigation';
import Academy from '@/components/academy';
const sections=['academy','professor','diagnosis','finance','interview','progress','sources','review'];
export default async function Page({params}:{params:Promise<{section:string}>}){const {section}=await params;if(!sections.includes(section))notFound();return <Academy section={section}/>}
