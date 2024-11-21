
import {gameManager} from './cache'
import  {startLogger} from './logger'


startLogger();
//push game every 2sec
setInterval(() => {
    gameManager.addGame(Math.random().toString())
    
}, 2000);