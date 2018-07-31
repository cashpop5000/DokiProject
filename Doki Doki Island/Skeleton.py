import pygame
from random import randint

import constants as constants
from bossAttacks.skele import skeAttack1 as FirstAtt
from bossAttacks.skele import skeAttack2 as SecondAtt
from bossAttacks.skele import skeAttack3 as ThirdAtt
from bossAttacks.skele import skeHealth as skeHealth
from spritesheet_functions import SpriteSheet



class Skeleton(pygame.sprite.Sprite):


    def __init__(self):


        """
        This initializes the boss


        Variables:

            self.player: The player object
            self.screen: Display window
            self.skeletonHead: Holds the different sprites for the skeleton head
            self.hp: The boss' hp
            self.dead: True is boss is dead
            self.boss: The group the boss resides in
            self.change_y: Changes the y-position of the boss
            self.attackSelection: Randomly chooses a number to choose which attack to use
            self.limit: Used during the hover, determines when to change direction or hover speed
            self.popup: True when boss is popping up
            self.popdown: True if boss is trying to hide
            self.popupTime: Determines how long boss stays popped up
            self.transformed: True for boss to change sprites
            self.quick_sand: Holds the quicksand
            self.AfterDeath: Used once boss is dead
            self.whenAtt: Timer used to determine when boss will attack the player
            self.durAtt: True if boss is currently using an attack
            self.attacks: Group to hold the attacks
            self.health: Group to hold hp bar
            sprite_sheet: The spritesheet to where the custom sprites came from
            image: Holds the custom
            self.image: The sprite used to represent
            self.rect: This creates the shape of the sprite
            self.rect.x: The x-position of the sprite
            self.rect.y: The y-position of the sprite


        """

        super().__init__()

        self.skeletonHead = []

        self.screen = None
        self.hp = 1000

        self.hover = False
        self.half = False
        self.boss = None

        self.change_x = 0
        self.change_y = 0

        self.transformed = True

        self.node = 0

        self.nodeList = [[450, -170],
                 [-150, 250],
                 [1100, 250],
                 [450, 800],
                 #[180, 180, 120, 120],
                 ]

        #remmebe to random the attacks
        self.attackSelection = 0
        self.whenAtt = 0
        self.durAtt = False

        self.player = None
        self.quick_sand = None

        self.popup = True
        self.popdown = False
        self.popupTime = 200

        self.AfterDeath = 0
        self.dead = False

        self.attacks = pygame.sprite.Group()
        self.health = pygame.sprite.Group()
        bar = skeHealth.Ske()
        self.health.add(bar)

        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("Skeleton.png")

        #Upisode down
        image = sprite_sheet.get_image(282, 115, 163, 131)
        self.skeletonHead.append(image)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = 450

        #Upside up
        image = sprite_sheet.get_image(282, 294, 163, 131)
        self.skeletonHead.append(image)

        #Left side
        image = sprite_sheet.get_image(66, 101, 131, 163)
        self.skeletonHead.append(image)

        #Right side
        image = sprite_sheet.get_image(48, 297, 131, 163)
        self.skeletonHead.append(image)


    def update(self):

        """ Updates the boss

        Variables:
            hit_player: Checks if the sprite touches the player

        Boss pops up and down at different places.

        When boss pops down, the hp bar hides and quicksand fills the room followed by an attack.
        Once the attack is finished, the quicksand spills out and the boss pops up, vulnerable to attack
        Once boss is defeated, will allow the player to 'win'

        """


        self.health.update(self.hp)

        hit_player = pygame.sprite.spritecollide(self.player, self.boss, False)



        if self.hp <= 0:
            self.popdown = False
            self.popup = False
            self.popupTime = 0
            self.dead = True
            self.attacks.empty()
            self.quick_sand.empty()


        if len(hit_player) > 0 and not self.dead:
            print('got em')
            if not self.player.hurt:
                self.player.hurt = True
                self.player.hp -= 10
                self.player.getHit = True


        if self.popupTime > 0 and self.popup and not self.popdown:
            self.popupTime -= 1

        if self.popupTime <= 0 and not self.popdown and not self.dead:
            self.popup = False

            #first node
            if self.node == 0:

                if self.rect.y <= -110:
                    #for test
                    self.node = 1

                    self.popdown = True
                    self.transformed = False
                    if not self.transformed:

                        self.image = self.skeletonHead[2]
                        self.rect = self.image.get_rect()
                        self.rect.x = self.nodeList[self.node][0]
                        self.rect.y = self.nodeList[self.node][1]
                        self.transformed = True


                else:
                    self.rect.y -= 2

            #second node
            if self.node == 1:

                if self.rect.x <= -160:

                    #for test
                    self.node = 2
                    self.popdown = True
                    self.transformed = False
                    if not self.transformed:

                        self.image = self.skeletonHead[3]
                        self.rect = self.image.get_rect()
                        self.rect.x = self.nodeList[self.node][0]
                        self.rect.y = self.nodeList[self.node][1]
                        self.transformed = True

                else:
                    self.rect.x -= 2



            if self.node == 2:

                if self.rect.x >= constants.SCREEN_WIDTH + 150:

                    #for test
                    self.node = 3

                    self.popdown = True
                    self.transformed = False
                    if not self.transformed:

                        self.image = self.skeletonHead[1]
                        self.rect = self.image.get_rect()
                        self.rect.x = self.nodeList[self.node][0]
                        self.rect.y = self.nodeList[self.node][1]
                        self.transformed = True

                else:
                    self.rect.x += 2


            if self.node == 3:

                if self.rect.y >= constants.SCREEN_HEIGHT + 150:

                    #for test
                    self.node = 0

                    self.popdown = True
                    self.transformed = False

                    if not self.transformed:

                        self.image = self.skeletonHead[0]
                        self.rect = self.image.get_rect()
                        self.rect.x = self.nodeList[self.node][0]
                        self.rect.y = self.nodeList[self.node][1]
                        self.transformed = True

                else:
                    self.rect.y += 2





        if self.popupTime >= 200 and not self.popup and not self.dead:
            self.popdown = False
            if self.node == 0:
                print('moving node 0')
                if self.rect.y >= 10:
                    self.popup = True
                else:
                    self.rect.y += 2

            if self.node == 1:
                print('moving node 1')
                if self.rect.x >= 10:
                    self.popup = True
                else:
                    self.rect.x += 2

            if self.node == 2:
                print('moving node 2')
                if self.rect.x <= constants.SCREEN_WIDTH - 141:
                    self.popup = True
                else:
                    self.rect.x -= 2

            if self.node == 3:
                print('moving node 3')
                if self.rect.y <= constants.SCREEN_HEIGHT - 131:
                    self.popup = True
                else:
                    self.rect.y -= 2




        if not self.durAtt and not self.popup and self.popdown and self.popupTime <= 0:
            self.whenAtt += 1

        if self.whenAtt == 100 and not self.durAtt:
            self.durAtt = True
            self.whenAtt = 0
            self.attackSelection = randint(0,2)
            if self.attackSelection == 0:
                FillItQ = FirstAtt.QuickS(self.player, self)
                FillItQ.screen = self.screen
                self.quick_sand.add(FillItQ)

            if self.attackSelection == 1:
                FillItQ = SecondAtt.QuickS(self.player, self)
                FillItQ.screen = self.screen
                self.quick_sand.add(FillItQ)

            if self.attackSelection == 2:
                FillItQ = ThirdAtt.QuickS(self.player, self)
                FillItQ.screen = self.screen
                self.quick_sand.add(FillItQ)



        if len(self.attacks) <= 0 and len(self.quick_sand) <= 0:
            if self.durAtt:
                self.popupTime = 200
                self.durAtt = False



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
        """
        :param screen: Display window

        Draws the assets

        """
        self.attacks.draw(screen)

        for pon in self.quick_sand:
            pon.draw(screen)

        if len(self.quick_sand) < 1:
            self.health.draw(screen)








