import game 
import chessboard

if __name__ == "__main__":
    game = game.Game()
    # TODO populate objects etc..\
    c = chessboard.Chessboard()
    game.objects.append(c)
    print(chessboard.Chessboard.toSAN((0,0)))

    game.run()
