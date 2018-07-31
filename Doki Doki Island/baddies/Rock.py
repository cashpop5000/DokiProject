import pygame
import constants as constants


class Rock(pygame.sprite.Sprite):

    def __init__(self, x, y, direction):

        super().__init__()


        width = 20
        height = 20
        self.image = pygame.Surface([width, height])
        self.image.fill(constants.WHITE)

        self.rect = self.image.get_rect()

        self.change_x = 14
        self.change_y = -3

        # List of sprites we can bump against
        self.regBlo = None
        self.falBlo = None

        self.rect.x = x
        self.rect.y = y

        self.player = None
        self.attacks = None

        self.direction = direction

    def update(self):

        if self.rect.x <= 0 or self.rect.x >= constants.SCREEN_WIDTH\
            or self.rect.y >= constants.SCREEN_HEIGHT:
                self.attacks.remove(self)

        if self.direction == 'r':
            self.rect.x += self.change_x
        else:
            self.rect.x -= self.change_x

        self.rect.y += self.change_y

        self.change_y += .3
        self.change_x -= .1
        print(self.change_x)

        if self.change_x <= 0:
            self.change_x = 0

        if self.change_y >= 7:
            self.change_y = 7







