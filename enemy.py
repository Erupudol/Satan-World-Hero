import pygame , spritesheet_functions, cpu
import constants ,funçoes_enemy
#==============================================================================
"""Bosses"""
#==============================================================================

class Boss_Satan (cpu.CPU):
    """ This class represents the bar at the bottom that the player
     controls. """
 
 
    # -- Methods
    def __init__(self):
        """ Constructor function """
        # Call the parent's constructor
        super().__init__()
        
        self.Hp_Max = 100
        self.hp = self.Hp_Max
        self.Mp_Max = 50
        self.mp = self.Mp_Max
        self.Atk = 20
        self.Def = 10
        

        #Carrega a Spritesheet:
        sprite_sheet = spritesheet_functions.SpriteSheet("Fotos\MrSatan.PNG")   
        #Sprites Para Personagem Parado:
        self.Para_Frames_R = spritesheet_functions.createSprite(sprite_sheet,[[4,155,72,110,0],[82,155,72,110,0],[159,155,72,111,0]])        
        self.Para_Frames_L = spritesheet_functions.createSprite(sprite_sheet,[[4,155,72,110,0],[82,155,72,110,0],[159,155,72,111,0]],1)
        
        """Movimentos:"""
        #Sprites para Personagem Andando:
        self.Move_Frames_R = spritesheet_functions.createSprite(sprite_sheet,[[338,155,66,110,0],[414,155,64,110,0],[482,155,64,110,0],[552,155,64,110,0],[623,155,64,110,0]])
        self.Move_Frames_L = spritesheet_functions.createSprite(sprite_sheet,[[338,155,66,110,0],[414,155,64,110,0],[482,155,64,110,0],[552,155,64,110,0],[623,155,64,110,0]],1)               
        #Sprites para Salto Parado
        self.Salto_Para_Frames_R = spritesheet_functions.createSprite(sprite_sheet,[[90,520,70,110,0],[170,511,66,119,0],[249,517,64,113,0],[321,525,64,103,0],[392,520,70,110,0]])        
        self.Salto_Para_Frames_L = spritesheet_functions.createSprite(sprite_sheet,[[90,520,70,110,0],[170,511,66,119,0],[249,517,64,113,0],[321,525,64,103,0],[392,520,70,110,0]],1)
        #Sprites Para Salto em Movimento:
        self.Salto_Move_Frames_R = spritesheet_functions.createSprite(sprite_sheet,[[90,676,70,110,0],[171,689,80,97,0],[362,673,64,113,0],[432,676,61,110,0],[502,676,69,110,0]])                
        self.Salto_Move_Frames_L = spritesheet_functions.createSprite(sprite_sheet,[[90,676,70,110,0],[171,689,80,97,0],[362,673,64,113,0],[432,676,61,110,0],[502,676,69,110,0]],1)
        #Recebe Dano:
        self.Dmg_R = spritesheet_functions.createSprite(sprite_sheet,[[184,1098,71,110,0],[261,1098,81,110,0]])
        self.Dmg_L = spritesheet_functions.createSprite(sprite_sheet,[[184,1098,71,110,0],[261,1098,81,110,0]],1)
        #Morte:
        self.Dead_R = spritesheet_functions.createSprite(sprite_sheet,[[12,1239,115,110,0],[137,1239,115,110,0],[266,1239,112,110,0],[385,1239,119,110,0],[510,1239,118,110,0]])
        self.Dead_L =spritesheet_functions.createSprite(sprite_sheet, [[12,1239,115,110,0],[137,1239,115,110,0],[266,1239,112,110,0],[385,1239,119,110,0],[510,1239,118,110,0]],1)
        """Golpes:"""
       #ATAQUE BASICO:
        self.Atk_P1_R =spritesheet_functions.createSprite(sprite_sheet,[[8,1933,70,110,0],[85,1933,72,110,0],[162,1933,99,110,0]])
        self.Atk_P2_R =spritesheet_functions.createSprite(sprite_sheet,[[286,1933,72,110,0],[362,1933,72,110,0],[438,1933,98,110,0]])
        self.Atk_P1_L =spritesheet_functions.createSprite(sprite_sheet,[[8,1933,70,110,0],[85,1933,72,110,0],[162,1933,99,110,0]],1)
        self.Atk_P2_L =spritesheet_functions.createSprite(sprite_sheet,[[286,1933,72,110,0],[362,1933,72,110,0],[438,1933,98,110,0]],1)
        #Chutes:
        self.Atk_K1_R =spritesheet_functions.createSprite(sprite_sheet,[[276,2067,73,110,0],[362,2067,63,110,0],[431,2067,97,110,0]])
        self.Atk_K1_L =spritesheet_functions.createSprite(sprite_sheet,[[276,2067,73,110,0],[362,2067,63,110,0],[431,2067,97,110,0]],1)

        
        
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
           funçoes_enemy.Anima(self)            
        ## Move left/right       
        if self.change_x != 0 and self.change_y == 0:
           funçoes_enemy.Anima_Mov(self)             
    
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
        funçoes_enemy.Anima_Dmg(self)
        funçoes_enemy.Anima_Dead(self)
        funçoes_enemy.Anima_Golpes_Soco(self)
        funçoes_enemy.Anima_Golpes_Chute(self)


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
        
        self.Hp_Max = 100
        self.hp = self.Hp_Max
        self.Mp_Max = 50
        self.mp = self.Mp_Max
        self.Atk = 20
        self.Def = 10
        self.nome = "Cell"

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
           funçoes_enemy.Anima(self)            
        ## Move left/right       
        if self.change_x != 0 and self.change_y == 0:
           funçoes_enemy.Anima_Mov(self)             
    
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
        funçoes_enemy.Anima_Dmg(self)
        funçoes_enemy.Anima_Dead(self)
        funçoes_enemy.Anima_Golpes_Soco(self)
        funçoes_enemy.Anima_Golpes_Chute(self)

class Fat_Buu():
    pass

class Kid_Buu():
    pass

class Vegeta_Majin():
    pass

class Beerus():
    pass
#==============================================================================
"""Inimigos Padroes"""
#==============================================================================
class Cell_Jr(cpu.CPU):
    def __init__(self):
        """ Constructor function """
        # Call the parent's constructor
        super().__init__()
        
        self.Hp_Max = 100
        self.hp = self.Hp_Max
        self.Mp_Max = 50
        self.mp = self.Mp_Max
        self.Atk = 20
        self.Def = 10
        

        #Carrega a Spritesheet:
        sprite_sheet = spritesheet_functions.SpriteSheet("Fotos\SB2_CellJr.PNG")   
        #Sprites Para Personagem Parado:
        self.Para_Frames_R = spritesheet_functions.createSprite(sprite_sheet,[[5,5,38,49,0],[47,5,39,49,0]])        
        self.Para_Frames_L = spritesheet_functions.createSprite(sprite_sheet,[[5,5,38,49,0],[47,5,39,49,0]],1)
        
        """Movimentos:"""
        #Sprites para Personagem Andando:
        self.Move_Frames_R = spritesheet_functions.createSprite(sprite_sheet,[[5,58,38,49,0],[47,58,39,49,0],[90,58,38,49,0],[132,58,38,49,0]])
        self.Move_Frames_L = spritesheet_functions.createSprite(sprite_sheet,[[5,58,38,49,0],[47,58,39,49,0],[90,58,38,49,0],[132,58,38,49,0]],1)                
        #Sprites para Salto Parado
        self.Salto_Para_Frames_R = spritesheet_functions.createSprite(sprite_sheet,[[5,118,38,49,0],[121,111,39,56,0],[164,111,42,42,0],[210,111,36,56,0],[5,118,38,49,0]])        
        self.Salto_Para_Frames_L = spritesheet_functions.createSprite(sprite_sheet,[[5,118,38,49,0],[121,111,39,56,0],[164,111,42,42,0],[210,111,36,56,0],[5,118,38,49,0]],1)
        #Sprites Para Salto em Movimento:
#        self.Salto_Move_Frames_R = spritesheet_functions.createSprite(sprite_sheet,[[17,448,65,108,0],[91,448,77,108,0],[176,448,85,108,0],[270,448,77,108,0],[355,589,65,108,0]])                
#        self.Salto_Move_Frames_L = spritesheet_functions.createSprite(sprite_sheet,[[17,448,65,108,0],[91,448,77,108,0],[176,448,85,108,0],[270,448,77,108,0],[355,589,65,108,0]],1)
        #Recebe Dano:
        self.Dmg_R = spritesheet_functions.createSprite(sprite_sheet,[[43,984,42,50,0]])
        self.Dmg_L = spritesheet_functions.createSprite(sprite_sheet,[[43,984,42,50,0]],1)
        #Morte:
        self.Dead_R = spritesheet_functions.createSprite(sprite_sheet,[[5,1038,38,45,0],[47,1034,42,49,0],[93,1034,43,49,0],[140,1034,42,49,0],[186,1034,51,49,0]])
        self.Dead_L =spritesheet_functions.createSprite(sprite_sheet, [[5,1038,38,45,0],[47,1034,42,49,0],[93,1034,43,49,0],[140,1034,42,49,0],[186,1034,51,49,0]],1)
        """Golpes:"""
       #ATAQUE BASICO:
        self.Atk_P1_R =spritesheet_functions.createSprite(sprite_sheet,[[189,386,41,48,0],[234,386,47,48,0],[234,386,47,48,0]])
        self.Atk_P2_R =spritesheet_functions.createSprite(sprite_sheet,[[284,386,43,48,0],[332,386,46,48,0],[332,386,46,48,0]])
        self.Atk_P1_L =spritesheet_functions.createSprite(sprite_sheet,[[189,386,41,48,0],[234,386,47,48,0],[234,386,47,48,0]],1)
        self.Atk_P2_L =spritesheet_functions.createSprite(sprite_sheet,[[284,386,43,48,0],[332,386,46,48,0],[332,386,46,48,0]],1)
        #Chutes:
        self.Atk_K1_R =spritesheet_functions.createSprite(sprite_sheet,[[5,275,34,52,0],[43,275,47,52,0],[43,275,47,52,0],[94,275,34,52,0]])
        self.Atk_K1_L =spritesheet_functions.createSprite(sprite_sheet,[[5,275,34,52,0],[43,275,47,52,0],[43,275,47,52,0],[94,275,34,52,0]],1)

        
        
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
           funçoes_enemy.Anima(self)            
        ## Move left/right       
        if self.change_x != 0 and self.change_y == 0:
           funçoes_enemy.Anima_Mov(self)             
    
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
        if self.change_y != 0:# and self.change_x == 0  :
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
#        #Salto em Movimento 
#        elif self.change_x != 0 and self.change_y != 0:
#            self.rect.y += self.change_y
#            self.rect.x += self.change_x
#                       
#            if self.direction == "R" and self.jump: 
#                if -10 <= self.change_y <= -9.9 :
#                    self.image = self.Salto_Move_Frames_R[0]
#                elif (-9.9 < self.change_y <= 0):
#                    self.image = self.Salto_Move_Frames_R[1]
#                elif (0 <= self.change_y <= 2):
#                    self.image = self.Salto_Move_Frames_R[2]
#                elif 2 < self.change_y <= 9.9:
#                    self.image = self.Salto_Move_Frames_R[3]
#                elif 9.9 < self.change_y <= 10:
#                    self.image = self.Salto_Move_Frames_R[4]
#            elif self.direction == "L" and self.jump:
#                if -10 <= self.change_y <= -9.9 :
#                    self.image = self.Salto_Move_Frames_L[0]
#                elif (-9.9 < self.change_y <= 0):
#                    self.image = self.Salto_Move_Frames_L[1]
#                elif (0 <= self.change_y <= 2):
#                    self.image = self.Salto_Move_Frames_L[2]
#                elif 2 < self.change_y <= 9.9:
#                    self.image = self.Salto_Move_Frames_L[3]
#                elif 9.9 < self.change_y <= 10:
#                    self.image = self.Salto_Move_Frames_L[4]
                    
        
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
        funçoes_enemy.Anima_Dmg(self)
        funçoes_enemy.Anima_Dead(self)
        funçoes_enemy.Anima_Golpes_Soco(self)
        funçoes_enemy.Anima_Golpes_Chute(self)
   
    
      
                
   