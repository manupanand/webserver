import { App } from "./app";

const PORT=3000

const app=App.serverInstance()

app.listen(PORT)