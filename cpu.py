import pygame, constants, math, random, Sounds

class CPU (pygame.sprite.Sprite):
    def __init__(self):
        
        super().__init__()
        # Stats:
#==============================================================================
#        Status: 
#==============================================================================
        self.Hp_Max = 0
        self.hp = self.Hp_Max
        self.Mp_Max = 0
        self.mp = self.Mp_Max
        self.Atk = 0
        self.Def = 0
#==============================================================================
        """constantes de animaçao""" 
#==============================================================================
        self.delay_standby = self.delay_dmg= self.delay_dead = self.delay = 0
        self.delay_punch = self.delay_kick = 0
        self.i = self.p = self.k = self.h = self.d = self.r = 0
        self.count = 0
        self.count_p = self.count_k = 0
        self.dano = 0
        self.nome = None
        self.Action = None
        self.Sub_Action = None
        self.Action_list = ["Chase","Dont"]
        self.Sub_Action_list = ['Stop','Punch','Kick']
#==============================================================================
        """Define o movimento do Enemy"""
#==============================================================================
        self.change_x = 0   
        self.change_y = 0
        self.Muda_Rota = 0
        self.Rota_Seg = 0  
#==============================================================================
        """Lista de Imagens das Posiçoes ESQUERDA\DIREITA:"""
#==============================================================================
        self.Face = None  
        #==============================================================================
        """Movimentos de Movimentaçao:""" 
        #==============================================================================
        """Personagem Parado:"""
        self.Para_Frames_L = []     
        self.Para_Frames_R = []
        """Peronagem Andando:"""
        self.Move_Frames_L = []
        self.Move_Frames_R = []
        """Salto Parado:"""
        self.Salto_Para_Frames_L = []
        self.Salto_Para_Frames_R = []
        """Salto Movimento :"""
        self.Salto_Move_Frames_L = []
        self.Salto_Move_Frames_R = []
        #==============================================================================
        """Movimentos que envolvem dano:"""                                     #Comentarios e Descriçoes
        #==============================================================================
        """Recebendo dano """
        self.Dmg_R = []                                                         #Leva dano para a Direita       
        self.Dmg_R = []                                                         #Leva dano para a Esquerda
        """Morte"""
        self.Dead_R =[]                                                         #Morre para a Direita
        self.Dead_L = []                                                        #Morre para a Esquerda
        #==============================================================================
        """Movimentos de Ataque:"""
        #==============================================================================
        """Soco""" 
        self.Atk_P_R = []                                                       #Socos para Direita
        self.Atk_P_L = []                                                       #Socos para Esquerda
        """Chute"""
        self.Atk_K_R = []                                                       #Chutes para Direita
        self.Atk_K_L = []                                                       #Chutes para Esquerda                          
#==============================================================================
        """Vericaçoes:"""
#==============================================================================
        self.Lives = 2                                                          #Desnecessario
        self.direction = "R"                                                    #Verifica para q lado esta virado a Sprite                
        self.level = None                                                       #Verifica a fase em questao
        self.ml = False 
#==============================================================================
        """Estados:"""
#==============================================================================
        self.a = False
        self.live = True                                                        #Verifica se o enemy esta vivo 
        self.jump = False                                                       #Verifica se esta Pulando 
        self.ki_charge = False                                                  #Verifica se esta carregando o ki 
        self.dmg = False                                                        #Verifica se esta levando dano
        self.dealdmg = False
        self.rec = False
        self.punch = False                                                      #Verifica se esta socando 
        self.kick = False                                                       #Verifica se esta chutanto
        self.SPC1_Atk = False                                                   #Verifica se esta dando o Especial 1
        self.SPC2_Atk = False                                                   #Verifica se esta dando o Especial 2
        self.SPC3_Atk = False                                                   #Verifica se esta dando o Especial 3
        self.Ult_Atk = False                                                    #Verifica se esta Dando o ultimate 
        self.onGround = False                                                   #Verifica se esta no Chao
#============================================================================== 
        self.mask = None
#==============================================================================
    """Funcoes do  Enemy:"""
#==============================================================================
    def update(self): #Faz a animaçao do Enemy
        pass
#==============================================================================
        """Faz a Verificaçao do que é possivel o Enemy fazer"""
#==============================================================================
    def State(self,event):    
        if event == 'wait':
            if self.live and not self.jump and not self.ki_charge and not self.punch and not self.kick and not self.SPC1_Atk and not self.SPC2_Atk and not self.SPC3_Atk and not self.Ult_Atk:
                return True
        elif event == 'move':
            if self.live and not self.ki_charge and not self.dmg and not self.punch and not self.kick and not self.SPC1_Atk and not self.SPC2_Atk and not self.SPC3_Atk and not self.Ult_Atk:
                return True
        elif event == 'jump':
            if self.live and not self.jump and not self.ki_charge and not self.punch and not self.kick and not self.SPC1_Atk and not self.SPC2_Atk and not self.SPC3_Atk and not self.Ult_Atk:
                return True
        elif event == 'ki_charge':
            if self.live and not self.jump and not self.punch and not self.kick and not self.SPC1_Atk and not self.SPC2_Atk and not self.SPC3_Atk and not self.Ult_Atk:
                return True
        elif event == 'punch':
            if self.live and not self.jump and not self.ki_charge and not self.kick and not self.SPC1_Atk and not self.SPC2_Atk and not self.SPC3_Atk and not self.Ult_Atk:
                return True
        elif event == 'kick':
            if self.live and not self.jump and not self.ki_charge and not self.punch and not self.SPC1_Atk and not self.SPC2_Atk and not self.SPC3_Atk and not self.Ult_Atk:
                return True
        elif event == 'Special_1':
            if self.live and not self.jump and not self.ki_charge and not self.punch and not self.kick and not self.SPC2_Atk and not self.SPC3_Atk and not self.Ult_Atk:
                return True
        elif event == 'Special_2':
            if self.live and not self.jump and not self.ki_charge and not self.punch and not self.kick and not self.SPC1_Atk and not self.SPC3_Atk and not self.Ult_Atk:
                return True
        elif event == 'Special_3':
            if self.live and not self.jump and not self.ki_charge and not self.punch and not self.kick and not self.SPC1_Atk and not self.SPC2_Atk and not self.Ult_Atk:
                return True
        elif event == 'Ultimate':
            if self.live and not self.jump and not self.ki_charge and not self.punch and not self.kick and not self.SPC1_Atk and not self.SPC2_Atk and not self.SPC3_Atk:
                return True
#==============================================================================
    """Inteligencia Artificial"""
#============================================================================== 
    def ai (self,player):
        if self.live:
            if player.rect.left > self.rect.right + 250 or player.rect.right < self.rect.left -250:
                self.stop()
            else:
                if player.rect.centerx > self.rect.centerx:
                    self.direction = "R"
                else:
                    self.direction = "L" 
                    
                if self.Action == "Chase":
                    if player.rect.bottom < self.rect.bottom and not player.jump:
                        if self.State('move'):
                            self.Muda_Rota_Sup()
                    if player.rect.bottom > self.rect.bottom and not player.jump :
                        if self.State('move'):
                            self.Muda_Rota_Inf()
                    if player.rect.centerx + 100 < self.rect.left:
                        if self.State('move'):
                            self.go_left()
                    if player.rect.centerx - 100 > self.rect.right:
                        if self.State('move'):
                            self.go_right()
                    elif player.rect.left == self.rect.right or player.rect.right == self.rect.left:
                        self.stop()
                        if self.dmg:
                            self.rec = True
                        self.time_rec()
                        if player.live and not self.rec :
                            if self.Sub_Action == 'Punch':
                                if self.State('punch'):
                                    if self.count_p > 25:
                                        self.count_p = 0
                                        self.Soco_1()
                                    else:
                                        self.count_p += 1
                            if self.Sub_Action == 'Kick':
                                if self.State('kick'):
                                    if self.count_k > 25:
                                        self.count_k = 0
                                        self.Chute_1()
                                    else:
                                        self.count_k += 1
                            if self.Sub_Action == "Stop":
                                self.stop()
                                
                if self.Action == "Dont":
                    self.stop()
                    if self.dmg:
                            self.rec = True
                    self.time_rec()
                    if self.State('jump') and not self.rec:
                        self.Jump()
#==============================================================================
# Funçoes Surporte da ai:           
#==============================================================================
    def boss_action(self): 
        self.Action = random.choice(self.Action_list)
        return self.Action
    
    def sub_action(self):
        self.Sub_Action = random.choice(self.Sub_Action_list)
        return self.Sub_Action
#==============================================================================
#        if player.rect.centerx > self.rect.centerx:
#            self.direction = "R"
#        else:
#            self.direction = "L"
#        if player.rect.centerx + 100 < self.rect.left:
#            if self.State('move'):
#                self.go_left()
#        elif player.rect.centerx - 100 > self.rect.right:
#            if self.State('move'):
#                self.go_right()
#        elif player.rect.left == self.rect.right or player.rect.right == self.rect.left:
#            self.stop()
#            if player.live and not self.dmg:
##                if clock.get_fps>60:
#                    if self.Action == 0:
#                        if self.State('punch'):
#                            self.Soco_1()
#                    if self.Action == 1:
#                        if self.State('kick'):
#                            self.Chute_1()
#                    if self.Action == 1 or 2 or 3 or 4 or 5 or 6: 
#                        pass
##               
#            
#                
#        if player.rect.bottom < self.rect.bottom and not player.jump:
#            if self.State('move'):
#                self.Muda_Rota_Sup()
#        elif player.rect.bottom > self.rect.bottom and not player.jump :
#            if self.State('move'):
#                self.Muda_Rota_Inf()
        
       
#==============================================================================
    """Mecanicas Gerais"""       
#==============================================================================
    def calc_grav(self):
        """ Calcula o efeito da Gravidade """
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
#==============================================================================
    """Funcoes de Movimento """
#==============================================================================
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
#==============================================================================
    """Mecanicas no Enemy"""
#==============================================================================

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
    
    def time_rec(self):
        if self.rec:
            if self.delay > 10:
                self.delay = 0
                self.rec = False
            else:
                self.delay +=1
        
    def Recive_Dmg(self,player):
            if self.dmg:
                self.ml = True
                if player.Atk >self.Def :
                    self.dano = 0.5*(player.Atk - 0.79*self.Def * math.e **(-0.27*(self.Def/player.Atk)))
                    if self.dano < self.hp: 
                        self.hp = self.hp - self.dano 
                    else:
                        self.hp = 0
                        self.live = False
                        
                else:
                    self.ml = True
                    self.dano = 0.5*(0.4*(player.Atk**3/self.Def**2)-0.09*(player.Atk**2/self.Def)+0.1*player.Atk)
                    if self.dano < self.hp: 
                        self.hp = self.hp - self.dano 
                    else:
                        self.hp = 0
                        self.live = False
                                            
                
#==============================================================================
    """Barra de Vida do enemy"""                                           
#==============================================================================
    def enemy_hud(self, screen):
        if self.live:
            self.Hp_Max_Porc = (self.Hp_Max/self.Hp_Max)*100
            self.Hp_Porc = (self.hp/self.Hp_Max)*100
            pygame.draw.rect(screen, constants.WHITE, (self.rect.left,self.rect.top - 12,0.75*self.Hp_Max_Porc+2, 12))
            pygame.draw.rect(screen, constants.GRAY, (self.rect.left +1,self.rect.top - 11,0.75*self.Hp_Max_Porc, 10))
            if self.Hp_Porc >0:        
                pygame.draw.rect(screen, constants.RED, (self.rect.left +1,self.rect.top - 11,0.75*self.Hp_Porc, 10))
            else:
                pygame.draw.rect(screen, constants.GRAY, (self.rect.left +1,self.rect.top - 11,0.75*self.Hp_Max_Porc, 10))
                
    def boss_hud(self,screen):
        if self.live:
            self.boss_name = self.nome
            self.Hp_Max_Porc = (self.Hp_Max/self.Hp_Max)*100
            self.Hp_Porc = (self.hp/self.Hp_Max)*100
            
            
        
            nome  = constants.Get_Font("font\8-BIT WONDER.TTF", 10)
            
            nome = nome.render(self.boss_name, True, constants.WHITE, None)
            nome_Rect = nome.get_rect()
            nome_Rect.x ,nome_Rect.y = 1000,104 
            
           
#            pygame.draw.rect(screen, constants.WHITE,(0,60,60,69))
#            pygame.draw.rect(screen, constants.BGREEN,(1,61,58,67))
#            screen.blit(self.Face, (1,60))
            pygame.draw.rect(screen, constants.WHITE, (951, 117, (2*self.Hp_Max_Porc)+2, 12))
            pygame.draw.rect(screen, constants.GRAY, (952, 118, 2*self.Hp_Max_Porc, 10))
            if self.Hp_Porc > 0.75*self.Hp_Max_Porc:
                pygame.draw.rect(screen, constants.GREEN, (952, 118, 2*self.Hp_Max_Porc, 10))
                pygame.draw.rect(screen, constants.BLUE, (952, 118, 2*self.Hp_Porc, 10))
            if 0.5*self.Hp_Max_Porc < self.Hp_Porc <= .75*self.Hp_Max_Porc:
                pygame.draw.rect(screen, constants.YELLOW, (952, 118, 2*self.Hp_Max_Porc, 10))
                pygame.draw.rect(screen, constants.GREEN, (952, 118, 2*self.Hp_Porc, 10))
            if 0.25*self.Hp_Max_Porc < self.Hp_Porc <= .5*self.Hp_Max_Porc:
                pygame.draw.rect(screen, constants.RED, (952, 118, 2*self.Hp_Max_Porc, 10))
                pygame.draw.rect(screen, constants.YELLOW, (952, 118, 2*self.Hp_Porc, 10))
            if 0.25*self.Hp_Max_Porc >= self.Hp_Porc:
                pygame.draw.rect(screen, constants.RED, (952, 118, 2*self.Hp_Porc, 10))
        
    
    
    