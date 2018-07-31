""" The black transition screen

Imports:
    pygame: Tools to be used for sprite
    constants: For screen height and width


Class:
    Fade: The main body of the cover

"""


import pygame
import constants as constants
from spritesheet_functions import SpriteSheet

class Fade(pygame.sprite.Sprite):

    def __init__(self, screen):

        """

        :param screen: display window
        Initializes the cover

        Variables:

            sprite_sheet: The spritesheet to where the custom spries came from
            image: Holds the custom
            self.image: The sprite used to represent
            self.rect: This creates the shape of the sprite
            self.rect.x: The x-position of the sprite
            self.rect.y: The y-position of the sprite
            self.time: The opacity of the sprite
            self.go: Determines when the cover should begin fading
            self.inout: Determines if cover is fading in or out

        """

        super().__init__()

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface(screen.get_size())
        self.image = self.image.convert()
        self.image.fill(constants.BLACK)

        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = 0

        self.time = 255
        self.go = True
        self.inout = False


    def draw(self, screen):

        """

        :param screen: Display window
        Draws the cover

        """
        screen.blit(self.image, (self.rect.x, self.rect.y))


    def update(self):

        """ Updates the cover during transitions


        """

        if self.go:
            if not self.inout:
                self.time -= 5
                self.image.set_alpha(self.time)
            elif self.inout and self.time < 255:
                self.time += 5
                self.image.set_alpha(self.time)



