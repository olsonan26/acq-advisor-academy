import {cookies} from 'next/headers';
import {redirect} from 'next/navigation';
import {verifyAccess} from '@/lib/access';
export const dynamic='force-dynamic';
export default async function ProtectedAcademy({children}:{children:React.ReactNode}){const secret=process.env.ACADEMY_ACCESS_PASSWORD;if(secret){const cookie=(await cookies()).get('academy-access')?.value||'';if(!verifyAccess(cookie,secret))redirect('/access');}else if(process.env.NODE_ENV==='production'&&process.env.ACADEMY_LOCAL_DEMO!=='true')redirect('/access');return children;}
