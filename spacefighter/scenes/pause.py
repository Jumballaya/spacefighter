'''
Pause Menu Scene
'''
import pygame as pg
from spacefighter.scene import Scene

class PauseScene(Scene):

    def handle_event(self, e):
        Scene.handle_event(self, e)

        if e.type == pg.KEYDOWN:
            if e.key == pg.K_SPACE:
                self.done = True

    def render_ui(self):
        self.player.pause()
        px = (self.display[0] / 2)
        py = (self.display[1] / 2)
        self.ui.write_text('PAUSED', (px, py - 10), align='center')
        self.ui.write_text('press [ Escape ] to continue', (px, py + 20), align='center')
