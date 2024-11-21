//logger middleware 
import { Request,Response,NextFunction } from "express";

export const logger=(req:Request,res:Response,next:NextFunction):void=>{
    console.log(`[${new Date().toISOString()} : ${req.method} - ${req.url}]`);
    next();//pass control to the next middleware
}