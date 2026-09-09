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
placar = 0
fonte = font.SysFont("Courier", 20)
cenario = image.load("imagens/cenarioluta1.png")
cenario = transform.scale(cenario, (600,600))
tela.blit(cenario, (0, 0))
tela.blit(prota.protaskin, prota.protapos)
tela.blit(prota.gatoprota, (prota.protapos[0] -20, prota.protapos[1] - 20))

while rodando:
    fps.tick(30)
    for e in event.get():
        if e.type == QUIT:
            rodando = False
        elif e.type == KEYDOWN:
            tela.fill((0,0,0))
            cenario = image.load("imagens/cenarioluta1.png")    
            cenario = transform.scale(cenario, (600,600))
            tela.blit(cenario, (0, 0))
            
            if e.key == K_UP:
                prota.change_to = "UP"
                prota.protapos = (prota.protapos[0], prota.protapos[1] - 22)        
                tela.blit(prota.protaskin, prota.protapos)
                tela.blit(prota.gatoprota_tras, (prota.protapos[0] -20, prota.protapos[1] - 20))
            if e.key == K_DOWN:
                prota.change_to = "DOWN"
                prota.protapos = (prota.protapos[0], prota.protapos[1] + 22)
                tela.blit(prota.protaskin, prota.protapos)
                tela.blit(prota.gatoprota, (prota.protapos[0] -20, prota.protapos[1] - 20))
            if e.key == K_LEFT:
                prota.change_to = "LEFT"
                prota.protapos = (prota.protapos[0] - 22, prota.protapos[1])
                tela.blit(prota.protaskin, prota.protapos)
                tela.blit(prota.gatoprota_esquerda, (prota.protapos[0] -20, prota.protapos[1] - 20))
            if e.key == K_RIGHT:
                prota.change_to = "RIGHT"
                prota.protapos = (prota.protapos[0] + 22, prota.protapos[1])
                tela.blit(prota.protaskin, prota.protapos)
                tela.blit(prota.gatoprota_direita, (prota.protapos[0] -20, prota.protapos[1] - 20))
    
    texto = fonte.render("Placar: " + str(placar), True, (255,255,255))
    tela.blit(texto, (20, 10))
    display.update()


quit()