import pygame


class SpriteSheet(object):
    """ Classe para tirar uma imagem de um sprite sheet. """
 
    def __init__(self, file_name):
        """ Construtor. Carrega a imagem do sprite sheet. """
 
        self.sprite_sheet = pygame.image.load(file_name).convert()
  
    def get_image(self, x, y, width, height,colorkey = None):
        """ Pega uma única imagem do sprite sheet através das coord.
            x e y do sprit sheet e da largura e altura da imagem. """
 
        # Cria uma superfície em branco
        image = pygame.Surface([width, height]).convert()
 
        # Copia 
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
