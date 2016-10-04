"""Armazena todos os personagens """
import pygame 
import constants
from player import * 
from platforms import MovingPlatform
from spritesheet_functions import *
from funçoes_players import *


class MrSatan(player):
    """ This class represents the bar at the bottom that the player
    controls. """
 
 
    # -- Methods
    def __init__(self):
        """ Constructor function """
        # Call the parent's constructor
        super().__init__()
        
        constants.Hp_Max = 100
        self.hp = constants.Hp = constants.Hp_Max
        constants.Mp_Max = 50
        self.mp = constants.Mp = constants.Mp_Max
        self.Atk = constants.Atk = 20
        self.Def = constants.Def = 10
        

        #Carrega a Spritesheet:
        sprite_sheet = SpriteSheet("Fotos\MrSatan.PNG")   
        #Face do personagem:
        self.Face =   sprite_sheet.get_image(1378,348,174,227,0)
        self.Face =  pygame.transform.scale(self.Face,(58, 67))
        #Sprites Para Personagem Parado:
        self.Para_Frames_R = createSprite(sprite_sheet,[[4,160,72,105,0],[82,160,72,105,0],[159,160,72,105,0]])        
        self.Para_Frames_L = createSprite(sprite_sheet,[[4,160,72,105,0],[82,160,72,105,0],[159,160,72,105,0]],1)
        
        """Movimentos:"""
        #Sprites para Personagem Andando:
        self.Move_Frames_R = createSprite(sprite_sheet,[[338,160,66,105,0],[414,160,64,105,0],[482,160,64,105,0],[552,160,64,105,0],[623,160,64,105,0]])
        self.Move_Frames_L = createSprite(sprite_sheet,[[338,160,66,105,0],[414,160,64,105,0],[482,160,64,105,0],[552,160,64,105,0],[623,160,64,105,0]],1)                
        #Sprites para Salto Parado
        self.Salto_Para_Frames_R = createSprite(sprite_sheet,[[90,525,70,105,0],[170,511,66,119,0],[249,517,64,113,0],[321,525,64,103,0],[392,525,70,105,0]])        
        self.Salto_Para_Frames_L = createSprite(sprite_sheet,[[90,525,70,105,0],[170,511,66,119,0],[249,517,64,113,0],[321,525,64,103,0],[392,525,70,105,0]],1)
        #Sprites Para Salto em Movimento:
        self.Salto_Move_Frames_R = createSprite(sprite_sheet,[[90,681,70,105,0],[171,689,80,97,0],[362,673,64,113,0],[432,681,61,105,0],[502,681,69,105,0]])                
        self.Salto_Move_Frames_L = createSprite(sprite_sheet,[[90,681,70,105,0],[171,689,80,97,0],[362,673,64,113,0],[432,681,61,105,0],[502,681,69,105,0]],1)
        # Defesa:  
        self.Def_R = createSprite(sprite_sheet,[[16,971,72,103,0],[93,971,61,103,0]]) 
        self.Def_L = createSprite(sprite_sheet,[[16,971,72,103,0],[93,971,61,103,0]],1)
        #Recebe Dano:
        self.Dmg_R = createSprite(sprite_sheet,[[184,1103,71,105,0],[261,1103,81,105,0]])
        self.Dmg_L = createSprite(sprite_sheet,[[184,1103,71,105,0],[261,1103,81,105,0]],1)
        #Morte:
        self.Dead_R = createSprite(sprite_sheet,[[12,1244,115,105,0],[137,1244,115,105,0],[266,1244,112,105,0],[385,1244,119,105,0],[510,1244,118,105,0]])
        self.Dead_L =createSprite(sprite_sheet, [[12,1244,115,105,0],[137,1244,115,105,0],[266,1244,112,105,0],[385,1244,119,105,0],[510,1244,118,105,0]],1)
        """Golpes:"""
       #ATAQUE BASICO:
        self.Atk_P1_R =createSprite(sprite_sheet,[[0,1937,80,105,0],
[80,1937,80,105,0],
[160,1937,105,105,0]])
        self.Atk_P2_R =createSprite(sprite_sheet,[[280,1937,80,105,0],
[358,1937,80,105,0],
[435,1937,105,105,0]])
        self.Atk_P1_L =createSprite(sprite_sheet,[[0,1937,80,105,0],
[80,1937,80,105,0],
[160,1937,105,105,0]],1)
        self.Atk_P2_L =createSprite(sprite_sheet,[[280,1937,80,105,0],
[358,1937,80,105,0],
[435,1937,105,105,0]],1)
        #Chutes:
        self.Atk_K1_R =createSprite(sprite_sheet,[[7,2060,66,117,0],
[73,2060,66,117,0],
[143,2060,106,117,0]])
        self.Atk_K2_R =createSprite(sprite_sheet,[[275,2072,75,104,0],
[361,2072,64,104,0],
[430,2066,100,112,0]])
        self.Atk_K3_R =createSprite(sprite_sheet,[[558,2077,52,101,0],
[623,2075,55,103,0],
[684,2073,76,103,0]])
        self.Atk_K4_R =createSprite(sprite_sheet,[[790,2064,57,113,0],
[851,2064,57,113,0],
[913,2064,71,113,0],
[991,2064,115,113,0],
[1113,2064,71,113,0]])
        self.Atk_K1_L =createSprite(sprite_sheet,[[7,2060,66,117,0],
[73,2060,66,117,0],
[143,2060,106,117,0]],1)
        self.Atk_K2_L =createSprite(sprite_sheet,[[275,2072,75,104,0],
[361,2072,64,104,0],
[430,2066,100,112,0]],1)
        self.Atk_K3_L =createSprite(sprite_sheet,[[558,2077,52,101,0],
[623,2075,55,103,0],
[684,2073,76,103,0]],1)
        self.Atk_K4_L =createSprite(sprite_sheet,[[790,2064,57,113,0],
[851,2064,57,113,0],
[913,2064,71,113,0],
[991,2064,115,113,0],
[1113,2064,71,113,0]],1)
       
        
        
        # Set the image the player starts with
        self.image = self.Para_Frames_R[0]
        self.image = self.Move_Frames_R[0]
        self.image = self.Salto_Para_Frames_R[0]
        self.image = self.Atk_P1_R [0]
        self.image = self.Atk_P2_R [0]
        self.image = self.Atk_K1_R [0]
        self.image = self.Atk_K2_R [0]
        self.image = self.Atk_K3_R [0]
        self.image = self.Atk_K4_R [0]
        self.image = self.Def_R[0]
        # Set a reference to the image rect.
        
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
#        self.mask.rect = self.image.get_rect()
    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()
 
        # Movimento Sprite Parado
       
        if self.State('wait'):
           Anima(self)            
        ## Move left/right       
        if self.change_x != 0 and self.change_y == 0:
           Anima_Mov(self)             
    
        block_hit_list =  self.level.platform_list
        for block in block_hit_list:
            
            if not self.jump:
                if self.rect.bottom < block.rect.bottom and self.rect.bottom > block.rect.top:
                    if self.rect.left < block.rect.left and self.rect.right > block.rect.left:
                        self.rect.right = block.rect.left
                    if self.rect.right > block.rect.right and self.rect.left < block.rect.right:
                        self.rect.left = block.rect.right
                if self.rect.top > block.rect.top and self.rect.top < block.rect.bottom:
                    if self.rect.left < block.rect.left and self.rect.right > block.rect.left:
                        self.rect.right = block.rect.left
                    if self.rect.right > block.rect.right and self.rect.left < block.rect.right:
                        self.rect.left = block.rect.right
                if self.rect.top <= block.rect.top and self.rect.bottom >= block.rect.bottom:
                    if self.rect.left < block.rect.left and self.rect.right > block.rect.left:
                        self.rect.right = block.rect.left
                    if self.rect.right > block.rect.right and self.rect.left < block.rect.right:
                        self.rect.left = block.rect.right
            if self.rect.top >= block.rect.top and self.rect.bottom <= block.rect.bottom:
                    if self.rect.left < block.rect.left and self.rect.right > block.rect.left:
                        self.rect.right = block.rect.left
                    if self.rect.right > block.rect.right and self.rect.left < block.rect.right:
                        self.rect.left = block.rect.right

        
#        for Enemy in block_enemy_list:
#             if pygame.sprite.collide_mask(self,Enemy):
#                 self.change_x = 0
#                 if self.punch or self.kick:
#                     Enemy.Dano()
#==============================================================================
                
        # Salto Parado:
        if self.change_x == 0 and self.change_y != 0:
            self.rect.top += self.change_y
            if self.direction == "R" and self.jump:                                
                if -9.9 >= self.change_y >= -10 :
                    self.image = self.Salto_Para_Frames_R[0]
                elif (0 > self.change_y >= -9.9):
                    self.image = self.Salto_Para_Frames_R[1]
                elif (0 <= self.change_y <= 2):
                    self.image = self.Salto_Para_Frames_R[2]
                elif 2 < self.change_y <= 9.9:
                    self.image = self.Salto_Para_Frames_R[3]
                elif 9.9 < self.change_y <= 10:
                    self.image = self.Salto_Para_Frames_R[4]
                   
            elif self.direction == "L"and self.jump:              
                if -10 <= self.change_y <= -9.9 :
                    self.image = self.Salto_Para_Frames_L[0]
                elif (-9.9 < self.change_y <= 0):
                    self.image = self.Salto_Para_Frames_L[1]
                elif (0 <= self.change_y <= 2):
                    self.image = self.Salto_Para_Frames_L[2]
                elif 2 < self.change_y <= 9.9:
                    self.image = self.Salto_Para_Frames_L[3]
                elif 9.9 < self.change_y <= 10:
                    self.image = self.Salto_Para_Frames_L[4] 
        #Salto em Movimento 
        elif self.change_x != 0 and self.change_y != 0:
            self.rect.y += self.change_y
            self.rect.x += self.change_x
                       
            if self.direction == "R" and self.jump: 
                if -10 <= self.change_y <= -9.9 :
                    self.image = self.Salto_Move_Frames_R[0]
                elif (-9.9 < self.change_y <= 0):
                    self.image = self.Salto_Move_Frames_R[1]
                elif (0 <= self.change_y <= 2):
                    self.image = self.Salto_Move_Frames_R[2]
                elif 2 < self.change_y <= 9.9:
                    self.image = self.Salto_Move_Frames_R[3]
                elif 9.9 < self.change_y <= 10:
                    self.image = self.Salto_Move_Frames_R[4]
            elif self.direction == "L" and self.jump:
                if -10 <= self.change_y <= -9.9 :
                    self.image = self.Salto_Move_Frames_L[0]
                elif (-9.9 < self.change_y <= 0):
                    self.image = self.Salto_Move_Frames_L[1]
                elif (0 <= self.change_y <= 2):
                    self.image = self.Salto_Move_Frames_L[2]
                elif 2 < self.change_y <= 9.9:
                    self.image = self.Salto_Move_Frames_L[3]
                elif 9.9 < self.change_y <= 10:
                    self.image = self.Salto_Move_Frames_L[4]
                    
        
        # Check and see if we hit anything
        self.onGround = False
        block_hit_list =  self.level.platform_list
        for block in block_hit_list: 
            if self.rect.right > block.rect.left and self.rect.left < block.rect.right:
                    if self.rect.bottom > block.rect.top and (self.rect.bottom - 10) < block.rect.top:
                        if self.change_y > 0 and not self.onGround:
                            self.rect.bottom = block.rect.top
                            self.onGround = True
                            self.jump = False
                            self.change_y = 0
                    if self.rect.top < block.rect.bottom and (self.rect.top + 10) > block.rect.bottom:
                        if self.change_y < 0 and not self.onGround:
                            self.rect.top = block.rect.bottom
                            
        block_enemy_list =  self.level.enemy_list
        
        for Enemy in block_enemy_list: 
            if pygame.sprite.collide_rect(self,Enemy) and self.Muda_Rota == Enemy.Muda_Rota: 
          # Reset our position based on the top/bottom of the object.
                if self.change_y > 0 :
                    self.rect.bottom = Enemy.rect.top
                elif self.change_y < 0:
                    self.rect.top = Enemy.rect.bottom 
            # Stop our vertical movement
                
            
            
            
        #Golpes:
        #Socos e Chutes:
        Anima_Def(self)
        Anima_Dmg(self)
        Anima_Dead(self)
        Anima_Def(self)
        Anima_Golpes_Soco(self)
        Anima_Golpes_Chute(self)


class Goku_Ssj(player):
    pass

class Goku_Ssj_Blue(player):
    pass

class Goku_Black_Ssj_Rose(player):
    pass

class Frieza(player):
    pass

class Frieza_Gold(player):
    pass

class Cell(player):
    pass

class Fat_Buu(player):
    pass

class Kid_Buu(player):
    pass

class Vegeta_Majin(player):
    pass

class Beerus(player):
    pass


   
    
      
                
   