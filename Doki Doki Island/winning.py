""" The win message
Imports:
    pygame: Tools to be used for sprite
    spritesheet_functions: Allows use for custom sprites

Class:
    win: The main body of the message

"""


import pygame
from random import randint

import constants as constants
from bossAttacks.golem import golAttack1 as FirstAtt
from bossAttacks.golem import golAttack2 as SecondAtt
from bossAttacks.golem import golAttack3 as ThirdAtt
from bossAttacks.golem import golAttack4 as FourthAtt
from spritesheet_functions import SpriteSheet


class win(pygame.sprite.Sprite):


    def __init__(self):


        """
        This initializes the boss


        Variables:

            sprite_sheet: The spritesheet to where the custom sprites came from
            image: Holds the custom
            self.image: The sprite used to represent
            self.rect: This creates the shape of the sprite
            self.rect.x: The x-position of the sprite
            self.rect.y: The y-position of the sprite
            self.change_y: Changes the y-position of the message
            self.bounce: Allows message to bounce
            self.count: Determines how long the message stays on screen
            self.beginCount: True once win message stops bouncing, begins countdown


        """


        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("Golem.png")

        image = sprite_sheet.get_image(262, 471, 272, 47)
        self.image = image

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        # Set a referance to the image rect.
        self.rect = self.image.get_rect()

        self.rect.x = 400
        self.rect.y = -47

        self.change_y = 0
        self.bounce = 0


        self.count = 0
        self.beginCount = False

    def update(self):

        """
        Bounces the win message when player wins
        Goes away when time is up

        """

        if self.rect.y < 320:
            self.change_y += 1
        elif self.rect.y >= 320 and self.bounce < 5:
            if self.bounce == 0:
                self.change_y = -8
                self.bounce += 1

            elif self.bounce == 1:
                self.change_y = -6
                self.bounce += 1

            elif self.bounce == 2:
                self.change_y = -4
                self.bounce += 1

            elif self.bounce == 3:
                self.change_y = -2
                self.bounce += 1

            elif self.bounce == 4:
                self.change_y = 0
                self.bounce += 1
                self.beginCount = True

        if self.beginCount:
            self.count += 1


        if self.count >= 90:
            self.change_y += 1



        self.rect.y += self.change_y







