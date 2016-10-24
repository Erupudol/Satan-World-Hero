"""Neste modulo tera todas musicas e efeitos sonoros do jogo."""

import pygame ,constants

pygame.init()
pygame.mixer.init()
Errou = pygame.mixer.Sound("Music\Fausto.ogg")
#==============================================================================
# Sons de Feito:
#==============================================================================
Hit_kill =pygame.mixer.Sound("Music\Hit_kill.wav")
Punch = pygame.mixer.Sound("Music\Sounds_Effects\LPswing.wav")
HitP = pygame.mixer.Sound("Music\Sounds_Effects\LPhit.wav")
Kick = pygame.mixer.Sound("Music\Sounds_Effects\LKswing.wav")
HitK = pygame.mixer.Sound("Music\Sounds_Effects\LKhit.wav")
Down = pygame.mixer.Sound("Music\Sounds_Effects\HitGround.wav")
Jump = pygame.mixer.Sound("Music\Sounds_Effects\Jumping.wav")
Landing = pygame.mixer.Sound("Music\Sounds_Effects\Landing.wav")
Read_go = pygame.mixer.Sound("Music\Sounds_Effects\ReadyGo.wav")
#==============================================================================
# Contagem
#==============================================================================
cont_10 = pygame.mixer.Sound("Music\Sounds_Game_Over\C_10Seconds.wav") 
cont_9  = pygame.mixer.Sound("Music\Sounds_Game_Over\C_9.wav")
cont_8  = pygame.mixer.Sound("Music\Sounds_Game_Over\C_8.wav")
cont_7  = pygame.mixer.Sound("Music\Sounds_Game_Over\C_7.wav")
cont_6  = pygame.mixer.Sound("Music\Sounds_Game_Over\C_6.wav")
cont_5  = pygame.mixer.Sound("Music\Sounds_Game_Over\C_5.wav")
cont_4  = pygame.mixer.Sound("Music\Sounds_Game_Over\C_4.wav")
cont_3  = pygame.mixer.Sound("Music\Sounds_Game_Over\C_3.wav")
cont_2  = pygame.mixer.Sound("Music\Sounds_Game_Over\C_2.wav")
cont_1  = pygame.mixer.Sound("Music\Sounds_Game_Over\C_1.wav")
cont_0  = pygame.mixer.Sound("Music\Sounds_Game_Over\C_0.wav")
def contagem ():
    if constants.regrecive == 10:
        cont_10.play(0)
    elif constants.regrecive == 9:
        cont_9.play(0)
    elif constants.regrecive == 8:
        cont_8.play(0)
    elif constants.regrecive == 7:
        cont_7.play(0)
    elif constants.regrecive == 6:
        cont_6.play(0)
    elif constants.regrecive == 5:
        cont_5.play(0)
    elif constants.regrecive == 4:
        cont_4.play(0)
    elif constants.regrecive == 3:
        cont_3.play(0)
    elif constants.regrecive == 2:
        cont_2.play(0)
    elif constants.regrecive == 1:
        cont_1.play(0)
    elif constants.regrecive == 0:
        cont_0.play(0)
#==============================================================================
# Game Over
#==============================================================================
Game_Over  = pygame.mixer.Sound("Music\Sounds_Game_Over\GameOver.wav")