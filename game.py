import pygame as pg


class Game():
    def __init__(self, name='Game', w=512, h=512):
        self.objects = []
        self._isRunning = True
        self._screen = None
        self._width = w
        self._height = h
        self._init()
        pg.display.set_caption(name)
        

    # initialization, screen etc.
    def _init(self):
        pg.init()
        pg.font.init()
        size = (self._width, self._height)
        self._screen = pg.display.set_mode(size)
        pg.display.set_icon(pg.image.load('images/game_icon.png'))

    # game logic
    def _handleLoop(self):
        loopHandlers = [o for o in self.objects if callable(getattr(o, 'onLoop', None))]
        for o in loopHandlers:
            loopHandlers.onLoop()


    # pygame event handling
    def _handleEvents(self):
        eventHandlers = [o for o in self.objects if callable(getattr(o, 'onEvent', None))]
        for event in pg.event.get():
            # quit
            if event.type == pg.QUIT:
                self._isRunning = False
            # others...
            for o in eventHandlers:
                o.onEvent(event)


    # pygame drawing
    def _handleDraw(self):
        drawHandlers = [o for o in self.objects if callable(getattr(o, 'onDraw', None))]
        for o in drawHandlers:
            o.onDraw(self._screen)
        pg.display.flip()

    # user requested exit
    def _cleanup(self):
        pg.quit()

    # starts game and keeps it running
    def run(self):
        while self._isRunning:
            self._handleLoop()
            self._handleEvents()
            self._handleDraw()
        self._cleanup()
