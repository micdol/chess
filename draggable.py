import pygame as pg
from abc import ABC


# provides functionality for handling mouse drag
class AbstractDraggable(ABC):
    def __init__(self, dragRect: pg.Rect):
        # array of function(draggable: AbstractDraggable)
        self.dragListeners = []
        self.dropListeners = []
        self.moveListeners = []
        self.isDragging = False
        self.dragRect = dragRect
        self.prevPos = self.currPos = (0, 0)
        self.offset = (0, 0)
        self.eventtypes = [pg.MOUSEBUTTONDOWN,
                            pg.MOUSEBUTTONUP, pg.MOUSEMOTION]

    def handleDrag(self, event: pg.event):
        # event not relevant for drag purposes
        if event.type not in self.eventtypes:
            print(f'event not relevant for drag: {event}')
            return

        if hasattr(event, 'handled') and event.handled:
            return

        # start dragging on click within rect
        if not self.isDragging and event.type == pg.MOUSEBUTTONDOWN and self.dragRect.collidepoint(event.pos):
            event.handled = True
            self.prevPos = self.currPos = event.pos
            self.onDrag()    
        elif self.isDragging:
            event.handled = True
            self.prevPos = self.currPos
            self.currPos = event.pos
            if event.type == pg.MOUSEMOTION:
                self.onMove()
            elif event.type == pg.MOUSEBUTTONUP:
                self.onDrop()

    # called when drag is initiated, a.k.a on click
    def onDrag(self):
        print(f'drag started at: {self.currPos}')
        self.isDragging = True
        mx, my = self.currPos
        self.offset = (self.dragRect.x - mx, self.dragRect.y - my)
        for f in self.dragListeners:
            f(self)

    # called when drag is finsihed, a.k.a on release
    def onDrop(self):
        print(f'drag finished at: {self.currPos}')
        self.isDragging = False
        for f in self.dropListeners:
            f(self)

    # called when drag is ongoing, a.k.a mouse pressed and dragged
    def onMove(self):
        print(f'drag from {self.prevPos} to {self.currPos}')
        ox, oy = self.offset
        mx, my = self.currPos
        self.dragRect.x = mx + ox
        self.dragRect.y = my + oy
        for f in self.moveListeners:
            f(self)
