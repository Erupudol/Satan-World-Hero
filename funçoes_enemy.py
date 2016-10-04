import pygame
 
import constants
 
from platforms import MovingPlatform
from spritesheet_functions import *

def Anima(self):
    while self.delay > constants.FPS/10:
        self.delay = 0
        if self.direction == "R":
            self.image = self.Para_Frames_R[self.i]
        else:
            self.image = self.Para_Frames_L[self.i]
        if self.i >= len(self.Para_Frames_R) - 1:
            self.i = 0
        else:
            self.i += 1            
    self.delay += 1
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
    if self.punch == True  and self.count == 0:
            self.change_x = 0
            if self.delay > constants.FPS/35:
                self.delay = 0
                if self.direction == "R":
                    self.image = self.Atk_P1_R[self.s]
                else:
                    self.image = self.Atk_P1_L[self.s]
                    self.rect.right -=  self.rect.width - 72 
                if self.s >= (len(self.Atk_P1_R)) - 1:
                    self.s = 0
                    if self.direction == "L":
                        self.rect.right += self.rect.width - 72
                    self.punch = False
                else:
                    self.s += 1
                    
            else:
                self.delay += 1
            self.count = 1
    
    elif self.punch == True  and self.count == 1 :
            if self.delay > constants.FPS/35 :
                self.delay = 0
                if self.direction == "R":
                    self.image = self.Atk_P2_R[self.s]
                else:
                    self.image = self.Atk_P2_L[self.s]
                    self.rect.right -= self.rect.width - 72
                if self.s >= (len(self.Atk_P1_R)) - 1:
                    self.s = 0
                    if self.direction == "L":
                        self.rect.right += self.rect.width - 72
                    self.punch = False
                    
                else:
                    self.s += 1                  
            else:
                self.delay += 1
            self.count = 0
            
    elif self.punch == True and self.count >= 1:
        self.count = 0
        
def Anima_Golpes_Chute(self):       #Chutes:
    if self.kick:
        if self.delay > constants.FPS/25:
            self.delay = 0
            if self.direction == "R":
                self.image = self.Atk_K1_R[self.s]
            else:
                self.image = self.Atk_K1_L[self.s]
            if self.s >= len(self.Atk_K1_R) - 1:
                self.s = 0
                self.kick = False
            else:
                self.s += 1
                    
        else:
            self.delay += 1
            
def Anima_Def(self):
    if self.defending:
            if self.delay > constants.FPS/30:
                self.delay = 0
                if self.direction == "R":
                    self.image = self.Def_R[self.s]
                else:
                    self.image = self.Def_L[self.s]
                if self.s >= len(self.Def_R) - 1 :
                    self.s = 1
                else:
                    self.s +=1
            else: self.delay +=1
def Anima_Dmg(self):
    if self.dmg and self.live:
            if self.delay > constants.FPS/30:
                self.delay = 0
                if self.direction == "R":
                    self.image = self.Dmg_R[self.s]
                else:
                    self.image = self.Dmg_L[self.s]
                if self.s >= len(self.Dmg_R) - 1 :
                    self.s = 0
                    self.dmg = False
                else:
                    self.s +=1
            else: self.delay +=1
            
def Anima_Dead(self):
     if not self.live:
            if self.delay > constants.FPS/10:
                self.delay = 0
                if self.direction == "R":
                    self.image = self.Dead_R[self.s]
                    self.rect.x += self.change_x
                    self.rect.y = self.rect.bottom 
                else:
                    self.image = self.Dead_L[self.s]
                    self.rect.x -= self.change_x
                    self.rect.y = self.rect.bottom 
                if self.s >= len(self.Dead_R) - 1 :
                    self.s = 4
                    self.change_x = 0
                    if self.Lives > 0 and self.i >= 15:
                        self.Dead()
                        self.s = 0
                        self.i = 0
                    else:
                        self.i += 1
                else:
                    self.change_x -= 10
                    self.s +=1
            else: self.delay +=1
            
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



