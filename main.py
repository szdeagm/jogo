from pygame import *
from classes import *
import random
import sys
import asyncio 

async def main():
    init()

    libelula = libelula()
    lib2 = libelula2()
    flor = flor()
    bat = morcego()
    prota = Prota()
    LARGURA, ALTURA = 600, 600
    tela = display.set_mode((600, 600))
    display.set_caption("CastleCat: Em busca da dignidade do povo felino")
    rodando = True
    fps = time.Clock()

    vidaprota = 5
    vida_bat = 1
    vida_flor = 1
    vida_libelula = 1
    vida_libelula2 = 1
    vidadracula = 20
    placar = 0

    tiros = []                                  

    fonte = font.SysFont("Courier", 20)

    cenario = image.load("imagens/cenarioluta1.png")
    cenario = transform.scale(cenario, (600, 600))

    jogo_iniciado = False
    
    # Cores
    PRETO = (0, 0, 0)
    BRANCO = (255, 255, 255)
    VERDE = (0, 255, 0)

    # Fonte
    fonte_titulo = font.SysFont("Courier", 50, bold=True)
    fonte_subtitulo = font.SysFont("Courier", 20)



    def exibir_tela_vitoria():
        """Loop exclusivo para a tela de vitória."""
        executando_win = True
        
        while executando_win:
            tela.fill(PRETO)
            
            # Renderização dos textos
            texto_ganhou = fonte_titulo.render("VOCÊ VENCEU!", True, VERDE)
            texto_instrucao = fonte_subtitulo.render("Pressione ESPAÇO para reiniciar ou ESC para sair", True, BRANCO)
            
            # Centralizando os textos na tela
            tela.blit(texto_ganhou, (LARGURA // 2 - texto_ganhou.get_width() // 2, ALTURA // 3))
            tela.blit(texto_instrucao, (LARGURA // 2 - texto_instrucao.get_width() // 2, ALTURA // 2))
            
            # Captura de eventos na tela de vitória
            for evento in event.get():
                if evento.type == QUIT:
                    quit()
                    sys.exit()
                if evento.type == KEYDOWN:
                    if evento.key == K_SPACE:
                        executando_win = False  # Sai da tela de vitória e volta ao jogo
                    if evento.key == K_ESCAPE:
                        quit()
                        sys.exit()
                        
            display.flip()
            fps.tick(60)


    while rodando:
        fps.tick(60)
        await asyncio.sleep(0)

        # ---------------- EVENTOS ----------------
        for e in event.get():
            if e.type == QUIT:
                rodando = False

            if e.type == KEYDOWN and e.key == K_SPACE:
                cx = prota.protapos[0] + 15      # centro horizontal do gato
                cy = prota.protapos[1] + 25      # centro vertical do gato
                tiros.append(Tiro(cx, cy, prota.change_to))

            if placar >= 150:
                exibir_tela_vitoria()
                # Reinicia o jogo após a tela de vitória
                vidaprota = 5
                vida_bat = 1
                vida_flor = 1
                vida_libelula = 1
                vida_libelula2 = 1
                placar = 0
                prota.protapos = (300, 300)
                flor.florpos = (random.randint(40, 560), 600)
                libelula.libelulapos = (0, random.randint(40, 560))
                lib2.libelula2pos = (600, random.randint(40, 560))
                bat.morcegopos = (random.randint(40, 560), 0)

        # ---------------- MOVIMENTO ----------------
        teclas = key.get_pressed()

        if teclas[K_w] or teclas[K_s] or teclas[K_a] or teclas[K_d]:
            jogo_iniciado = True

        if teclas[K_w] and prota.protapos[1] > 0:
            prota.change_to = "UP"
            prota.protapos = (prota.protapos[0], prota.protapos[1] - 4)

        if teclas[K_s] and prota.protapos[1] < 550:
            prota.change_to = "DOWN"
            prota.protapos = (prota.protapos[0], prota.protapos[1] + 4)

        if teclas[K_a] and prota.protapos[0] > 0:
            prota.change_to = "LEFT"
            prota.protapos = (prota.protapos[0] - 4, prota.protapos[1])

        if teclas[K_d] and prota.protapos[0] < 550:
            prota.change_to = "RIGHT"
            prota.protapos = (prota.protapos[0] + 4, prota.protapos[1])


        tela.fill((0, 0, 0))
        tela.blit(cenario, (0, 0))

        # Protagonista
        if prota.change_to == "UP":
            tela.blit(prota.protaskin, prota.protapos)
            tela.blit(prota.gatoprota_tras,
                    (prota.protapos[0] - 20, prota.protapos[1] - 20))
        elif prota.change_to == "DOWN":
            tela.blit(prota.protaskin, prota.protapos)
            tela.blit(prota.gatoprota,
                    (prota.protapos[0] - 20, prota.protapos[1] - 20))
        elif prota.change_to == "LEFT":
            tela.blit(prota.protaskin, prota.protapos)
            tela.blit(prota.gatoprota_esquerda,
                    (prota.protapos[0] - 20, prota.protapos[1] - 20))
        elif prota.change_to == "RIGHT":
            tela.blit(prota.protaskin, prota.protapos)
            tela.blit(prota.gatoprota_direita,
                    (prota.protapos[0] - 20, prota.protapos[1] - 20))


        if jogo_iniciado:
            # Inimigo flor
            tela.blit(flor.flor, flor.florpos)
            if flor.florpos[1] < 0:
                x_novo = random.randint(40, 560)
                flor.florpos = (x_novo, 600)
            else:
                y_novo = flor.florpos[1] - 6
                flor.florpos = (flor.florpos[0], y_novo)

            #Inimigo libelula
            tela.blit(libelula.libelula, libelula.libelulapos)
            if libelula.libelulapos[0] > 600:
                dy_novo = random.randint(40, 560)
                libelula.libelulapos = (0, dy_novo)
            else:
                dx_novo = libelula.libelulapos[0] + 5
                libelula.libelulapos = (dx_novo, libelula.libelulapos[1])

            #libelula2
            tela.blit(lib2.libelula2, lib2.libelula2pos)
            if lib2.libelula2pos[0] < 0:
                fy_novo = random.randint(40, 560)
                lib2.libelula2pos = (600, fy_novo)
            else:
                fx_novo = lib2.libelula2pos[0] - 5
                lib2.libelula2pos = (fx_novo, lib2.libelula2pos[1])

            #Morcego
            tela.blit(bat.morcego, bat.morcegopos)
            if bat.morcegopos[1] > 600:
                by_novo = random.randint(40, 560)
                bat.morcegopos = (by_novo, 0)
            else:
                bx_novo = bat.morcegopos[1] + 3
                bat.morcegopos = (bat.morcegopos[0], bx_novo)

        # ---------------- TIROS ----------------
        for t in tiros[:]:                        # [:] para poder remover durante o loop
            t.atualizar()
            if t.fora_da_tela():
                tiros.remove(t)
            else:
                t.desenhar(tela)

        for t in tiros[:]:
            if t.rect.colliderect(flor.flor.get_rect(topleft=flor.florpos)):
                tiros.remove(t)
                vida_flor -= 1  
                placar += 10
                # reposiciona a flor
                flor.florpos = (random.randint(40, 560), 0)

            if t.rect.colliderect(libelula.libelula.get_rect(topleft=libelula.libelulapos)):
                tiros.remove(t)
                vida_libelula -= 1  
                placar += 10
                # reposiciona a libelula
                libelula.libelulapos = (0, random.randint(0, 560))

            if t.rect.colliderect(lib2.libelula2.get_rect(topleft=lib2.libelula2pos)):
                tiros.remove(t)
                vida_libelula2 -= 1  
                placar += 10
                # reposiciona a libelula2
                lib2.libelula2pos = (600, random.randint(0, 560))
            
            if t.rect.colliderect(bat.morcego.get_rect(topleft=bat.morcegopos)):
                tiros.remove(t)
                vida_bat -= 1  
                placar += 10
                # reposiciona o morcego
                bat.morcegopos = (random.randint(40, 560), 0)

        if vida_flor <= 0:
            vida_flor = 1
            flor.florpos = (random.randint(40, 560), 0)

        if vida_libelula <= 0:
            vida_libelula = 1
            libelula.libelulapos = (libelula.libelulapos[1], random.randint(40, 560))

        if vida_libelula2 <= 0:
            vida_libelula2 = 1
            lib2.libelula2pos = (lib2.libelula2pos[1], random.randint(40, 560))
        
        if vida_bat <= 0:
            vida_bat = 1
            bat.morcegopos = (random.randint(40, 560), 0)

        if prota.protaskin.get_rect(topleft=prota.protapos).colliderect(flor.flor.get_rect(topleft=flor.florpos)):
            vidaprota -= 1
            flor.florpos = (random.randint(40, 560), 0)
        if prota.protaskin.get_rect(topleft=prota.protapos).colliderect(libelula.libelula.get_rect(topleft=libelula.libelulapos)):
            vidaprota -= 1
            libelula.libelulapos = (libelula.libelulapos[1], random.randint(40, 560))
        if prota.protaskin.get_rect(topleft=prota.protapos).colliderect(lib2.libelula2.get_rect(topleft=lib2.libelula2pos)):
            vidaprota -= 1
            lib2.libelula2pos = (lib2.libelula2pos[1], random.randint(40, 560))
        if prota.protaskin.get_rect(topleft=prota.protapos).colliderect(bat.morcego.get_rect(topleft=bat.morcegopos)):
            vidaprota -= 1
            bat.morcegopos = (random.randint(40, 560), 0)
        if vidaprota == 0:
            rodando = False

        # ---------------- HUD ----------------
        texto = fonte.render("Placar: " + str(placar), True, (255, 255, 255))
        texto2 = fonte.render("Vida: " + str(vidaprota), True, (255, 255, 255))
        tela.blit(texto, (20, 10))
        tela.blit(texto2, (500, 10))

        display.update()

    quit()

syncio.run(main()) 