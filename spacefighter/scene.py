'''
Game Scene
'''
import pygame as pg
from spacefighter.ui import UI
from spacefighter.colors import *
from spacefighter.player import Player
from spacefighter.enemy_manager import EnemyManager


class Scene(object):

    def __init__(self, screen, bg, player, enemy_manager, clock):
        self.screen = screen
        self.rect = screen.get_rect()
        self.display = (self.rect.w, self.rect.h)
        self.player = player
        self.enemy_manager = enemy_manager
        self.ui = UI(self.screen)
        self.bg = bg
        self.clock = clock

        self.paused = False

        self.joystick = None

        self.bg_color = (33, 33, 33)

        self.handlers = []

        if self.player:
            self.handlers.append(self.player.handle_event)
        if self.enemy_manager:
            self.handlers.append(self.enemy_manager.handle_event)

        self.handlers.append(self.ui.handle_event)

        self.setup()

    def handle_event(self, e):
        for h in self.handlers:
            h(e)
        return

    def render_bg(self):
        self.screen.fill(self.bg_color)

    def render_foreground(self):
        if self.player:
            self.player.update()

        if self.enemy_manager:
            self.enemy_manager.update()

    def render_ui(self):
        self.ui.update()

    def check_collision(self):
        return

    def pause(self):
        self.paused = True

        if self.player and self.enemy_manager:
            self.player.pause()
            self.enemy_manager.pause()

    def unpause(self):
        self.paused = False

        if self.player and self.enemy_manager:
            self.player.unpause()
            self.enemy_manager.unpause()

    def setup(self):
        return

    def set_joystick(self, joystick):
        self.joystick = joystick
        if self.player:
            self.player.set_joystick(joystick)

    def update(self):
        self.render_bg()

        if not self.paused:
            self.render_foreground()
            self.check_collision()

        self.render_ui()
