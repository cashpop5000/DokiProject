"""
This module is used to hold the Player class. The Player represents the user-
controlled sprite on the screen.
"""
import pygame

import constants as constants
from spritesheet_functions import SpriteSheet



class Player(pygame.sprite.Sprite):
    """
    This class represents the bar at the bottom that the player controls.
    """

    # -- Methods


    # This holds all the images for the animated walk left/right
    # of our player


    def __init__(self):
        """ Constructor function """
        pygame.mixer.init()
        self.jumpSound = pygame.mixer.Sound('Jump.wav')
        self.hitSound = pygame.mixer.Sound('Smacked.wav')

        #Walking frames
        self.walking_frames_l = []
        self.walking_frames_r = []

        #Idle frames
        self.idle_frames_r = []
        self.idle_frames_l = []

        #Jump frames
        self.jump_rightOrLeft = []

        #falling frames
        self.fall_rightOrLeft = []

        #Hurt frames
        self.hurt_rightOrLeft = []

        #crouch frames
        self.crouch_right = []
        self.crouch_left = []

        #Checks if player can crouch or not
        self.canCrouch = False

        #Used to determine which crouch frame to use
        self.crouching = 0

        #Checks if player is in boss level
        self.bossTime = False
        self.bossChange = False

        #Used for idle frames
        self.normalChange = False

        #Sets player hp and checks if player is dead or hurt
        self.hp = 100
        self.dead = False
        self.hurt = False
        self.getHit = False
        self.hurtCounter = 30


        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("idleTest.png")


        #Right idle
        image = sprite_sheet.get_image(26, 17, 43, 106)
        self.idle_frames_r.append(image)
        self.image = image

        image = sprite_sheet.get_image(89, 17, 49, 106)
        self.idle_frames_r.append(image)

        image = sprite_sheet.get_image(164, 11, 49, 112)
        self.idle_frames_r.append(image)

        image = sprite_sheet.get_image(233, 11, 55, 112)
        self.idle_frames_r.append(image)

        image = sprite_sheet.get_image(308, 17, 49, 106)
        self.idle_frames_r.append(image)

        image = sprite_sheet.get_image(395, 23, 43, 106)
        self.idle_frames_r.append(image)



        #Left idle
        image = sprite_sheet.get_image(26, 17, 43, 106)
        image = pygame.transform.flip(image, True, False)
        self.idle_frames_l.append(image)

        image = sprite_sheet.get_image(89, 17, 49, 106)
        image = pygame.transform.flip(image, True, False)
        self.idle_frames_l.append(image)

        image = sprite_sheet.get_image(164, 11, 49, 112)
        image = pygame.transform.flip(image, True, False)
        self.idle_frames_l.append(image)

        image = sprite_sheet.get_image(233, 11, 55, 112)
        image = pygame.transform.flip(image, True, False)
        self.idle_frames_l.append(image)

        image = sprite_sheet.get_image(308, 17, 49, 106)
        image = pygame.transform.flip(image, True, False)
        self.idle_frames_l.append(image)

        image = sprite_sheet.get_image(395, 23, 43, 106)
        image = pygame.transform.flip(image, True, False)
        self.idle_frames_l.append(image)



        #Walk right
        image = sprite_sheet.get_image(26, 168, 70, 102)
        self.walking_frames_r.append(image)

        image = sprite_sheet.get_image(117, 165, 58, 106)
        self.walking_frames_r.append(image)

        image = sprite_sheet.get_image(198, 167, 46, 103)
        self.walking_frames_r.append(image)

        image = sprite_sheet.get_image(278, 169, 49, 103)
        self.walking_frames_r.append(image)

        image = sprite_sheet.get_image(351, 172, 58, 103)
        self.walking_frames_r.append(image)

        image = sprite_sheet.get_image(431, 172, 57, 103)
        self.walking_frames_r.append(image)

        image = sprite_sheet.get_image(516, 169, 52, 106)
        self.walking_frames_r.append(image)

        image = sprite_sheet.get_image(602, 172, 52, 106)
        self.walking_frames_r.append(image)

        image = sprite_sheet.get_image(46, 291, 49, 105)
        self.walking_frames_r.append(image)

        image = sprite_sheet.get_image(136, 293, 48, 105)
        self.walking_frames_r.append(image)

        image = sprite_sheet.get_image(215, 292, 61, 105)
        self.walking_frames_r.append(image)




        #Walk left
        image = sprite_sheet.get_image(26, 168, 70, 102)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        image = sprite_sheet.get_image(117, 165, 58, 106)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        image = sprite_sheet.get_image(198, 167, 46, 103)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        image = sprite_sheet.get_image(278, 169, 49, 103)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        image = sprite_sheet.get_image(351, 172, 58, 103)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        image = sprite_sheet.get_image(431, 172, 57, 103)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        image = sprite_sheet.get_image(516, 169, 52, 106)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        image = sprite_sheet.get_image(602, 172, 52, 106)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        image = sprite_sheet.get_image(46, 291, 49, 105)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        image = sprite_sheet.get_image(136, 293, 48, 105)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        image = sprite_sheet.get_image(215, 292, 61, 105)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)




        #jump right and left
        image = sprite_sheet.get_image(406, 300, 70, 106)
        self.jump_rightOrLeft.append(image)

        image = pygame.transform.flip(image, True, False)
        self.jump_rightOrLeft.append(image)



        #fall right and left
        image = sprite_sheet.get_image(510, 306, 61, 106)
        self.fall_rightOrLeft.append(image)

        image = pygame.transform.flip(image, True, False)
        self.fall_rightOrLeft.append(image)


        #crouch right
        image = sprite_sheet.get_image(37, 425, 43, 106)
        self.crouch_right.append(image)

        image = sprite_sheet.get_image(129, 430, 46, 97)
        self.crouch_right.append(image)

        image = sprite_sheet.get_image(203, 467, 52, 61)
        self.crouch_right.append(image)


        #crouch left
        image = sprite_sheet.get_image(37, 425, 43, 106)
        image = pygame.transform.flip(image, True, False)
        self.crouch_left.append(image)

        image = sprite_sheet.get_image(129, 430, 46, 97)
        image = pygame.transform.flip(image, True, False)
        self.crouch_left.append(image)

        image = sprite_sheet.get_image(203, 467, 52, 61)
        image = pygame.transform.flip(image, True, False)
        self.crouch_left.append(image)


        #hurt right and left
        image = sprite_sheet.get_image(505, 439, 70, 100)
        self.hurt_rightOrLeft.append(image)

        image = pygame.transform.flip(image, True, False)
        self.hurt_rightOrLeft.append(image)


        #Checks if player wins level
        self.winner = False

        #Used for idle frames
        self.idleCho = 0
        self.idleChange = 0

        #gets the rect of the image
        self.rect = self.image.get_rect()

        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0

        # List of sprites we can bump against
        self.level = None

        # Player's bullets
        self.bullets = None

        #Sets the player's initial direction
        self.direction = 'r'

    def update(self,hugRight,hugLeft):
        """ Move the player. """
        # Gravity
        self.calc_grav(hugRight, hugLeft)


        self.rect.y += 2
        slime_hit_list = pygame.sprite.spritecollide(self, self.level.platform_slime, False)
        self.rect.y -= 2

        # Checks to see if player is on a slime block, slows them down
        if len(slime_hit_list) > 0 and (self.change_x > 0 or 0 > self.change_x):
            if self.change_x > 0:
                self.change_x = 2
            else:
                self.change_x = -2

        # Move left/right
        self.rect.x += self.change_x

        # If player is not hurt, changes direction based on if player is mvoing left/right
        if self.change_x < 0 and not self.hurt:
            self.direction = 'l'
        elif self.change_x > 0 and not self.hurt:
            self.direction = 'r'


        #if the player is hurt
        if self.hurt:
            self.stumble()

        #Plays sound when player is hit
        if self.getHit:
            self.hitSound.play()
            self.getHit = False

        #If hp is 0, player is dead
        if self.hp <= 0:
            self.dead = True

        #When player stops moving, stes the player back to idle frames
        if self.normalChange:
            self.image = self.idle_frames_r[0]
            self.rect = self.image.get_rect()
            self.normalChange = False

        #If plauyer touches a kill block, will insta-die
        kill_hit_list = pygame.sprite.spritecollide(self, self.level.kill_blocks, False)
        if len(kill_hit_list) > 0:
            self.hp = 0
            self.dead = True




        # Checks to see if player collided with a slime block from left/right
        slime_hit_list = pygame.sprite.spritecollide(self, self.level.platform_slime, False)
        for block in slime_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right


        # HITTING REGULAR PLATFORMS
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.

            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

        #Checks to see if player hits a fallblock
        FallBlock_hit_list = pygame.sprite.spritecollide(self, self.level.platform_fallthrough, False)
        for block in FallBlock_hit_list:
            # Reset our position based on the top/bottom of the object.

            if self.change_y > 0 and block.rect.top + 5 >= self.rect.bottom >= block.rect.top - 7:
                self.rect.bottom = block.rect.top
                self.change_y = 0

            # Stop our vertical movement only if player lands on top

        # Checks if player is in quicksand
        Quick_hit_list = pygame.sprite.spritecollide(self, self.level.platform_quicksand, False)
        for block in Quick_hit_list:

            if self.change_y > 0:
                self.change_y = 1
            # Causes player to slowly descend

        # Checks to see if player collided with a slime block from top/bottom
        slime_hit_list = pygame.sprite.spritecollide(self, self.level.platform_slime, False)
        for block in slime_hit_list:

            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

        #Grabs player's current position
        x = self.rect.x
        y = self.rect.y

        #Allows the player to be hit again
        if self.hurtCounter <= 0:
            self.hurt = False
            self.hurtCounter = 30
            self.change_x = 0


        #All this sets what sprites you see on the player

        #If player is hurt, use hurt sprites
        if self.hurt:
            self.hurtCounter -= 1

            if self.direction == 'r':
                self.image = self.hurt_rightOrLeft[0]
            elif self.direction == 'l':
                self.image = self.hurt_rightOrLeft[1]

        #Crouch sprites
        elif self.canCrouch:

            if self.crouching <= 15:
                self.crouching += 1

            if self.direction == 'r':
                if 10 > self.crouching >= 5:
                    self.image = self.crouch_right[0]
                if 15 > self.crouching >= 10:
                    self.image = self.crouch_right[1]
                if self.crouching >= 15:
                    self.image = self.crouch_right[2]

            if self.direction == 'l':
                if 20 > self.crouching >= 10:
                    self.image = self.crouch_left[0]
                if 30 > self.crouching >= 20:
                    self.image = self.crouch_left[1]
                if self.crouching >= 30:
                    self.image = self.crouch_left[2]

            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

        #Idle spries
        elif self.change_x == 0 and self.change_y == 0:

            self.idleChange += 1

            if self.idleChange == 10:
                self.idleCho += 1
                self.idleChange = 0

            if self.idleCho >= len(self.idle_frames_r):
                self.idleCho = 0

            if self.direction == 'r':
                self.image = self.idle_frames_r[self.idleCho]
            elif self.direction == 'l':
                self.image = self.idle_frames_l[self.idleCho]

        #Jump sprites
        elif self.change_y > 0:
            if self.direction == 'r':
                self.image = self.fall_rightOrLeft[0]
            elif self.direction == 'l':
                self.image = self.fall_rightOrLeft[1]

        #Fall spries
        elif self.change_y < 0:
            if self.direction == 'r':
                self.image = self.jump_rightOrLeft[0]
            elif self.direction == 'l':
                self.image = self.jump_rightOrLeft[1]

        #Walking sprites
        elif (self.change_x > 0 or self.change_x < 0) and self.change_y == 0:

            pos = self.rect.x + self.level.world_shift

            if self.direction == 'r':
                if not self.bossChange:
                    pos = -pos
                frame = (pos // 30) % len(self.walking_frames_r)
                self.image = self.walking_frames_r[frame]

            elif self.direction == 'l':
                if self.bossChange:
                    pos = -pos
                frame = (pos // 30) % len(self.walking_frames_l)
                self.image = self.walking_frames_l[frame]

        #If not sprites used, sets the variables
        else:
            self.idleChange = 0
            self.idleCho = 0
            self.crouching = 0
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

        #If player is in a boss level, sets this variable
        if self.bossTime:
            self.bossChange = True

        #If player leaves boss level, stes this to false
        if not self.bossChange:
            self.bossTime = False

        #Makes the player small when in a boss level
        if self.bossTime:
            self.image = pygame.transform.scale(self.image, (30, 65))
            x = self.rect.x
            y = self.rect.y
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y



    def calc_grav(self, hugR, hugL):
        """ Calculate effect of gravity. """

        #See if player is touching a wall to the right/left
        self.rect.x += 2
        tugWallR = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.x -= 2

        self.rect.x -= 2
        tugWallL = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.x += 2

        if self.change_y == 0:
            self.change_y = 1

        #If player is hugging a wall and the appropriate bool is true, allows player to cling to wall
        elif (len(tugWallR) > 0 and hugR) or (len(tugWallL) > 0 and hugL):
            if self.change_y <= 0:
                self.change_y += .65
            else:
                self.change_y += .02
                if self.change_y > 1:
                    self.change_y = 1
        #Player falls, but doesn't go faster than 10 pixels
        else:
            self.change_y += .35

            if self.change_y >= 10:
                self.change_y = 10



    def jump(self, hugR, hugL):
        """
        :param hugR: True if player is holding down right key
        :param hugR: True if player is holding down left key
        Called when user hits 'jump' button.
         """


        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        FallBlock_hit_list = pygame.sprite.spritecollide(self, self.level.platform_fallthrough, False)
        Quick_hit_list = pygame.sprite.spritecollide(self, self.level.platform_quicksand, False)
        Slime_hit_list = pygame.sprite.spritecollide(self, self.level.platform_slime, False)
        self.rect.y -= 2

        #See if we're on the specific blocks
        fallJump = False
        QSjump = False
        SLjump = False

        #If on a fallblock, sets to true
        for block in FallBlock_hit_list:
            if block.rect.top + 2 >= self.rect.bottom >= block.rect.top - 2:
                fallJump = True

        #Sets true if we are in quick sand
        for block in Quick_hit_list:
            QSjump = True

        #Sets true if we are touching slime
        for block in Slime_hit_list:
            SLjump = True


        # If it is ok to jump, set our speed upwards

        if fallJump:
            self.change_y = -10
            self.jumpSound.play()

        if QSjump:
            self.rect.y -= 2
            OutOfIt = pygame.sprite.spritecollide(self, self.level.platform_quicksand, False)
            self.rect.y += 2

        #If player is out of quick sand, jump normally to escape, otherwise very low jump height
            if len(OutOfIt) == 0:
                self.change_y = -10
                self.jumpSound.play()
            else:
                self.change_y = -3

        #if on slime, lower jump height
        if SLjump:
            self.jumpSound.play()
            self.change_y = -7


        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 :
            self.jumpSound.play()
            self.change_y = -10

        #Checks to see if player is touching a wall
        self.rect.x += 2
        tugWallR = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.x -= 2

        self.rect.x -= 2
        tugWallL = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.x += 2

        #If player is touching a wall, allows player to walljump
        if len(tugWallR) > 0 and hugR:
            self.change_y = -8
            self.jumpSound.play()
            self.change_x = -2

        if  len(tugWallL) > 0 and hugL:
            self.change_y = -8
            self.jumpSound.play()
            self.change_x = 2


    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.direction = 'l'
        self.change_x = -6
        self.canCrouch = False
        self.crouching = 0

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.direction = 'r'
        self.change_x = 6
        self.canCrouch = False
        self.crouching = 0

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0

    def crouch(self):
        """
         Called when user his the down key
        """
        self.canCrouch = True


    def stand(self):
        """
        called when user lets go down key
        """
        self.canCrouch = False
        self.crouching = 0



    def stumble(self):
        """
        Called when user is is hit
        """

        # Makes user 'stumble' backwards when hurt
        if self.direction == 'r':
            self.change_x = -2
        if self.direction == 'l':
            self.change_x = 2
        self.crouch = False






