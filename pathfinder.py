import pygame as pg
from random import choice
from settings import *

class Pathfinder:
    def __init__(self):
        self.directions = [vec(SHEEP_SPEED, 0), vec(-SHEEP_SPEED, 0), vec(0, SHEEP_SPEED), vec(0, -SHEEP_SPEED),
                            vec(SHEEP_SPEED * 0.7071, SHEEP_SPEED * 0.7071), vec(-SHEEP_SPEED * 0.7071, SHEEP_SPEED * 0.7071), vec(-SHEEP_SPEED * 0.7071, - SHEEP_SPEED * 0.7071), vec(SHEEP_SPEED * 0.7071, -SHEEP_SPEED * 0.7071)]
        self.last_dir_change = 0

    def wander(self, object):
        vel = object.vel
        now = pg.time.get_ticks()
        if now - self.last_dir_change > CHANGE_DIR_TIME:
            vel = self.getDir()
            self.last_dir_change = now
        return vel
    
    def getDir(self):
        return choice(self.directions)

    def seek(self, target, seeker, speed):
        vel = (target.pos - seeker.pos).normalize() * speed
        return vel
    
    def findTarget(self, object, subject):
        distance = object.pos - subject.pos
        return distance
    
    def flee(self, fleer, target, flee_radius, speed):
        isHunted = False 
        steer = fleer.vel
        desired = vec(0, 0)
        distance = fleer.pos - target.pos
        if distance.length() < flee_radius:
            isHunted = True
            desired = distance.normalize() * speed
            steer = desired
        return steer, isHunted
    
    def wallDetection(self, object, speed, isFleeing):
        if isFleeing:
            if object.rect.left <= 0:
                object.vel = vec(0, -speed)
            elif object.rect.right >= WIDTH:
                object.vel = vec(0, speed)
            elif object.rect.bottom >= HEIGHT:
                object.vel = vec(-speed, 0)
            elif object.rect.top <= 0:
                object.vel = vec(speed, 0)
        else:
            if object.rect.left <= 0:
                object.vel = vec(speed, 0)
            elif object.rect.right >= WIDTH:
                object.vel = vec(-speed, 0)
            elif object.rect.bottom >= HEIGHT:
                object.vel = vec(0, -speed)
            elif object.rect.top <= 0:
                object.vel = vec(0, speed)
