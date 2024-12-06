//web socket server
import { WebSocketServer,WebSocket } from "ws";


const wss= new WebSocketServer({port:8080})

wss.on("connection",(socket)=>{
    socket.on("message",(data)=>{
    console.log(data.toString());
    const parsedData=JSON.parse(data as unknown as string)
    if(parsedData.type =="join"){

    }
    if(parsedData.type =="chat"){

    }
  })    
})
