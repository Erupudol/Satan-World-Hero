import pygame as pg

pg.init()
 
# Colors
# Cores
BGREEN = (21, 35, 12)
BLACK    = (0, 0, 0) 
BLUE     = (0, 0, 255)
DARKBLUE = (47, 54, 153)
FAINTBLUE = (0, 64, 128)
GRAY = (81, 74, 67)
GREEN = (55, 117, 44)
ORANGE = (186, 53, 7)
RED = (255, 0, 0)
WHITE    = (255, 255, 255)
YELLOW = (253, 235, 7)
 
# Screen dimensions
SCREEN_WIDTH  = 1150
SCREEN_HEIGHT = 700
#Gerais:
Game_loop = False
FPS = 60
i = 0
s = 0
d = 0
delay = 0
delays = 0
teste = 0
count = 0

"""Status dos Personagens:"""
Hp = 0 #Hp Atual do Jogador 
Hp_Max = 0 # Hp Max do Jogador 
Mp = 0 # MP Atual do Jogador 
Mp_Max =0 #Mp Max do Jogador
Atk = 0 # Ataque do Jogador 
Def = 0 # defesa do Jogador 
Crit_Rate = 0 # Chance de Critico 
Crit_Dmg = 0 # Multiplicador de Dano Critico 
Esq = 0   # Chance de esquiva     
        
"""Atributos:"""
Vit = 0 #Aumenta o Hp Max
Int = 0 #Aumenta o Mp Max 
Str = 0 #Aumenta o Ataque
Vig = 0 #Aumenta a Defesa
Agi = 0 #Aumenta a Chance de Esquiva 
Luk = 0 #Aumanta a Chance de Critico e Dano Critico 


#Fontes:
def Get_Font(Nome_Font,Size):
    font = pg.font.Font(Nome_Font,Size)
    return font
    
SaiyanFont = Get_Font("font\SaiyanSans.ttf",72)
BitFont = pg.font.Font("font\8-BIT WONDER.TTF",22)
SFon = pg.font.Font("font\SaiyanSans.ttf",12)
