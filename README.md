# CastleCat: Em busca da dignidade do povo felino


meio revolução russa. no final o reino vira União das Vilas Felinutópicas Felinasticas (UVFF). 

Class do Prota
        self.gatoprota_frente = image.load("gatoprota_frente.png")
        self.gatoprota_frente = transform.scale(self.gatoprota_frente, (300,300))
        self.gatoprota_tras = image.load("gatoprota_tras.png")
        self.gatoprota_tras = transform.scale(self.gatoprota_tras, (300,300))
        self.gatoprota_direita = image.load("gatoprota_direita.png")
        self.gatoprota_direita = transform.scale(self.gatoprota_direita, (300,300))
        self.gatoprota_esquerda = image.load("gatoprota_esquerda.png")
        self.gatoprota_esquerda = transform.scale(self.gatoprota_esquerda, (300,300))


class Fundo():
    def __init__(self):
        self.fundo = image.load("fundodaluta.png")
        self.fundo = transform.scale(self.fundodaluta, (600,600))