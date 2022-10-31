import sys
import pygame as pg
from config_jogo import ConfigJogo
from persona import Lista1
from persona import Lista2
from personagem_bat import Personagem_batalha

class CenaPrincipal:
    def __init__(self, tela, indice1, indice2):
        self.tela = tela
        self.encerra = False
        
        py = ConfigJogo.ALTURA_TELA // 2 - ConfigJogo.ALTURA_P // 2
        px_esq = ConfigJogo.POS_X1
        px_dir = ConfigJogo.POS_X2

        self.player1 = Lista1[indice1]
        self.player2 = Lista2[indice2]

        self.player1.posicao = (px_esq, py)     #self.player1 = Personagem_batalha(posicao=(px_esq, py))
        self.player2.posicao = (px_dir, py)     #self.player2 = Personagem_batalha(posicao=(px_dir, py))
        

    def tratamento_eventos(self):

        for event in pg.event.get():
            if (event.type == pg.QUIT):
                sys.exit()
            
            if (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                ConfigJogo.TELA -= 2
                self.encerra = True

            if pg.key.get_pressed()[pg.K_a]:
                self.player1.mover_para_esquerda()
            elif pg.key.get_pressed()[pg.K_d]:
                self.player1.mover_para_direita()
            else:
                self.player1.parar_x()
            
            if pg.key.get_pressed()[pg.K_j]:
                self.player2.mover_para_esquerda()
            elif pg.key.get_pressed()[pg.K_l]:
                self.player2.mover_para_direita()
            else:
                self.player2.parar_x()
            
            
            if pg.key.get_pressed()[pg.K_w]:
                self.player1.mover_para_cima()
            elif pg.key.get_pressed()[pg.K_s]:
                self.player1.mover_para_baixo()
            else:
                self.player1.parar_y()
            
            if pg.key.get_pressed()[pg.K_i]:
                self.player2.mover_para_cima()
            elif pg.key.get_pressed()[pg.K_k]:
                self.player2.mover_para_baixo()
            else:
                self.player2.parar_y()
    
    def rodar(self):
        while not self.encerra:
            self.tratamento_eventos()
            self.atualiza_estado()
            self.desenha()
            

    def desenha(self):
        self.tela.fill((255, 255, 255))
        self.player2.desenha(self.tela)
        self.player1.desenha(self.tela)

        pg.display.flip()

    def atualiza_estado(self):
        self.player1.atualizar_posicao()
        self.player2.atualizar_posicao()