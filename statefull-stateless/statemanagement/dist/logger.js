"use strict";
//log the state every 5 seconds
Object.defineProperty(exports, "__esModule", { value: true });
exports.startLogger = startLogger;
const cache_1 = require("./cache");
function startLogger() {
    setInterval(() => {
        console.log(cache_1.gameManager.log());
    }, 5000); //every 5 sec
}
