import { PubSubManager } from "./PubSubManager";

setInterval(()=>{
    PubSubManager.getInstance().userSubscribe(Math.random().toString(),"TCS")
},5000)