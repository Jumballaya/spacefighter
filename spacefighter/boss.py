'''
Boss Class
'''
import random
import math
import pygame as pg
from spacefighter.ship import Ship
from spacefighter.colors import *
from spacefighter.utils import minmax
from spacefighter.animations import Combustion



class Boss(Ship):
    def __init__(self, image="assets/player/ship2.png", screen=None):
        Ship.__init__(self, image=image, screen=screen)

        self.bullet_v = 20
        self.bullet_type = 2
        self.rect.w = 256
        self.rect.h = 256
        self.image = pg.transform.rotate(self.image, 180)

        self.dead = False
        self.death_slide = 0
        self.combustion = Combustion(self.image)

        self.entered = False

    def check_collision(self, group):
        collided = pg.sprite.spritecollide(self, group, False)
        for c in collided:
            self.dx = 0
            self.dy = 0
            self.death()
            break

    def death(self):
        self.dead = True
        self.image = self.combustion.next()
        pg.mixer.stop()
        pg.mixer.music.load('assets/sounds/explosion1.wav')
        pg.mixer.music.play()

    def move(self):
        Ship.move(self)

        r = self.screen.get_rect()
        self.rect.x = minmax(0 + 15, r.w - 90, self.rect.x)
        self.rect.y = minmax(0, r.h * 0.75, self.rect.y)


        if (self.rect.y > (r.h / 6)):
            self.entered = True
            self.dx = 0
            self.dy = 0

        if self.entered:
            self.dx = math.sin(pg.time.get_ticks()) * math.pi
            self.dy = math.cos(pg.time.get_ticks()) * math.pi


    def update(self):
        self.move()
        self.shoot()
        Ship.update(self)

        if self.dead:
            if self.combustion.done:
                self.kill()
            else:
                self.image = self.combustion.next()
