""" The background for the title screen

Imports:
    pygame: Tools to be used for sprite
    spritesheet_functions: Allows use for custom sprites


Class:
    Start: The main body of the background

"""

import pygame
import constants as constants
from spritesheet_functions import SpriteSheet

class Start(pygame.sprite.Sprite):

    def __init__(self):

        """
        Initializes the background

        Variables:

            sprite_sheet: The spritesheet to where the custom spries came from
            image: Holds the custom
            self.image: The sprite used to represent
            self.rect: This creates the shape of the sprite
            self.rect.x: The x-position of the sprite
            self.rect.y: The y-position of the sprite

        """

        super().__init__()

        pygame.sprite.Sprite.__init__(self)

        self.sprite_sheet = SpriteSheet("backTitle.png")

        image = self.sprite_sheet.get_image(0, 0, 1000, 700)

        self.image = image

        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = 0


    def draw(self, screen):
        """ drwas the background

        :param screen: Display window

        """
        screen.blit(self.image, (self.rect.x, self.rect.y))

