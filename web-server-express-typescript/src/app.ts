import express,{Application} from 'express';
import { logger } from './middleware/logger';
import { indexRouter } from './routes/indexRoute';

export class App{
    private static instance:App;
    public app:Application;
    

    constructor(){
        this.app=express();
        // this.port=port;
        //initialise methods
        //initializeMiddlewares
        this.intializeMiddleWares();
        //initializeRoutes
        this.initalizeRoutes()
        //initializeErrorHandling
        this.initalizeErrorHandling()

    }
    private intializeMiddleWares():void{
        //middleares
        this.app.use(express.json());//JSON Parse
        this.app.use(logger)
    }
    private initalizeRoutes():void{
        this.app.use('/api/v1',indexRouter)

    }
    private initalizeErrorHandling():void{
        console.log("error initialized")
    }

    // create instance -singleton  pattern
    public static serverInstance():App{
        if(!App.instance){
            App.instance =new App();
        }
        return App.instance;

    }

    //listen to port
    public listen(port:number):void{
        this.app.listen(port,()=>{
            console.log(`App is running on port:${port}`)
        })
    }

}