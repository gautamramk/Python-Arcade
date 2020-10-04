import pygame
from pygame.locals import *


class snakepart:
    x = None
    y = None
    screen = None
    img = None
    head = None
    direc = None

    def __init__(self, xloc, yloc, s, i, h, d):
        self.x = xloc
        self.y = yloc
        self.screen = s
        self.img = i
        self.head = h
        self.direc = d

    def render(self):
        self.screen.blit(self.img, (self.x, self.y))

    def update(self, k):
        if not self.head:
            self.direc = k
        elif self.head:
            if k[K_w] and not k[K_s] and self.direc != 1:
                self.direc = -1
            elif k[K_s] and not k[K_w] and self.direc != -1:
                self.direc = 1
            elif k[K_a] and not k[K_d] and self.direc != 2:
                self.direc = -2
            elif k[K_d] and not k[K_a] and self.direc != -2:
                self.direc = 2

        if self.direc == 1 or self.direc == -1:
            self.y += (self.direc) * 16
        else:
            self.x += (self.direc / 2) * 16

        if self.x < 0:
            self.x = 624
        elif self.x > 640:
            self.x = 16
        if self.y < 0:
            self.y = 624
        elif self.y > 640:
            self.y = 16
