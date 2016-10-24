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
y = 2000
#Gerais:
Game_loop = False
reset =  False
Pause = False
game_clear = False
game_start = False
FPS = 60
#contadores e sons
i = 0 #Usado
s = 0 #Usado
d = 0 #Usado
n = 0 #Usado
e = 0 #Usado
a = 0 #Usado
b = 0 #Usado
delay_dead = 0 #Usado
delays = 0 #Usado
teste = 0 #Usado
count = 0 #Usado
f_s = 72 #Usado

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
regrecive = 10        
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
    
SaiyanFont = "font\SaiyanSans.ttf"
BitFont = "font\8-BIT WONDER.TTF"


