"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const app_1 = require("./app");
const PORT = 3000;
const app = app_1.App.serverInstance();
app.listen(PORT);
