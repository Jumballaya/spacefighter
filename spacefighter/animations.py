'''
Animations
'''
import pygame as pg
from spacefighter.spritesheet import Spritesheet
from spacefighter.colors import *

'''
Explosion -- player death
'''
class Explosion(object):
    def __init__(self, original):
        self.original = original
        self.filename = 'assets/player/death.png'
        ss = Spritesheet(self.filename)

        rect = pg.Rect((0, 0, 38, 32))
        self.images = ss.load_strip(rect, 4, BLACK)

        self.i = 0
        self.frames = 4
        self.f = self.frames

        self.done = False

    def iter(self):
        self.i = 0
        self.f = self.frames
        return self

    def next(self):
        if self.i >= len(self.images):
            self.done = True
            return self.original

        image = self.images[self.i]
        self.f -= 1
        if self.f == 0:
            self.i += 1
            self.f = self.frames
        image = pg.transform.scale(image, (114, 96))
        return image

'''
Combustion -- player death
'''
class Combustion(object):
    def __init__(self, original):
        self.original = original
        self.filename = 'assets/enemy/boss_death.png'
        ss = Spritesheet(self.filename)

        rect = pg.Rect((0, 0, 38, 38))
        self.images = ss.load_strip(rect, 4, BLACK)

        self.i = 0
        self.frames = 4
        self.f = self.frames

        self.done = False

    def iter(self):
        self.i = 0
        self.f = self.frames
        return self

    def next(self):
        if self.i >= len(self.images):
            self.done = True
            return self.original

        image = self.images[self.i]
        self.f -= 1
        if self.f == 0:
            self.i += 1
            self.f = self.frames
        image = pg.transform.scale(image, (152, 152))
        return image
