from pygame import *


class Prota():
    def __init__(self): #gatoprota 
        self.protaskin = Surface((30,30))
        self.protapos = (300,300)
        self.protaskin.fill((255,0,0))
        self.direction = "up"
        self.change_to = self.direction
