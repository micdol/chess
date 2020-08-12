import pygame as pg
from abc import ABC

# provides functionality to draw something on screen


class AbstractImageDrawable():
    def __init__(self, image: pg.image):
        self.image = image
        self.drawRect = image.get_rect()

    def handleDraw(self, screen: pg.Surface):
        screen.blit(self.image, self.drawRect)
