import pygame
import constants as constants


class Laser(pygame.sprite.Sprite):

    def __init__(self, player):

        super().__init__()

        width = 100
        height = 10
        self.image = pygame.Surface([width, height])
        self.image.fill(constants.WHITE)

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()

        if player.direction == 'r':
            self.rect.x = player.rect.x + 60
            self.dir = 'r'
        elif player.direction == 'l':
            self.rect.x = player.rect.x - 120
            self.dir = 'l'

        self.rect.y = player.rect.y + 20


    def update(self, player):

        if self.dir == 'r':
            self.rect.x = player.rect.x + 60
        elif self.dir == 'l':
            self.rect.x = player.rect.x - 120
        self.rect.y = player.rect.y + 20









