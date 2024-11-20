import express from 'express'
import { createClient } from 'redis'

const client=createClient()
const app=express()
 app.post("/submit",async(req,res)=>{
    const user=req.body.user
    const title=req.body.title
    //idealy write logic to save to db
    try{
        await client.lPush("submission",JSON.stringify({user,title}))
        res.json({
            message:"submmision recieved"
        })
    }catch(error){
        console.error("error in pushing to redis :",error);
        res.json({
            error:"error in submiting to redis"
        })
        
    }
 })



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