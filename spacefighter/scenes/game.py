'''
Game Scene
'''
import pygame as pg
from spacefighter.scene import Scene

class GameScene(Scene):

    def setup(self):
        self.player.rect.centerx = self.display[0] / 2
        self.player.rect.y = self.display[1] - 90
        self.enemy_manager.setup_level()

    def render_ui(self):
        self.player.unpause()
        self.ui.write_text(self.get_lives(), (10, 10))
        self.ui.write_text(self.get_score(), (10, 40))
        self.ui.write_text(self.get_level(), (10, 70))

        x = self.screen.get_rect().w - 30
        self.ui.write_text(self.get_wave(), (x, 30), align='right')

    def check_collision(self):
        self.enemy_manager.check_collision(self.player.bullets, cb=self.player.shoot_object)

        self.player.check_collision(self.enemy_manager.ships)
        for s in self.enemy_manager.ships:
            self.player.check_collision(s.bullets)

    def get_score(self):
        s = 'Score: %d' % self.player.score
        return s

    def get_lives(self):
        l = 'Lives: %d' % self.player.lives
        return l

    def get_level(self):
        l = 'Level: %d' % self.player.level
        return l

    def get_wave(self):
        l = 'Wave: %d' % self.enemy_manager.level
        return l

