"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
//web socket server
const ws_1 = require("ws");
const wss = new ws_1.WebSocketServer({ port: 8080 });
//global variable
let senderSocket = null;
let receiverSocket = null;
wss.on("connection", (websocket) => {
    websocket.on("message", (data) => {
        const parsedMessage = JSON.parse(data);
        if (parsedMessage.type === "identify-as-sender") { //identify-as-sender
            console.log("identified sender");
            senderSocket = websocket;
        }
        else if (parsedMessage.type === "identify-as-receiver") { //identify-as-receiver
            console.log("identified receiver");
            receiverSocket = websocket;
        }
        else if (parsedMessage.type === "create-offer") { //createOffer
            console.log("offer received");
            receiverSocket === null || receiverSocket === void 0 ? void 0 : receiverSocket.send(JSON.stringify({
                type: "create-offer",
                offer: parsedMessage.offer, //sdp
            }));
        }
        else if (parsedMessage.type === "create-answer") { //createAnswer
            console.log("answer received");
            senderSocket === null || senderSocket === void 0 ? void 0 : senderSocket.send(JSON.stringify({
                type: "create-answer",
                answer: parsedMessage.answer //sdp
            }));
        }
        else if (parsedMessage.type === "ice-candidate") { //add ice candidate
            if (websocket === senderSocket) {
                receiverSocket === null || receiverSocket === void 0 ? void 0 : receiverSocket.send(JSON.stringify({
                    type: "ice-candidate",
                    candidate: parsedMessage.candidate
                }));
            }
            else if (websocket === receiverSocket) {
                senderSocket === null || senderSocket === void 0 ? void 0 : senderSocket.send(JSON.stringify({
                    type: "ice-candidate",
                    candidate: parsedMessage.candidate
                }));
            }
        }
    });
});
