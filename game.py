'''
Space Fighter -- Space Invaders clone in PyGame
'''
import pygame as pg
import sys
from spacefighter.engine import Engine


def entry():
    pg.init()
    pg.joystick.init()

    display = (800, 600)
    if len(sys.argv) == 3:
        display = (int(sys.argv[1]), int(sys.argv[2]))

    e = Engine(display=display)
    e.run()

    pg.quit
    sys.exit()


if __name__ == '__main__':
    entry()
