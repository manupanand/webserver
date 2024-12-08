import React,{ useEffect, useState ,useRef}  from 'react'

const peerconnection=new RTCPeerConnection();
export function Receiver() {
    const videoRef=useRef<HTMLVideoElement>(null)
    //set global varibale for websocket
const [websocket,setSocket]=useState<WebSocket|null>(null);//need to store websocket object
    useEffect(()=>{
        const ws= new WebSocket("ws://localhost:8080")
        ws.onopen=()=>{
            ws.send(JSON.stringify({
                type:'identify-as-receiver'
            }))
        }
        ws.onmessage=async (event)=>{
            const message = JSON.parse(event.data);
            if(message.type==='create-offer'){
                // const peerconnection=new RTCPeerConnection();
                peerconnection.setRemoteDescription(message.offer)//sets the offer of sender
                peerconnection.onicecandidate=(event)=>{
                    console.log(event);
                    if(event.candidate){
                        websocket?.send(JSON.stringify({
                            type:'ice-candidate',
                            candidate:event.candidate,
                        }))
                    }
                }//anytime in eciving ice candidate set ice candidate
                //add video logic
                //reciever-end video.control=true//play button
                peerconnection.ontrack=(event)=>{
                    console.log(event)
                    if(videoRef.current){
                        videoRef.current.srcObject=new MediaStream([event.track])
                    }
                }
                
                const answer= await peerconnection.createAnswer();//answer for sender
                await peerconnection.setLocalDescription(answer);
                ws?.send(JSON.stringify({
                    type:'create-answer',
                    answer:peerconnection.localDescription,//sdp
                }))
            }else if(message.type==='ice-candidate'){
                peerconnection.addIceCandidate(message.candidate)

            }
        }

    },[])
  return (
    <div>
      receiver
      <video ref={videoRef}  src=""></video>
    </div>
  )
}


