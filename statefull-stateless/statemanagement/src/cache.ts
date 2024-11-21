interface Game{
    id:string;
    whitePlayerName:string;
    blackPlayerName:string;
    moves:string[];
}



// export const games:Game[]=[];//state variable in memeory - current  list of games
 class GameManager{
    games: Game[]=[];
    private static instance: GameManager;
   private constructor(){
        this.games=[];
    }
    static getInstance(){
        //create singleton instance of gamemanager and return it
        if(GameManager.instance){
            return GameManager.instance;
        }
        GameManager.instance=new GameManager();
        return GameManager.instance;
    }
    addMove(gameId:string,move:string){
        console.log(`Adding move ${move} to game ${gameId}`);
        const game= this.games.find(game=>game.id===gameId);
        game?.moves.push(move)
    }
    addGame(gameId:string){
        const game={
            id:gameId,
            whitePlayerName:"alice",
            blackPlayerName:"denizel",
            moves:[]
        }
        this.games.push(game);
    }
    log(){
        console.log(this.games)
    }
}

//export the simgle instance of gameManager
export const gameManager=GameManager.getInstance()

