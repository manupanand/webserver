"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
//web socket server
const ws_1 = require("ws");
const wss = new ws_1.WebSocketServer({ port: 8080 });
wss.on("connection", (socket) => {
    socket.on("message", (data) => {
        console.log(data.toString());
    });
});
