""" The Magma boss

Imports:
    pygame: Tools to be used for sprite
    spritesheet_functions: Allows use for custom sprites
    random: Used for random numbers
    constants: For screen height and width
    magAttack1: First golem attack
    magAttack2: Second golem attack
    magHealth: the golem hp bar


Class:
    Magma: The main body of the boss

"""


import pygame
from random import randint
from spritesheet_functions import SpriteSheet
import constants as constants
from bossAttacks.mag import magHealth as magHealth
from bossAttacks.mag import magAttack1 as magAttack1
from bossAttacks.mag import magAttack2 as magAttack2


class Magma(pygame.sprite.Sprite):


    def __init__(self):

        """
        This initializes the boss


        Variables:

            self.player: The player object
            self.screen: Display window
            self.hp: The boss' hp
            self.bounce: True if boss is able to bounce around
            self.dead: True is boss is dead
            self.boss: The group the boss resides in
            self.hover: Determines the direction of the hovering head
            self.half: Slows down the boss halfway into the hover
            self.change_y: Changes the y-position of the boss
            self.attackSelection: Randomly chooses a number to choose which attack to use
            self.limit: Used during the hover, determines when to change direction or hover speed
            self.AfterDeath: Used once boss is dead
            self.whenAtt: Timer used to determine when boss will attack the player
            self.durAtt: True if boss is currently using an attack
            self.attacks: Group to hold the attacks
            self.health: Group to hold hp bar
            self.fallRock: True if boulders will be used as an attack
            self.fallRockCount: Keeps count on how many boulders were spawned
            sprite_sheet: The spritesheet to where the custom sprites came from
            image: Holds the custom
            self.image: The sprite used to represent
            self.rect: This creates the shape of the sprite
            self.rect.x: The x-position of the sprite
            self.rect.y: The y-position of the sprite


        """

        super().__init__()

        self.screen = None
        self.hp = 1000
        self.dead = False
        self.AfterDeath = 0

        self.height = 100
        self.width = 100

        self.bounce = True

        self.change_x = 2
        self.change_y = 2

        #remmebe to random the attacks
        self.attackSelection = 1
        self.limit = 0
        self.whenAtt = 0
        self.durAtt = False

        self.player = None

        self.attacks = pygame.sprite.Group()
        self.boss = None

        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("Lava.png")

        image = sprite_sheet.get_image(284, 264, 174, 174)
        self.image = image

        self.rect = self.image.get_rect()

        self.fallRock = False
        self.fallRockCount = 0

        self.tosser = False
        self.tosserCount = 0

        self.spawnAtt = 0

        self.health = pygame.sprite.Group()
        bar = magHealth.Mag()
        self.health.add(bar)



    def update(self):

        """ Updates the boss

        Variables:
            hit_player: Checks if the sprite touches the player

        Boss bounces around, the environment tries to kill the player


        """

        self.health.update(self.hp)
        self.attacks.update(self.attacks)

        if self.hp <= 0:
            self.dead = True
            self.bounce = False
            self.attacks.empty()


        hit_player = pygame.sprite.spritecollide(self.player, self.boss, False)

        if len(hit_player) > 0 and not self.dead:
            print('got em')
            if not self.player.hurt:
                self.player.hurt = True
                self.player.hp -= 10
                self.player.getHit = True

        if self.bounce and not self.dead:

            if self.rect.x <= 0:
                self.change_x = 2
            elif self.rect.x >= constants.SCREEN_WIDTH - 174:
                self.change_x = -2

            if self.rect.y <= 0:
                self.change_y = 2
            elif self.rect.y >= constants.SCREEN_HEIGHT - 174:
                self.change_y = -2

            self.rect.x += self.change_x

            self.rect.y += self.change_y



        if not self.durAtt:
            self.whenAtt += 1


        if self.whenAtt >= 100 and not self.durAtt:
            self.durAtt = True
            self.whenAtt = 0
            self.attackSelection = randint(0,1)

            #Creates lava pillars to damage player
            if self.attackSelection == 0:
                lavaPillar = magAttack1.Pillar(self.player)
                self.attacks.add(lavaPillar)

            #Creats falling rocks that fall to damage player
            elif self.attackSelection == 1:
                self.fallRock = True


            elif self.attackSelection == 2:
                ...

        if self.fallRock:
            self.spawnAtt += 1

        if self.fallRock and self.spawnAtt >= 200:
            self.spawnAtt = 0
            rock = magAttack2.RockDown(self.player)
            self.attacks.add(rock)
            self.fallRockCount += 1

        if self.fallRockCount >= 3:
            self.fallRock = False
            self.fallRockCount = 0

        if len(self.attacks) < 1 and self.durAtt and not self.fallRock:
            self.durAtt = False
            print('again')



        if self.hp <= 0:
            self.AfterDeath += 1


        if self.AfterDeath >= 60 and self.rect.y <= constants.SCREEN_HEIGHT:
            self.change_y += .2
            self.rect.y += self.change_y

        if self.rect.y >= constants.SCREEN_HEIGHT and self.dead:
            print('oh')
            self.player.winner = True
            self.boss.remove(self)


    def draw(self, screen):
        self.health.draw(screen)
        self.attacks.draw(screen)




