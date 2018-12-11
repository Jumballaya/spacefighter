'''
Game UI Class
'''
import math
import pygame as pg
from spacefighter.colors import *

class TextBox(object):
    def __init__(self, screen, text, pos, font, color=WHITE, aa=True, align=None):
        self.screen = screen
        r = self.screen.get_rect()
        self.display = (r.w, r.h)

        if type(text) == str:
            self.text = text
            self.txtFn = None
        else:
            self.text = text()
            self.txtFn = text

        self.font = font
        self.pos = pos
        self.rotate = 0
        self.color = color
        self.aa = aa
        self.align = align

        self.surface = self.font.render(self.text, self.aa, self.color)

        if self.align:
            rect = self.surface.get_rect()
            if self.align == 'center':
                x = pos[0] - (rect.w / 2)
                y = pos[1] - (rect.h / 2)
                self.pos = (x, y)
            if self.align == 'right':
                x = pos[0] - rect.w
                y = pos[1] - (rect.h / 2)
                self.pos = (x, y)
            if self.align == 'left':
                x = pos[0]
                y = pos[1] - (rect.h / 2)
                self.pos = (x, y)


    def rotate(self, rot):
        self.rotate = rot
        self.surface = pg.transform.rotate(self.surface, self.rotate)

    def update(self):
        if self.txtFn:
            self.text = self.txtFn()

        self.surface = self.font.render(self.text, self.aa, self.color)
        self.screen.blit(self.surface, self.pos)

class UI(object):
    def __init__(self, screen):
        self.screen = screen
        self.rect = self.screen.get_rect()
        self.display = (self.rect.w, self.rect.h)

        self.font_size = 18
        self.font_file = 'assets/FiraMono-Regular.ttf'
        self.font = pg.font.Font(self.font_file, self.font_size)

        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def add_text_item(self, txt, pos, rotate=None, align=None):
        t = TextBox(self.screen, txt, pos, self.font, align=align)
        if rotate != None:
            t.rotate(rotate)

        self.items.append(t)

    def write_text(self, txt, pos, rotate=None, align=None):
        t = TextBox(self.screen, txt, pos, self.font, align=align)
        if rotate != None:
            t.rotate(rotate)
        t.update()

    def handle_event(self, e):
        return

    def update(self):
        for i in self.items:
            i.update()

        return
