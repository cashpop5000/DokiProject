""" The scarab - Enemy

Imports:
    pygame: Tools to be used for sprite
    constants: For screen ehight and width
    spritesheet_functions: Allows use for custom sprites
    random: Used to randomnly place the cactus as it spawns

Class:
    Scarab: The main body of the enemy


"""


import pygame
import constants as constants
import levels as levels
from spritesheet_functions import SpriteSheet
from random import randint


class Scarab(pygame.sprite.Sprite):

    """
    Functions:
        __init__
        update
    """


    def __init__(self, player):

        """
        :param player:  The player object

        This initializes the scarab


        Variables:
            self.LRframes: A list to hold the custom sprites for animation when going right or left
            self.LRframes: A list to hold the custom sprites for animation when going top or bottom
            self.player: The player object
            sprite_sheet: The spritesheet to where the custom spries came from
            image: Holds the custom
            self.image: The sprite used to represent the flyer
            self.rect: This creates the shape of the sprite
            self.rect.x: The x-position of the sprite
            self.rect.y: The y-position of the sprite
            selection: A random int to select the direction the scarab faces
            selectSpot: Selects where to place the scarab based on its direction
            self.distance: How far the scarab will go before turning around
            self.oriDistance: To set the distance when scarab reaches the end of its patrol
            self.direction: The facing direction of the scarab

        """

        super().__init__()

        #Frames
        self.LRframes = []
        self.TBframes = []

        #Selects what spot the scarab will be placed in
        selection = randint(0,3)
        selectSpot = randint(0,2)

        #Sets how far the scarab will crawl
        self.distance = 0
        self.oriDistance = 0
        self.direction = ''


        pygame.sprite.Sprite.__init__(self)

        #Load sheet
        sprite_sheet = SpriteSheet("Skeleton.png")


        #Right
        image = sprite_sheet.get_image(46, 11, 78, 61)
        self.LRframes.append(image)

        #Left
        image = sprite_sheet.get_image(351, 10, 78, 61)
        self.LRframes.append(image)

        #Top
        image = sprite_sheet.get_image(160, 5, 61, 78)
        self.TBframes.append(image)

        #Bottom
        image = sprite_sheet.get_image(252, 6, 61, 78)
        self.TBframes.append(image)

        self.image = image
        self.rect = self.image.get_rect()

        #Sets the scarab based on previous int variables
        if selection == 0:

            image = self.LRframes[0]
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x = 30
            self.direction = 'r'

            if selectSpot == 0:
                self.rect.y = 35
            elif selectSpot == 1:
                self.rect.y = 315
            elif selectSpot == 2:
                self.rect.y = 600

            self.distance = 900
            self.oriDistance = 900


        elif selection == 1:

            image = self.LRframes[1]
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x = constants.SCREEN_WIDTH - 108
            self.direction = 'l'

            if selectSpot == 0:
                self.rect.y = 35
            elif selectSpot == 1:
                self.rect.y = 315
            elif selectSpot == 2:
                self.rect.y = 600

            self.distance = 900
            self.oriDistance = 900



        elif selection == 2:
            image = self.TBframes[0]
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.y = constants.SCREEN_HEIGHT - 108
            self.direction = 't'

            if selectSpot == 0:
                self.rect.x = 40
            elif selectSpot == 1:
                self.rect.x = 470
            elif selectSpot == 2:
                self.rect.x = 895

            self.distance = 620
            self.oriDistance = 620


        elif selection == 3:
            image = self.TBframes[1]
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.y = 35
            self.direction = 'b'

            if selectSpot == 0:
                self.rect.x = 40
            elif selectSpot == 1:
                self.rect.x = 470
            elif selectSpot == 2:
                self.rect.x = 895

            self.distance = 620
            self.oriDistance = 620


        self.player = player

    def update(self, bugs):


        """ Moves in a patrol back and forth in a line
        :param bugs: The group this sprite is in

        This updates the scarab accordingly during the game

        playhit: Checks if the sprite touches the player
        bullet_hit: Checks if the sprite was hit by a bullet


        """

        #Checks if touch player
        playhit = pygame.sprite.spritecollide(self.player, bugs, False)

        #If player touch, hurt player
        if len(playhit) > 0:
            print('got em')
            if not self.player.hurt:
                self.player.hurt = True
                self.player.hp -= 10
                self.player.getHit = True

        #Checks if self touch bullets, then removes it
        bullet_hit = pygame.sprite.spritecollide(self, self.player.bullets, True)
        for bul in bullet_hit:
            self.player.bullets.remove(bul)

        #Removes self if hit by bullets
        if len(bullet_hit):
            print('OUCH')
            bugs.remove(self)


        #Checks distance, changes direction and sprite if hit distance limit

        self.distance -= 5

        if self.distance <= 0:
            if self.direction == 'r':
                self.direction = 'l'
                image = self.LRframes[1]
                self.image = image

            elif self.direction == 'l':
                self.direction = 'r'
                image = self.LRframes[0]
                self.image = image

            elif self.direction == 't':
                self.direction = 'b'
                image = self.TBframes[1]
                self.image = image

            else:
                self.direction = 't'
                image = self.TBframes[0]
                self.image = image


            self.distance = self.oriDistance


        #Moves scarab
        if self.direction == 'r':
            self.rect.x += 5
        elif self.direction == 'l':
            self.rect.x -= 5
        elif self.direction == 't':
            self.rect.y -= 5
        else:
            self.rect.y += 5













