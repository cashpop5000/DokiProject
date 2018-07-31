import pygame
import constants as constants


class ShootCh(pygame.sprite.Sprite):

    def __init__(self, player):

        super().__init__()


        self.width = 15
        self.height = 15
        self.image = pygame.Surface([self.width, self.height])
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
        self.fly = False
        self.charge = 0
        self.change = 0


        if player.direction == 'r':
            self.rect.x = player.rect.x + 60
            self.dir = 'r'
        elif player.direction == 'l':
            self.rect.x = player.rect.x - 30
            self.dir = 'l'



    def update(self, chargeGro, player):

        if self.dir == 'r' and not self.fly:
            self.rect.x = player.rect.x + 60
        elif self.dir == 'l' and not self.fly:
            self.rect.x = player.rect.x - 30

        if not self.fly:
            self.rect.y = player.rect.y + 20


        if self.charge == 5 and self.change == 0:
            self.change = 1
            self.width += 20
            self.height += 20
            self.image = pygame.transform.scale(self.image, (self.width, self.height))

        if self.charge == 20 and self.change == 1:
            self.change = 2
            self.width += 20
            self.height += 20
            self.image = pygame.transform.scale(self.image, (self.width, self.height))

        if self.fly > 0:
            self.limit += 1

        if self.dir == 'r' and self.fly:
            self.rect.x += 5
        elif self.dir == 'l' and self.fly:
            self.rect.x -= 5

        if self.limit >= 80:
            chargeGro.remove(self)










