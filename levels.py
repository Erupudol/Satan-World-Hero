import pygame
import platforms 
import constants
import Music_Sounds
from hud import *
from enemy import*

class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """
 
    def __init__(self, player,enemy):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
 
        # Lists of sprites used in all levels. Add or remove
        # lists as needed for your game.
        self.platform_list = None
        
 
        # Background image
        self.background = None
 
        # How far this world has been scrolled left/right
        self.world_shift = 0
        self.level_limit = -1000
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player
        self.enemy = enemy
 
    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        
        
 
    def draw(self, screen):
        """ Draw everything on this level. """
 
        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(constants.BLUE)
        screen.blit(self.background,(self.world_shift // 3,0))
        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
 
    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """
 
        # Keep track of the shift amount
        self.world_shift += shift_x
 
        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x
 
        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
 
# Create platforms for the level

class Level_01(Level):
    """ Definition for level 1. """
 
    def __init__(self, player,enemy):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player,enemy)
        
 
        self.background = pygame.image.load("Fotos\Teste1.png").convert()
        self.background=  pygame.transform.scale(self.background,(5500,700))
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -7000

#        level = [ [platforms.STONE_PLATFORM_MIDDLE, constants.SCREEN_WIDTH-50, constants.SCREEN_HEIGHT-500],
#                      [platforms.STONE_PLATFORM_MIDDLE, constants.SCREEN_WIDTH-(48*2), constants.SCREEN_HEIGHT-12],
#                      [platforms.STONE_PLATFORM_MIDDLE, constants.SCREEN_WIDTH-(48*3), constants.SCREEN_HEIGHT-12],
#                      [platforms.STONE_PLATFORM_MIDDLE, constants.SCREEN_WIDTH-(48*4), constants.SCREEN_HEIGHT-12],
#                      [platforms.STONE_PLATFORM_MIDDLE, constants.SCREEN_WIDTH-(48*5), constants.SCREEN_HEIGHT-12],
#                      [platforms.STONE_PLATFORM_MIDDLE, constants.SCREEN_WIDTH-48, constants.SCREEN_HEIGHT-24],
#                      [platforms.STONE_PLATFORM_MIDDLE, constants.SCREEN_WIDTH-(48*2), constants.SCREEN_HEIGHT-24],
#                      [platforms.STONE_PLATFORM_MIDDLE, constants.SCREEN_WIDTH-(48*3), constants.SCREEN_HEIGHT-24],
#                      [platforms.STONE_PLATFORM_MIDDLE, constants.SCREEN_WIDTH-(48*4), constants.SCREEN_HEIGHT-24],
#                      [platforms.STONE_PLATFORM_MIDDLE, constants.SCREEN_WIDTH-(48*5), constants.SCREEN_HEIGHT-24]
#                      ]
#     
#            # Passa pelo array e adiciona plataformas
#        for platform in level:
#                block = platforms.Platform(platform[0])
#                block.rect.x = platform[1]
#                block.rect.y = platform[2]
#                block.player = self.player
#                self.platform_list.add(block)
#     

#           

#        L_e = [ [Boss_Satan(player), constants.SCREEN_WIDTH + 400, constants.SCREEN_HEIGHT - 100]]
#        for enemy in L_e:
#            Enemy = enemy[0]    
#            Enemy.rect.x = enemy[1]
#            Enemy.rect.y = enemy[2]
##            Enemy.ai(player)
#            self.enemy_list.add(Enemy)
        

def Start_Screen():
    pygame.mixer.music.load("Music\StartScreean.ogg")
    pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.play()
    
    
    background = pygame.image.load("Fotos\Start Screen.png").convert()
    
    game_title = constants.SaiyanFont.render("Satan World Hero", True, constants.WHITE, None)
    press_start = constants.BitFont.render("Press ENTER", False, constants.WHITE)

    instart = True

    while instart:
        
        screen1 = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        screen1.blit(background, (0,0))
        game_title_rect = game_title.get_rect()
        game_title_rect.center = (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 600)
        screen1.blit(game_title, game_title_rect)
        press_start_rect = press_start.get_rect()
        press_start_rect.center = (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 150)
        screen1.blit(press_start, press_start_rect)
        pygame.display.update()
        
        for event in pygame.event.get():
            
            pressed = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit() 
            if event.type == pygame.KEYDOWN:
                if ((pressed[pygame.K_LALT] and pressed[pygame.K_F4])):
                    pygame.quit() 
                    
                elif pressed[pygame.K_RETURN]:
                    pygame.mixer.music.stop()
                    instart = False 
                else:
                    #ERRROU
                    Music_Sounds.Errou.play()
                    """pygame.mixer.music.load("Music\Fausto.mp3")
                    pygame.mixer.music.play()"""
                    pygame.display.update()
                    pygame.event.wait()
                    
        
def Pause():
    
    background = pygame.image.load("Fotos\Start Screen.png").convert()
    press_start = constants.BitFont.render("Pause", True, constants.WHITE, None)
    
    instart = True
    
    while instart:
        
        screen1 = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        screen1.blit(background, (0,0))
        press_start_rect = press_start.get_rect()
        press_start_rect.center = (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT/2)
        screen1.blit(press_start, press_start_rect)
        pygame.display.update()
        
        
        for event in pygame.event.get():
            
            pressed = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit() 
            if event.type == pygame.KEYDOWN:
                if ((pressed[pygame.K_LALT] and pressed[pygame.K_F4])):
                    pygame.quit() 
                    
                elif pressed[pygame.K_RETURN]:
                    instart = False
    


 
 
