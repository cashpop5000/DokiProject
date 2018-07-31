""" Player's second attack, shoots bullets

Imports:
    pygame: Tools to be used for sprite
    constants: For screen height and width


Class:
    Shooter: The main body of the attack

"""

import pygame
import constants as constants


class Shooter(pygame.sprite.Sprite):

    def __init__(self, player):

        """
        This initializes the attack

        :param player:

        Variables:
            width: The width of the bullet
            height: The height of the bullet
            self.image: The sprite used to represent
            self.rect: This creates the shape of the sprite
            self.rect.x: The x-position of the sprite
            self.rect.y: The y-position of the sprite
            self.move: How fast the bullet moves
            self.limit: How long before the bullet disappears
            self.level: Used so the bullet can collide with enemies

        """

        super().__init__()


        width = 15
        height = 15
        self.image = pygame.Surface([width, height])
        self.image.fill(constants.WHITE)

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()

        if player.direction == 'r':
            self.rect.x = player.rect.x + 60
            self.dir = 'r'
        elif player.direction == 'l':
            self.rect.x = player.rect.x - 30
            self.dir = 'l'

        self.rect.y = player.rect.y + 20

        self.move_x = 5

        self.limit = 0

        self.level = None


    def update(self, bullets):

        """ After being shot, flies from the player at a direction

        updates the bullet accordingly in game

        :param bullets: the group the sprite is in

        Variables:
            hitBoss: Checks if bullets hits a boss
            hitBeBoss: Checks if bullets hit a boss


        """

        hitBoss = pygame.sprite.spritecollide(self, self.level.boss_man, False)
        hitBeBoss = pygame.sprite.spritecollide(self, self.level.behind_boss_man, False)

        if len(hitBoss) > 0 or len(hitBeBoss) > 0:

            for smack in hitBoss:
                smack.hp -= 10
            for smack in hitBeBoss:
                smack.hp -= 10


            bullets.remove(self)

        self.limit += 1

        if self.dir == 'r':
            self.rect.x += 5
        elif self.dir == 'l':
            self.rect.x -= 5

        if self.limit >= 90 or self.rect.x >= constants.SCREEN_WIDTH - 20 or self.rect.x <= 20:
            bullets.remove(self)










