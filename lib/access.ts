import {createHmac,timingSafeEqual} from 'node:crypto';
export const accessToken=(secret:string,expires:number)=>`${expires}.${createHmac('sha256',secret).update(String(expires)).digest('hex')}`;
export function verifyAccess(token:string,secret:string){const parts=token.split('.');const expires=Number(parts[0]);if(parts.length!==2||!Number.isFinite(expires)||expires<Date.now())return false;const expected=accessToken(secret,expires);return expected.length===token.length&&timingSafeEqual(Buffer.from(expected),Buffer.from(token));}
