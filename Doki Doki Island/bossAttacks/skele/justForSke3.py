""" Used as skeleton's thrid attack

Imports:
    pygame: Tools to be used for sprite
    spritesheet_functions: Allows use for custom sprites
    constants: For screen height and width
    random: Used for random numbers

Class:
    SandPush: The main body of the enemy

"""



import pygame
import constants as constants
from spritesheet_functions import SpriteSheet
from random import randint


class SandPush(pygame.sprite.Sprite):

    """
    Functions:
        __init__
        update
    """


    def __init__(self, player):

        """
        :param player:  The player object

        This initializes the sandpush


        Variables:

            self.player: The player object
            self.direction: The direcion the sprite faces
            pieceOne: The right side sprite
            pieceTwo: The left side sprite
            pieceThree: The top side sprite
            pieceFour: The bottom side sprite
            self.spawnTime: The amount of time the sprite  will stay on screen
            self.move: Allows sprite to move
            sprite_sheet: The spritesheet to where the custom spries came from
            image: Holds the custom
            self.image: The sprite used to represent
            self.rect: This creates the shape of the sprite
            self.rect.x: The x-position of the sprite
            self.rect.y: The y-position of the sprite
            selection: Randomly chooses the direction of the sprite
            selectSpot: The random spot placed based off the direction of the sprite


        """

        super().__init__()

        self.player = player
        self.direction = ''


        pygame.sprite.Sprite.__init__(self)

        #Right
        pieceOne = [994, 1022, 158, 101]

        #Left
        pieceTwo = [1012, 1152, 158, 101]

        #Top
        pieceThree = [874, 1012, 101, 158]

        #Bot
        pieceFour = [874, 1214, 101, 158]

        selection = randint(0,3)
        selectSpot = randint(0,2)

        sprite_sheet = SpriteSheet("Terrain.png")

        if selection == 0:

            image = sprite_sheet.get_image(pieceOne[0], pieceOne[1], pieceOne[2], pieceOne[3])
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x = -158
            self.direction = 'r'

            if selectSpot == 0:
                self.rect.y = 30
            elif selectSpot == 1:
                self.rect.y = 305
            elif selectSpot == 2:
                self.rect.y = 600


        elif selection == 1:

            image = sprite_sheet.get_image(pieceTwo[0], pieceTwo[1], pieceTwo[2], pieceTwo[3])
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x = constants.SCREEN_WIDTH
            self.direction = 'l'

            if selectSpot == 0:
                self.rect.y = 25
            elif selectSpot == 1:
                self.rect.y = 305
            elif selectSpot == 2:
                self.rect.y = 600



        elif selection == 2:

            image = sprite_sheet.get_image(pieceThree[0], pieceThree[1], pieceThree[2], pieceThree[3])
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.y = constants.SCREEN_HEIGHT
            self.direction = 't'

            if selectSpot == 0:
                self.rect.x = 35
            elif selectSpot == 1:
                self.rect.x = 450
            elif selectSpot == 2:
                self.rect.x = 870




        elif selection == 3:
            image = sprite_sheet.get_image(pieceFour[0], pieceFour[1], pieceFour[2], pieceFour[3])
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.y = -158
            self.direction = 'b'

            if selectSpot == 0:
                self.rect.x = 35
            elif selectSpot == 1:
                self.rect.x = 450
            elif selectSpot == 2:
                self.rect.x = 870


        self.spawnTime = 0
        self.move = False


    def update(self, sandStone):

        """ Sand sprite will appear at a direction in the quicksand and move towards to the other end
        :param sandStone: The group this sprite is in

        This updates the punch accordingly during the game

        hit_player: Checks if the sprite touches the player


        """

        hit_player = pygame.sprite.spritecollide(self.player, sandStone, False)

        if len(hit_player) > 0:
            print('got em')
            if not self.player.hurt:
                self.player.hurt = True
                self.player.hp -= 10
                self.player.getHit = True

        if not self.move:
            self.spawnTime += 1

        if self.spawnTime == 45:
            self.move = True

        if self.move:
            if self.direction == 'r':
                if self.rect.x >= constants.SCREEN_WIDTH:
                    sandStone.remove(self)
                else:
                    self.rect.x += 5

            elif self.direction == 'l':
                if self.rect.x <= -158:
                    sandStone.remove(self)
                else:
                    self.rect.x -= 5

            elif self.direction == 't':
                if self.rect.y <= 0:
                    sandStone.remove(self)
                else:
                    self.rect.y -= 5

            else:
                if self.rect.y >= constants.SCREEN_HEIGHT:
                    sandStone.remove(self)
                else:
                    self.rect.y += 5

