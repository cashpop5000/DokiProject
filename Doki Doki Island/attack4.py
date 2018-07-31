import pygame
import constants as constants
import math


class Wave(pygame.sprite.Sprite):

    def __init__(self, player, sign):

        super().__init__()

        self.sign = sign

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


    def update(self, bullets):
        print('yo')
        self.limit += 1

        t = pygame.time.get_ticks() / 2 % 400
        t *= self.sign
        self.rect.y = math.sin(t/50.0) * 4 + self.rect.y
        self.rect.y = int(self.rect.y)

        if self.dir == 'r':
            self.rect.x += 5
        elif self.dir == 'l':
            self.rect.x -= 5




        if self.limit >= 80:
            bullets.remove(self)










