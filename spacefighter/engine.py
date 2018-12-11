'''
Game Engine -- Runs the game
'''
import pygame as pg
import time

from spacefighter.colors import *
from spacefighter.player import Player
from spacefighter.enemy_manager import EnemyManager
from spacefighter.ui import UI

from spacefighter.scene_manager import SceneManager
from spacefighter.scenes.title import TitleScene
from spacefighter.scenes.pause import PauseScene
from spacefighter.scenes.game import GameScene
from spacefighter.scenes.over import GameOverScene

###
#
# PS4 controller mapping:
#
# x        -> 0
# square   -> 3
# triangle -> 2
# circle   -> 1
# options  -> 9
# dpad L   -> hat0 (-1, 0)
# dpad R   -> hat0 (1, 0)
# dpad U   -> hat0 (0, 1)
# dpad D   -> hat0 (0, -1)
# stick L  -> Axis 0 (-)
# stick R  -> Axis 0 (+)
# stick U  -> Axis 1 (-)
# stick D  -> Axis 1 (+)
#
###

class Engine(object):

    def __init__(self, display=(800, 600)):
        self.display = display
        self.screen = pg.display.set_mode(self.display, pg.FULLSCREEN)
        # self.screen = pg.display.set_mode(self.display)
        self.clock = pg.time.Clock()
        self.running = True

        self.player = Player(screen=self.screen)
        self.enemy_manager = EnemyManager(self.screen, self.clock)

        self.ui = UI(self.screen)

        self.intro = True
        self.paused = False

        self.scene_manager = None
        self.current = 'title'

        self.joystick = None
        self.ui_sound = pg.mixer.Sound('assets/sounds/ui_action.wav')

        pg.display.set_caption('Space Fighter')

    def handle_event(self, e):
        if e.type == pg.QUIT:
            self.running = False

        if self.joystick:
            if e.type == pg.JOYBUTTONDOWN:
                opts_button = self.joystick.get_button(9)
                x_button = self.joystick.get_button(0)

                if x_button == 1 and self.intro:
                    self.ui_sound.play()
                    self.intro = False

                if opts_button == 1 and self.player.lives < 1:
                    self.ui_sound.play()
                    self.intro = True
                    self.player.reset()
                    self.enemy_manager.reset()

                if opts_button == 1 and self.player.lives > 0 and not self.intro:
                    self.ui_sound.play()
                    self.pause()

        if e.type == pg.KEYDOWN:
            if e.key == pg.K_ESCAPE and self.player.lives > 0 and not self.intro:
                self.ui_sound.play()
                self.pause()

            if self.player.lives < 1 and e.key == pg.K_RETURN:
                self.ui_sound.play()
                self.intro = True
                self.player.reset()
                self.enemy_manager.reset()

            if self.intro and e.key == pg.K_RETURN:
                self.ui_sound.play()
                self.intro = False

            if e.key == pg.K_q and pg.key.get_mods() & pg.KMOD_CTRL:
                self.running = False

    def pause(self):
        self.paused = not self.paused

    def set_state(self):
        old = self.current

        if self.intro:
            self.current = 'title'

        if self.player.lives > 0 and not self.intro:
            self.current = 'game'

        if self.paused and not self.intro:
            self.current = 'pause'

        if self.player.lives < 1:
            self.current = 'dead'

        if self.current != old:
            self.scene_manager.set_scene(self.current)

    def setup(self):
        title = TitleScene(self.screen, None, None, None, self.clock)
        pause = PauseScene(self.screen, None, self.player, None, self.clock)
        game = GameScene(self.screen, None, self.player, self.enemy_manager, self.clock)
        dead = GameOverScene(self.screen, None, self.player, None, self.clock)

        game.setup()

        self.scene_manager = SceneManager(title)
        self.scene_manager.add_scene('pause', pause)
        self.scene_manager.add_scene('game', game)
        self.scene_manager.add_scene('dead', dead)

    def run(self):
        self.setup()

        while self.running:

            js_count = pg.joystick.get_count()
            if js_count > 0:
                self.joystick = pg.joystick.Joystick(0)
                self.joystick.init()
                self.scene_manager.use_joystick(self.joystick)


            for e in pg.event.get():
                self.handle_event(e)
                self.scene_manager.handle_event(e)

            self.screen.fill(BG_COLOR)
            self.set_state()
            self.scene_manager.update()


            pg.display.flip()
            self.clock.tick(40)

