import pygame as pg
from settings import *

class Wolf(pg.sprite.Sprite):
    def __init__(self, x, y):
        self.groups = all_sprites, wolves
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = WOLF_IMG.convert_alpha()
        self.rect = self.image.get_rect(center=(x,y))
        self.vel = vec(0, 0)
        self.pos = vec(x, y) * TILESIZE
    
    def update(self):
        self.pos += self.vel * dt
        self.rect.center = self.pos
        self.wallCollide()
    
    def wallCollide(self):
        self.rect.center = self.pos
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top <= 0:
            self.rect.top = 0
    
