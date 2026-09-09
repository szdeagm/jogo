from pygame import *
from classes import *

init()

prota = Prota()
tela = display.set_mode((600,600))
display.set_caption("CastleCat: Em busca da dignidade do povo felino")
rodando = True
fps = time.Clock()
vidaprota = 5
vida_bat = 1
vida_flor = 2
vida_libelula = 1
vidadracula = 20
placar = 0
fonte = font.SysFont("Courier", 20)
cenario = image.load("imagens/cenarioluta1.png")
cenario = transform.scale(cenario, (600,600))
tela.blit(cenario, (0, 0))
tela.blit(prota.protaskin, prota.protapos)
tela.blit(prota.gatoprota, (prota.protapos[0] -20, prota.protapos[1] - 20))

while rodando:
    fps.tick(60) # Aumentei para 60 para o movimento ficar muito mais liso
    
    # 1. LOOP DE EVENTOS (Apenas para fechar a janela)
    for e in event.get():
        if e.type == QUIT:
            rodando = False
        
    # 2. CAPTURA DE TECLAS (FORA do loop de eventos - Alinhado com o "for")
    teclas = key.get_pressed()
        
    if teclas[K_w] and prota.protapos[1] > 0:
        prota.change_to = "UP"
        prota.protapos = (prota.protapos[0], prota.protapos[1] - 4) # Reduzi o passo para compensar os 60 FPS
            
    if teclas[K_s] and prota.protapos[1] < 550: # Ajustado limite para o boneco não sumir embaixo
        prota.change_to = "DOWN"
        prota.protapos = (prota.protapos[0], prota.protapos[1] + 4)                
        
    if teclas[K_a] and prota.protapos[0] > 0:
        prota.change_to = "LEFT"
        prota.protapos = (prota.protapos[0] - 4, prota.protapos[1])
            
    if teclas[K_d] and prota.protapos[0] < 550: # Ajustado limite para o boneco não sumir na direita
        prota.change_to = "RIGHT"
        prota.protapos = (prota.protapos[0] + 4, prota.protapos[1])

    # 3. RENDERIZAÇÃO (FORA do loop de eventos)
    tela.fill((0,0,0))
    
    # REMOVIDO o image.load daqui. Usamos a variável 'cenario' que foi criada lá no topo!
    tela.blit(cenario, (0, 0))
            
    if prota.change_to == "UP":
        tela.blit(prota.protaskin, prota.protapos)
        tela.blit(prota.gatoprota_tras, (prota.protapos[0] - 20, prota.protapos[1] - 20))
    elif prota.change_to == "DOWN":
        tela.blit(prota.protaskin, prota.protapos)
        tela.blit(prota.gatoprota, (prota.protapos[0] - 20, prota.protapos[1] - 20))
    elif prota.change_to == "LEFT":
        tela.blit(prota.protaskin, prota.protapos)
        tela.blit(prota.gatoprota_esquerda, (prota.protapos[0] - 20, prota.protapos[1] - 20))  
    elif prota.change_to == "RIGHT":
        tela.blit(prota.protaskin, prota.protapos)
        tela.blit(prota.gatoprota_direita, (prota.protapos[0] - 20, prota.protapos[1] - 20))

    # Texto do Placar e Vida
    texto = fonte.render("Placar: " + str(placar), True, (255,255,255))
    texto2 = fonte.render("Vida: " + str(vidaprota), True, (255,255,255))
    tela.blit(texto, (20, 10))
    tela.blit(texto2, (500, 10))
    
    # Atualiza a tela inteira de uma vez só
    display.update()

quit()
