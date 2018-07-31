import pygame
import constants as constants
import levels as levels
from spritesheet_functions import SpriteSheet
from random import randint


class Scarab(pygame.sprite.Sprite):

    def __init__(self, player):

        super().__init__()

        self.LRframes = []
        self.TBframes = []

        selection = randint(0,1)
        selectSpot = randint(0,2)


        self.distance = 0
        self.oriDistance = 0
        self.direction = ''


        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("Skeleton.png")


        #Right
        image = sprite_sheet.get_image(46, 11, 78, 61)
        self.LRframes.append(image)

        #Left
        image = sprite_sheet.get_image(351, 10, 78, 61)
        self.LRframes.append(image)

        #Top
        image = sprite_sheet.get_image(160, 5, 61, 78)
        self.TBframes.append(image)

        #Bottom
        image = sprite_sheet.get_image(252, 6, 61, 78)
        self.TBframes.append(image)

        self.image = image
        self.rect = self.image.get_rect()

        if selection == 0:

            image = self.LRframes[0]
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x = 30
            self.direction = 'r'

            if selectSpot == 0:
                self.rect.y = 30
            elif selectSpot == 1:
                self.rect.y = 305
            elif selectSpot == 2:
                self.rect.y = 600

            self.distance = 920
            self.oriDistance = 920


        elif selection == 1:

            image = self.LRframes[1]
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x = constants.SCREEN_WIDTH - 108
            self.direction = 'l'

            if selectSpot == 0:
                self.rect.y = 25
            elif selectSpot == 1:
                self.rect.y = 305
            elif selectSpot == 2:
                self.rect.y = 600

                self.distance = 920
                self.oriDistance = 920



        elif selection == 2:
            image = self.TBframes[0]
            self.image = image
            self.direction = 't'



        elif selection == 3:
            image = self.TBframes[1]
            self.image = image
            self.direction = 'b'



        self.stopped = 0

        # List of sprites we can bump against
        self.regBlo = None
        self.falBlo = None

        self.player = player

        #test only
        self.spawnTime = 0

    def update(self, bugs):


        playhit = pygame.sprite.spritecollide(self.player, bugs, False)

        if len(playhit) > 0:
            print('hit the player')

        bullet_hit = pygame.sprite.spritecollide(self, self.player.bullets, False)
        for bul in bullet_hit:
            self.player.bullets.remove(bul)

        if len(bullet_hit):
            print('OUCH')
            self.stopped = 30
            bugs.remove(self)

        self.distance -= 5

        if self.distance <= 0:
            if self.direction == 'r':
                self.direction = 'l'
            elif self.direction == 'l':
                self.direction = 'r'
            elif self.direction == 't':
                self.direction = 'b'
            else:
                self.direction = 't'

            self.distance = self.oriDistance



        if self.direction == 'r':
            self.rect.x += 5
        elif self.direction == 'l':
            self.rect.x -= 5
        elif self.direction == 't':
            self.rect.y -= 5
        else:
            self.rect.y += 5



        self.spawnTime += 1

        if self.spawnTime >= 600:
            bugs.remove(self)













