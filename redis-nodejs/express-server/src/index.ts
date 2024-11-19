import express from 'express'
import { createClient } from 'redis'

const client=createClient()
const app=express()


async function startServer(){
    try{
        await client.connect()
    console.log("connected to redis");
    }catch(error){
        console.error("error in connecting to redis",error)
    }
    app.listen(2500,()=>{
        try{
            console.log("Server started to port 2500")
        }catch(error){
            console.error("error in starting server",error)
        }
    })

}
startServer();