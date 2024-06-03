"use server"

import { redirect } from 'next/navigation'
 
 export default async function urlPush(urlstring: string) {
    redirect(urlstring)
 }