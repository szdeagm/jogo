from pygame import *

class Tela():
    def __init__(self):


class Personagens():
    def __init__(self): #gatoprota
        self.gatoprota_frente = image.load("gatoprota_frente.png")
        self.gatoprota_frente = transform.scale(self.gatoprota_frente, (300,300))
        self.gatoprota_tras = image.load("gatoprota_tras.png")
        self.gatoprota_tras = transform.scale(self.gatoprota_tras, (300,300))
        self.gatoprota_direita = image.load("gatoprota_direita.png")
        self.gatoprota_direita = transform.scale(self.gatoprota_direita, (300,300))
        self.gatoprota_esquerda = image.load("gatoprota_esquerda.png")
        self.gatoprota_esquerda = transform.scale(self.gatoprota_esquerda, (300,300))
        self.skin = Surface((10,10))
        self.skin.fill((0,0,0))
