//web socket server
import { WebSocketServer,WebSocket } from "ws";


const wss= new WebSocketServer({port:8080})

wss.on("connection",(socket)=>{
    
})