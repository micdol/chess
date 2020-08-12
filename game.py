import pygame as pg


class Game():
    def __init__(self, name='Game', w=512, h=512, fps=60):
        self.gameObjects = []
        self.isRunning = True
        self.screen = None
        self.width = w
        self.height = h
        self.time = 0
        self.fps = fps
        self.clock = pg.time.Clock()
        self.init()
        pg.display.set_caption(name)

    # initialization, screen etc.

    def init(self):
        pg.init()
        pg.font.init()
        size = (self.width, self.height)
        self.screen = pg.display.set_mode(size)
        pg.display.set_icon(pg.image.load('images/game_icon.png'))

    # game logic
    def handleLoop(self):
        ticks = pg.time.get_ticks()
        elapsed = ticks - self.time
        for o in self.gameObjects:
            o.onLoop(elapsed)
        self.time = ticks

    # pygame event handling

    def handleEvents(self):
        for event in pg.event.get():
            # quit
            if event.type == pg.QUIT:
                self.isRunning = False
            # others...
            for o in self.gameObjects:
                o.onEvent(event)

    # pygame drawing

    def handleDraw(self):
        for o in self.gameObjects:
            o.onDraw(self.screen)
        pg.display.flip()

    # user requested exit
    def cleanup(self):
        pg.quit()

    # starts game and keeps it running
    def run(self):
        while self.isRunning:
            self.handleLoop()
            self.handleEvents()
            self.handleDraw()
            self.clock.tick(self.fps)
        self.cleanup()
