import constants, Sounds
 

def Anima(self):
    while self.delay_standby > constants.FPS/10:
        self.delay_standby = 0
        if self.direction == "R":
            self.image = self.Para_Frames_R[self.i]
        else:
            self.image = self.Para_Frames_L[self.i]
        if self.i >= len(self.Para_Frames_R) - 1:
            self.i = 0  
        else:
            self.i += 1            
    self.delay_standby += 1
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
            if self.delay_punch > constants.FPS/45:
                self.delay_punch = 0
                if self.direction == "R":
                    self.image = self.Atk_P1_R[self.p]
                else:
                    self.image = self.Atk_P1_L[self.p]
                if self.p >= (len(self.Atk_P1_R)) - 1:
                    self.p = 0
                    self.punch = False
                else:
                    self.p += 1
                if self.p == 2:
                    self.dealdmg = True
                else:
                    self.dealdmg = False
                    
            else:
                self.delay_punch += 1
            self.count = 1
    
    elif self.punch == True  and self.count == 1 :
            if self.delay_punch > constants.FPS/35 :
                self.delay_punch = 0
                if self.direction == "R":
                    self.image = self.Atk_P2_R[self.p]
                else:
                    self.image = self.Atk_P2_L[self.p]
                if self.p >= (len(self.Atk_P1_R)) - 1:
                    self.p = 0
                    self.punch = False
                else:
                    self.p += 1 
                if self.p == 2:
                    self.dealdmg = True
                    
                else:
                    self.dealdmg = False
                                
            else:
                self.delay_punch += 1
            self.count = 0
            
    elif self.punch == True and self.count >= 1:
        self.count = 0
        
def Anima_Golpes_Chute(self):       #Chutes:
    if self.kick:
        if self.delay_kick > constants.FPS/35:
            self.delay_kick = 0
            if self.direction == "R":
                self.image = self.Atk_K1_R[self.k]
            else:
                self.image = self.Atk_K1_L[self.k]
            if self.k >= len(self.Atk_K1_R) - 1:
                self.k = 0
                self.kick = False
            else:
                self.k += 1
            if self.k == 2:
                self.dealdmg = True
            else:
                self.dealdmg = False
        else:
            self.delay_kick += 1
            
def Anima_Def(self):
    if self.defending:
            if self.delay_def > constants.FPS/30:
                self.delay_def = 0
                if self.direction == "R":
                    self.image = self.Def_R[self.a]
                else:
                    self.image = self.Def_L[self.a]
                if self.a >= len(self.Def_R) - 1 :
                    self.a = 1
                else:
                    self.a +=1
            else: self.delay_def +=1
def Anima_Dmg(self):
    if self.dmg and self.live and not self.defending:
            if self.delay_dmg > constants.FPS/30:
                self.delay_dmg = 0
                if self.direction == "R":
                    self.image = self.Dmg_R[self.h]
                else:
                    self.image = self.Dmg_L[self.h]
                if self.h >= len(self.Dmg_R) - 1 :
                    self.h = 0
                    self.dmg = False
                
                else:
                    self.h +=1
            else: self.delay_dmg +=1
            
def Anima_Dead(self):
     if not self.live:
            self.defending =  False
            if self.delay_dead > constants.FPS/10:
                self.delay_dead = 0
                if self.direction == "R":
                    self.image = self.Dead_R[self.d]
                    self.rect.y = self.rect.bottom 
                else:
                    self.image = self.Dead_L[self.d]
                    self.rect.y = self.rect.bottom 
                if self.d >= len(self.Dead_R) - 1 :
                    self.d = 4
                    self.change_x = 0
                    if self.Lives > 0 and self.c >= 15:
                        self.Dead()
                        self.d = 0
                        self.c = 0
                    else:
                        self.c += 1
                    if self.d == 2:
                        Sounds.Down.play()
                else:
                    self.d +=1
            else: self.delay_dead +=1
            
def Anima_vit(self):
    if self.com:
        if self.delay_vit > constants.FPS/10:
            self.delay_vit = 0
            self.image = self.Com_R[self.v]
            if self.v >= len(self.Com_R)-1:
                self.v = 7
            else:
                self.v += 1
        else:
            self.delay_vit +=1
            




