'''
Bullet Class
'''
import pygame as pg
from spacefighter.colors import *

class Bullet(pg.sprite.Sprite):
    def __init__(self, facing, init_x=0, init_y=0, vx=0, vy=0, screen=None):
        pg.sprite.Sprite.__init__(self)

        self.facing = min(3, facing)

        self.sheet = pg.image.load("assets/bullet1.png")
        self.image = pg.Surface((13, 13)).convert()
        self.image.blit(self.sheet, (0, 0), (self.facing * 13, 0, 13, 13))
        self.image.set_colorkey(BLACK, pg.RLEACCEL)

        self.rect = self.image.get_rect()
        self.rect.x = init_x
        self.rect.y = init_y
        self.dx = vx
        self.dy = vy

        self.screen = screen

        self.image = pg.transform.scale(self.image, (26, 26))
        self.rect.w = 26
        self.rect.h = 26

    def update(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

    def check_collision(self, group):
        return
