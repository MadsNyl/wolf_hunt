import pygame as pg
import random
from settings import *

class Grass(pg.sprite.Sprite):
    def __init__(self, x, y):
        self.groups = all_sprites, grass_group 
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = GRASS_IMG.convert_alpha()
        self.rect = self.image.get_rect(center=(x,y))
        self.pos = vec(x, y) * TILESIZE
    
    def update(self):
        self.rect.center = self.pos