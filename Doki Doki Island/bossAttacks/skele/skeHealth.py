""" The skeleton health

Imports:
    pygame: Tools to be used for sprite
    spritesheet_functions: Allows use for custom sprites

Class:
    ske: The main health

"""


import pygame
from random import randint

import constants as constants
from spritesheet_functions import SpriteSheet


class Ske(pygame.sprite.Sprite):


    def __init__(self):

        """
        This initializes the health


        Variables:
            self.status: Holds the custom sprites
            sprite_sheet: The spritesheet to where the custom spries came from
            image: Holds the custom
            self.image: The sprite used to represent
            self.rect: This creates the shape of the sprite
            self.rect.y: The y-position of the sprite
            self.hp: The hp of the boss
            self.change: Allows hp bar to appear if quicksand is retracted

        """

        self.status = []

        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("Golem.png")

        image = sprite_sheet.get_image(165, 547, 389, 28)
        self.status.append(image)
        self.image = image
        self.rect = self.image.get_rect()

        image = sprite_sheet.get_image(165, 576, 389, 28)
        self.status.append(image)

        image = sprite_sheet.get_image(165, 608, 389, 28)
        self.status.append(image)

        image = sprite_sheet.get_image(165, 642, 389, 28)
        self.status.append(image)

        image = sprite_sheet.get_image(165, 678, 389, 28)
        self.status.append(image)

        image = sprite_sheet.get_image(165, 708, 389, 28)
        self.status.append(image)

        image = sprite_sheet.get_image(165, 742, 389, 28)
        self.status.append(image)

        image = sprite_sheet.get_image(165, 774, 389, 28)
        self.status.append(image)

        image = sprite_sheet.get_image(165, 802, 389, 28)
        self.status.append(image)

        self.hp = 1000

        self.rect.y = -30
        self.rect.x = 50
        self.change = False


    def update(self, current):

        """ Places the hp bar
        :param current: The current hp of the boss

        Updates the health as the battle goes on, changing sprites based on health

        """


        self.hp = current

        if self.change:

            if self.hp <= 0:
                self.image = self.status[8]

            if 0 < self.hp < 100:
                self.image = self.status[7]

            if 100 <= self.hp < 250:
                self.image = self.status[6]

            if 250 <= self.hp < 450:
                self.image = self.status[5]

            if 450 <= self.hp < 600:
                self.image = self.status[4]

            if 600 <= self.hp < 750:
                self.image = self.status[3]

            if 750 <= self.hp < 850:
                self.image = self.status[2]

            if 850 <= self.hp < 1000:
                self.image = self.status[1]

            if 1000 <= self.hp:
                self.image = self.status[0]


        if self.rect.y <= 30:
            self.rect.y += 4

        if self.rect.y >= 30:
            self.change = True







