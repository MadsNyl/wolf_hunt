import pygame as pg
from random import randint
from settings import *
from sheep import Sheep
from wolf import Wolf
from pathfinder import Pathfinder
from grass import Grass
from rock import Rock

class Board:
    def __init__(self):
        self.score = 0
        self.grass_eaten = False
        self.sheep = Sheep(10, 10)
        self.wolf = Wolf(18, 7)
        self.pathfinder = Pathfinder()
        self.generateGrass()
        #self.generateRocks()

    def update(self):
        self.score += 1 * dt
        #self.draw_grid()
        self.seek(self.sheep, self.wolf, WOLF_SPEED)
        self.sheepPathHandler(self.sheep, self.wolf)

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(screen, LIGHTGRAY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(screen, LIGHTGRAY, (0, y), (WIDTH, y))
    
    def wander(self, object):
        object.vel = self.pathfinder.wander(object)
    
    def seek(self, target, seeker, speed):
        seeker.vel = self.pathfinder.seek(target, seeker, speed)
    
    def flee(self, fleer, target, flee_radius, speed):
        fleer.vel, self.isHaunted = self.pathfinder.flee(fleer, target, flee_radius, speed)
    
    def generateGrass(self):
        for grass in range(randint(GRASS_NUM_MIN, GRASS_NUM_MAX)):
            grass = Grass(randint(1, 18), randint(1, 18))
    
    def generateRocks(self):
        for rock in range(randint(ROCK_NUM_MIN, ROCK_NUM_MAX)):
            rock = Rock(randint(1, 18), randint(1, 18))
    
    def eatGrass(self):
        for grass in grass_group:
            distance = self.pathfinder.findTarget(grass, self.sheep)
            if distance.length() < GRASS_SEEK_RADIUS:
                self.seek(grass, self.sheep, SHEEP_SPEED)
    
    def sheepPathHandler(self, target, hunter):
        # for rock in rocks:
        #     distance = self.pathfinder.findTarget(rock, target)
        #     if distance.length() < 20:
        #         target.vel = -target.vel
        self.flee(target, hunter, FLEE_RADIUS, SHEEP_SPEED)
        self.pathfinder.wallDetection(target, SHEEP_SPEED, True)
        if self.isHaunted == False:
            self.pathfinder.wallDetection(target, SHEEP_SPEED, False)
            self.wander(target)
            self.eatGrass()





    

        

        
            
