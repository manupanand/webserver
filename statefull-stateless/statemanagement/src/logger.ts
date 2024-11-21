//log the state every 5 seconds

import {gameManager} from './cache'


export function startLogger(){
    setInterval(() => {
        console.log(gameManager.log())
    }, 5000);//every 5 sec
}
