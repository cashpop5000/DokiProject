""" The first magma attack

Imports:
    pygame: Tools to be used for sprite
    spritesheet_functions: Allows use for custom sprites
    constants: For screen height and width
    random: Used for random numbers

Class:
    Pillar: The main body of the enemy

"""


import pygame
import constants as constants
from spritesheet_functions import SpriteSheet
from random import randint

class Pillar(pygame.sprite.Sprite):


    def __init__(self, player):

        """
        :param player:  The player object

        This initializes the pillar


        Variables:

            self.player: The player object
            self.spawnTime: The amout of time the punch will stay on screen
            self.lava_frames: Holds the custom sprites
            self.disappear: True to allow the punch to disappear
            sprite_sheet: The spritesheet to where the custom spries came from
            image: Holds the custom
            self.image: The sprite used to represent
            self.rect: This creates the shape of the sprite
            self.rect.x: The x-position of the sprite
            self.rect.y: The y-position of the sprite
            self.whichOne: Used during update to determine which frame to use for the animation
            spot: Randomly chooses which spot the pillar will appear
            spotChose: The chosen spot


        """

        super().__init__()

        self.lava_frames = []

        self.player = player

        self.spawnTime = 0
        self.disappear = False

        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("Lava.png")

        image = sprite_sheet.get_image(733, 160, 194, 342)
        self.image = image
        self.rect = self.image.get_rect()
        self.lava_frames.append(image)

        image = sprite_sheet.get_image(968, 160, 194, 342)
        self.lava_frames.append(image)

        self.whichFrame = 0

        spot = randint(0,2)

        if spot == 0:
            spotChose = 90
        elif spot == 1:
            spotChose = 410
        elif spot == 2:
            spotChose = 745


        self.rect.x = spotChose
        self.rect.y = constants.SCREEN_HEIGHT

    def update(self, attacks):

        """ A lava pillar will rise from the lava, retracts and disappear

        :param attacks: The group this sprite is in

        This updates the pillar accordingly during the game

        hit_player: Checks if the sprite touches the player


        """

        #Checks if touch player
        playhit = pygame.sprite.spritecollide(self.player, attacks, False)

        #If player touch, hurt player
        if len(playhit) > 0:
            print('got em')
            if not self.player.hurt:
                self.player.hurt = True
                self.player.hp -= 10
                self.player.getHit = True

        if self.spawnTime == 45:
            print('here i come!')


        if 364 >= self.spawnTime >= 45 and self.rect.y >= 380:
            self.rect.y -= 4

        if self.spawnTime >= 365:
            self.disappear = True
            self.rect.y += 6

        self.spawnTime += 1

        if self.spawnTime % 30 == 0:
            if self.whichFrame == 0:
                self.whichFrame = 1
                self.image = self.lava_frames[1]
            else:
                self.whichFrame = 0
                self.image = self.lava_frames[0]


        if self.disappear and self.rect.y >= constants.SCREEN_HEIGHT:
            attacks.remove(self)








