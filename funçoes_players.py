import pygame
 
import constants
 
from platforms import MovingPlatform
from spritesheet_functions import *

def Anima(self):
    while constants.delay > constants.FPS/10:
        constants.delay = 0
        if self.direction == "R":
            self.image = self.Para_Frames_R[constants.i]
        else:
            self.image = self.Para_Frames_L[constants.i]
        if constants.i >= len(self.Para_Frames_R) - 1:
            constants.i = 0
        else:
            constants.i += 1            
    constants.delay += 1
def Anima_Mov(self):
        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift
        if self.direction == "R":
            frame = (pos // 30) % len(self.Move_Frames_R)
            self.image = self.Move_Frames_R[frame]
        else:
            frame = (pos // 30) % len(self.Move_Frames_L)
            self.image = self.Move_Frames_L[frame]
            
def Anima_Golpes_Soco(self):
    if self.punch == True  and constants.count == 0:
            self.change_x = 0
            if constants.delay > constants.FPS/35:
                constants.delay = 0
                if self.direction == "R":
                    self.image = self.Atk_P1_R[constants.s]
                    self.mask = pygame.mask.from_surface(self.image)
                else:
                    self.image = self.Atk_P1_L[constants.s]
                    self.mask = pygame.mask.from_surface(self.image)
                    self.rect.right -=  self.rect.width - 72 
                if constants.s >= (len(self.Atk_P1_R)) - 1:
                    constants.s = 0
                    if self.direction == "L":
                        self.rect.right += self.rect.width - 72
                    self.punch = False
                else:
                    constants.s += 1
                    
            else:
                constants.delay += 1
            constants.count = 1
    
    elif self.punch == True  and constants.count == 1 :
            if constants.delay > constants.FPS/35 :
                constants.delay = 0
                if self.direction == "R":
                    self.image = self.Atk_P2_R[constants.s]
                    self.mask = pygame.mask.from_surface(self.image)
                else:
                    self.image = self.Atk_P2_L[constants.s]
                    self.mask = pygame.mask.from_surface(self.image)
                if constants.s >= (len(self.Atk_P1_R)) - 1:
                    constants.s = 0
                    self.punch = False
                    
                else:
                    constants.s += 1                  
            else:
                constants.delay += 1
            constants.count = 0
            
    elif self.punch == True and constants.count >= 1:
        constants.count = 0
        
def Anima_Golpes_Chute(self):       #Chutes:
    if self.kick:
        if constants.delay > constants.FPS/25:
            constants.delay = 0
            if self.direction == "R":
                self.image = self.Atk_K1_R[constants.s]
            else:
                self.image = self.Atk_K1_L[constants.s]
            if constants.s >= len(self.Atk_K1_R) - 1:
                constants.s = 0
                self.kick = False
            else:
                constants.s += 1
                    
        else:
            constants.delay += 1
            
def Anima_Def(self):
    if self.defending:
            if constants.delay > constants.FPS/30:
                constants.delay = 0
                if self.direction == "R":
                    self.image = self.Def_R[constants.s]
                else:
                    self.image = self.Def_L[constants.s]
                if constants.s >= len(self.Def_R) - 1 :
                    constants.s = 1
                else:
                    constants.s +=1
            else: constants.delay +=1
def Anima_Dmg(self):
    if self.dmg and self.live:
            if constants.delay > constants.FPS/30:
                constants.delay = 0
                if self.direction == "R":
                    self.image = self.Dmg_R[constants.s]
                else:
                    self.image = self.Dmg_L[constants.s]
                if constants.s >= len(self.Dmg_R) - 1 :
                    constants.s = 0
                    self.dmg = False
                else:
                    constants.s +=1
            else: constants.delay +=1
            
def Anima_Dead(self):
     if not self.live:
            if constants.delay > constants.FPS/10:
                constants.delay = 0
                if self.direction == "R":
                    self.image = self.Dead_R[constants.s]
                    self.rect.x += self.change_x
                    self.rect.y = self.rect.bottom 
                else:
                    self.image = self.Dead_L[constants.s]
                    self.rect.x -= self.change_x
                    self.rect.y = self.rect.bottom 
                if constants.s >= len(self.Dead_R) - 1 :
                    constants.s = 4
                    self.change_x = 0
                    if self.Lives > 0 and constants.i >= 15:
                        self.Dead()
                        constants.s = 0
                        constants.i = 0
                    else:
                        constants.i += 1
                else:
                    self.change_x -= 10
                    constants.s +=1
            else: constants.delay +=1
            
def Anima_Golpes_ASoco(self):
    pass

def Anima_Golpes_AChute(self):
    pass

def Anima_Golpes_Agarra(self):
    pass

def Anima_Golpes_DSoco(self):
    pass

def Anima_Golpes_DChute(self):
    pass

def Anima_Golpes_SBast(self):
    pass

def Anima_Golpes_SGrad(self):
    pass

def Anima_Golpes_SRocket(self):
    pass

def Anima_Golpes_SDouRocket(self):
    pass

def Anima_Golpes_SMiss(self):
    pass



