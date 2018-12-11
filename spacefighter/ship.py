'''
Space Ship Class
'''
import pygame as pg
from spacefighter.colors import *
from spacefighter.bullet import Bullet

class Ship(pg.sprite.Sprite):
    def __init__(self, image="assets/enemy/enemy1.png", screen=None):
        pg.sprite.Sprite.__init__(self)

        self.image_path = image
        self.load_sprite()

        self.paused = False

        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.dx = 0
        self.dy = 0

        self.bullets = pg.sprite.Group()
        self.bullet_type = 2
        self.bullet_v = 12
        self.last_shot_time = pg.time.get_ticks()
        self.reload_time = 1000

        self.screen = screen

        self.shoot_sound = pg.mixer.Sound('assets/sounds/shoot.wav')


    def load_sprite(self):
        self.sheet = pg.image.load(self.image_path)
        self.image = pg.Surface((19, 20)).convert()
        self.image.blit(self.sheet, (0, 0), (0, 0, 19, 20))
        self.image.set_colorkey(BLACK, pg.RLEACCEL)

    def move(self):
        if not self.paused:
            self.rect = self.rect.move(self.dx, self.dy)

    def shoot(self):
        if not self.paused:
            if pg.time.get_ticks() - self.last_shot_time > self.reload_time:
                self.shoot_sound.play()
                x = self.rect.x + 20
                y = self.rect.y - 5
                bullet = Bullet(self.bullet_type, init_x=x, init_y=y, vy=self.bullet_v, screen=self.screen)
                self.bullets.add(bullet)
                self.last_shot_time = pg.time.get_ticks()

    def pause(self):
        self.paused = True

    def unpause(self):
        self.paused = False

    def tSize(self, size):
        self.image = pg.transform.scale(self.image, size)
        self.rect.w = size[0]
        self.rect.h = size[1]

    def update(self):
        for b in self.bullets:
            b.rect = b.rect.move(b.dx, b.dy)
            if b.rect.y < 0:
                b.kill()
        self.bullets.update()

        self.screen.blit(self.image, (self.rect.x, self.rect.y))
