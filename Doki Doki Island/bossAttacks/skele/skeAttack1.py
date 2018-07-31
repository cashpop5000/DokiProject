""" The first skeleton attack

Imports:
    pygame: Tools to be used for sprite
    spritesheet_functions: Allows use for custom sprites
    constants: For screen height and width
    Scarab The attack to go along with the quicksand

Class:
    QuickS: The main body of the sprite

"""


import pygame

import constants as constants
from baddies import Scarab as Scarab
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
            self.bugs: The group to hold the attack
            self.makeBugs: Allows to make the attack sprites
            self.GoAway: When attack finishes, allows quicksand to retract
            self.bugAmount: The amount of attacks spawned
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

        self.bugs = pygame.sprite.Group()
        self.makeBugs = False

        self.GoAway = False
        self.bugAmount = 0

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

        self.bugs.update(self.bugs)

        if self.rect.y >= 0 and not self.GoAway:
            self.rect.y -= 6

        if self.rect.y <= 0 and not self.makeBugs and not self.GoAway:
            self.spawnTime += 1

        if self.spawnTime >= 200:
            self.makeBugs = True
            self.spawnTime = 45


        if self.makeBugs:
            self.makeBugs = False
            bug = Scarab.Scarab(self.player)
            self.bugs.add(bug)
            self.bugAmount += 1

        if self.bugAmount == 8:
            self.GoAway = True

        if self.GoAway and len(self.bugs) <= 0:
            self.rect.y += 6


        if len(self.bugs) <= 0 and self.rect.y >= 800 and self.GoAway:
            print('delete')
            sand.remove(self)

    def draw(self, screen):

        """ Draws the quicksand

        :param screen: The display of the window


        """
        self.bugs.draw(screen)






