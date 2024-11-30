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
                    const result=await pgClient.query(`CREATE TABLE IF NOT EXISTS users( id SERIAL PRIMARY KEY,
                        username VARCHAR(50) UNIQUE NOT NULL,
                        email VARCHAR(255) UNIQUE NOT NULL,
                        password VARCHAR(255) NOT NULL,
                        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP);`)
                      
                         // Insert default users
                            const insertUsersQuery = `
                            INSERT INTO users (username, email, password) 
                            VALUES
                                ('user1', 'user1@example.com', 'password1'),
                                ('user2', 'user2@example.com', 'password2'),
                                ('user3', 'user3@example.com', 'password3')
                            ON CONFLICT (username) DO NOTHING;
                        `;
                        const insert = await pgClient.query(insertUsersQuery);
                        console.log("Default users added successfully.");
                }catch(error){
                    console.log(`user creation error`,error)
                }finally {
                    // Disconnect from the database
                    await pgClient.end();
                    console.log("Disconnected from the database.");
                }
        }
    }
    dbConnect()
}catch(error){
    console.log(`Error in database connection :`,error)
}

const app = express()
app.use(express.json())