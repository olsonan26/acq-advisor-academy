import type { Metadata } from 'next';
import './globals.css';
import {ProgressProvider} from '@/components/progress';
export const metadata:Metadata={title:'ACQ Advisor Academy',description:'Independent business advisory practice and interview preparation.'};
export default function RootLayout({children}:{children:React.ReactNode}){return <html lang="en"><body><ProgressProvider>{children}</ProgressProvider></body></html>}
