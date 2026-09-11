from pygame import *
import random

class Prota():
    def __init__(self): #gatoprota 
        self.gatoprota = image.load("imagens/gatoprotafrente.png")
        self.gatoprota = transform.scale(self.gatoprota, (70,85))
        self.gatoprota_tras = image.load("imagens/gatoprota_tras.png")
        self.gatoprota_tras = transform.scale(self.gatoprota_tras, (70,85))
        self.gatoprota_direita = image.load("imagens/gatoprota_direita.png")
        self.gatoprota_direita = transform.scale(self.gatoprota_direita, (70,85))
        self.gatoprota_esquerda = image.load("imagens/gatoprota_esquerda.png")
        self.gatoprota_esquerda = transform.scale(self.gatoprota_esquerda, (70,85))
        self.protaskin = Surface((30,50))
        self.protapos = (300,300)
        self.protaskin.fill((255,0,0))
        self.direction = "up"
        self.change_to = self.direction


x = random.randint(40, 560)
y = 0

class flor():
    def __init__(self):
        self.flor = image.load("imagens/flor.png")
        self.flor = transform.scale(self.flor, (60,60))
        self.florpos = (x,y)