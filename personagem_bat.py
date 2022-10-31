from typing import Tuple
import pygame as pg
from config_jogo import ConfigJogo


class Personagem_batalha:
    def __init__(self, nome: str, vida: float, dano: float,
    velocidade: float, posicao: Tuple[float, float]):
        self.nome = nome
        self.vida = vida
        self.dano = dano
        self.velocidade = velocidade
        self.posicao = posicao
        self.velocidade_x = 0
        self.velocidade_y = 0
        '''self.sprite_comum = sprite_persona
        self.sprite_hit = sprite_hit
        self.sprite_dano = sprite_dano'''

    def mover_para_cima(self):
        self.velocidade_y = -self.velocidade

    def mover_para_baixo(self):
        self.velocidade_y = self.velocidade

    def mover_para_direita(self):
        self.velocidade_x = self.velocidade

    def mover_para_esquerda(self):
        self.velocidade_x = -self.velocidade

    def parar_x(self):
        self.velocidade_x = 0
    def parar_y(self):
        self.velocidade_y = 0

    def atualizar_posicao(self):
        x, y = self.posicao
        novo_x = x + self.velocidade_x
        novo_y = y + self.velocidade_y

        if ((novo_y >= 0) and \
                ((novo_y + ConfigJogo.ALTURA_P) <= ConfigJogo.ALTURA_TELA_PRINCIPAL)) and ((novo_x >= 0) \
                    and ((novo_x + ConfigJogo.LARGURA_P) <= ConfigJogo.LARGURA_TELA_PRINCIPAL)): 
            self.posicao = (novo_x, novo_y)

    def rect(self) -> Tuple[float, float, float, float]:
        """ retorna os dados da P como os retangulos sao representados 
            no pygame, i.e., como uma tupla do tipo (px, py, largura, altura).
        """
        return self.posicao + (ConfigJogo.LARGURA_P, ConfigJogo.ALTURA_P)

    def desenha(self, tela):
        x = self.posicao[0]
        y = self.posicao[1]
        l = ConfigJogo.LARGURA_P
        a = ConfigJogo.ALTURA_P
        pg.draw.rect(
            tela,
            (0,0,0),
            pg.rect.Rect(x, y, l, a)
        )
    
    def ataque(self):
        #TODO: cria um circulo de alcance de ataque
        #se distancia < raio: dano no oponente, isto é,
        #if self.ataque == True: 
        #   persona2.vida -= persona1.dano
        #   imprimir sprite de ataque
        pass
