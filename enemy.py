import pygame , spritesheet_functions, cpu
import constants
from funçoes_enemy import *


class Boss_Satan (cpu.CPU):
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
        sprite_sheet = spritesheet_functions.SpriteSheet("Fotos\MrSatan.PNG")   
        #Sprites Para Personagem Parado:
        self.Para_Frames_R = spritesheet_functions.createSprite(sprite_sheet,[[4,160,72,105,0],[82,160,72,105,0],[159,160,72,105,0]])        
        self.Para_Frames_L = spritesheet_functions.createSprite(sprite_sheet,[[4,160,72,105,0],[82,160,72,105,0],[159,160,72,105,0]],1)
        
        """Movimentos:"""
        #Sprites para Personagem Andando:
        self.Move_Frames_R = spritesheet_functions.createSprite(sprite_sheet,[[338,160,66,105,0],[414,160,64,105,0],[482,160,64,105,0],[552,160,64,105,0],[623,160,64,105,0]])
        self.Move_Frames_L = spritesheet_functions.createSprite(sprite_sheet,[[338,160,66,105,0],[414,160,64,105,0],[482,160,64,105,0],[552,160,64,105,0],[623,160,64,105,0]],1)                
        #Sprites para Salto Parado
        self.Salto_Para_Frames_R = spritesheet_functions.createSprite(sprite_sheet,[[90,525,70,105,0],[170,511,66,119,0],[249,517,64,113,0],[321,525,64,103,0],[392,525,70,105,0]])        
        self.Salto_Para_Frames_L = spritesheet_functions.createSprite(sprite_sheet,[[90,525,70,105,0],[170,511,66,119,0],[249,517,64,113,0],[321,525,64,103,0],[392,525,70,105,0]],1)
        #Sprites Para Salto em Movimento:
        self.Salto_Move_Frames_R = spritesheet_functions.createSprite(sprite_sheet,[[90,681,70,105,0],[171,689,80,97,0],[362,673,64,113,0],[432,681,61,105,0],[502,681,69,105,0]])                
        self.Salto_Move_Frames_L = spritesheet_functions.createSprite(sprite_sheet,[[90,681,70,105,0],[171,689,80,97,0],[362,673,64,113,0],[432,681,61,105,0],[502,681,69,105,0]],1)
        #Recebe Dano:
        self.Dmg_R = spritesheet_functions.createSprite(sprite_sheet,[[184,1103,71,105,0],[261,1103,81,105,0]])
        self.Dmg_L = spritesheet_functions.createSprite(sprite_sheet,[[184,1103,71,105,0],[261,1103,81,105,0]],1)
        #Morte:
        self.Dead_R = spritesheet_functions.createSprite(sprite_sheet,[[12,1244,115,105,0],[137,1244,115,105,0],[266,1244,112,105,0],[385,1244,119,105,0],[510,1244,118,105,0]])
        self.Dead_L =spritesheet_functions.createSprite(sprite_sheet, [[12,1244,115,105,0],[137,1244,115,105,0],[266,1244,112,105,0],[385,1244,119,105,0],[510,1244,118,105,0]],1)
        """Golpes:"""
       #ATAQUE BASICO:
        self.Atk_P1_R =spritesheet_functions.createSprite(sprite_sheet,[[0,1937,80,105,0],
[80,1937,80,105,0],
[160,1937,105,105,0]])
        self.Atk_P2_R =spritesheet_functions.createSprite(sprite_sheet,[[280,1937,80,105,0],
[358,1937,80,105,0],
[435,1937,105,105,0]])
        self.Atk_P1_L =spritesheet_functions.createSprite(sprite_sheet,[[0,1937,80,105,0],
[80,1937,80,105,0],
[160,1937,105,105,0]],1)
        self.Atk_P2_L =spritesheet_functions.createSprite(sprite_sheet,[[280,1937,80,105,0],
[358,1937,80,105,0],
[435,1937,105,105,0]],1)
        #Chutes:
        self.Atk_K1_R =spritesheet_functions.createSprite(sprite_sheet,[[7,2060,66,117,0],
[73,2060,66,117,0],
[143,2060,106,117,0]])
        self.Atk_K1_L =spritesheet_functions.createSprite(sprite_sheet,[[7,2060,66,117,0],
[73,2060,66,117,0],
[143,2060,106,117,0]],1)

        
        
        """Define a imagem inicial"""
        self.image = self.Para_Frames_R[0]
        # Set a reference to the image rect.
        
        self.rect = self.image.get_rect()
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

#        
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
        Anima_Dmg(self)
        Anima_Dead(self)
        Anima_Golpes_Soco(self)
        Anima_Golpes_Chute(self)


class Goku_Ssj():
    pass

class Goku_Ssj_Blue():
    pass

class Goku_Black_Ssj_Rose():
    pass

class Frieza():
    pass

class Frieza_Gold():
    pass

class Cell(cpu.CPU):
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
        sprite_sheet = spritesheet_functions.SpriteSheet("Fotos\CellHD.PNG")   
        #Sprites Para Personagem Parado:
        self.Para_Frames_R = spritesheet_functions.createSprite(sprite_sheet,[[17,35,44,108,0],[71,35,44,108,0], [125,35,44,108,0],[179,35,44,108,0]])        
        self.Para_Frames_L = spritesheet_functions.createSprite(sprite_sheet,[[17,35,44,108,0],[71,35,44,108,0], [125,35,44,108,0],[179,35,44,108,0]],1)
        
        """Movimentos:"""
        #Sprites para Personagem Andando:
        self.Move_Frames_R = spritesheet_functions.createSprite(sprite_sheet,[[17,180,49,108,0],[76,180,44,108,0],[130,180,45,108,0],[185,180,45,108,0]])
        self.Move_Frames_L = spritesheet_functions.createSprite(sprite_sheet,[[17,180,49,108,0],[76,180,44,108,0],[130,180,45,108,0],[185,180,45,108,0]],1)                
        #Sprites para Salto Parado
        self.Salto_Para_Frames_R = spritesheet_functions.createSprite(sprite_sheet,[[17,589,65,108,0],[91,589,77,108,0],[176,589,85,108,0],[270,589,77,108,0],[355,589,65,108,0]])        
        self.Salto_Para_Frames_L = spritesheet_functions.createSprite(sprite_sheet,[[17,589,65,108,0],[91,589,77,108,0],[176,589,85,108,0],[270,589,77,108,0],[355,589,65,108,0]],1)
        #Sprites Para Salto em Movimento:
        self.Salto_Move_Frames_R = spritesheet_functions.createSprite(sprite_sheet,[[17,448,65,108,0],[91,448,77,108,0],[176,448,85,108,0],[270,448,77,108,0],[355,589,65,108,0]])                
        self.Salto_Move_Frames_L = spritesheet_functions.createSprite(sprite_sheet,[[17,448,65,108,0],[91,448,77,108,0],[176,448,85,108,0],[270,448,77,108,0],[355,589,65,108,0]],1)
        #Recebe Dano:
        self.Dmg_R = spritesheet_functions.createSprite(sprite_sheet,[[285,3496,50,108,0]])
        self.Dmg_L = spritesheet_functions.createSprite(sprite_sheet,[[285,3496,50,108,0]],1)
        #Morte:
        self.Dead_R = spritesheet_functions.createSprite(sprite_sheet,[[17,3631,55,108,0],[81,3631,80,108,0],[17,3631,55,108,0],[170,3631,109,108,0],[287,3631,104,108,0]])
        self.Dead_L =spritesheet_functions.createSprite(sprite_sheet, [[17,3631,55,108,0],[81,3631,80,108,0],[17,3631,55,108,0],[170,3631,109,108,0],[287,3631,104,108,0]],1)
        """Golpes:"""
       #ATAQUE BASICO:
        self.Atk_P1_R =spritesheet_functions.createSprite(sprite_sheet,[[775,731,75,108,0],[839,731,78,108,0],[927,731,66,108,0]])
        self.Atk_P2_R =spritesheet_functions.createSprite(sprite_sheet,[[775,731,75,108,0],[839,731,78,108,0],[927,731,66,108,0]])
        self.Atk_P1_L =spritesheet_functions.createSprite(sprite_sheet,[[775,731,75,108,0],[839,731,78,108,0],[927,731,66,108,0]],1)
        self.Atk_P2_L =spritesheet_functions.createSprite(sprite_sheet,[[775,731,75,108,0],[839,731,78,108,0],[927,731,66,108,0]],1)
        #Chutes:
        self.Atk_K1_R =spritesheet_functions.createSprite(sprite_sheet,[[17,731,65,108,0],[91,731,76,108,0],[176,731,99,108,0],[285,731,76,108,0],[369,731,65,108,0]])
        self.Atk_K1_L =spritesheet_functions.createSprite(sprite_sheet,[[17,731,65,108,0],[91,731,76,108,0],[176,731,99,108,0],[285,731,76,108,0],[369,731,65,108,0]],1)

        
        
        """Define a imagem inicial"""
        self.image = self.Para_Frames_R[0]
        # Set a reference to the image rect.
        
        self.rect = self.image.get_rect()
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

#        
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
        Anima_Dmg(self)
        Anima_Dead(self)
        Anima_Golpes_Soco(self)
        Anima_Golpes_Chute(self)

class Fat_Buu():
    pass

class Kid_Buu():
    pass

class Vegeta_Majin():
    pass

class Beerus():
    pass


   
    
      
                
   