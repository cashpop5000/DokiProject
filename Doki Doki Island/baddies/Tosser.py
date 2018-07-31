import pygame
import constants as constants
from baddies import Rock as Rock



class Toss(pygame.sprite.Sprite):

    def __init__(self,x, y):

        super().__init__()

        self.walking_frames_l = []
        self.walking_frames_r = []

        width = 50
        height = 50
        self.image = pygame.Surface([width, height])
        self.image.fill(constants.RED)

        self.rect = self.image.get_rect()

        self.change_x = 1
        self.change_y = 0

        self.rect.x = x
        self.rect.y = y

        self.stopped = 0

        # List of sprites we can bump against
        self.regBlo = None
        self.falBlo = None

        self.player = None
        self.inRange = False
        self.attacks = None
        self.enemy = None

        self.spawnRock = 90

        self.animation = 3

        self.direction = 'r'

    def update(self):

        bullet_hit = pygame.sprite.spritecollide(self, self.player.bullets, False)
        for bul in bullet_hit:
            self.player.bullets.remove(bul)

        if len(bullet_hit):
            print('OUCH')
            self.enemy.remove(self)


        if self.rect.x - 300 < self.player.rect.x + 3 < self.rect.x\
                or self.rect.x + 300 > self.player.rect.x + 3 >= self.rect.x:

            self.inRange = True

            if self.rect.x - 300 < self.player.rect.x + 3 < self.rect.x:
                self.direction = 'l'
            else:
                self.direction = 'r'

        else:
            self.inRange = False

        #use the self.animation to go from holding up position to throwing, which when throw spawns rock
        if self.inRange:
            self.spawnRock -= 1

        if self.spawnRock == 0:
            if self.animation == 3:
                rockEm = Rock.Rock(self.rect.x + 25, self.rect.y - 10, self.direction)
                self.attacks.add(rockEm)
                rockEm.attacks = self.attacks
                self.spawnRock = 90



        if self.direction == 'r' and not self.inRange:

            self.rect.x += 50
            self.rect.y += 1

            block_hit_list = pygame.sprite.spritecollide(self, self.regBlo, False)
            FallBlock_hit_list = pygame.sprite.spritecollide(self, self.falBlo, False)

            self.rect.x -= 50
            self.rect.y -= 1

            if self.stopped == 0:
                if len(block_hit_list) or len(FallBlock_hit_list):
                    self.rect.x += self.change_x
                else:
                    self.direction = 'l'
                    self.stopped = 5
            else:
                self.stopped -= 1


        elif self.direction == 'l' and not self.inRange:

            self.rect.x -= 50
            self.rect.y += 1

            block_hit_list = pygame.sprite.spritecollide(self, self.regBlo, False)
            FallBlock_hit_list = pygame.sprite.spritecollide(self, self.falBlo, False)

            self.rect.x += 50
            self.rect.y -= 1

            if self.stopped == 0:
                if len(block_hit_list) or len(FallBlock_hit_list):
                    self.rect.x -= self.change_x
                else:
                    self.direction = 'r'
                    self.stopped = 5
            else:
                self.stopped -= 1











