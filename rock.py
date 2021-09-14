import pygame as pg
import random
from settings import *

class Rock(pg.sprite.Sprite):
    def __init__(self, x, y):
        self.groups = all_sprites, rocks
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = ROCK_IMG.convert_alpha()
        self.rect = self.image.get_rect(center=(x,y))
        self.pos = vec(x, y) * TILESIZE
    
    def update(self):
        self.rect.center = self.pos