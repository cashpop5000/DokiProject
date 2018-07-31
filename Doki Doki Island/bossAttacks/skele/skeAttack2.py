""" The second skeleton attack

Imports:
    pygame: Tools to be used for sprite
    spritesheet_functions: Allows use for custom sprites
    constants: For screen height and width
    CactiFlyer: The attack to go along with the quicksand

Class:
    QuickS: The main body of the sprite

"""

import pygame

import constants as constants
from baddies import CactiFlyer as CactiFlyer
from spritesheet_functions import SpriteSheet

class QuickS(pygame.sprite.Sprite):

    def __init__(self, player, skeleton):

        """
        :param player:  The player object

        This initializes the quicksand


        Variables:

            self.player: The player object
            self.spawnTime: The amount of time the punch will stay on screen
            self.screen: The display of the window
            self.cacti: The group to hold the attack
            self.makeCacti: Allows to make the attack sprites
            self.GoAway: When attack finishes, allows quicksand to retract
            self.cacAmount: The amount of attacks spawned
            sprite_sheet: The spritesheet to where the custom spries came from
            image: Holds the custom
            self.image: The sprite used to represent
            self.rect: This creates the shape of the sprite
            self.rect.x: The x-position of the sprite
            self.rect.y: The y-position of the sprite


        """

        super().__init__()

        self.player = player
        self.screen = None

        self.cacti = pygame.sprite.Group()
        self.makeCacti = False

        self.GoAway = False
        self.cacAmount = 0


        self.spawnTime = 0

        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("RoomOfQuickSand.png")

        image = sprite_sheet.get_image(0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        self.image = image
        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = 800

    def update(self, sand):

        """ The quicksand rises, then spawns the attacks, retracts once attack is finished
        :param sand: The group this sprite is in

        This updates the quicksand and attacks accordingly during the game

        hit_player: Checks if the sprite touches the player


        """

        self.cacti.update(self.cacti)



        if self.rect.y >= 0 and not self.GoAway:
            self.rect.y -= 6

        if self.rect.y <= 0 and not self.makeCacti and not self.GoAway:
            self.spawnTime += 1

        if self.spawnTime >= 135:
            self.makeCacti = True
            self.spawnTime = 35


        if self.makeCacti:
            print('make cactus')
            self.makeCacti = False
            cact = CactiFlyer.Flyer(self.player)
            self.cacti.add(cact)
            self.cacAmount += 1

        if self.cacAmount == 5:
            self.GoAway = True

        if self.GoAway and len(self.cacti) <= 0:
            self.rect.y += 6


        if len(self.cacti) <= 0 and self.rect.y >= 800 and self.GoAway:
            print('delete')
            sand.remove(self)

    def draw(self, screen):

        """ Draws the quicksand

        :param screen: The display of the window


        """
        self.cacti.draw(screen)






