import game
import chessboard
import pieces
import player

if __name__ == "__main__":

    whitePlayer = player.Player('white')
    blackPlayer = player.Player('black')

    game = game.Game()
    gos = game.gameObjects

    # TODO populate objects etc..\
    c = chessboard.Chessboard()

    gos.append(c)
    for i in range(8):
        gos.append(pieces.Pawn(1, i, c, whitePlayer))
        gos.append(pieces.Pawn(6, i, c, blackPlayer))

    gos.append(pieces.Rook(0, 0, c, whitePlayer))
    gos.append(pieces.Knight(0, 1, c, whitePlayer))
    gos.append(pieces.Bishop(0, 2, c, whitePlayer))
    gos.append(pieces.Queen(0, 3, c, whitePlayer))
    gos.append(pieces.King(0, 4, c, whitePlayer))
    gos.append(pieces.Bishop(0, 5, c, whitePlayer))
    gos.append(pieces.Knight(0, 6, c, whitePlayer))
    gos.append(pieces.Rook(0, 7, c, whitePlayer))

    gos.append(pieces.Rook(7, 0, c, blackPlayer))
    gos.append(pieces.Knight(7, 1, c, blackPlayer))
    gos.append(pieces.Bishop(7, 2, c, blackPlayer))
    gos.append(pieces.Queen(7, 3, c, blackPlayer))
    gos.append(pieces.King(7, 4, c, blackPlayer))
    gos.append(pieces.Bishop(7, 5, c, blackPlayer))
    gos.append(pieces.Knight(7, 6, c, blackPlayer))
    gos.append(pieces.Rook(7, 7, c, blackPlayer))

    game.run()
