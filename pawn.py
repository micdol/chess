import pygame as pg
import gameObject
import drawable
import draggable
import math

class Pawn(gameObject.GameObject, drawable.AbstractImageDrawable, draggable.AbstractDraggable):
    def __init__(self, row, col, chessboard):
        self.image = pg.image.load('images/pawn.png')
        self.row = row
        self.col = col
        self.chessboard = chessboard
        drawable.AbstractImageDrawable.__init__(self, self.image)
        draggable.AbstractDraggable.__init__(self, self.image.get_rect())
        # draw rect and drag rect are supposed to act as one object
        self.drawRect = self.dragRect
        self.drawRect.x = self.col * self.drawRect.w
        self.drawRect.y = self.row * self.drawRect.h

    def onDraw(self, screen):
        self.handleDraw(screen)

    def onEvent(self, event):
        self.handleDrag(event)

    def onDrop(self):
        draggable.AbstractDraggable.onDrop(self)
        # snap to closest square (one which mouse is over)
        x, y = self.currPos
        w, h = self.image.get_size()
        row =  math.floor(y / h)
        col = math.floor(x / w)
        valid = self.isValidMove(row, col)
        if not valid:
            row = self.col
            col = self.row       
        self.drawRect.x = col * w
        self.drawRect.y = row * h

    def isValidMove(self, toRow, toCol):
        return True