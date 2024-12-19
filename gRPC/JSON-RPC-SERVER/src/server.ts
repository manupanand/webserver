import express from 'express'
import bodyParser  from 'body-parser'

const app =express()
const port =3000

app.use(bodyParser.json())


//define method to RPC
function add(a:number,b:number):number{
    return a+b;
}
function multiply(a:number,b:number):number{
    return a*b;
}
//handle JSON RPC request
app.post('/rpc',(req,res)=>{
    const {jsonrpc,method,params,id}=req.body
    if(jsonrpc!=='2.0'|| !method || !Array.isArray(params)){
        res.status(400).json({
            jsonrpc:'2.0',
            error:{
                code:-32600,
                message:'Invalid Request'
            },id
        })
        return;
    }
    //execute method
    let result;
    switch(method){
        case 'add':
            result=add(params[0],params[1]);
            break;
        case 'multiply':
            result=multiply(params[0],params[1]);
            break;
        default:
            res.status(400).json({
                jsonrpc:'2.0',
                error:{
                code:-32601,
                message:'method not found'
                },id

            });
            return;  
    }
    //send back response 
    res.status(200).json({jsonrpc:'2.0',result,id})

})

app.listen(port,()=>{
    console.log(`JSON RPC server running on port ${port}`)
})

