import pygame
import constants as constants
import levels as levels



class Fodder(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.walking_frames_l = []
        self.walking_frames_r = []

        width = 30
        height = 30
        self.image = pygame.Surface([width, height])
        self.image.fill(constants.RED)

        self.rect = self.image.get_rect()

        self.change_x = 1
        self.change_y = 0

        self.stopped = 0

        # List of sprites we can bump against
        self.regBlo = None
        self.falBlo = None

        self.player = None

        self.direction = 'r'

    def update(self):

        bullet_hit = pygame.sprite.spritecollide(self, self.player.bullets, False)
        for bul in bullet_hit:
            self.player.bullets.remove(bul)

        if len(bullet_hit):
            print('OUCH')
            self.stopped = 30

        if self.direction == 'r':

            self.rect.x += 30
            self.rect.y += 1

            block_hit_list = pygame.sprite.spritecollide(self, self.regBlo, False)
            FallBlock_hit_list = pygame.sprite.spritecollide(self, self.falBlo, False)

            self.rect.x -= 30
            self.rect.y -= 1

            if self.stopped == 0:
                if len(block_hit_list) or len(FallBlock_hit_list):
                    self.rect.x += self.change_x
                else:
                    self.direction = 'l'
            else:
                self.stopped -= 1


        elif self.direction == 'l':

            self.rect.x -= 30
            self.rect.y += 1

            block_hit_list = pygame.sprite.spritecollide(self, self.regBlo, False)
            FallBlock_hit_list = pygame.sprite.spritecollide(self, self.falBlo, False)

            self.rect.x += 30
            self.rect.y -= 1

            if self.stopped == 0:
                if len(block_hit_list) or len(FallBlock_hit_list):
                    self.rect.x -= self.change_x
                else:
                    self.direction = 'r'
            else:
                self.stopped -= 1











