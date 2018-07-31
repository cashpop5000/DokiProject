""" The fourth golem attack

Imports:
    pygame: Tools to be used for sprite
    spritesheet_functions: Allows use for custom sprites


Variables:
    BIG_CIRC = list of coords for a sprite
    MED_CIRC = list of coords for a sprite
    SMA_CIRC = list of coords for a sprite
    BIG_BEAM = list of coords for a sprite
    MED_BEAM = list of coords for a sprite
    SMA_BEAM = list of coords for a sprite

Class:
    Laser: The main body of the enemy

"""


import pygame
import constants as constants
from spritesheet_functions import SpriteSheet


BIG_CIRC = [619, 234, 34, 33]
MED_CIRC = [577, 236, 26, 26]
SMA_CIRC = [537, 241, 16, 16]

BIG_BEAM = [56, 918, 479, 33]
MED_BEAM = [56, 887, 479, 23]
SMA_BEAM = [56, 870, 479, 9]




class Laser(pygame.sprite.Sprite):

    def __init__(self, player, golem):

        """
        :param player:  The player object
        :param golem:  The golem object

        This initializes the laser


        Variables:

            self.player: The player object
            self.golem: The golem object
            self.lazeroz: Holds the custom sprites
            self.spawnTime: The amout of time the punch will stay on screen
            sprite_sheet: The spritesheet to where the custom spries came from
            image: Holds the custom
            self.image: The sprite used to represent
            self.rect: This creates the shape of the sprite
            self.rect.x: The x-position of the sprite
            self.rect.y: The y-position of the sprite
            self.oriX: The original x-position of the laser once it changes form


        """


        super().__init__()

        self.lazeroz = []

        self.player = player
        self.golem = golem

        self.spawnTime = 0

        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("Golem.png")

        image = sprite_sheet.get_image(BIG_CIRC[0], BIG_CIRC[1], BIG_CIRC[2], BIG_CIRC[3])
        self.image = image
        self.rect = self.image.get_rect()
        self.lazeroz.append(image)

        image = sprite_sheet.get_image(MED_CIRC[0], MED_CIRC[1], MED_CIRC[2], MED_CIRC[3])
        self.lazeroz.append(image)

        image = sprite_sheet.get_image(SMA_CIRC[0], SMA_CIRC[1], SMA_CIRC[2], SMA_CIRC[3])
        self.lazeroz.append(image)

        image = sprite_sheet.get_image(SMA_BEAM[0], SMA_BEAM[1], SMA_BEAM[2], SMA_BEAM[3])
        self.lazeroz.append(image)

        image = sprite_sheet.get_image(MED_BEAM[0], MED_BEAM[1], MED_BEAM[2], MED_BEAM[3])
        self.lazeroz.append(image)

        image = sprite_sheet.get_image(BIG_BEAM[0], BIG_BEAM[1], BIG_BEAM[2], BIG_BEAM[3])
        self.lazeroz.append(image)

        self.rect.x = golem.rect.x
        self.oriX = golem.rect.x

        self.rect.y = golem.rect.y + 131

    def update(self, attacks):

        """ will fire a lasor from the golem's eyes, increasing in size than disappearing
        :param attacks: The group this sprite is in

        This updates the laser accordingly during the game

        hit_player: Checks if the sprite touches the player


        """

        hit_player = pygame.sprite.spritecollide(self.player, attacks, False)

        if len(hit_player) > 0:
            print('got em')
            if not self.player.hurt:
                self.player.hurt = True
                self.player.hp -= 10
                self.player.getHit = True


        self.rect.y = self.golem.rect.y + 131

        if self.spawnTime == 30:
            image = self.lazeroz[1]
            self.image = image

        if self.spawnTime == 45:
            image = self.lazeroz[2]
            self.image = image

        if self.spawnTime == 60:
            image = self.lazeroz[3]
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.y = self.golem.rect.y + 131
            self.rect.x = self.oriX - 479

        if self.spawnTime == 100:
            image = self.lazeroz[4]
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.y = self.golem.rect.y + 131
            self.rect.x = self.oriX - 479

        if self.spawnTime == 140:
            image = self.lazeroz[5]
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.y = self.golem.rect.y + 131
            self.rect.x = self.oriX - 479


        self.spawnTime += 1

        if self.spawnTime >= 230:
            attacks.remove(self)








