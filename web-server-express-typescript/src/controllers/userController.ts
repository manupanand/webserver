//user controller

import { Request,Response } from "express";

export const getUsers=(req:Request,res:Response):void=>{
    res.status(200).json({
        message:`got user`
    })
}
export const createUser=(req:Request,res:Response):void=>{
    const {name,email}=req.body;
    res.status(200).json({
        message:`User created`,
        name:`${name}`,
        email:`${email}`
    })
}