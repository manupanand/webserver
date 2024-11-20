"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = __importDefault(require("express"));
const redis_1 = require("redis");
const client = (0, redis_1.createClient)();
const app = (0, express_1.default)();
app.post("/submit", (req, res) => __awaiter(void 0, void 0, void 0, function* () {
    const user = req.body.user;
    const title = req.body.title;
    //idealy write logic to save to db
    try {
        yield client.lPush("submission", JSON.stringify({ user, title }));
        res.json({
            message: "submmision recieved"
        });
    }
    catch (error) {
        console.error("error in pushing to redis :", error);
        res.json({
            error: "error in submiting to redis"
        });
    }
}));
function startServer() {
    return __awaiter(this, void 0, void 0, function* () {
        try {
            yield client.connect();
            console.log("connected to redis");
        }
        catch (error) {
            console.error("error in connecting to redis", error);
        }
        app.listen(2500, () => {
            try {
                console.log("Server started to port 2500");
            }
            catch (error) {
                console.error("error in starting server", error);
            }
        });
    });
}
startServer();
