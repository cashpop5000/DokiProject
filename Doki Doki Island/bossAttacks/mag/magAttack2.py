""" The second magma attack

Imports:
    pygame: Tools to be used for sprite
    spritesheet_functions: Allows use for custom sprites
    constants: For screen height and width
    random: Used for random numbers

Class:
    RockDown: The main body of the enemy

"""

import pygame
import constants as constants
from spritesheet_functions import SpriteSheet
from random import randint

class RockDown(pygame.sprite.Sprite):

    def __init__(self, player):

        """
        :param player:  The player object

        This initializes the boulder


        Variables:

            self.player: The player object
            self.spawnTime: The amount of time the punch will stay on screen
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
            self.change_y: Affects the gravity of the boulder


        """

        super().__init__()

        self.player = player

        self.spawnTime = 0
        self.disappear = False

        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("Lava.png")

        image = sprite_sheet.get_image(547, 252, 133, 133)
        self.image = image
        self.rect = self.image.get_rect()


        spot = randint(0,2)

        if spot == 0:
            spotChose = 70
        elif spot == 1:
            spotChose = 410
        elif spot == 2:
            spotChose = 745


        self.rect.x = spotChose
        self.rect.y = -133

        self.change_y = 0

    def update(self, attacks):

        """ A rock will fall from the top towards the lava

        :param attacks: The group this sprite is in

        This updates the boulder accordingly during the game

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


        if self.spawnTime >= 45:
            self.change_y += 0.7

        self.spawnTime += 1

        self.rect.y += self.change_y


        if self.rect.y >= constants.SCREEN_HEIGHT:
            print('delete rock')
            attacks.remove(self)








