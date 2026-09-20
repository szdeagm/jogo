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

#flor
x = random.randint(40, 500)
y = 600
#libelula
dx = 0
dy = random.randint(40, 500)

fx = 600
fy = random.randint(40, 500)

bx = random.randint(40, 500)
by = 0

class flor():
    def __init__(self):
        self.flor = image.load("imagens/flor.png")
        self.flor = transform.scale(self.flor, (60,60))
        self.florpos = (x,y)

class libelula():
    def __init__(self):
        self.libelula = image.load("imagens/libelula.png")
        self.libelula = transform.scale(self.libelula, (60,60))
        self.libelulapos = (dx,dy)

class libelula2():
    def __init__(self):
        self.libelula2 = image.load("imagens/libelula2.png")
        self.libelula2 = transform.scale(self.libelula2, (60,60))
        self.libelula2pos = (fx,fy)

class morcego():
    def __init__(self):
        self.morcego = image.load("imagens/morceguinho.png")
        self.morcego = transform.scale(self.morcego, (85,60))
        self.morcegopos = (bx,by)

class Tiro():
    def __init__(self, x, y, direcao):
        self.direcao = direcao.upper()    # "UP", "DOWN", "LEFT", "RIGHT"
        self.velocidade = 8

        
        if direcao in ("UP", "DOWN"):
            self.tiro = image.load("imagens/olho.png")
            self.tiro = transform.scale(self.tiro, (18, 26))
        else:
            self.tiro = image.load("imagens/olho.png")
            self.tiro = transform.scale(self.tiro, (26, 18))
      # vermelho

        # Posição inicial centralizada no personagem
        self.rect = self.tiro.get_rect(center=(x, y))

    def atualizar(self):
        if self.direcao == "UP":
            self.rect.y -= self.velocidade
        elif self.direcao == "DOWN":
            self.rect.y += self.velocidade
        elif self.direcao == "LEFT":
            self.rect.x -= self.velocidade
        elif self.direcao == "RIGHT":
            self.rect.x += self.velocidade

    def desenhar(self, tela):
        tela.blit(self.tiro, self.rect)

    def fora_da_tela(self):
        return (self.rect.right < 0 or self.rect.left > 600 or
                self.rect.bottom < 0 or self.rect.top > 600)