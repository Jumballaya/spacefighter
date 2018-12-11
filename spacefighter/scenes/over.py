'''
GameOver Scene
'''
import pygame as pg
from spacefighter.scene import Scene

class GameOverScene(Scene):

    def handle_event(self, e):
        Scene.handle_event(self, e)

        if e.type == pg.KEYDOWN:
            if e.key == pg.K_RETURN:
                self.done = True

        if self.joystick:
            if e.type == pg.JOYBUTTONDOWN:
                x_button = self.joystick.get_button(0)
                if x_button == 1:
                    self.done = True

    def get_score(self):
        s = 'your score was: %d' % self.player.score
        return s

    def render_ui(self):
        self.player.pause()
        px = (self.display[0] / 2)
        py = (self.display[1] / 2)

        button = "Enter"
        if self.joystick: button = "Options"
        message = 'press [ %s ] to continue' % button

        self.ui.write_text('GAMEOVER', (px, py - 30), align='center')
        self.ui.write_text(message, (px, py), align='center')
        self.ui.write_text(self.get_score(), (px, py + 60), align='center')
