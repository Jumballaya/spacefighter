'''
Enemy Manager
'''
import math
import pygame as pg
from spacefighter.ship import Ship
from spacefighter.boss import Boss

class EnemyManager(object):
    def __init__(self, screen, clock):
        self.screen = screen
        self.level = 1
        self.ships = pg.sprite.Group()
        self.clock = clock
        self.paused = False

    def setup_level(self):
        self.ships.empty()

        if self.level % 4 == 0:
            self.spawn_boss()
        else:
            self.spawn_ships()

    def check_collision(self, group, cb=None):
        col = pg.sprite.groupcollide(self.ships, group, False, True)
        if cb:
            for c in col:
                if type(c) != Boss:
                    c.kill()
                else:
                    c.death()
                cb(c)

    def handle_event(self, e):
        return

    def empty(self):
        self.ships.empty()

    def reset(self):
        self.level = 1
        self.setup_level()

    def pause(self):
        self.paused = True
        for s in self.ships:
            s.pause()

    def unpause(self):
        self.paused = False
        for s in self.ships:
            s.unpause()

    def spawn_ships(self):
        w = self.screen.get_rect().w
        row_count = math.floor(w / 95)
        for i in range(0, row_count):
            for j in range(0, 4):
                img = "assets/enemy/enemy%d.png" % ((self.level % 3) + 1)
                s = Ship(image=img, screen=self.screen)
                s.tSize((64, 64))
                s.rect.x = i * 95
                if j % 2 == 1:
                    s.rect.x += 25
                s.rect.y = (j * 95) - 600
                s.dy = min(self.level + 2, 6)
                self.ships.add(s)

    def spawn_boss(self):
        s = Boss(screen=self.screen)
        r = self.screen.get_rect()
        s.tSize((64, 64))
        s.rect.centerx = r.w / 2
        s.rect.y = -1 * r.h / 2
        self.ships.add(s)
        s.dy = 3
        s.dx = 3


    def update_boss_wave(self):
        for s in self.ships:
            s.update()


    def update_normal_wave(self):
        for i, s in enumerate(self.ships):
            s.move()
            s.update()
            if (i + 1) % 8 == 0:
                if self.clock.get_time() % 6 == 0:
                    s.shoot()
            if s.rect.y > (self.screen.get_rect().h - 50):
                s.kill()


    def update(self):
        if not self.paused:
            if self.level % 4 == 0:
                self.update_boss_wave()
            else:
                self.update_normal_wave()

            if len(self.ships.sprites()) < 1:
                self.level += 1
                self.setup_level()
