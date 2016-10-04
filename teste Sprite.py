# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 19:38:23 2016

@author: Gabriel
"""
import pygame as pg
import pyganim as pa
from spritesheet_functions import *
import constants



pg.init()
background = pygame.image.load("Fotos\Teste1.png")
'''teste2 = []'''
tela = pg.display.set_mode((800,600))
'''
teste = SpriteSheet("Fotos\MrSatan.PNG")
teste2 = createSprite(teste,[[0,1937,80,105,0],
[80,1937,80,105,0],
[160,1937,105,105,0],
[280,1937,80,105,0],
[358,1937,80,105,0],
[435,1937,105,105,0],
[7,2060,66,117,0],
[73,2060,66,117,0],
[143,2060,106,117,0],
[275,2072,75,104,0],
[361,2072,64,104,0],
[430,2066,100,112,0],
[558,2077,52,101,0],
[623,2075,55,103,0],
[684,2073,76,103,0],
[790,2064,57,113,0],
[851,2064,57,113,0],
[913,2064,71,113,0],
[991,2064,115,113,0],
[1113,2064,71,113,0]
])

    
'''

List = ((16,971,72,103),(94,971,61,102))
tempo = [200,200]
image = pa.getImagesFromSpriteSheet("Fotos\MrSatan.PNG",rects=List)
Frames= list(zip(image,tempo))
anima = pa.PygAnimation(Frames)
anima.play()
onground = False
y =20
muday = 0

fps=60
GameLoop = False

clock = pg.time.Clock()
pg.mixer.music.load("Music\StartScreean.ogg")
pg.mixer.music.play()
while not GameLoop:
     
    for event in pg.event.get():
        if event.type == pg.QUIT:
            GameLoop = True 
        pressed = pg.key.get_pressed()
        if pressed[pg.K_UP]: 
            if onground: 
                muday -= 10
                onground = False
    tela.blit(background,(0,0))
    y += muday
    print (y)
    if (y+106) >= 600:
        onground = True
        muday = 0
    if not onground:
        muday +=0.35               
    anima.blit(tela,(20,y))
        

    
    clock.tick(fps)
 
    pg.display.flip()