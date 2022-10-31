from personagem_bat import Personagem_batalha

#====================================================
#           definição dos personagens
#====================================================

#TODO: como identificar o movimento especial do personagem?
#TODO: colocar as sprites nos personagens 

toninha_maga = Personagem_batalha("Toninha Maga", 50, 15, 1, (0, 0))
toninha_golen = Personagem_batalha("Toninha Golen", 150, 30, 0.5, (0, 0))
toninha_rei = Personagem_batalha("Toninha Rei", 70, 15, 1.5, (0, 0))        #gerador de minions
toninha_monge = Personagem_batalha("Toninha Monge", 90, 15, 1, (0, 0))

soldado_atirador = Personagem_batalha("Soldado Atirador", 50, 15, 1, (0, 0))
soldado_blindado = Personagem_batalha("Soldado Blindado", 150, 30, 0.5, (0, 0))
soldado_general = Personagem_batalha("General", 70, 15, 1.5, (0, 0))        #gerador de minions
soldado_medico = Personagem_batalha("Soldado Medico", 90, 15, 1, (0, 0))

Lista1 = [toninha_maga, toninha_golen, toninha_rei, toninha_monge]
Lista2 = [soldado_atirador, soldado_blindado, soldado_general, soldado_medico]
