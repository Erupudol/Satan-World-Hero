"""Neste modulo tera todas musicas e efeitos sonoros do jogo."""

import pygame

pygame.init()
pygame.mixer.init()
Errou = pygame.mixer.Sound("Music\Fausto.ogg")
Hit_kill =pygame.mixer.Sound("Music\Hit_kill.wav")
Punch = pygame.mixer.Sound("Music\Punch.wav")
kick = pygame.mixer.Sound("Music\Kick.wav")
Down = pygame.mixer.Sound("Music\Queda.wav")