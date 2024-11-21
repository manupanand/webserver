"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.logger = void 0;
const logger = (req, res, next) => {
    console.log(`[${new Date().toISOString()} : ${req.method} - ${req.url}]`);
    next(); //pass control to the next middleware
};
exports.logger = logger;
