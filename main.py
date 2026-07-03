from pygame import *
from classes import *

init()

prota = Prota()
tela = display.set_mode((600,600))
display.set_caption("CastleCat: Em busca da dignidade do povo felino")
rodando = True
fps = time.Clock()
vidaprota = 100
vidaoponente = 50
vidadracula = 200

while rodando:
    fps.tick(60)
    for e in event.get():
        if e.type == QUIT:
            rodando = False
        elif e.type == KEYDOWN:
            tela.fill((0,0,0))
            if e.key == K_UP:
                prota.change_to = "UP"
                prota.protapos = (prota.protapos[0], prota.protapos[1] - 15)
            if e.key == K_DOWN:
                prota.change_to = "DOWN"
                prota.protapos = (prota.protapos[0], prota.protapos[1] + 15)
            if e.key == K_LEFT:
                prota.change_to = "LEFT"
                prota.protapos = (prota.protapos[0] - 15, prota.protapos[1])
            if e.key == K_RIGHT:
                prota.change_to = "RIGHT"
                prota.protapos = (prota.protapos[0] + 15, prota.protapos[1])
    tela.blit(prota.protaskin, prota.protapos)
    display.update()


quit()