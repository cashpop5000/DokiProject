""" The second golem attack

Imports:
    pygame: Tools to be used for sprite
    spritesheet_functions: Allows use for custom sprites
    random: Used for random numbers

Class:
    Rocket: The main body of the enemy

"""


import pygame
import constants as constants
from spritesheet_functions import SpriteSheet
from random import randint

class Rocket(pygame.sprite.Sprite):



    def __init__(self, position, player):
        """
        :param player:  The player object
        :param position:  The x-position of the player

        This initializes the rocket


        Variables:

            self.player: The player object
            self.spawnTime: The amout of time the punch will stay on screen
            whichPice: Randomly chooses a number to choose which sprite to use
            pieceOne: The first sprite
            pieceTwo: the second sprite
            pieceThree: The third sprite
            usePice: The chosen sprite to be used
            sprite_sheet: The spritesheet to where the custom spries came from
            image: Holds the custom
            self.image: The sprite used to represent
            self.rect: This creates the shape of the sprite
            self.rect.x: The x-position of the sprite
            self.rect.y: The y-position of the sprite
            self.direction: The direction of the sprite
            self.TDdirection: The direction of the sprite


        """

        super().__init__()

        self.spawnTime = 0

        self.player = player

        #Lists out rock sprites, chooses which sprite to use when initialized
        whichPice = randint(1,3)

        pieceOne = [154, 251, 34, 34]
        pieceTwo = [199, 254, 39, 33]
        pieceThree = [259, 254, 39, 34]

        if whichPice == 1:
            usePice = pieceOne
        elif whichPice == 2:
            usePice = pieceTwo
        else:
            usePice = pieceThree


        pygame.sprite.Sprite.__init__(self)

        #Load sheet
        sprite_sheet = SpriteSheet("Golem.png")

        image = sprite_sheet.get_image(usePice[0], usePice[1], usePice[2], usePice[3])
        self.image = image

        self.rect = self.image.get_rect()

        #Sets rock position
        self.rect.x = position
        self.rect.y = -10

        #Sets rock direction as it flies
        self.direction = 'r'
        self.TDdirection = 'b'

    def update(self, attacks):

        """ Follows the player
        :param attacks: The group this sprite is in

        This updates the rocket accordingly during the game

        hit_player: Checks if the sprite touches the player


        """

        #Checks if touch player, then hurts them
        hit_player = pygame.sprite.spritecollide(self.player, attacks, False)

        if len(hit_player) > 0:
            print('got em')
            if not self.player.hurt:
                self.player.hurt = True
                self.player.hp -= 10
                self.player.getHit = True
                attacks.remove(self)

        self.spawnTime += 1

        #Follows the player around
        if self.player.rect.x + 7 < self.rect.x:
            self.rect.x -= 2
            self.direction = 'l'
        elif self.player.rect.x + 7 > self.rect.x:
            self.rect.x += 2
            self.direction = 'r'


        if self.player.rect.y + 10 < self.rect.y:
            self.rect.y -= 2
            self.TDdirection = 't'
        elif self.player.rect.y + 10 > self.rect.y:
            self.rect.y += 2
            self.TDdirection = 'b'

        #Disappears when time is up
        if self.spawnTime == 400:
            attacks.remove(self)




