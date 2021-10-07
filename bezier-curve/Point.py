import pygame as pg
import math



class Point:
    def __init__(self, position) -> None:
        self.position = position
    
    def draw(self, surface, color, radius):
        pg.draw.circle(surface, color, self.position, radius)
    
    def distanceTo(self, other):
        x = self.position[0] - other.position[0]
        y = self.position[1] - other.position[1]
        return math.sqrt(math.pow(x, 2) + math.pow(y, 2))
    
    def collidesWith(self, point, radius):
        return radius > self.distanceTo(point)









