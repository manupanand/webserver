//web socket server
import { WebSocketServer,WebSocket } from "ws";


const wss= new WebSocketServer({port:8080})
//global variable
let senderSocket:null | WebSocket=null;
let receiverSocket:null | WebSocket=null;

wss.on("connection",(websocket)=>{
    websocket.on("message",(data:any)=>{
    
    const parsedMessage=JSON.parse(data as unknown as string)
    if(parsedMessage.type==="identify-as-sender"){//identify-as-sender
      console.log("identified sender")
      senderSocket=websocket;
    }else if(parsedMessage.type==="identify-as-receiver"){//identify-as-receiver
     console.log("identified receiver")
      receiverSocket=websocket;
    }else if (parsedMessage.type==="create-offer"){ //createOffer
      console.log("offer received")
      receiverSocket?.send(JSON.stringify({
        type:"create-offer",
        offer:parsedMessage.offer, //sdp
        }))
    }else if (parsedMessage.type==="create-answer"){ //createAnswer
      console.log("answer received")
      senderSocket?.send(JSON.stringify({
        type:"create-answer",
        answer:parsedMessage.answer//sdp
      }))
    }else if(parsedMessage.type === "ice-candidate"){//add ice candidate
      if(websocket===senderSocket){
        receiverSocket?.send(JSON.stringify({
          type:"ice-candidate",
          candidate:parsedMessage.candidate

        }))
      }else if(websocket===receiverSocket){
        senderSocket?.send(JSON.stringify({
          type:"ice-candidate",
          candidate:parsedMessage.candidate
        }))
      }
    }
    
    
   
   
    
   
  })    
})
