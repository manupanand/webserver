//user specific routes
import { Router } from "express";
import { getUsers,createUser } from "../controllers/userController";

export const userRouter=Router();

userRouter.get('/get',getUsers);
userRouter.post('/create',createUser)

