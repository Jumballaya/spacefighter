'''
Player Class
'''
import math
import pygame as pg
from spacefighter.ship import Ship
from spacefighter.colors import *
from spacefighter.utils import minmax
from spacefighter.animations import Explosion



class Player(Ship):
    def __init__(self, image="assets/player/ship1.png", screen=None):
        Ship.__init__(self, image=image, screen=screen)
        self.level = 1
        self.lives = 3
        self.score = 0

        self.bullet_v = -20
        self.bullet_type = 0
        self.tSize((64, 64))

        self.dead = False
        self.death_slide = 0
        self.reload_time = 200

        self.paused = False
        self.freeze = self.rect

        self.joystick = None

        self.explosion = Explosion(self.image)

        self.level_up_sound = pg.mixer.Sound('assets/sounds/level_up.wav')
        self.death_sound = pg.mixer.Sound('assets/sounds/explosion1.wav')

    def move(self):
        Ship.move(self)
        self.check_joystick()

        r = self.screen.get_rect()
        self.rect.x = minmax(0 + 15, r.w - 90, self.rect.x)
        self.rect.y = minmax(0, r.h - 75, self.rect.y)

    def check_collision(self, group):
        if not self.dead:
            collided = pg.sprite.spritecollide(self, group, True)
            for c in collided:
                self.dx = 0
                self.dy = 0
                self.death()
                break

    def death(self):
        self.dead = True
        self.lives -= 1
        self.image = self.explosion.next()
        self.dx = 0
        self.dy = 0
        self.death_sound.play()

    def level_up(self):
        self.level_up_sound.play()
        self.level += 1
        self.lives += 1
        self.image_path = "assets/player/ship%d.png" % ((self.level % 4) + 1)
        self.load_sprite()
        self.tSize((64, 64))
        self.explosion.original = self.image

    def respawn(self):
        self.death_slide = 0
        self.dead = False
        self.paused = False
        self.image = self.explosion.original
        self.explosion = Explosion(self.image)

        rect = self.screen.get_rect()
        self.rect.centerx = rect.w / 2
        self.rect.y = rect.h - 90

    def reset(self):
        self.unpause()
        self.score = 0
        self.lives = 3
        self.level = 1

        self.image_path = "assets/player/ship%d.png" % self.level
        self.load_sprite()
        self.tSize((64, 64))
        self.explosion.original = self.image

        rect = self.screen.get_rect()
        self.rect.centerx = rect.w / 2
        self.rect.y = rect.h - 90


    def pause(self):
        rect = self.screen.get_rect()

        if not self.paused:
            self.freeze = pg.Rect(self.rect)
            self.rect.centerx = (rect.w / 2)
            self.rect.centery = (rect.h / 2) - (self.rect.h / 2) - 60
        self.paused = True

    def unpause(self):
        if self.paused:
            self.rect = self.freeze
        self.paused = False

    def shoot_object(self, obj):
        if type(obj) == Ship:
            self.score += 150
        else:
            self.score += 300
            self.level_up()

    def update(self):
        self.move()
        Ship.update(self)

        if self.dead:
            if self.explosion.done:
                self.kill()
                self.respawn()
            else:
                self.image = self.explosion.next()

        if pg.key.get_pressed()[pg.K_SPACE]:
            self.shoot()

    def set_joystick(self, joystick):
        self.joystick = joystick

    def check_joystick(self):
        if not self.joystick: return
        if self.dead: return

        x_axis = self.joystick.get_axis(0)
        y_axis = self.joystick.get_axis(1)

        dpad = self.joystick.get_hat(0)

        if x_axis > 0: x_axis = 10
        elif x_axis < 0: x_axis = -10
        else: x_axis = 0

        if y_axis > 0: y_axis = 10
        elif y_axis < 0: y_axis = -10
        else: y_axis = 0

        if dpad[0] < 0 or x_axis < 0:
            self.dx = -10
        elif dpad[0] > 0 or x_axis > 0:
            self.dx = 10
        else:
            self.dx = 0

        if dpad[1] > 0 or y_axis < 0:
            self.dy = -10
        elif dpad[1] < 0 or y_axis > 0:
            self.dy = 10
        else:
            self.dy = 0


    def handle_event(self, e):
        if not self.dead:
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_LEFT or e.key == ord('a'):
                    self.dx -= 10
                if e.key == pg.K_RIGHT or e.key == ord('d'):
                    self.dx += 10
                if e.key == pg.K_UP or e.key == ord('w'):
                    self.dy = -10
                if e.key == pg.K_DOWN or e.key == ord('s'):
                    self.dy = 10

            if e.type == pg.KEYUP:
                if e.key == pg.K_LEFT or e.key == pg.K_RIGHT or e.key == ord('a') or e.key == ord('d'):
                    self.dx = 0
                if e.key == pg.K_UP or e.key == pg.K_DOWN or e.key == ord('w') or e.key == ord('s'):
                    self.dy = 0

            if self.joystick:
                if not self.dead:
                    x_button = self.joystick.get_button(0)
                    if x_button == 1:
                        self.shoot()
