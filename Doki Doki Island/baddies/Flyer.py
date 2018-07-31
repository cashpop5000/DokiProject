import pygame
import constants as constants
import levels as levels



class Flyer(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.fly_frames_l = []
        self.fly_frames_r = []

        width = 30
        height = 30
        self.image = pygame.Surface([width, height])
        self.image.fill(constants.RED)

        self.rect = self.image.get_rect()

        self.moved_x = 0
        self.moved_y = 0

        # List of sprites we can bump against
        self.regBlo = None
        self.falBlo =  None
        self.player = None

        self.direction = 'r'
        self.TDdirection = 't'

    def update(self):

        if self.player.rect.x + 7 < self.rect.x:
            self.rect.x -= 1
            self.direction = 'l'
        elif self.player.rect.x + 7 > self.rect.x:
            self.rect.x += 1
            self.direction = 'r'

        block_hit_list = pygame.sprite.spritecollide(self, self.regBlo, False)
        for block in block_hit_list:

            if self.direction == 'r':
                self.rect.right = block.rect.left
            elif self.direction == 'l':
                self.rect.left = block.rect.right



        if self.player.rect.y + 10 < self.rect.y:
            self.rect.y -= 1
            self.TDdirection = 't'
        elif self.player.rect.y + 10 > self.rect.y:
            self.rect.y += 1
            self.TDdirection = 'b'


        block_hit_list = pygame.sprite.spritecollide(self, self.regBlo, False)
        for block in block_hit_list:

            if self.TDdirection == 't':
                self.rect.top = block.rect.bottom
            elif self.TDdirection == 'b':
                self.rect.bottom = block.rect.top














