"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.App = void 0;
const express_1 = __importDefault(require("express"));
const logger_1 = require("./middleware/logger");
const indexRoute_1 = require("./routes/indexRoute");
class App {
    constructor() {
        this.app = (0, express_1.default)();
        // this.port=port;
        //initialise methods
        //initializeMiddlewares
        this.intializeMiddleWares();
        //initializeRoutes
        this.initalizeRoutes();
        //initializeErrorHandling
        this.initalizeErrorHandling();
    }
    intializeMiddleWares() {
        //middleares
        this.app.use(express_1.default.json()); //JSON Parse
        this.app.use(logger_1.logger);
    }
    initalizeRoutes() {
        this.app.use('/api/v1', indexRoute_1.indexRouter);
    }
    initalizeErrorHandling() {
        console.log("error initialized");
    }
    // create instance -singleton  pattern
    static serverInstance() {
        if (!App.instance) {
            App.instance = new App();
        }
        return App.instance;
    }
    //listen to port
    listen(port) {
        this.app.listen(port, () => {
            console.log(`App is running on port:${port}`);
        });
    }
}
exports.App = App;
