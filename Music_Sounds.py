"""Neste modulo tera todas musicas e efeitos sonoros do jogo."""

import pygame

pygame.init()
pygame.mixer.init()
Errou = pygame.mixer.Sound("Music\Fausto.ogg")
Star_M = pygame.mixer.music.load("Music\StartScreean.ogg")

