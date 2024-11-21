import { Router } from "express";
import {userRouter} from './userRoutes'

export const indexRouter=Router();

indexRouter.use('/user',userRouter)
