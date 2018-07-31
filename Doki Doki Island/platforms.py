"""
Module for managing platforms.

Imports:
    pygame: Tools to be used for sprite
    spritesheet_functions: Allows use for custom sprites
    constants: For screen height and width

Variables:
    GRASS_MID = Coords for sprite
    GRASS_RIGHT_CORNER = Coords for sprite
    GRASS_RIGHT = Coords for sprite
    GRASS_LEFT = Coords for sprite
    GRASS_LEFT_CORNER = Coords for sprite
    GRASS_DIRT = Coords for sprite
    SAND_GROUND = Coords for sprite
    SAND_WITHIN = Coords for sprite
    SAND_FLOAT = Coords for sprite
    SAND_BIG = Coords for sprite
    STONE_PIECE1 = Coords for sprite
    STONE_PIECE2 = Coords for sprite
    STONE_PIECE3 = Coords for sprite
    STONE_PIECE4 = Coords for sprite
    STONE_WALL = Coords for sprite
    LAVA = Coords for sprite
    PORTAL = Coords for sprite
    GOLEM = Coords for sprite

"""
import pygame
import constants as constants
from spritesheet_functions import SpriteSheet
# from spritesheet_functions import SpriteSheet



GRASS_MID = [519, 144, 211, 76]
GRASS_RIGHT_CORNER = [869, 484, 83, 93]
GRASS_RIGHT_EDGE = [849, 144, 86, 76]
GRASS_RIGHT_EDGE_DIRT = [849, 234, 86, 221]
GRASS_RIGHT = [869, 579, 83, 211]
GRASS_RIGHT_LONG = [179, 144, 83, 441]
GRASS_LEFT_CORNER = [355, 484, 83, 93]
GRASS_LEFT_EDGE = [352, 142, 86, 76]
GRASS_LEFT_EDGE_DIRT = [362, 232, 86, 221]
GRASS_LEFT = [355, 599, 83, 211]
GRASS_LEFT_LONG = [49, 144, 83, 631]
GRASS_DIRT = [519, 231, 211, 221]
GRASS_DIRT_LONG = [519, 462, 211, 441]

SAND_GROUND = [499, 1019, 261, 111]
SAND_LONG_GROUND = [0, 839, 1430, 660]
SAND_PYRAMID_LONG = [7, 296, 1278, 114]
SAND_WITHIN = [499, 1144, 261, 151]
SAND_FLOAT = [214, 1019, 261, 199]
SAND_BIG = [214, 1242, 261, 642]

STONE_PIECE1 = [1032, 149, 231, 76]
STONE_PIECE2 = [1032, 257, 231, 76]
STONE_PIECE3 = [1032, 347, 231, 76]
STONE_PIECE4 = [1032, 442, 231, 76]

STONE_WALL = [1234, 567, 231, 928]

LAVA = [3, 599, 1056, 118]

PORTAL = [29, 869, 211, 58]

GOLEM = [787, 399, 213, 533]







class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, spriteCho):

        """
        :param spriteCho: The chosen sprite to use
        """

        super().__init__()

        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("Terrain.png")

        image = sprite_sheet.get_image(spriteCho[0], spriteCho[1], spriteCho[2], spriteCho[3])
        self.image = image

        self.rect = self.image.get_rect()


class FallPlatform(pygame.sprite.Sprite):
    """ Platform the user can jump on, but just from top """

    def __init__(self, spriteCho):
        """
        :param spriteCho: The chosen sprite to use
        """

        super().__init__()

        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("Terrain.png")

        image = sprite_sheet.get_image(spriteCho[0], spriteCho[1], spriteCho[2], spriteCho[3])
        self.image = image

        self.rect = self.image.get_rect()


class ChooseLev(pygame.sprite.Sprite):
    """ Portal user can choose """

    def __init__(self, spriteCho, world):
        """
        :param spriteCho: The chosen sprite to use
        """

        super().__init__()

        self.choice = world

        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("Terrain.png")

        image = sprite_sheet.get_image(spriteCho[0], spriteCho[1], spriteCho[2], spriteCho[3])
        self.image = image

        self.rect = self.image.get_rect()

class nextHub(pygame.sprite.Sprite):
    """ Portal user can choose """

    def __init__(self, spriteCho, world):
        """
        :param spriteCho: The chosen sprite to use
        """

        super().__init__()

        self.choice = world

        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("Terrain.png")

        image = sprite_sheet.get_image(spriteCho[0], spriteCho[1], spriteCho[2], spriteCho[3])
        self.image = image

        self.rect = self.image.get_rect()


class forGol(pygame.sprite.Sprite):
    """ The golem body
    """

    def __init__(self, spriteCho):
        """
        :param spriteCho: The chosen sprite to use
        """

        super().__init__()

        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("Golem.png")

        image = sprite_sheet.get_image(spriteCho[0], spriteCho[1], spriteCho[2], spriteCho[3])
        self.image = image

        self.rect = self.image.get_rect()


class backgroundGrass(pygame.sprite.Sprite):
    """ The grass boss and hub background
    """

    def __init__(self):
        """
        :param spriteCho: The chosen sprite to use
        """

        super().__init__()

        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("backGrass.png")

        image = sprite_sheet.get_image(0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        self.image = image

        self.rect = self.image.get_rect()

class backgroundSand(pygame.sprite.Sprite):
    """ The sand boss background
    """

    def __init__(self):
        """
        :param spriteCho: The chosen sprite to use
        """

        super().__init__()

        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("skeBack.png")

        image = sprite_sheet.get_image(0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        self.image = image

        self.rect = self.image.get_rect()


class backgroundSandHub(pygame.sprite.Sprite):
    """ The sand boss background
    """

    def __init__(self):
        """
        :param spriteCho: The chosen sprite to use
        """

        super().__init__()

        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("backSand.png")

        image = sprite_sheet.get_image(0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        self.image = image

        self.rect = self.image.get_rect()


class hubSandBits(pygame.sprite.Sprite):
    """ The sand boss background
    """

    def __init__(self, spriteCho):
        """
        :param spriteCho: The chosen sprite to use
        """

        super().__init__()

        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("SandHub.png")

        image = sprite_sheet.get_image(spriteCho[0], spriteCho[1], spriteCho[2], spriteCho[3])
        self.image = image

        self.rect = self.image.get_rect()


class backgroundMag(pygame.sprite.Sprite):
    """ the magma boss background
    """

    def __init__(self):
        """
        :param spriteCho: The chosen sprite to use
        """

        super().__init__()

        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("magBack.png")

        image = sprite_sheet.get_image(0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        self.image = image

        self.rect = self.image.get_rect()


class lava(pygame.sprite.Sprite):
    """ The lava
    """

    def __init__(self, spriteCho):
        """
        :param spriteCho: The chosen sprite to use
        """

        super().__init__()

        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("Lava.png")

        image = sprite_sheet.get_image(spriteCho[0], spriteCho[1], spriteCho[2], spriteCho[3])
        self.image = image

        self.rect = self.image.get_rect()

    def update(self):
        """
        Updates lava, making it move to the right
        """

        self.rect.x += 3

        if self.rect.x >= constants.SCREEN_WIDTH:
            self.rect.x = -1109

