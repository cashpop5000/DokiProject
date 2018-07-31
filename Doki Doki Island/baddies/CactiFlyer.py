""" The cactus flyer - Enemy

Imports:
    pygame: Tools to be used for sprite
    spritesheet_functions: Allows use for custom sprites
    random: Used to randomnly place the cactus as it spawns

Class:
    Flyer: The main body of the enemy


"""


import pygame
import constants as constants
from spritesheet_functions import SpriteSheet
from random import randint


class Flyer(pygame.sprite.Sprite):

    """
    Functions:
        __init__
        update
    """

    def __init__(self, player):

        """
        :param player:  The player object

        This initializes the flyer


        Variables:
            self.fly_frames: A list to hold the custom sprites for animation
            self.player: The player object
            sprite_sheet: The spritesheet to where the custom spries came from
            image: Holds the custom
            self.image: The sprite used to represent the flyer
            self.rect: This creates the shape of the sprite
            self.rect.x: The x-position of the sprite
            self.rect.y: The y-position of the sprite

        """

        super().__init__()


        #Flying frames
        self.fly_frames = []

        #The player themselves
        self.player = player

        pygame.sprite.Sprite.__init__(self)

        #Loads in spritesheet
        sprite_sheet = SpriteSheet("Terrain.png")

        #Appends sprites to list and used
        image = sprite_sheet.get_image(614, 1579, 109, 64)
        self.fly_frames.append(image)
        self.image = image
        self.rect = self.image.get_rect()

        image = sprite_sheet.get_image(739, 1579, 109, 64)
        self.fly_frames.append(image)

        #Sets initial spot
        self.rect.x = randint(0, 850)
        self.rect.y = -30


        # List of sprites we can bump against


    def update(self, cacti):

        """ Follows the player
        :param cacti: The group this sprite is in

        This updates the flyer accordingly during the game

        playhit: Checks if the sprite touches the player
        bullet_hit: Checks if the sprite was hit by a bullet
        frame: Chooses the sprite based on its position to be used for animation

        """


        #Checks if player is hit
        playhit = pygame.sprite.spritecollide(self.player, cacti, False)

        #If player is hit, makes player hurt
        if len(playhit) > 0:
            print('got em')
            if not self.player.hurt:
                self.player.hurt = True
                self.player.hp -= 10
                self.player.getHit = True

        #Checks to see if hit by bullets
        bullet_hit = pygame.sprite.spritecollide(self, self.player.bullets, True)

        #Removes bullet that hit
        for bul in bullet_hit:
            self.player.bullets.remove(bul)

        #Removes self if hit
        if len(bullet_hit):
            print('OUCH')
            cacti.remove(self)

        #Sets the sprites as it flies
        frame = (self.rect.x // 30) % len(self.fly_frames)
        self.image = self.fly_frames[frame]



        #Follows the player around

        if self.player.rect.x + 7 < self.rect.x:
            self.rect.x -= 1

        elif self.player.rect.x + 7 > self.rect.x:
            self.rect.x += 1

        if self.player.rect.y + 10 < self.rect.y:
            self.rect.y -= 1

        elif self.player.rect.y + 10 > self.rect.y:
            self.rect.y += 1






















