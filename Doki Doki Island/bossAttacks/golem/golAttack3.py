""" The third golem attack

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
        self.spawnTime = 0

        self.disappear = False

        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("Golem.png")

        image = sprite_sheet.get_image(29, 11, 101, 319)
        self.image = image
        self.rect = self.image.get_rect()

        self.rect.x = player.rect.x
        self.rect.y = -319

    def update(self, attacks):

        """ A punch will come from the top towards the bottom, will retract and disappear
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

        if 45 <= self.spawnTime <= 105 and self.rect.y <= constants.SCREEN_HEIGHT:
            self.rect.y += 15

        if self.spawnTime >= 135:
            self.disappear = True
            self.rect.y -= 6

        self.spawnTime += 1

        if self.disappear and self.rect.y <= -319:
            attacks.remove(self)








