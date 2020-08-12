import pygame as pg
import gameObject

class Chessboard(gameObject.GameObject):
    files = list(range(ord('a'), ord('h') + 1))

    def __init__(self):
        self.rows = 8
        self.cols = 8
        self.squareSize = (64, 64)  # in pixels

    def onDraw(self, screen: pg.Surface):
        colors = [(238, 238, 210), (118, 150, 86)]
        w, h = self.squareSize
        i = 0
        r = pg.Rect(0, 0, w, h)
        f = pg.font.SysFont('Consolas', 10)
        for row in range(self.rows):
            for col in range(self.cols):
                r.x = row * w
                r.y = col * h
                pg.draw.rect(screen, colors[i % 2], r)
                san = Chessboard.toSAN(row, col)
                sf = f.render(san, True, pg.Color("black"))
                screen.blit(sf, (r.x, r.y))
                i += 1
            i += 1

    @classmethod
    # converts x,y square idx (x,y in [0,7]) to Standard Algebraic Notation (SAN)
    # toSAN(1,2) => 'c2'
    # toSan((0,0)) => 'a1'
    def toSAN(cls, *args):
        x, y = (0, 0)
        if len(args) == 1:
            x, y = args[0]
        else:
            x = args[0]
            y = args[1]
        return f'{chr(Chessboard.files[x])}{y+1}'
