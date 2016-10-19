import pygame, Sounds, Main
 
import constants
 
from platforms import MovingPlatform
from spritesheet_functions import *
from funçoes_players import *
import math

class Player (pygame.sprite.Sprite):
    def __init__(self):
        
        super().__init__()
#==============================================================================
        """constantes de animaçao""" 
#==============================================================================
        self.delay_standby = self.delay_dmg= self.delay_dead = 0
        self.delay_punch = self.delay_kick = self.delay_def = self.delay_vit = 0
        self.i = self.p = self.k = self.h = self.d = self.r = self.a = self.v = self.c = 0
        self.count = 0
        self.dano = 0
#==============================================================================
        
        """Define o Vetor Velocidade do Player""" 
        self.change_x = 0
        self.change_y = 0
        self.Muda_Rota = 0
        self.Rota_Seg = 0 
        self.dano = 0
        """Salva as Imagens das Posiçoes ESQUERDA\DIREITA:"""
        self.Face = None
        # Personagem Parado:
        self.Para_Frames_L = []
        self.Para_Frames_R = []
        # Peronagem Andando:
        self.Move_Frames_L = []
        self.Move_Frames_R = []
        # Salto Parado:
        self.Salto_Para_Frames_L = []
        self.Salto_Para_Frames_R = []
        #Salto Move:
        self.Salto_Move_Frames_L = []
        self.Salto_Move_Frames_R = []
        """Movimentos Defensivos e  Dano :"""
        self.Def_R = []
        self.Def_L = []
        self.Dmg_R = []
        self.Dmg_R = []
        self.Dead_R =[]
        self.Dead_L = []
        """Movimentos de Ataque:
            Soco  """
        self.Atk_P_R = [] 
        self.Atk_P_L = []
        """Chute"""
        self.Atk_K_R = []
        self.Atk_K_L = []
        """Soco  Aerio"""
        self.Atk_AP_R = []
        self.Atk_AP_L = []
        """Chute  Aerio"""
        self.Atk_AK_R = [] 
        self.Atk_AK_L = []
        '''Soco com Dash'''
        self.Atk_DP_R = [] 
        self.Atk_DP_L = []
        """Chute com Dash"""
        self.Atk_DK_R = [] 
        self.Atk_DK_L = []     
        """Clear Stage"""
        self.Com_R = []
        self.Com_L = []
        
        
        # What direction is the player facing?
        self.Lives = 0
        self.direction = "R"                 
        self.level = None
        """Estados"""
        self.live = True
        self.jump = False
        self.ki_charge = False
        self.defending = False
        self.dmg = False
        self.dealdmg=False
        self.punch = False
        self.kick = False
        self.SPC1_Atk = False
        self.SPC2_Atk = False
        self.SPC3_Atk = False
        self.Ult_Atk = False
        self.com = False
       
        
        
        self.onGround = False
        self.mask = None
        
    def update(self):
        pass
    
    def State(self,event):    
        if event == 'wait':
            if self.live and not self.com and not self.jump and not self.ki_charge and not self.defending and not self.punch and not self.kick and not self.SPC1_Atk and not self.SPC2_Atk and not self.SPC3_Atk and not self.Ult_Atk:
                return True
        elif event == 'move':
            if self.live and not self.com and not self.ki_charge and not self.defending and not self.dmg and not self.punch and not self.kick and not self.SPC1_Atk and not self.SPC2_Atk and not self.SPC3_Atk and not self.Ult_Atk:
                return True
        elif event == 'jump':
            if self.live and not self.com and not self.jump and not self.ki_charge and not self.defending and not self.punch and not self.kick and not self.SPC1_Atk and not self.SPC2_Atk and not self.SPC3_Atk and not self.Ult_Atk:
                return True
        elif event == 'ki_charge':
            if self.live and not self.com and not self.jump and not self.defending and not self.punch and not self.kick and not self.SPC1_Atk and not self.SPC2_Atk and not self.SPC3_Atk and not self.Ult_Atk:
                return True
        elif event == 'defending':
            if self.live and not self.com and not self.jump and not self.ki_charge and not self.punch and not self.kick and not self.SPC1_Atk and not self.SPC2_Atk and not self.SPC3_Atk and not self.Ult_Atk:
                return True
        elif event == 'punch':
            if self.live and not self.com and not self.jump and not self.ki_charge and not self.defending and not self.kick and not self.SPC1_Atk and not self.SPC2_Atk and not self.SPC3_Atk and not self.Ult_Atk:
                return True
        elif event == 'kick':
            if self.live and not self.com and not self.jump and not self.ki_charge and not self.defending and not self.punch and not self.SPC1_Atk and not self.SPC2_Atk and not self.SPC3_Atk and not self.Ult_Atk:
                return True
        elif event == 'Special_1':
            if self.live and not self.com and not self.jump and not self.ki_charge and not self.defending and not self.punch and not self.kick and not self.SPC2_Atk and not self.SPC3_Atk and not self.Ult_Atk:
                return True
        elif event == 'Special_2':
            if self.live and not self.com and not self.jump and not self.ki_charge and not self.defending and not self.punch and not self.kick and not self.SPC1_Atk and not self.SPC3_Atk and not self.Ult_Atk:
                return True
        elif event == 'Special_3':
            if self.live and not self.com and not self.jump and not self.ki_charge and not self.defending and not self.punch and not self.kick and not self.SPC1_Atk and not self.SPC2_Atk and not self.Ult_Atk:
                return True
        elif event == 'Ultimate':
            if self.live and not self.com and not self.jump and not self.ki_charge and not self.defending and not self.punch and not self.kick and not self.SPC1_Atk and not self.SPC2_Atk and not self.SPC3_Atk:
                return True
                   
    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            if self.onGround:
                self.change_y = 0
            else:
                self.change_y = 1
                
        else:
            self.change_y += .35 
        # See if we are on the ground.
            
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height - self.Muda_Rota and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height -self.Muda_Rota
            self.jump = False
    def Jump(self):
        """ Called when user hits 'jump' button. """ 
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.   
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
        
        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT - self.Muda_Rota:
            self.change_y = -10
            self.jump = True
            self.onGround = False
            
    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -5
        self.direction = "L"
 
    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 5
        self.direction = "R"
        
    def Muda_Rota_Sup(self):
        if self.Rota_Seg < 100:
            self.Muda_Rota += 2
            self.Rota_Seg += 2
        else:
            self.Muda_Rota = 100
            
    def Muda_Rota_Inf(self):
        if self.Rota_Seg >  0:
            self.Muda_Rota -= 2
            self.Rota_Seg -= 2
        else:
            self.Muda_Rota = 0

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
        self.defending = False
        
        
    def Soco_1 (self):
        self.punch = True
        Sounds.Punch.play()
        
    def Chute_1 (self):
        self.kick = True
        Sounds.kick.play()
        
    def Recive_Dmg(self,enemy):
        if self.defending:
            if self.dmg:
                if enemy.Atk >self.Def :
                    self.dano =  enemy.Atk - 0.79*self.Def * math.e **(-0.27*(self.Def/enemy.Atk))
                    self.dano = self.dano * 0.65
                    if self.dano < self.hp: 
                        self.hp = self.hp - self.dano 
                    else:
                        self.hp = 0
                        self.live = False
                        #self.Dead()
                else:
                    self.dano =(0.4*(enemy.Atk**3/self.Def**2)-0.09*(enemy.Atk**2/self.Def)+0.1*enemy.Atk)
                    self.dano = self.dano *0.65
                    if self.dano < self.hp: 
                        self.hp = self.hp - self.dano 
                    else:
                        self.hp = 0
                        self.live = False
                        #self.Dead()
        else:
           if self.dmg:
            if enemy.Atk >self.Def :
                self.dano = 0.5*(enemy.Atk - 0.79*self.Def * math.e **(-0.27*(self.Def/enemy.Atk)))
                if self.dano < self.hp: 
                    self.hp = self.hp - self.dano 
                else:
                    self.hp = 0
                    self.live = False
                    #self.Dead()
            else:
                self.dano = 0.5*(0.4*(enemy.Atk**3/self.Def**2)-0.09*(enemy.Atk**2/self.Def)+0.1*enemy.Atk)
                if self.dano < self.hp: 
                    self.hp = self.hp - self.dano 
                else:
                    self.hp = 0
                    self.live = False
                    #self.Dead()
                    
            
    def Dead(self):
        if not self.live:
            if self.Lives > 0:
                self.rect.y = 100
                self.rect.x = 0
                self.Lives -=1
                self.hp = constants.Hp_Max
                self.mp = constants.Mp_Max
                self.live = True
                self.jump= True
                self.onGround = False
    def Vitoria(self):
        self.com = True
            
    def Defesa(self):
        self.defending = True     
                
    def healt_regen(self):
        if self.live:
            if self.hp < constants.Hp_Max and not self.live:
                self.hp +=0.01
    def Mp_regen(self):
        if self.live:
            if self.mp < constants.Mp_Max and not self.live:
                self.mp += 0.1
#==============================================================================
#Hud Do player:
#==============================================================================
    def player_hud(self, screen):
        
        self.Hp_Max_Porc = (constants.Hp_Max/constants.Hp_Max)*100
        self.Hp_Porc = (self.hp/constants.Hp_Max)*100
        self.Mp_Max_Porc = (constants.Mp_Max/constants.Mp_Max)*100
        self.Mp_Porc = (self.mp/constants.Mp_Max)*100
        Vida = constants.Get_Font("font\8-BIT WONDER.TTF", 10)
        
        Vidas = Vida.render("x"+str(self.Lives), True, constants.WHITE, None)
        Vidas_Rect = Vidas.get_rect()
        Vidas_Rect.x ,Vidas_Rect.y = 190,104 
        
       
        pygame.draw.rect(screen, constants.WHITE,(0,60,60,69))
        pygame.draw.rect(screen, constants.BGREEN,(1,61,58,67))
        screen.blit(self.Face, (1,60))
        pygame.draw.rect(screen, constants.WHITE, (61, 104, 1.5*self.Hp_Max_Porc+2, 12)) 
        pygame.draw.rect(screen, constants.GRAY, (62, 105, 1.5*self.Hp_Max_Porc, 10))
        if self.Hp_Porc >= self.Hp_Max_Porc * 0.75:
            pygame.draw.rect(screen, constants.GREEN, (62, 105, 1.5*self.Hp_Porc, 10))
        elif self.Hp_Porc >= self.Hp_Max_Porc * 0.25 and self.Hp_Porc < self.Hp_Max_Porc * 0.75:
            pygame.draw.rect(screen, constants.YELLOW, (62, 105, 1.5*self.Hp_Porc, 10))
        elif self.Hp_Porc < self.Hp_Max_Porc * 0.25 and self.Hp_Porc > 0:
            pygame.draw.rect(screen, constants.RED, (62, 105, 1.5*self.Hp_Porc, 10))
        elif self.Hp_Porc == 0:
            pygame.draw.rect(screen, constants.GRAY, (62, 105, 1.5*self.Hp_Max_Porc, 10))
        screen.blit(Vidas,Vidas_Rect)
        pygame.draw.rect(screen, constants.WHITE, (61, 117, (1.5*self.Mp_Max_Porc)+2, 12))
        pygame.draw.rect(screen, constants.GRAY, (62, 118, 1.5*self.Mp_Max_Porc, 10))
        pygame.draw.rect(screen, constants.BLUE, (62, 118, 1.5*self.Mp_Porc, 10))
        
#==============================================================================
# Tela de Morte Player        
#==============================================================================
def dead_screen(screen,enemy_l,boss_list,enemy_list,bac_enemy_l,bac_boss,bac_enemy,player):
    if constants.regrecive > 0:
        black_surf = pygame.Surface((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT), pygame.SRCALPHA)
        black_surf.fill((0, 0, 0, 180))
        screen.blit(black_surf, (0, 0))
    #==============================================================================
        #Carre as Fontes    
    #==============================================================================
        pre_game_over = constants.Get_Font(constants.SaiyanFont,72)        
        Continue = constants.Get_Font(constants.BitFont, 22)
        Cont = constants.Get_Font(constants.BitFont,200)
        you_died_txt = pre_game_over.render("Meu Estomago Doi", True, constants.WHITE, None)
        continue_txt = Continue.render("Continue?", True, constants.WHITE, None)
    #==============================================================================
        #Carrega Es informaçoes:
    #==============================================================================
        black_surf = pygame.Surface((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT), pygame.SRCALPHA)
        black_surf.fill((0, 0, 0, 180))
        screen.blit(black_surf, (0, 0))
        you_died_rect = you_died_txt.get_rect()
        you_died_rect.center = ((constants.SCREEN_WIDTH/2),(constants.SCREEN_HEIGHT/5-100))
        screen.blit(you_died_txt, you_died_rect)
        continue_rect = you_died_txt.get_rect()
        continue_rect.center = ((100+constants.SCREEN_WIDTH/2),(constants.SCREEN_HEIGHT/5))
        screen.blit(continue_txt, continue_rect)    
        cont_txt = Cont.render(str(constants.regrecive),True,constants.WHITE,None)
        cont_txt_rect = cont_txt.get_rect()
        cont_txt_rect.center = ((constants.SCREEN_WIDTH/2),(constants.SCREEN_HEIGHT/2))
        screen.blit (cont_txt,cont_txt_rect)
        if constants.delays > 60:
            constants.delays = 0
            constants.regrecive -= 1
        else:
            constants.delays += 1 
    
        for event in pygame.event.get():
                pressed = pygame.key.get_pressed()
                if event.type == pygame.QUIT:
                    pygame.quit() # Fecha a janela se o usuário clicar em fechar
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        enemy_l = bac_enemy_l
                      #  enemy_list = bac_enemy
                        boss_list = bac_boss
                        player.live = True
                        player.hp = constants.Hp_Max
                        player.rect.x = 200
                        player.Muda_Rota = 20
                        player.rect.y = constants.SCREEN_HEIGHT - player.rect.height - player.Muda_Rota 
                        player.dmg = False
                        player.jump = False
                        
                        
                            
                        
                        
                    if ((pressed[pygame.K_LALT] and pressed[pygame.K_F4]) or (pressed[pygame.K_RALT] and pressed[pygame.K_F4])):
                        pygame.quit() # Fecha a janela se o usuário pressionar ALT+F4
                        quit()    
    else:
        black_surf = pygame.Surface((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT), pygame.SRCALPHA)
        black_surf.fill((0, 0, 0, 255))
        screen.blit(black_surf, (0, 0))
        game_over = constants.Get_Font(constants.SaiyanFont,90)
        Game_over = game_over.render("Game Over",True,constants.WHITE,None)
        Game_over_Rect = Game_over.get_rect()
        Game_over_Rect.center = ((constants.SCREEN_WIDTH/2),(constants.SCREEN_HEIGHT/2))
        screen.blit(Game_over, Game_over_Rect)
        for event in pygame.event.get():
                pressed = pygame.key.get_pressed()
                if event.type == pygame.QUIT:
                    pygame.quit() # Fecha a janela se o usuário clicar em fechar
                    quit()
                if event.type == pygame.KEYDOWN:
                    if ((pressed[pygame.K_LALT] and pressed[pygame.K_F4]) or (pressed[pygame.K_RALT] and pressed[pygame.K_F4])) or pygame.K_RETURN:
                        pygame.quit() # Fecha a janela se o usuário pressionar ALT+F4
                        quit() 
    return enemy_list
        
