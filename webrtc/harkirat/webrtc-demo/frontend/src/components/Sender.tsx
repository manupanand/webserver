import React, { useEffect, useState } from 'react'
//check where to put stun server as argument
const peerconnection = new RTCPeerConnection();//making it a global object-browser -api
export function Sender() {
    //set global varibale for websocket
const [websocket,setSocket]=useState<WebSocket|null>(null);//need to store websocket object
    useEffect(()=>{
        const ws= new WebSocket("ws://localhost:8080")
        ws.onopen=()=>{
            ws.send(JSON.stringify({
                type:'identify-as-sender'
            }))
        }
        setSocket(ws)
        
    },[])
    async function startSendingVideo(){
        //RTCpeerconnection-create an offer
        // const peerconnection = new RTCPeerConnection();//object for webRTC
        if(!websocket){ //for type safety
            return;
        }
        peerconnection.onnegotiationneeded=async ()=>{// need to create sdp as it changes again and again
            console.log("on negotiation")
            const offer= await peerconnection.createOffer();//create SDP
            await peerconnection.setLocalDescription(offer);//set sdp to local
            websocket?.send(JSON.stringify({
                type:'create-offer',
                offer:peerconnection.localDescription,//sdp
            }))
        }
        websocket.onmessage=async (event)=>{
            const message= JSON.parse(event.data);
            if(message.type==='create-answer'){
                peerconnection.setRemoteDescription(message.answer)
            }else if(message.type==='ice-candidate'){
                peerconnection.addIceCandidate(message.candidate)
            }
        }
        //add icecandidate
        peerconnection.onicecandidate=(event)=>{
            console.log(event)
            if(event.candidate){
                websocket?.send(JSON.stringify({
                    type:'ice-candidate',
                    candidate:event.candidate,
                }))
            }

        }
        //start sending video
        const stream= await navigator.mediaDevices.getUserMedia({
            video:true,
            audio:false
        })//screen share -getDisplay Media
        //reciever-end video.control=true//play button
        peerconnection.addTrack(stream.getVideoTracks()[0]);
        peerconnection.addTrack(stream.getAudioTracks()[0])



    }
  return (
    <div>
      sender
      <button onClick={startSendingVideo}>Send Video</button>
    </div>
  )
}


