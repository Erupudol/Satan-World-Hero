import pygame , spritesheet_functions, player
import constants,funçoes_players


class MrSatan(player.Player):
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
        #Face do personagem:
        self.Face =   sprite_sheet.get_image(1378,348,174,227,0)
        self.Face =  pygame.transform.scale(self.Face,(58, 67))
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
        # Defesa:  
        self.Def_R = spritesheet_functions.createSprite(sprite_sheet,[[16,971,72,103,0],[93,971,61,103,0]]) 
        self.Def_L = spritesheet_functions.createSprite(sprite_sheet,[[16,971,72,103,0],[93,971,61,103,0]],1)
        #Recebe Dano:
        self.Dmg_R = spritesheet_functions.createSprite(sprite_sheet,[[184,1098,71,110,0],[261,1098,81,110,0]])
        self.Dmg_L = spritesheet_functions.createSprite(sprite_sheet,[[184,1098,71,110,0],[261,1098,81,110,0]],1)
        #Morte:
        self.Dead_R = spritesheet_functions.createSprite(sprite_sheet,[[12,1239,115,110,0],[137,1239,115,110,0],[266,1239,112,110,0],[385,1239,119,110,0],[510,1239,118,110,0]])
        self.Dead_L = spritesheet_functions.createSprite(sprite_sheet, [[12,1239,115,110,0],[137,1239,115,110,0],[266,1239,112,110,0],[385,1239,119,110,0],[510,1239,118,110,0]],1)
        """Golpes:"""
       #ATAQUE BASICO:
        self.Atk_P1_R = spritesheet_functions.createSprite(sprite_sheet,[[8,1933,70,110,0],[85,1933,72,110,0],[162,1933,99,110,0],[162,1933,99,110,0]])
        self.Atk_P2_R = spritesheet_functions.createSprite(sprite_sheet,[[286,1933,72,110,0],[362,1933,72,110,0],[438,1933,98,110,0],[438,1933,98,110,0]])
        self.Atk_P1_L = spritesheet_functions.createSprite(sprite_sheet,[[8,1933,70,110,0],[85,1933,72,110,0],[162,1933,99,110,0],[162,1933,99,110,0]],1)
        self.Atk_P2_L = spritesheet_functions.createSprite(sprite_sheet,[[286,1933,72,110,0],[362,1933,72,110,0],[438,1933,98,110,0],[438,1933,98,110,0]],1)
        #Chutes:
        self.Atk_K1_R = spritesheet_functions.createSprite(sprite_sheet,[[276,2067,73,110,0],[362,2067,63,110,0],[431,2067,97,110,0],[431,2067,97,110,0],[431,2067,97,110,0]])
        self.Atk_K1_L = spritesheet_functions.createSprite(sprite_sheet,[[276,2067,73,110,0],[362,2067,63,110,0],[431,2067,97,110,0],[431,2067,97,110,0],[431,2067,97,110,0]],1)
        #Comemoraçao
        self.Com_R = spritesheet_functions.createSprite(sprite_sheet,[[6,37,51,116,0],[65,37,66,116,0],[141,37,86,116,0],[233,37,82,116,0],[326,37,82,116,0],[419,37,83,116,0],[511,37,66,116,0],[587,37,51,116,0]])        
        
        # Set the image the player starts with
        self.image = self.Para_Frames_R[0]
        # Set a reference to the image rect.
        
        self.rect = self.image.get_rect()
#        self.mask.rect = self.image.get_rect()
    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()
 
        # Movimento Sprite Parado
       
        if self.State('wait'):
           funçoes_players.Anima(self)            
        ## Move left/right       
        if self.change_x != 0 and self.change_y == 0:
           funçoes_players.Anima_Mov(self)             
    
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
        funçoes_players.Anima_Def(self)
        funçoes_players.Anima_vit(self)
        funçoes_players.Anima_Dmg(self)
        funçoes_players.Anima_Dead(self)
        funçoes_players.Anima_Def(self)
        funçoes_players.Anima_Golpes_Soco(self)
        funçoes_players.Anima_Golpes_Chute(self)


class Goku_Ssj(player.Player):
    pass

class Goku_Ssj_Blue(player.Player):
    pass

class Goku_Black_Ssj_Rose(player.Player):
    pass

class Frieza(player.Player):
    pass

class Frieza_Gold(player.Player):
    pass

class Cell(player.Player):
    pass

class Fat_Buu(player.Player):
    pass

class Kid_Buu(player.Player):
    pass

class Vegeta_Majin(player.Player):
    pass

class Beerus(player.Player):
    pass


   
    
      
                
   