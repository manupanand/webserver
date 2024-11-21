
//import necessary module redis package
import {createClient, RedisClientType} from 'redis';

export class PubSubManager{
    private static instance: PubSubManager;
    private redisClient:RedisClientType;
    private subscriptions:Map<string,string[]>;

    //private constructor to prevent direct constructor caall with new object
    private constructor(){
        //create redis client and connect to the redis server
        this.redisClient=createClient();
        this.redisClient.connect();
        this.subscriptions=new Map();

    }
    public static getInstance():PubSubManager{
        if(!PubSubManager.instance){
            PubSubManager.instance=new PubSubManager();
        }
        return PubSubManager.instance;
    }
    //add user to stock subscription
    public userSubscribe(userId:string,stock:string){
        if(!this.subscriptions.has(stock)){
            this.subscriptions.set(stock,[]);
        }
        this.subscriptions.get(stock)?.push(userId);

        if(this.subscriptions.get(stock)?.length===1){
            this.redisClient.subscribe(stock,(message)=>{
                this.handleMessage(stock,message);
            });
            console.log(`subscribed to Redis Channel ${stock}`)
        }

    }
    //remove user to stock subscription
    public userUnSubscribe(userId:string,stock:string){
        this.subscriptions.set(stock,this.subscriptions.get(stock)?.filter((sub)=>sub!==userId)|| []);

        if(this.subscriptions.get(stock)?.length===0){
            this.redisClient.unsubscribe(stock);
            console.log(`Unsubscribed to redis channel ${stock}`)
        }

    }
    
    //method that will be called when a message is published to the subscribed channel
    public handleMessage(stock:string,message:string){
        console.log(`Message recieved on channel ${stock}: ${message}`)
        this.subscriptions.get(stock)?.forEach((sub)=>{
            console.log(`Sending message to user :${sub}`);
        })

    }
    //clean up on instance destruction
    public async disconnect(){
        await this.redisClient.quit();
    }
}