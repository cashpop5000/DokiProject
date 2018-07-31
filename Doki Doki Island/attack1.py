import pygame
import constants as constants


class Hammer(pygame.sprite.Sprite):

    def __init__(self, player):

        super().__init__()

        width = 10
        height = 55

        self.player = player

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

        self.rect.y = player.rect.y




    def update(self):

        if self.dir == 'r':
            self.rect.x = self.player.rect.x + 60
        elif self.dir == 'l':
            self.rect.x = self.player.rect.x - 30
        self.rect.y = self.player.rect.y






