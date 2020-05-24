import neat
import time
import os
import pygame
import random

# size of the window
WIDTH = 600
HEIGHT = 800

# Loading images of the objects
# a bird has three images showing the different state of the bird's wings
BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(imgs/bird1.png)), pygame.transform.scale2x(pygame.image.load(imgs/bird2.png)), pygame.transform.scale2x(pygame.image.load(imgs/bird3.png))]
PIPE = pygame.transform.scale2x(pygame.image.load(imgs/pipe.png))
BASE = pygame.transform.scale2x(pygame.image.load(imgs/base.png))
BG = pygame.transform.scale2x(pygame.image.load(imgs/bg.png))


# defining bird object.
class Bird:
    IMG = BIRD_IMGS
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMG[0]

    def jump(self):
        self.vel = 10.5
        self.tick_count = 0
        self.height = self.y

