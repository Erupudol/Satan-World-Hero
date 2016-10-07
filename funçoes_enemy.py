import constants


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
            if self.delay_punch > constants.FPS/35:
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
        if self.delay_kick > constants.FPS/25:
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
            
def Anima_Dmg(self):
    if self.dmg and self.live:
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
            if self.delay_dead > constants.FPS/10:
                self.delay_dead = 0
                if self.direction == "R":
                    self.image = self.Dead_R[self.d]
                    self.rect.x += self.change_x
                    self.rect.y = self.rect.bottom 
                else:
                    self.image = self.Dead_L[self.d]
                    self.rect.x -= self.change_x
                    self.rect.y = self.rect.bottom 
                if self.d >= len(self.Dead_R) - 1 :
                    self.d = 4
                    self.change_x = 0
                    if self.Lives > 0 and self.r >= 15:
                        self.Dead()
                        self.d = 0
                        self.r = 0
                    else:
                        self.r += 1
                else:
                    self.change_x -= 10
                    self.d +=1
            else: self.delay_dead +=1
            




