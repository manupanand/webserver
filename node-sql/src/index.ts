import {Client}from "pg"
import  express from "express"
import 'dotenv/config' 

const pg_url=process.env.PG_URL

try{
    async function  dbConnect(){
        const pgClient = new Client({connectionString:pg_url})
        await pgClient.connect()
        if(pgClient){
            
                try{
                    const result=await pgClient.query(`CREATE TABLE users( id SERIAL PRIMARY KEY,
                        username VARCHAR(50) UNIQUE NOT NULL,
                        email VARCHAR(255) UNIQUE NOT NULL,
                        password VARCHAR(255) NOT NULL,
                        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP);`)
                        if(result){
                            console.log(`user created`,result)
                        }else(
                            console.log(`error in creating database`)
                        )
                }catch(error){
                    console.log(`user creation error`,error)
                }
        }
    }
    dbConnect()
}catch(error){
    console.log(`Error in database connection :`,error)
}

const app = express()
app.use(express.json())