# This class handles sprite sheets
# This was taken from www.scriptefun.com/transcript-2-using
# sprite-sheets-and-drawing-the-background
# I've added some code to fail if the file wasn't found..
# Note: When calling images_at the rect is the format:
# (x, y, x + offset, y + offset)

import pygame
import math
from PIL import Image

class Spritesheet(object):

    def __init__(self, filename, key={}):
        try:
            self.filename = filename
            self.sheet = pygame.image.load(filename).convert()
            self.key = key
        except (pygame.error):
            print('Unable to load spritesheet image:', filename)
            raise (SystemExit)

    # Load a specific image from a specific rectangle
    def image_at(self, rectangle, colorkey = None):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    # Load a whole bunch of images and return them as a list
    def images_at(self, rects, colorkey = None):
        return [self.image_at(rect, colorkey) for rect in rects]

    # Load all sprites in the sheet into an array
    def images_all(self, dimensions, colorkey = None):
        img = Image.open(self.filename)
        iW, iH = img.size
        tW, tH = dimensions
        imgs = []

        for i in range(0, math.floor(iW / tW)):
            for j in range(0, math.floor(iH / tH)):
                rect = (i * tW, j * tH, tW, tH)
                imgs.append(self.image_at(rect, colorkey))

        return imgs

    # Load a whole strip of images
    def load_strip(self, rect, image_count, colorkey = None):
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)
