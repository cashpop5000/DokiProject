import pygame
import constants as constants
from spritesheet_functions import SpriteSheet


class Start(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        pygame.sprite.Sprite.__init__(self)

        self.sprite_sheet = SpriteSheet("Title.png")

        image = self.sprite_sheet.get_image(207, 513, 201, 95)

        self.image = image

        self.rect = self.image.get_rect()

        self.change_y = -10
        self.bounce = 0

        self.rect.x = 225
        self.rect.y = 800

        self.highlighted = False
        self.selected = False



    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


    def update(self):

        if self.selected:
            image = self.sprite_sheet.get_image(207, 607, 201, 95)

            self.image = image

        elif self.highlighted:
            image = self.sprite_sheet.get_image(207, 700, 201, 95)

            self.image = image
        else:
            image = self.sprite_sheet.get_image(207, 513, 201, 95)

            self.image = image

        if self.change_y < 0:
            self.change_y += .2

        self.rect.y += self.change_y




