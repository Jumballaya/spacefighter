'''
Title Scene
'''
import pygame as pg
from spacefighter.scene import Scene

class TitleScene(Scene):

    def render_ui(self):
        px = (self.display[0] / 2)
        py = (self.display[1] / 2) - 120
        self.ui.write_text('Space Fighter', (px, py), align='center')

        if self.joystick:
            self.ui.write_text('Press [ x ] to continue', (px, py + 30), align='center')
            self.ui.write_text('[ D-Pad ] - Move your ship', (px - 152, py + 120), align='left')
            self.ui.write_text('[ x ]  - Shoot enemies', (px - 152, py + 150), align='left')
            self.ui.write_text('[ Options ] - Pause the game', (px - 152, py + 180), align='left')
        else:
            self.ui.write_text('Press [ Enter ] to continue', (px, py + 30), align='center')
            self.ui.write_text('[ Arrows ] - Move your ship', (px - 152, py + 120), align='left')
            self.ui.write_text('[ Space ]  - Shoot enemies', (px - 152, py + 150), align='left')
            self.ui.write_text('[ Escape ] - Pause the game', (px - 152, py + 180), align='left')
