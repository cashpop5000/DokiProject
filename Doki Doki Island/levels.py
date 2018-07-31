""" The levels of the game

Imports:
    pygame: Tools to be used for sprite
    constants: For screen height and width
    Golem: The golem boss
    Skeleton: the skeleton boss
    Magma: The magma boss
    platforms: Platforms to be interacted with in levels

Class:
    Level: All the levels


"""

import pygame

import Fallplatforms as FallPlatforms
import Golem as Golem
import Quicksand as Quicksand
import Skeleton as Skeleton
import Magma as Magma
import Slime as Slime
import constants as constants
import platforms as platforms
from baddies import Fodder as Fodder
from baddies import Flyer as Flyer
from baddies import Jumper as Jumper
from baddies import Tosser as Tosser

class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    def __init__(self, player, screen):
        """ Constructs levels
        :param player: The player object
        :param screen: Display window

        Variables:
            self.platform_list: Regular platforms
            self.decor: Decoration or background
            self.decorLayer: Decoration in layers
            self.platform_fallthrough: Platforms you can stand on, but not touch from the sides of bottom
            self.platform_quicksand: The quicksand
            self.platform_slime: Holds slime boxes
            self.platform_choose: Portals that player can go through
            self.enemy_list: The list of enemies
            self.behind_boss_man: Exclusive for skeleton, used so that he can be behind platforms
            self.boss_man: The bosses
            self.attacks: For certain boss attacks, right now just for skeleton
            self.end_blocks: When player reaches an end of level and transition to next
            self.kill_blocks: Kills player on contact
            self.player: Player object
            self.screen: Display window
            self.world_shift: shifts the world x-position
            self.world_shiftY: shifts the world y-position
            self.level_x_limit: The x-limit of the levels
            self.level_y_limit: The y-limit of the levels
            self.left_x = The limit of the level from the left, so player can't go back too far

        """
        self.platform_list = pygame.sprite.Group()
        self.decor = pygame.sprite.Group()
        self.decorLayer = pygame.sprite.OrderedUpdates()
        self.platform_fallthrough = pygame.sprite.Group()
        self.platform_quicksand = pygame.sprite.Group()
        self.platform_slime = pygame.sprite.Group()
        self.platform_choose = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.behind_boss_man = pygame.sprite.Group()
        self.boss_man = pygame.sprite.Group()
        self.attacks = pygame.sprite.Group()
        self.end_blocks = pygame.sprite.Group()
        self.kill_blocks = pygame.sprite.Group()
        self.player = player
        self.screen = screen

        # How far this world has been scrolled left/right
        self.world_shift = 0
        self.world_shiftY = 0

        self.ori_X = 0
        self.ori_Y = 0

        self.level_x_limit = 0
        self.level_y_limit = 0
        self.left_x = 0


    # Update everythign on this level
    def update(self):

        """ Update everything in this level."""
        self.platform_quicksand.update(self.platform_quicksand)
        self.behind_boss_man.update()
        self.platform_fallthrough.update()
        self.decor.update()
        self.decorLayer.update()
        self.platform_slime.update()
        self.platform_list.update()
        self.platform_choose.update()
        self.enemy_list.update()
        self.boss_man.update()
        self.end_blocks.update()
        self.attacks.update()
        self.kill_blocks.update()


    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        screen.fill(constants.BLUE)

        # Draw all the sprite lists that we have

        self.decor.draw(screen)
        self.decorLayer.draw(screen)
        self.platform_quicksand.draw(screen)
        for boss in self.behind_boss_man:
            boss.draw(screen)

        self.behind_boss_man.draw(screen)
        self.platform_choose.draw(screen)
        self.platform_fallthrough.draw(screen)
        self.platform_slime.draw(screen)
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        self.kill_blocks.draw(screen)
        self.boss_man.draw(screen)
        self.end_blocks.draw(screen)
        self.attacks.draw(screen)

        for boss in self.boss_man:
            boss.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll
        everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x
        self.left_x -= shift_x
        self.ori_X += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for platform in self.decorLayer:
            platform.rect.y += shift_x

        for platform in self.platform_fallthrough:
            platform.rect.x += shift_x

        for platform in self.platform_quicksand:
            platform.rect.x += shift_x

        for platform in self.platform_slime:
            platform.rect.x += shift_x

        for platform in self.platform_choose:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

        for end in self.end_blocks:
            end.rect.x += shift_x

        print(self.ori_X)

    def getOriX(self):
        return self.ori_X




    def shift_worldY(self, shift_y):
        """ When the user moves top/down and we need to scroll
        everything: """

        # Keep track of the shift amount
        self.world_shiftY += shift_y
        self.ori_Y += shift_y

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.y += shift_y

        for platform in self.decorLayer:
            platform.rect.y += shift_y

        for platform in self.platform_fallthrough:
            platform.rect.y += shift_y

        for platform in self.platform_quicksand:
            platform.rect.y += shift_y

        for platform in self.platform_slime:
            platform.rect.y += shift_y

        for platform in self.platform_choose:
            platform.rect.y += shift_y

        for enemy in self.enemy_list:
            enemy.rect.y += shift_y

        for end in self.end_blocks:
            end.rect.y += shift_y


    def resetHub(self, a ,b):

        """ When the user moves from/to any hub levels, will reset the positions of the sprites: """


        for platform in self.platform_list:
            platform.rect.x -= self.ori_X

        for platform in self.decorLayer:
            platform.rect.x -= self.ori_X

        for platform in self.platform_fallthrough:
            platform.rect.x -= self.ori_X

        for platform in self.platform_quicksand:
            platform.rect.x -= self.ori_X

        for platform in self.platform_slime:
            platform.rect.x -= self.ori_X

        for platform in self.platform_choose:
            platform.rect.x -= self.ori_X

        for enemy in self.enemy_list:
            enemy.rect.x -= self.ori_X

        for end in self.end_blocks:
            end.rect.x -= self.ori_X


        for platform in self.platform_list:
            platform.rect.y -= self.ori_Y

        for platform in self.decorLayer:
            platform.rect.y -= self.ori_Y

        for platform in self.platform_fallthrough:
            platform.rect.y -= self.ori_Y

        for platform in self.platform_quicksand:
            platform.rect.y -= self.ori_Y

        for platform in self.platform_slime:
            platform.rect.y -= self.ori_Y

        for platform in self.platform_choose:
            platform.rect.y -= self.ori_Y

        for enemy in self.enemy_list:
            enemy.rect.y -= self.ori_Y

        for end in self.end_blocks:
            end.rect.y -= self.ori_Y

        self.world_shift = 0
        self.world_shiftY = 0

        self.ori_X = 0
        self.ori_Y = 0

        self.level_x_limit = a
        self.level_y_limit = b
        self.left_x = 0





# Create platforms for the level
class Level_00(Level):


    def __init__(self, player, screen):
        """ Create grass hub level.

        """

        # Call the parent constructor
        Level.__init__(self, player, screen)

        self.level_x_limit = -1380
        self.level_y_limit = 270


        # Array with type of platform, and x, y location of the platform.
        level = [[platforms.GRASS_MID, 15, 500],
                 [platforms.GRASS_DIRT_LONG, 15, 575],
                 [platforms.GRASS_RIGHT_EDGE, 225, 500],
                 [platforms.GRASS_RIGHT_EDGE_DIRT, 225, 574],

                 [platforms.GRASS_RIGHT_LONG, -68, 290],


                 [platforms.GRASS_RIGHT_CORNER, 1274, 100],
                 [platforms.GRASS_RIGHT_LONG, 1274, 192],
                 [platforms.GRASS_LEFT_CORNER, 1193, 100],
                 [platforms.GRASS_LEFT_LONG, 1193, 192],
                 [platforms.GRASS_MID, 983, 193],
                 [platforms.GRASS_DIRT_LONG, 983, 268],
                 [platforms.GRASS_LEFT_CORNER, 901, 193],
                 [platforms.GRASS_LEFT_LONG, 901, 285],
                 [platforms.GRASS_MID, 691, 285],
                 [platforms.GRASS_DIRT_LONG, 691, 360],
                 [platforms.GRASS_LEFT_CORNER, 609, 285],
                 [platforms.GRASS_LEFT_LONG, 609, 377],
                 [platforms.GRASS_MID, 399, 377],
                 [platforms.GRASS_DIRT_LONG, 399, 452],
                 [platforms.GRASS_LEFT_CORNER, 318, 377],
                 [platforms.GRASS_LEFT_LONG, 317, 469],


                 [platforms.GRASS_LEFT_CORNER, 1558, 100],
                 [platforms.GRASS_LEFT_LONG, 1558, 192],
                 [platforms.GRASS_RIGHT_CORNER, 1639, 100],
                 [platforms.GRASS_RIGHT_LONG, 1639, 192],
                 [platforms.GRASS_MID, 1721, 193],
                 [platforms.GRASS_DIRT_LONG, 1721, 268],
                 [platforms.GRASS_RIGHT_CORNER, 1931, 193],
                 [platforms.GRASS_RIGHT_LONG, 1931, 285],
                 [platforms.GRASS_MID, 2013, 285],
                 [platforms.GRASS_DIRT_LONG, 2013, 360],
                 [platforms.GRASS_RIGHT_CORNER, 2223, 285],
                 [platforms.GRASS_RIGHT_LONG, 2223, 377],
                 [platforms.GRASS_MID, 2305, 377],
                 [platforms.GRASS_DIRT_LONG, 2305, 452],
                 [platforms.GRASS_RIGHT_CORNER, 2515, 377],
                 [platforms.GRASS_RIGHT_LONG, 2515, 469],

                 [platforms.GRASS_LEFT_EDGE, 2607, 500],
                 [platforms.GRASS_LEFT_EDGE_DIRT, 2617, 574],
                 [platforms.GRASS_MID, 2692, 500],
                 [platforms.GRASS_DIRT_LONG, 2692, 575],


                 ]

        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)




        choosePort =[[platforms.PORTAL, 1356, 420, 3],

                     [platforms.PORTAL, 2712, 320, 1],
                     ]

        for port in choosePort:
            wego = platforms.ChooseLev(port[0], port[3])
            wego.rect.x = port[1]
            wego.rect.y = port[2]
            wego.player = self.player
            self.platform_choose.add(wego)



        background = platforms.backgroundGrass()
        background.rect.x = 0
        background.rect.y = 0
        self.decor.add(background)



class Level_01(Level):


    def __init__(self, player, screen):
        """ Create sand hub level.

        """

        # Call the parent constructor
        Level.__init__(self, player, screen)

        self.level_x_limit = -1380
        self.level_y_limit = 270


        # Array with type of platform, and x, y location of the platform.
        level = [[platforms.SAND_LONG_GROUND, 0, 500],
                 [platforms.SAND_LONG_GROUND, 1431, 500],

                 [platforms.SAND_PYRAMID_LONG, 900, 386],
                 [platforms.SAND_PYRAMID_LONG, 1100, 273],
                 [platforms.SAND_PYRAMID_LONG, 2200, 160],
                 [platforms.SAND_PYRAMID_LONG, 2200, 57],
                 [platforms.SAND_PYRAMID_LONG, 1400, -55],
                 [platforms.SAND_PYRAMID_LONG, 1850, -168],
                 [platforms.SAND_PYRAMID_LONG, 1850, -281],

                 #be sure to place this in nonwalljump group
                 [platforms.SAND_PYRAMID_LONG, 2178, 386],
                 [platforms.SAND_PYRAMID_LONG, 2378, 273],
                 [platforms.SAND_PYRAMID_LONG, 1500, -394]


                 ]

        # Go through the array above and add platforms
        for platform in level:
            block = platforms.hubSandBits(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)




        choosePort =[[platforms.PORTAL, -30, 350, 0],
                     [platforms.PORTAL, 1556, -120, 2]
                     ]

        for port in choosePort:
            wego = platforms.ChooseLev(port[0], port[3])
            wego.rect.x = port[1]
            wego.rect.y = port[2]
            wego.player = self.player
            self.platform_choose.add(wego)



        background = platforms.backgroundSandHub()
        background.rect.x = 0
        background.rect.y = 0
        self.decor.add(background)




class Level_02(Level):


    def __init__(self, player, screen):
        """ Create sand hub level.

        """

        # Call the parent constructor
        Level.__init__(self, player, screen)

        self.level_x_limit = -1380
        self.level_y_limit = 270


        # Array with type of platform, and x, y location of the platform.
        level = [


                 ]

        # Go through the array above and add platforms
        for platform in level:
            block = platforms.hubSandBits(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)




        choosePort =[
                     ]

        for port in choosePort:
            wego = platforms.ChooseLev(port[0], port[3])
            wego.rect.x = port[1]
            wego.rect.y = port[2]
            wego.player = self.player
            self.platform_choose.add(wego)



        background = platforms.backgroundSandHub()
        background.rect.x = 0
        background.rect.y = 0
        self.decor.add(background)




#
# # Create platforms for the level
# class Level_01(Level):
#     """ Definition for level 1. """
#
#     def __init__(self, player, screen):
#         """ Create level 1. """
#
#         # Call the parent constructor
#         Level.__init__(self, player, screen)
#
#         # Array with width, height, x, and y of platform
#         level = [[210, 700, 500, 100],
#                  [210, 70, 800, 400],
#                  [210, 70, 1000, 500],
#                  [210, 70, 1120, 280],
#                  [210, 700, 170, 100],
#                  ]
#
#         # Go through the array above and add platforms
#         for platform in level:
#             block = platforms.Platform(platform[0], platform[1])
#             block.rect.x = platform[2]
#             block.rect.y = platform[3]
#             block.player = self.player
#             self.platform_list.add(block)
#
#         levelOt = [[210, 100, 800, 200]]
#
#         for fall in levelOt:
#             block = FallPlatforms.Platform(fall[0], fall[1])
#             block.rect.x = fall[2]
#             block.rect.y = fall[3]
#             block.player = self.player
#             self.platform_fallthrough.add(block)
#         # right here, make some thin fallthrough platforms
#
#         foddy = [[800 , 170]]
#
#         for enemy in foddy:
#             fod = Fodder.Fodder();
#             fod.rect.x = enemy[0]
#             fod.rect.y = enemy[1]
#             fod.player = self.player
#             fod.regBlo = self.platform_list
#             fod.falBlo = self.platform_fallthrough
#             self.enemy_list.add(fod)
#
#
#         levelQs = [[210, 100, 1600, 200],
#                  ]
#
#         # Go through the array above and add platforms
#         for platform in levelQs:
#             block = Quicksand.Platform(platform[0], platform[1])
#             block.rect.x = platform[2]
#             block.rect.y = platform[3]
#             block.player = self.player
#             self.platform_quicksand.add(block)
#
#
#         levelSl = [[210, 100, 1500, 500],
#                  ]
#
#         # Go through the array above and add platforms
#         for platform in levelSl:
#             block = Slime.Platform(platform[0], platform[1])
#             block.rect.x = platform[2]
#             block.rect.y = platform[3]
#             block.player = self.player
#             self.platform_slime.add(block)
#
#
#         fly = [[900 , 170]]
#
#         for enemy in fly:
#             fod = Flyer.Flyer();
#             fod.rect.x = enemy[0]
#             fod.rect.y = enemy[1]
#             fod.player = self.player
#             fod.regBlo = self.platform_list
#             self.enemy_list.add(fod)
#
#         jump = [[1200 , 170]]
#
#         for enemy in jump:
#             fod = Jumper.Jumper();
#             fod.rect.x = enemy[0]
#             fod.rect.y = enemy[1]
#             fod.player = self.player
#             fod.regBlo = self.platform_list
#             self.enemy_list.add(fod)
#
#
#         toss = [[500,50]]
#
#
#         for enemy in toss:
#             fod = Tosser.Toss(enemy[0], enemy[1]);
#             fod.player = self.player
#             fod.regBlo = self.platform_list
#             fod.falBlo = self.platform_fallthrough
#             fod.attacks = self.attacks
#             fod.enemy = self.enemy_list
#             self.enemy_list.add(fod)
#
#
#         #end block
#         theEnd = platforms.Platform(80, 800)
#         theEnd.rect.x = 2000
#         theEnd.rect.y = 0
#         theEnd.player = self.player
#         self.end_blocks.add(theEnd)
#
#
#
#
# # Create platforms for the level
# class Level_02(Level):
#     """ Definition for level 2. """
#
#     def __init__(self, player, screen):
#         """ Create level 1. """
#
#         # Call the parent constructor
#         Level.__init__(self, player, screen)
#
#         # Array with type of platform, and x, y location of the platform.
#         level = [[210, 30, 450, 570],
#                  [210, 30, 850, 420],
#                  [210, 30, 1000, 520],
#                  [210, 30, 1120, 280],
#                  ]
#
#         # Go through the array above and add platforms
#         for platform in level:
#             block = platforms.Platform(platform[0], platform[1])
#             block.rect.x = platform[2]
#             block.rect.y = platform[3]
#             block.player = self.player
#             self.platform_list.add(block)
#
#
#         gol = Golem.Golem();
#         gol.rect.x = 1500
#         gol.rect.y = 300
#         gol.player = self.player
#         gol.screen = screen
#         self.boss_man.add(gol)
#
#         #end block
#         theEnd = platforms.Platform(80, 800)
#         theEnd.rect.x = 2000
#         theEnd.rect.y = 0
#         theEnd.player = self.player
#         self.end_blocks.add(theEnd)
#
#
class Level_03 (Level):

    def __init__(self, player, screen):

        """

        :param player: Player object
        :param screen: Display window

        Creates skeleton boss level

        """

        Level.__init__(self, player, screen)

        level = [[platforms.SAND_GROUND, -1, 670],
                 [platforms.SAND_GROUND, 259, 670],
                 [platforms.SAND_GROUND, 519, 670],
                 [platforms.SAND_GROUND, 779, 670],

                 [platforms.SAND_GROUND, -1, -81],
                 [platforms.SAND_GROUND, 259, -81],
                 [platforms.SAND_GROUND, 519, -81],
                 [platforms.SAND_GROUND, 779, -81],

                 [platforms.SAND_BIG, -231, 29],
                 [platforms.SAND_BIG, constants.SCREEN_WIDTH -30, 29],


                 [platforms.SAND_FLOAT, 140, 400],
                 [platforms.SAND_FLOAT, 599, 400],
                 [platforms.SAND_FLOAT, 140, 120],
                 [platforms.SAND_FLOAT, 599, 120],
                 ]

        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        background = platforms.backgroundSand()
        background.rect.x = 0
        background.rect.y = 0
        self.decor.add(background)

        ske = Skeleton.Skeleton();
        ske.rect.x = 375
        ske.rect.y = 0
        ske.player = self.player
        ske.screen = screen
        ske.quick_sand = self.platform_quicksand
        self.attacks = ske.attacks
        ske.boss = self.behind_boss_man
        self.behind_boss_man.add(ske)



class Level_04 (Level):

    def __init__(self, player, screen):

        """

        :param player: Player object
        :param screen: Display window

        Creates golem boss level

        """

        Level.__init__(self, player, screen)

        #be sure to have blocks you cant wall jump, to keep player within boss area and so boss attacks dont collide
        level = [[platforms.GRASS_MID, 0, 640],
                 [platforms.GRASS_MID, 210, 640],
                 [platforms.GRASS_MID, 420, 640],
                 [platforms.GRASS_MID, 630, 640],
                 [platforms.GRASS_RIGHT, -83, 290],
                 [platforms.GRASS_RIGHT, -83, 100],
                 ]

        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)



        levelOt = [[platforms.GRASS_MID, 430, 500],
                   [platforms.GRASS_MID, 130, 510],
                   [platforms.GRASS_MID, 280, 400],
                   [platforms.GRASS_MID, 220, 200],
                   [platforms.GRASS_MID, 150, 300],
                   ]

        for platform in levelOt:
            block = platforms.FallPlatform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_fallthrough.add(block)


        levelDecFall = [[platforms.GRASS_DIRT, 220, 272],
                        [platforms.GRASS_DIRT, 150, 372],
                        [platforms.GRASS_DIRT, 280, 472],
                        [platforms.GRASS_DIRT, 430, 572],
                        [platforms.GRASS_DIRT, 130, 582],
                        ]

        for platform in levelDecFall:
            block = platforms.FallPlatform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.decorLayer.add(block)

        background = platforms.backgroundGrass()
        background.rect.x = 0
        background.rect.y = 0
        self.decor.add(background)

        golBody = platforms.forGol(platforms.GOLEM)
        golBody.rect.x = 750
        golBody.rect.y = 400
        golBody.player = self.player
        self.kill_blocks.add(golBody)

        gol = Golem.Golem();
        gol.rect.x = 700
        gol.rect.y = 100
        gol.player = self.player
        gol.screen = screen
        gol.boss = self.boss_man
        self.boss_man.add(gol)








class Level_05 (Level):

    def __init__(self, player, screen):

        """

        :param player: Player object
        :param screen: Display window

        Creates magma boss level

        """

        Level.__init__(self, player, screen)

        #be sure to have blocks you cant wall jump, to keep player within boss area and so boss attacks dont collide

        level = [[platforms.STONE_PIECE1, 50, 565],
                 [platforms.STONE_PIECE2, 389, 565],
                 [platforms.STONE_PIECE3, 719, 565],

                 [platforms.STONE_WALL, -200, -200],
                 [platforms.STONE_WALL, 968, -200],

                 [platforms.STONE_PIECE1, 50, -56],
                 [platforms.STONE_PIECE2, 389, -56],
                 [platforms.STONE_PIECE3, 719, -56],

                 ]


        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)


        lava = [[platforms.LAVA, 0, 615],
                [platforms.LAVA, -1056, 615],
                ]

        for burn in lava:
            block = platforms.lava(burn[0])
            block.rect.x = burn[1]
            block.rect.y = burn[2]
            block.player = self.player
            self.kill_blocks.add(block)

        background = platforms.backgroundMag()
        background.rect.x = 0
        background.rect.y = 0
        self.decor.add(background)


        mag = Magma.Magma();
        mag.rect.x = 500
        mag.rect.y = 200
        mag.player = self.player
        mag.screen = screen
        mag.boss = self.boss_man
        self.boss_man.add(mag)



