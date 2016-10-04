import pygame
import player 
import constants
from spritesheet_functions import *

def boss_hud(screen,boss_name, boss_health):
    boss_maxhealth = 1000
    boss_name = constants.boss_SF.render(boss_name, True, constants.WHITE, None)
    boss_name_rect = boss_name.get_rect()
    boss_name_rect.x = 50
    boss_name_rect.y = 515
    screen.blit(boss_name, boss_name_rect)

    pygame.draw.rect(screen, constants.WHITE, (49, 529, (0.8*boss_maxhealth)+2, 12))
    pygame.draw.rect(screen, constants.GRAY, (50, 530, 0.8*boss_maxhealth, 10))
    pygame.draw.rect(screen, constants.ORANGE, (850-(0.8*boss_health), 530, 0.8*boss_health, 10))
    
def use_estus(self):
        while (self.health < self.maxhealth or self.health < self.health + 35) and self.estus_rn > 0:  
            self.health += 2.5           
        self.estus_rn -= 1