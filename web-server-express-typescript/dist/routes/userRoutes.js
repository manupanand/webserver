"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.userRouter = void 0;
//user specific routes
const express_1 = require("express");
const userController_1 = require("../controllers/userController");
exports.userRouter = (0, express_1.Router)();
exports.userRouter.get('/get', userController_1.getUsers);
exports.userRouter.post('/create', userController_1.createUser);
