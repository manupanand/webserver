"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.gameManager = void 0;
// export const games:Game[]=[];//state variable in memeory - current  list of games
class GameManager {
    constructor() {
        this.games = [];
        this.games = [];
    }
    addMove(gameId, move) {
        console.log(`Adding move ${move} to game ${gameId}`);
        const game = this.games.find(game => game.id === gameId);
        game === null || game === void 0 ? void 0 : game.moves.push(move);
    }
    addGame(gameId) {
        const game = {
            id: gameId,
            whitePlayerName: "alice",
            blackPlayerName: "denizel",
            moves: []
        };
        this.games.push(game);
    }
    log() {
        console.log(this.games);
    }
}
//export the simgle instance of gameManager
exports.gameManager = new GameManager();
