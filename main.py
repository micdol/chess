import game
import chessboard
import pawn

if __name__ == "__main__":
    game = game.Game()
    gos = game.gameObjects

    # TODO populate objects etc..\
    c = chessboard.Chessboard()

    gos.append(c)
    for i in range(8):
        gos.append(pawn.Pawn(1, i, c))

    game.run()
