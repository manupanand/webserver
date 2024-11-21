"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const cache_1 = require("./cache");
const logger_1 = require("./logger");
(0, logger_1.startLogger)();
//push game every 2sec
setInterval(() => {
    cache_1.gameManager.addGame(Math.random().toString());
}, 2000);
