"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.indexRouter = void 0;
const express_1 = require("express");
const userRoutes_1 = require("./userRoutes");
exports.indexRouter = (0, express_1.Router)();
exports.indexRouter.use('/user', userRoutes_1.userRouter);
