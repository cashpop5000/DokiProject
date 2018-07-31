import pygame
import constants as constants


class Start(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        width = 200
        height = 100

        self.image = pygame.Surface([width, height])
        self.image.fill(constants.PURPLE)

        self.rect = self.image.get_rect()

        self.change_y = -10
        self.bounce = 0

        self.rect.x = 625
        self.rect.y = 800

        self.highlighted = False


    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


    def update(self):

        if self.highlighted:
            self.image.fill(constants.RED)
        else:
            self.image.fill(constants.PURPLE)

        if self.change_y < 0:
            self.change_y += .2

        self.rect.y += self.change_y




