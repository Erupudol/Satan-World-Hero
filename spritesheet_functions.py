"""
This module is used to pull individual sprites from sprite sheets.
"""
import pygame
import constants
 

def createSprite(sprite_sheet,lista,doFlip=0,trans=0):
    lista_2=[]
    for item in lista:
        image =  sprite_sheet.get_image(item[0],item[1],item[2],item[3],item[4])
        if doFlip:
            image = pygame.transform.flip(image,True,False)
        if trans :
            image = pygame.transform.scale2x(image) 
        lista_2.append(image)
    return lista_2
    
            
class SpriteSheet(object):
    """ Class used to grab images out of a sprite sheet. """
 
    def __init__(self, file_name):
        """ Constructor. Pass in the file name of the sprite sheet. """
 
        # Load the sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert()
 
 
    def get_image(self, x, y, width, height,colorkey = None):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """
 
        # Create a new blank image
        image = pygame.Surface([width, height]).convert()
 
        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
 
        # Assuming black works as the transparent color
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            elif type(colorkey) not in (pygame.Color,tuple,list):
                colorkey = image.get_at((colorkey,colorkey))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
 
        # Return the image
        return image