import pygame
import constants as constants
from spritesheet_functions import SpriteSheet



class Start(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("Title.png")

        image = sprite_sheet.get_image(26, 17, 610, 381)

        self.image = image

        self.rect = self.image.get_rect()

        self.change_y = 0
        self.bounce = 0

        self.rect.x = 225
        self.rect.y = -130


    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


    def update(self):

        if self.change_y <= 0 and self.rect.y < 90:
            self.change_y += .2

        if self.rect.y < 90:
            self.change_y += 1
        elif self.rect.y >= 90 and self.bounce < 5:
            if self.bounce == 0:
                self.change_y = -8
                self.bounce += 1

            elif self.bounce == 1:
                self.change_y = -6
                self.bounce += 1

            elif self.bounce == 2:
                self.change_y = -4
                self.bounce += 1

            elif self.bounce == 3:
                self.change_y = -2
                self.bounce += 1

            elif self.bounce == 4:
                self.change_y = 0
                self.bounce += 1

        self.rect.y += self.change_y





