from pygame import *

class Tela():
    def __init__(self):


class Personagens():
    def __init__(self): #Uxie
        self.uxie_frente = image.load("uxie_frente.png")
        self.uxie_frente = transform.scale(self.uxie_frente, (300,300))
        self.uxie_tras = image.load("uxie_tras.png")
        self.uxie_tras = transform.scale(self.uxie_tras, (300,300))
        self.uxie_direita = image.load("uxie_direita.png")
        self.uxie_direita = transform.scale(self.uxie_direita, (300,300))
        self.uxie_esquerda = image.load("uxie_esquerda.png")
        self.uxie_esquerda = transform.scale(self.uxie_esquerda, (300,300))
        self.skin = Surface((10,10))
        self.skin.fill((0,0,0))
