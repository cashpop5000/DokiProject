""" The first golem attack

Imports:
    pygame: Tools to be used for sprite
    spritesheet_functions: Allows use for custom sprites
    constants: For screen height and width

Class:
    Punch: The main body of the enemy

"""



import pygame
import constants as constants
from spritesheet_functions import SpriteSheet

class Punch(pygame.sprite.Sprite):

    """
    Functions:
        __init__
        update
    """

    def __init__(self, player):

        """
        :param player:  The player object

        This initializes the punch


        Variables:

            self.player: The player object
            self.spawnTime: The amout of time the punch will stay on screen
            self.disappear: True to allow the punch to disappear
            sprite_sheet: The spritesheet to where the custom spries came from
            image: Holds the custom
            self.image: The sprite used to represent
            self.rect: This creates the shape of the sprite
            self.rect.x: The x-position of the sprite
            self.rect.y: The y-position of the sprite


        """


        super().__init__()
        self.player = player

        #Sets spawntime and disappear when needed to be removed
        self.spawnTime = 0
        self.disappear = False

        pygame.sprite.Sprite.__init__(self)

        #load sheet
        sprite_sheet = SpriteSheet("Golem.png")

        #Sets sprite
        image = sprite_sheet.get_image(212, 319, 318, 101)
        self.image = image
        self.rect = self.image.get_rect()

        #Sets attack in level with player's Y position
        self.rect.x = constants.SCREEN_WIDTH
        self.rect.y = player.rect.y

    def update(self, attacks):

        """ Punch will appear from the right and move to the left, will retract and then disappear
        :param attacks: The group this sprite is in

        This updates the punch accordingly during the game

        hit_player: Checks if the sprite touches the player


        """


        hit_player = pygame.sprite.spritecollide(self.player, attacks, False)

        if len(hit_player) > 0:
            print('got em')
            if not self.player.hurt:
                self.player.hurt = True
                self.player.hp -= 10
                self.player.getHit = True

        if self.spawnTime == 45:
            print('here i come!')


        if 45 <= self.spawnTime <= 135 and self.rect.x > 0:
            self.rect.x -= 15

        if self.spawnTime >= 165:
            self.disappear = True
            self.rect.x += 6

        self.spawnTime += 1

        if self.disappear and self.rect.x >= constants.SCREEN_WIDTH:
            attacks.remove(self)








