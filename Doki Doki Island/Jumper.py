import pygame
import constants as constants
import levels as levels



class Jumper(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        #note, create an elite version

        self.fly_frames_l = []
        self.fly_frames_r = []

        width = 30
        height = 30
        self.image = pygame.Surface([width, height])
        self.image.fill(constants.RED)

        self.rect = self.image.get_rect()

        self.canJump = False
        self.moved_y = 0

        # List of sprites we can bump against
        self.regBlo = None
        self.falBlo = None
        self.player = None

        self.direction = 'r'
        self.TDdirection = 't'

    def update(self):

        self.calc_grav()

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

        self.rect.y += self.moved_y

        block_hit_list = pygame.sprite.spritecollide(self, self.regBlo, False)
        for block in block_hit_list:

            if self.moved_y < 0:
                self.rect.top = block.rect.bottom
            elif self.moved_y > 0:
                self.rect.bottom = block.rect.top
                self.canJump = True

            self.moved_y = 0

        if self.canJump:
            self.jump()
            self.canJump = False




    def calc_grav(self):

        if self.moved_y == 0:
            self.moved_y = 1
        else:
            self.moved_y += .35

        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.moved_y >= 0:
            self.moved_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height
            self.canJump = True

    def jump(self):
        self.moved_y = -7








