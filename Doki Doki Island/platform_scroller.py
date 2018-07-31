""" The entire game, used Keenan's platform_scroller example and expanded on it

Imports:
    pygame: For tools to make the game
    constants: Initially used for testing with the colors, but mostly for screen width and height
    levels: For the player to run around on
    menu: For the titlescreen when the game starts
    player: The hero for the user to control
    attack1: (Indev) melee attack
    attack2: Shoots energy balls
    attack3: A short range laser attack
    attack4: Shoots two energy balls in a two waves
    black: Used for transitioning
    backgroundTitle: The background for the titlescreen
    winning: When the player beats the boss, a 'clear' will appear


Game art drawn by me
OST from Rabi-Rabi

"""

import pygame

import constants as constants
import levels as levels
from menu import TitleScreen as Title
from menu import Button1 as But1
from menu import Button2 as But2

from player import Player
from attack1 import Hammer
from attack2 import Shooter
from attack3 import Laser
from attack4 import Wave

import black as black
import backgroundTitle as backgroundTitle

import winning as winning



def main():
    """ Main Program

    First initializes pygame and pygame.mixer

    variables:
        size: The size of the window
        screen: Sets the display for the game
        player: The player object
        title: The title itself
        butOne: The start button
        butTwo: Load game (didn't implement)
        hubLevel: Where the player begins and is able to choose other levels
        golBossLev: The golem boss
        skeBossLev: The skeleton boss
        magBosLev: The magma boss
        level_list: Holds the levels in a list
        TwoBut: Holds the starting buttons
        menuSelect: determins which button is currently selected
        cover: Used for transitions
        backTitle: background for the title
        current_level_no: The number of the current level the player is in
        current_level: The current level the player is in
        active_sprite_list: Used to hold the player sprite
        slash: Holds the melee sprite
        bullets: Holds the bullet sprites
        beampew: Holds the laser sprite
        begin: Holds sprites needed for the titlescreen
        beginBack: Holds the background for the title
        transition: Holds the sprite that covers the screen during transition
        winMes: Holds the win message
        hugLeft: True if player is moving left so they can cling to the wall
        hugRight: True if player is moving right so they can cling to the wall
        done: True if player wants to quit and exit the game
        toIntro: True when player leaves the titlescreen to the game or quit the application
        count2: Used to determine how long the melee attack will stay on screen
        attack: True if player wants to melee attack
        linger: Allows the melee attack to stay on screen
        laser: True if player wants to laser attack
        clock: Used to manage how fast the screen updates
        canSelect: Allows player to select the starting buttons
        ToNextPart: True when player presses the start button to get to the game
        canMove = Allows player to move in game
        canUpdate = Allows game to update most assets
        canChange = Allows player to change level
        fading = True if the game is in the process of a transition
        aboutToFade = True when the player hits a point to begin transition
        worldChosen = The level the player chose
        xLimR = Limits level layout to the right
        xLimL = Limits level layout to the left



    Functions:
        Reset: resets the levels after player loses or lears it

    While loops:
        First loop: The title loop
        Second loop: The main game loop


    """
    pygame.init()
    pygame.mixer.init()


    # Set the height and width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    #Sets the title
    pygame.display.set_caption("Doki Doki Island!")

    # Create the player
    player = Player()

    #Creates the title screen
    title = Title.Start()
    butOne = But1.Start()
    butTwo = But2.Start()

    # Create all the levels
    hubLevel = levels.Level_00(player, screen)
    hubLevel2 = levels.Level_01(player, screen)
    hubLevel3 = levels.Level_01(player, screen)
    golBossLev = levels.Level_04(player, screen)
    skeBossLev = levels.Level_03(player, screen)
    magBossLev = levels.Level_05(player, screen)

    # Appends the levels to the list
    level_list = []
    level_list.append(hubLevel)
    level_list.append(hubLevel2)
    level_list.append(hubLevel3)
    '''level_list.append(golBossLev)'''
    '''level_list.append(skeBossLev)'''
    '''level_list.append(magBossLev)'''

    # To hold the title buttons
    Twobut = []
    menuSelect = 0

    #Used during transitions, fades screen black
    cover = black.Fade(screen)

    #Sets the background in the title screen
    backTitle = backgroundTitle.Start()

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    # All relevant groups for sprites to be used in the game
    active_sprite_list = pygame.sprite.Group()
    slash = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    beampew = pygame.sprite.Group()
    begin = pygame.sprite.Group()
    beginBack = pygame.sprite.Group()
    transition = pygame.sprite.Group()
    winMes = pygame.sprite.Group()


    # Starts the player off in the hub level
    player.level = current_level
    player.bullets = bullets

    # this is to place the character
    player.rect.x = 200
    player.rect.y = 350
    active_sprite_list.add(player)

    #Adds these to their relevant groups
    begin.add(title)
    beginBack.add(backTitle)
    transition.add(cover)


    #Used when player hugs a wall
    hugLeft = False;
    hugRight = False;

    # Loop until the user clicks the close button.
    done = False
    toIntro = False


    count2 = 0
    attack = False
    linger = False
    laser = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    #Loads the first music file, the title screen music
    """pygame.mixer.music.load('RabiRabiMain.ogg')
    pygame.mixer.music.play(-1, 0.0)
    """

    # Used when selecting the buttons on title screen
    canSelect = False
    toNextPart = False

    #----- Title screen -------
    while not toIntro:

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True
                toIntro = True

            if event.type == pygame.KEYDOWN and canSelect:
                if event.key == pygame.K_LEFT:

                    #When use press left key, it selects the left button
                    if menuSelect == 1:
                        menuSelect = 0
                        butOne.highlighted = True
                        butTwo.highlighted = False

                if event.key == pygame.K_RIGHT:

                    #When use press right key, it selects the right button
                    if menuSelect == 0:
                        menuSelect = 1
                        butTwo.highlighted = True
                        butOne.highlighted = False

                if event.key == pygame.K_SPACE:
                    #When use press space key, it selects the button
                    if menuSelect == 1:
                        print('1')

                    if menuSelect == 0:

                        butOne.selected = True

            if event.type == pygame.KEYUP and canSelect:
                if event.key == pygame.K_SPACE:
                    #When player releases space key, then the button chosen will do its action
                    if menuSelect == 1:
                        #Meant for a load file button, but didn't get around to it
                        print('lol')

                    if menuSelect == 0:
                        butOne.selected = False
                        #fade out black, then to main game
                        cover.inout = True
                        cover.go = True
                        toNextPart = True
                        canSelect = False
                        #pygame.mixer.music.fadeout(1000)


        screen.fill(constants.BLUE)


        #Updates and draws the relevant groups for the title screen
        beginBack.update()
        begin.update()
        transition.update()

        beginBack.draw(screen)
        begin.draw(screen)
        transition.draw(screen)

        #Intially, 'cover' will be black. This is to stop the transition once the title screen can be seen
        if cover.time < 0 and cover.go:
            cover.go = False
            cover.time = 0


        #After the title finishes bouncing, the two buttons are added
        if title.change_y == 0 and len(begin) <= 1:
            begin.add(butOne)
            begin.add(butTwo)
            Twobut.append(butOne)
            Twobut.append(butTwo)


        #This to intially highlight the first button once the buttons stop moving
        if butOne.change_y >= 0 and butTwo.change_y >= 0 and not canSelect:
            butOne.highlighted = True
            canSelect = True

        #When the uer chooses an option, the screen will fade and break from the loop, then onto the game
        if toNextPart and cover.inout and cover.time >= 255:
            toIntro = True




        clock.tick(60)
        pygame.display.flip()





    #Variables used for various functions in the game
    canMove = True
    canUpdate = True
    canChange = False
    fading = False
    aboutToFade = True
    worldChosen = 0
    previousWorld = 0
    bossLev = False
    hubLev = True

    xLimR = True
    xLimL = True


    #Resets the levels so the player can play them again if they go back to the specific level
    def reset(player, screen, level_list, worldChosen):

        print(current_level.getOriX())

        if worldChosen == 0:

            current_level.resetHub(current_level.level_x_limit, current_level.level_y_limit)


        elif worldChosen == 1:

            current_level.resetHub(current_level.level_x_limit, current_level.level_y_limit)
            player.rect.x = 600


        elif worldChosen == 3:
            #hubLevel = levels.Level_00(player, screen)
            golBossLev = levels.Level_04(player, screen)

            if len(level_list) < 4:
                level_list.append(golBossLev)
            #level_list[0] = hubLevel
            else:
                level_list[3] = golBossLev




        player.rect.x = 200
        player.rect.y = 350






    # -------- Main Game Loop -----------
    while not done:

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

            if event.type == pygame.KEYDOWN and not player.hurt:
                if event.key == pygame.K_LEFT:
                #Moves the player left
                    if canMove:

                        player.go_left()
                        hugLeft = True
                        hugRight = False
                        player.direction = 'l'
                if event.key == pygame.K_RIGHT:
                #Moves the player right
                    if canMove:
                        player.go_right()
                        hugRight = True
                        hugLeft = False
                        player.direction = 'r'

                if event.key == pygame.K_UP:
                #Makes player jump
                    if canMove:
                        player.jump(hugRight, hugLeft)

                if event.key == pygame.K_DOWN:
                #Makes player crouch
                    if canMove:
                        player.crouch()

                if event.key == pygame.K_y:
                #Allows player to melee attack
                    if canMove:
                        attack = True
                if event.key == pygame.K_w:
                #Allows player to shoot
                    if canMove:
                        shot = Shooter(player)
                        shot.level = current_level
                        bullets.add(shot)

                if event.key == pygame.K_i:
                #Allows player to fire the laser
                    if canMove:
                        laser = True

                if event.key == pygame.K_o:
                #Allows player to fire the wave shot
                    if canMove:
                        waveshot = Wave(player, 1)
                        waveshot2 = Wave(player, -1)
                        bullets.add(waveshot)
                        bullets.add(waveshot2)


            if event.type == pygame.KEYUP and not player.hurt:
                #When player releases left key, stops moving
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                    hugLeft = False
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                #When player releases right key, stops moving
                    player.stop()
                    hugRight = False

                '''if event.key == pygame.K_DOWN:
                #When player releases down key, makes player stand up
                    if canMove:
                        player.stand()'''
                if event.key == pygame.K_i:
                    beampew.empty()


        #checks what level the player is in and if music isn't pkaying at the moment and plays the appropriate song
        """
        if current_level_no == 0 and not pygame.mixer.music.get_busy():
            pygame.mixer.music.load('RabiRabiHub.ogg')
            pygame.mixer.music.play(-1, 0.0)
        elif current_level_no == 1 and not pygame.mixer.music.get_busy():
            pygame.mixer.music.load('RabiRabiRavine.ogg')
            pygame.mixer.music.play(-1, 0.0)
        elif current_level_no == 2 and not pygame.mixer.music.get_busy():
            pygame.mixer.music.load('RabiRabiPandora.ogg')
            pygame.mixer.music.play(-1, 0.0)
        elif current_level_no == 3 and not pygame.mixer.music.get_busy():
            pygame.mixer.music.load('RabiRabiVolcano.ogg')
            pygame.mixer.music.play(-1, 0.0)
        """



        #When player wins, creates the 'clear' that falls down from the top
        if player.winner:
            player.winner = False
            win = winning.win()
            winMes.add(win)
            bullets.empty()
            beampew.empty()

        #When the 'clear' is gone, it begins transition
        if len(winMes) > 0:
            for winThi in winMes:
                if winThi.rect.y >= constants.SCREEN_HEIGHT:
                    winMes.empty()
                    aboutToFade = True
                    worldChosen = previousWorld


        #If player is dead, begin transition
        if player.dead:
            aboutToFade = True
            worldChosen = previousWorld

        #Sets the variables before transitioning
        if aboutToFade and not fading:
            cover.go = True
            canMove = False
            canUpdate = False
            fading = True
            if cover.inout:
                cover.inout = False
            else:
                cover.inout = True
            #pygame.mixer.music.fadeout(800)



        #If true, allows to update the relevant game assets
        if canUpdate:
            active_sprite_list.update(hugRight, hugLeft)
            current_level.update()
            bullets.update(bullets)
            beampew.update(player)
            winMes.update()

            """

            if attack == True:
                swipe = Hammer(player)
                slash.add(swipe)
                linger = True

            if linger == True:
                slash.update()
                count2 += 1

            if count2 == 5:
                slash.empty()
                count2 = 0
                linger = False

            if laser == True:
                beam = Laser(player)
                beampew.add(beam)
                laser = False

            """



        #Used to determine if player is close to an edge of a level
        toTheRight = player.rect.x + current_level.world_shift
        toTheLeft = player.rect.x + current_level.left_x

        #Sets the relevant variables when player reaches an edge from the right or the left
        if toTheRight < current_level.level_x_limit:
            xLimR = False

        if toTheLeft <= 450:
            xLimL = False




        # If the player gets near the right side, shift the world left (-x)
        # Wont shift if in boss level
        if player.rect.x >= 550 and not player.bossChange and xLimR:
            diff = player.rect.x - 550
            player.rect.x = 550
            current_level.shift_world(-diff)
            xLimL = True

        # If the player gets near the left side, shift the world right (+x)
        # Wont shift if in boss level
        if player.rect.x <= 450 and not player.bossChange and xLimL:
            diff = 450 - player.rect.x
            player.rect.x = 450
            current_level.shift_world(diff)
            xLimR = True

        # if player is jumping up, shift the world up when appropriate
        # Wont shift if in boss level
        if player.rect.y <= 150 and not player.bossChange:
            diff = 150 - player.rect.y
            player.rect.y = 150
            current_level.shift_worldY(diff)

        # if player is falling, shift world down when appropriate
        # Wont shift if in boss level
        if player.rect.y >= 500 and not player.bossChange:
            diff = player.rect.y - 500
            player.rect.y = 500
            current_level.shift_worldY(-diff)


        # When a player chose a portal, will transport player to appropriate level
        playerChose = pygame.sprite.spritecollide(player, current_level.platform_choose, False)
        if len(playerChose) > 0 and not aboutToFade:
            aboutToFade = True
            for chosen in playerChose:
                worldChosen = chosen.choice
                if worldChosen < 2:
                    previousWorld = worldChosen
                print(worldChosen)

        #if true, changes the level
        if canChange:
            canChange = False
            print(worldChosen)

            if worldChosen < 2:
                hubLev = True
                bossLev = False
            else:
                bossLev = True
                hubLev = False


            #Checks player's current level and then transports to the approprate level
            if bossLev:
                reset(player, screen, level_list, worldChosen)
                current_level_no = worldChosen
                current_level = level_list[current_level_no]


            elif hubLev:
                current_level_no = worldChosen
                current_level = level_list[current_level_no]
                reset(player, screen, level_list, worldChosen)



            player.level = current_level

            # Checks if player is in a boss level
            if bossLev:
                player.bossTime = True




        # Draws the sprites
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        slash.draw(screen)
        bullets.draw(screen)
        beampew.draw(screen)
        winMes.draw(screen)


        #When the transition is fully finished, it sets the variables
        if cover.time <= 0 and not cover.inout and cover.go:
            cover.go = False
            fading = False
            aboutToFade = False
            canMove = True
            canUpdate = True


        #As the screen is fully black, sets the variables
        if cover.time >= 255 and cover.inout and cover.go:
            cover.inout = False
            canChange = True
            player.hp = 100
            player.dead = False
            player.bossTime = False

            #If the player's last level was a boss level, sets these variables
            if bossLev:
                player.bossTime = False
                player.bossChange = False
                player.normalChange = True
                player.hurtCounter = 0
                '''player.rect.y = 450'''
                active_sprite_list.update(hugRight, hugLeft)
                active_sprite_list.draw(screen)

            #If the player's last level was the hub level, sets these variables
            else:
                player.bossTime = True
                print("yo")
                active_sprite_list.update(hugRight, hugLeft)
                active_sprite_list.draw(screen)




        # if true, does the transition
        if fading:
            transition.update()
            transition.draw(screen)

        #For hammer, prevents multiple melee attacks in one spot
        #attack = False




        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()


if __name__ == "__main__":
    main()


