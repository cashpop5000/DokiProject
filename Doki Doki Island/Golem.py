""" The Golem boss

Imports:
    pygame: Tools to be used for sprite
    spritesheet_functions: Allows use for custom sprites
    random: Used for random numbers
    constants: For screen height and width
    golAttack1: First golem attack
    golAttack2: Second golem attack
    golAttack3: third golem attack
    golAttack4: fourth golem attack
    golHealth: the golem hp bar


Class:
    Golem: The main body of the boss

"""


import pygame
from random import randint

import constants as constants
from bossAttacks.golem import golAttack1 as FirstAtt
from bossAttacks.golem import golAttack2 as SecondAtt
from bossAttacks.golem import golAttack3 as ThirdAtt
from bossAttacks.golem import golAttack4 as FourthAtt
from spritesheet_functions import SpriteSheet
from bossAttacks.golem import golHealth as golHealth


class Golem(pygame.sprite.Sprite):


    def __init__(self):

        """
        This initializes the boss


        Variables:

            self.player: The player object
            self.screen: Display window
            self.hp: The boss' hp
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
            self.rockets: True if rockets will be used as an attack
            self.rocketSpawn: Timer used to spawn rocks in intervals
            self.stopRockets: Keeps count on how many rocks were spawned
            sprite_sheet: The spritesheet to where the custom sprites came from
            image: Holds the custom
            self.image: The sprite used to represent
            self.rect: This creates the shape of the sprite
            self.rect.x: The x-position of the sprite
            self.rect.y: The y-position of the sprite


        """



        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("Golem.png")

        image = sprite_sheet.get_image(662, 69, 286, 263)
        self.image = image

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        # Set a referance to the image rect.
        self.rect = self.image.get_rect()

        self.screen = None
        self.hp = 100
        self.dead = False

        self.boss = None

        self.hover = False
        self.half = False

        self.change_x = 0
        self.change_y = 0

        #remmebe to random the attacks
        self.attackSelection = 0
        self.limit = 0
        self.AfterDeath = 0
        self.whenAtt = 0
        self.durAtt = False

        self.player = None

        self.attacks = pygame.sprite.Group()
        self.health = pygame.sprite.Group()
        bar = golHealth.Golem()
        self.health.add(bar)

        self.rockets = False
        self.rocketSpawn = 0
        self.stopRockets = 0

        self.rect = self.image.get_rect()

    def update(self):

        """ Updates the boss

        Variables:
            hit_player: Checks if the sprite touches the player

        Boss hovers in place, dishing out different attacks.
        Once boss is defeated, will allow the player to 'win'

        """

        hit_player = pygame.sprite.spritecollide(self.player, self.boss, False)

        if len(hit_player) > 0:
            print('got em')
            if not self.player.hurt:
                self.player.hurt = True
                self.player.hp -= 10
                self.player.getHit = True

        if self.hp > 0:
            self.limit += 1
        else:
            self.durAtt = False
            self.limit = 0
            self.whenAtt = 0
            self.attacks.empty()

            if not self.dead and self.change_y > 0:
                self.change_y = 0
                self.dead = True



        if self.limit == 15:
            self.change_y = 1

        elif self.limit == 30:
            self.change_y = 2


        elif self.limit == 60:
            self.change_y = 1

        elif self.limit == 75:
            if self.hover:
                self.hover = False

            else:
                self.hover = True

        elif self.limit == 90:
            self.limit = 0
            self.change_y = 1.0

        if self.hover and not self.dead:
            self.rect.y += self.change_y

        elif not self.hover and not self.dead:
            self.rect.y -= self.change_y

        self.attacks.update(self.attacks)
        self.health.update(self.hp)

        if not self.durAtt and self.hp > 0:
            self.whenAtt += 1

        if self.whenAtt == 150 and not self.durAtt:
            self.durAtt = True
            self.whenAtt = 0
            #randomize attackselection variable
            self.attackSelection = randint(0,3)

            #Punch
            #Rockets
            #OtherPunch

            if self.attackSelection == 0:
                punchy = FirstAtt.Punch(self.player)
                self.attacks.add(punchy)
            if self.attackSelection == 1:
                self.rockets = True
                print('rocket time')
            if self.attackSelection == 2:
                DownPunchy = ThirdAtt.Punch(self.player)
                self.attacks.add(DownPunchy)
            if self.attackSelection == 3:
                EyeBeam = FourthAtt.Laser(self.player, self)
                self.attacks.add(EyeBeam)


        #For second attack the homing rockets
        ##############################################
        if self.rockets:
            self.rocketSpawn += 1

        if self.rocketSpawn == 290:
            blowEmUp = SecondAtt.Rocket(self.player.rect.x, self.player)
            self.attacks.add(blowEmUp)
            self.rocketSpawn = 0
            self.stopRockets += 1

        if self.stopRockets == 3:
            self.rockets = False
            self.stopRockets = 0

        ##############################################








        if len(self.attacks) <= 0:
            self.durAtt = False


       #This for when the boss dies


        if self.hp <= 0:
            self.AfterDeath += 1


        if self.AfterDeath >= 60 and self.rect.y <= constants.SCREEN_HEIGHT:
            self.change_y += .2
            self.rect.y += self.change_y

        if self.rect.y >= constants.SCREEN_HEIGHT:
            self.player.winner = True
            self.boss.remove(self)



    def draw(self, screen):
        self.attacks.draw(screen)
        self.health.draw(screen)


    def shift(self, shift_x):
        for att in self.attacks:
            att.rect.x += shift_x





