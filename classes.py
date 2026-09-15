from pygame import *
import random

class Prota():
    def __init__(self): #gatoprota 
        self.rect = Rect(300, 300, 30, 50)
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


x = random.randint(40, 500)
y = 0

class flor():
    def __init__(self):
        self.flor = image.load("imagens/flor.png")
        self.flor = transform.scale(self.flor, (60,60))
        self.florpos = (x,y)

class Tiro:
    def __init__(self, x, y, dx, dy):
        self.rect = Rect(x, y, 8, 8)
        self.velocidade = 8
        self.dx = dx
        self.dy = dy

    def atualizar(self):
        self.rect.x += self.dx * self.velocidade
        self.rect.y += self.dy * self.velocidade

    def desenhar(self, superficie):
        pygame.draw.rect(superficie, (255, 0, 0), self.rect)