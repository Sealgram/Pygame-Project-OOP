# Note That all comments are referencing the line/lines directly above them. Block comments reference the functions
# and classes directly below them.

import pygame, random, time
# imports needed modules into the game
# global variable is defined for how many leviathans (the enemy) are active in my game.

'''
The below class is created for my player sprite, the seamoth. It defines the seamoth, as well as the seamoth's
location, and orientation to be used in the pygame loop.
'''


class Seamoth(pygame.sprite.Sprite):
    # the class is defined, the parameter letting the program know it is a pygame sprite
    def __init__(self, x, y, orientation):
        # init function within the class including all parameters
        super().__init__()
        # initiating super, which allows us to avoid directly referencing the base class (where it is specified that
        # this class is a pygame sprite, taking the pygame native )
        self.imageleft = pygame.image.load('Assets/Sprites/seamoth.png').convert_alpha()
        self.imageleft = pygame.transform.scale(self.imageleft, (80, 46))
        self.imageright = pygame.transform.flip(self.imageleft, True, False)
        # loads the sprite image and flips it in one variable
        if orientation:
            self.image = self.imageright
        else:
            self.image = self.imageleft
        # uses the parameter 'orientation', which is either true or false, to determine if the image is flipped.
        self.rect = self.image.get_rect()
        # defines the image size as self.rect
        self.rect.x = x
        self.rect.y = y
        # defines the location of the sprite as the parameters x and y


'''
The below class is created for one of my enemy sprites, the Reaper Leviathan. It defines the reaper, as well as the 
reaper's location, and orientation to be used in the pygame loop. The code is almost identical to the one in the class
above, (the only major difference being that in this one orientation will either be a zero or a 1, instead of a true
or a false) so I will leave it uncommented.
'''


class Reaper(pygame.sprite.Sprite):
    def __init__(self, x, y, orientation):
        super().__init__()
        self.imageleft = pygame.image.load('Assets/Sprites/Reaper Leviathan.png')
        self.imageleft = pygame.transform.scale(self.imageleft, (300, 209))
        self.imageright = pygame.transform.flip(self.imageleft, True, False)
        if orientation == 1:
            self.image = self.imageright
        else:
            self.image = self.imageleft
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


'''
The below class is created for one of my enemy sprites, the Ghost Leviathan. It defines the ghost, as well as the 
ghost's location, and orientation to be used in the pygame loop. The code is almost identical to the one in the class
for the seamoth, (the only major difference being that in this one orientation will either be a zero or a 1, instead of a true
or a false) so I will leave it uncommented.
'''


class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y, orientation):
        super().__init__()
        self.imageleft = pygame.image.load('Assets/Sprites/Ghost Leviathan.png')
        self.imageleft = pygame.transform.scale(self.imageleft, (300, 209))
        self.imageright = pygame.transform.flip(self.imageleft, True, False)
        if orientation == 1:
            self.image = self.imageright
        else:
            self.image = self.imageleft
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


'''
The following function will spit out the chance a leviathan has to spawn based on the depth of the seamoth, returning
that to where the function was called from. The chance goes up the deeper you get, as you can see in the code below.
The reason it is so high in the beginning is because this function will be called rapidly- even though it is a 1 in
15 chance of spawning, you will most likely see one within 5 seconds of descending past 50m.
'''


def leviathanchance(depth):
    if depth < 50:
        chance = 0
    elif 50 < depth < 150:
        chance = random.randint(0, 15)
    elif 150 < depth < 300:
        chance = random.randint(0, 10)
    elif 300 < depth < 450:
        chance = random.randint(0, 8)
    elif 450 < depth < 600:
        chance = random.randint(0, 4)
    elif depth > 600:
        chance = random.randint(0, 1)
    else:
        chance = 1
    return chance


'''
The below function takes in depth as a parameter and returns all the attributes for a leviathan about to be spawned.
They are random for the most part, but the deeper you go the more dangerous the attributes are going to be (the 
leviathans will be faster, move sideways at more of an angle, etc.) Also, this function defines what kind of leviathan
will spawn, so you will see more reapers in shallow water, and more ghosts in deeper water.
'''


def leviathanattributes(depth):
    angleseasy = [0, 2, 4]
    angleshard = [6, 8, 12]
    speedseasy = [6, 10, 14]
    speedshard = [16, 18, 20]
    levtypes1 = ['Reaper', 'Reaper', 'Ghost']
    levtypes2 = ['Ghost', 'Ghost', 'Reaper']
    # all the attributes that will be randomly chosen are put in lists, which then can be randomly drawn from
    # based on the depth.
    if depth < 150:
        speed = random.choice(speedseasy)
        angle = random.choice(angleseasy)
        leviathantype = 'Reaper'
    elif depth < 150:
        speed = random.choice(speedseasy)
        angle = random.choice(angleseasy)
        leviathantype = 'Reaper'
    elif depth < 300:
        speed = random.choice(speedshard)
        angle = random.choice(angleshard)
        leviathantype = 'Reaper'
    elif depth < 450:
        speed = random.choice(speedshard)
        angle = random.choice(angleshard)
        leviathantype = random.choice(levtypes1)
    elif depth < 600:
        speed = random.choice(speedshard)
        angle = random.choice(angleshard)
        leviathantype = random.choice(levtypes2)
    else:
        speed = random.choice(speedshard)
        angle = random.choice(angleshard)
        leviathantype = 'Ghost'
    return [speed, angle, leviathantype]
    # returns the three selected attributes back to the function's call origin


'''
The function below is a simple function that plays a roar sound effect based on what type of roar is inputted as the
parameter (the ghost's roar or the reaper's roar).
'''


def roar(roartype):
    reaper_roar = pygame.mixer.Sound("Assets/SoundEffects/Reaper Roar.wav")
    ghost_roar = pygame.mixer.Sound("Assets/SoundEffects/Ghost Roar.wav")
    # defining variables aas the sound effects
    if roartype == 'Reaper':
        pygame.mixer.Sound.play(reaper_roar)
        pygame.mixer.music.stop()
    elif roartype == 'Ghost':
        pygame.mixer.Sound.play(ghost_roar)
        pygame.mixer.music.stop()
    # playing the sound effects based on the parameter


'''
This simple function opens the text document that the game's highscore is stored in, and returns it as an integer
to the function's call location
'''


def getscore():
    stored = open('Highscore', 'r')
    score = stored.read().strip()
    return int(score)


'''
This is another simple function that takes in the current score as a parameter from where it is called, checks if that
score is above the highscore, and if it is, replaces the highscore with the current score.
'''


def savescore(score):
    scoresaved = getscore()
    if score > scoresaved:
        stored = open('Highscore', 'w')
        stored.write(str(score))


'''
The below function is used to find the backgrounds that appear throughout the game as you progress. When it is called,
It takes in two parameters, the current depth, and 'iteration', which will be a random number between 0 and 3.
The function opens the text document where all the paths are stored, and splits them along a question mark, which will
make a list of all the paths split by depth category. It then splits each piece of the list again by all the \ns which
got carried in with the background directories file, making a 2d list of categories and directories that can be
targeted accordingly.
'''


def getbackground(depth, iteration):
    depthpaths = open('BackgroundDirectories', "r")
    depthpathslist = depthpaths.read()
    depthpathslist = depthpathslist.split("?")
    bglist = []
    for i in depthpathslist:
        bglist.append(i.split("\n"))
    # opens the text file, and creates the 2d list, as defined above
    if depth < 100:
        background = pygame.image.load(bglist[0][iteration])
    elif 100 < depth < 200:
        background = pygame.image.load(bglist[1][iteration + 1])
    elif 200 < depth < 300:
        background = pygame.image.load(bglist[2][iteration + 1])
    elif 300 < depth < 400:
        background = pygame.image.load(bglist[3][iteration + 1])
    elif 400 < depth < 500:
        background = pygame.image.load(bglist[4][iteration + 1])
    elif 500 < depth < 600:
        background = pygame.image.load(bglist[5][iteration + 1])
    elif depth > 600:
        background = pygame.image.load(bglist[5][iteration + 1])
    else:
        background = pygame.image.load(bglist[0][iteration + 1])
        # gets the proper background based on the depth and iteration parameters
    background = pygame.transform.scale(background, (960, 540))
    # transforms the background to scale to the game size
    return background
    # returns the chosen background to the function call


'''
The following function is used to draw text on the desired surface you would like to draw text upon. It takes in
multiple variables: the surface, the text contents, the text size, the text color, the font name, and the position.
It then uses those parameters to draw up the text, and blit it to the desired surface.
'''


def draw_text(surf, text, size, color, font_name, x, y):
    font = pygame.font.SysFont(font_name, size)
    # finds the font and loads it with the proper size
    text_surface = font.render(text, True, color)
    # renders the font with the text and color
    text_rect = text_surface.get_rect()
    # finds the size of the rendered text
    text_rect.midtop = (x, y)
    # places the text with x and y in the middle top
    surf.blit(text_surface, text_rect)
    # blits the text to the surface


'''
The following function is one of the three main interface functions for my code: the start menu. it displays a start
screen when the code is run, which displays the highscore, as well as the game's name and a cool background. the player
must press any button to begin the game when this screen is up.
'''


def start_menu():
    pygame.init()
    # initializing pygame
    display_width = 960
    display_height = 540
    # defining the display width and height as variables so they can be referenced multiple times in the code
    white = (255, 255, 255)
    # defining white's RGB color code
    backgrounds = ['Assets/Backgrounds/loadingscreen1.jpg',
                   'Assets/Backgrounds/loadingscreen2.jpg',
                   'Assets/Backgrounds/loadingscreen3.png',
                   'Assets/Backgrounds/loadingscreen4.jpg',
                   'Assets/Backgrounds/loadingscreen5.jpg',
                   'Assets/Backgrounds/loadingscreen6.png']
    # creating a list of possible loading screens
    background = pygame.image.load(random.choice(backgrounds))
    # picks one of the possible loading screens to be the background for the starting menu
    pygame.mixer.music.load('Assets/SoundEffects/Salutations.mp3')
    pygame.mixer.music.play(-1)
    # loads and plays the menu music
    title = pygame.image.load('Assets/General/Title.png')
    start = pygame.image.load('Assets/General/ClicktoStart.png')
    highscore = pygame.image.load('Assets/General/Highscore.png')
    # loads the three images that will be blitted onto the menu
    gamedisplay = pygame.display.set_mode((display_width, display_height))
    # defines the game display size
    pygame.display.set_caption('Reaper')
    # sets the display caption
    font_name = 'Helvetica'
    # big surprise, we're using helvetica (i couldn't get my custom font to work properly)
    icon = pygame.image.load('Assets/General/alterra logo.png')
    pygame.display.set_icon(icon)
    # loads and sets the icon for the game
    clock = pygame.time.Clock()
    # defines the pygame clock
    crashed = False
    exitgame = False
    # defines both crashed and exitgame as false
    while not crashed:
        # while crashed is false, loop is active
        gamedisplay.blit(background, (0, 0))
        gamedisplay.blit(title, (330, 100))
        gamedisplay.blit(start, (350, 300))
        gamedisplay.blit(highscore, (285, 200))
        # blits the background and proper images onto the game display
        draw_text(gamedisplay, str(getscore()) + ' metres', 25, white, font_name, 650, 240)
        # displays the metre highscore on the main screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
                exitgame = True
                # if the player presses the red x on the top corner of the screen, sets both variables to true so the
                # code itself will exit
            if event.type == pygame.KEYDOWN:
                crashed = True
                exitgame = False
                # if the player presses any key (press any key to begin) closes this window and begins the next one.)
        pygame.display.flip()
        # flips the display
        clock.tick(60)
        # ticks the pygame clock 60
    if exitgame:
        quit()
        # if the exitgame value is true (the player pressed the red x), the code quits
    maingame()
    # once the loop is broken, calls the maingame function with the parameter exitgame


'''
The following function is the function that contains the main interface and functionality of the game, including the
spawning and controlling of sprites, and the functionality to keep score, change the backgrounds, and collide with the
enemy sprites, thus losing the game.
'''


def maingame():
    leviathansactive = 0
    # defining the active leviathans variable for later use
    pygame.init()
    # initiating pygame
    display_width = 960
    display_height = 540
    gamedisplay = pygame.display.set_mode((display_width, display_height))
    # defining the gamedisplay with the defined width and height variables
    white = (255, 255, 255)
    # defining white's RGB color code for later use
    background = pygame.image.load('Assets/backgrounds/1. First Depth 1.png')
    background = pygame.transform.scale(background, (960, 540))
    # loading the first background and scaling it accordingly
    pygame.display.set_caption('Reaper')
    font_name = 'Helvetica'
    icon = pygame.image.load('Assets/General/alterra logo.png')
    pygame.display.set_icon(icon)
    # setting the caption, font name, and icon
    explosion = pygame.image.load('Assets/General/explosion.png')
    iconsmall = pygame.transform.scale(icon, (100, 100))
    # loading the image for an explosion when the sprite gets hit by the reaper
    pygame.mixer.music.load('Assets/SoundEffects/Abandon Ship.mp3')
    pygame.mixer.music.play(-1)
    # loading and playing the background music
    xpos = 10
    ypos = 100
    # setting the initial start and finish point for the seamoth sprite
    seamoth = Seamoth(xpos, ypos, True)
    # calling the seamoth sprite to it's initial position
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(seamoth)
    # defining all_sprites_list and adding the seamoth to it
    clock = pygame.time.Clock()
    # defining the clock
    crashed = False
    lastkey = 0
    depth = 0
    speed = 10
    ghost = 0
    reaper = 0
    willyoudie = 0
    orientation = True
    levxpos = display_width / 2
    levypos = display_height
    leftorright = random.randint(0, 1)
    attributes = leviathanattributes(depth)
    deathvia = 'Reaper'
    wait = 0
    # defining all necessary variables for later use in the code
    while not crashed:
        # while loop containing main game
        gamedisplay.blit(background, (0, 0))
        gamedisplay.blit(iconsmall, (5, 5))
        # blits the background and icon on to the game display
        for event in pygame.event.get():
            # for loop that gets the current pygame 'event'
            if event.type == pygame.QUIT:
                exit()
                # if the player presses the red x button, exits the code
            if event.type == pygame.KEYDOWN:
                # if the event is pressing a key, moves in to handle those specific keys
                if event.key == pygame.K_RIGHT:
                    lastkey = 0
                    orientation = True
                    # if the player presses the right key, defines lastkey as zero (moving the sprite right)
                    # and faces the sprite right by defining orientation as true
                elif event.key == pygame.K_LEFT:
                    lastkey = 1
                    orientation = False
                    # if the player presses the left key, defines lastkey as 1 (moving the sprite left)
                    # and faces the sprite left by defining orientation as False
                elif event.key == pygame.K_UP:
                    speed += 2.5
                    # if the player presses the up arrow, accelerates the sprite by increasing the 'speed' variable
                elif event.key == pygame.K_DOWN:
                    speed -= 2.5
                    # if the player presses the down arrow, decelerates the sprite by decreasing the 'speed' variable
        if speed > 15:
            speed = 15
        elif speed < 5:
            speed = 5
        # two if statements that make sure the player cannot accelerate past 15 or decelerate under 5
        if lastkey == 0:
            xpos += speed
            # if the lastkey is zero, adds the current speed to the x position, moving the sprite right
        else:
            xpos -= speed
            # if the lastkey is 1, subtracts the current speed from the x position, moving the sprite left
        ypos += 5
        # moves the sprite down 5
        if xpos > display_width - 80:
            lastkey = 1
            orientation = False
            # if the sprite touches the far right side of the display, turns the sprite left
        elif xpos < 0:
            lastkey = 0
            orientation = True
            # if the sprite touches the far left side of the display, turns the sprite right
        all_sprites_list.remove(seamoth)
        # removes the last seamoth from the sprites list
        seamoth = Seamoth(xpos, ypos, orientation)
        # redefines seamoth with the new variables
        if leviathansactive == 0:
            # if there are no leviathans active, triggers the chance to activate a leviathan
            leftorright = random.randint(0, 1)
            # decides randomly if the leviathan will face left or right
            attributes = leviathanattributes(depth)
            # gets the leviathan attributes based on depth
            levxpos = random.randint(1, 500)
            # randomly decides where on the x axis the leviathan will spawn
            if depth > 50:
                willyoudie = leviathanchance(depth)
                # if you are below 50 metres, gets the chance for a leviathan to spawn based on depth
        if willyoudie == 1:
            leviathansactive = 1
            # if the leviathan chance rolled a 1, activates a leviathan, and makes sure leviathansactive == 1 so that
            # the attributes being used for the leviathan will not be rerolled as it is active.
            if attributes[2] == 'Reaper':
                # if the attributes function rolled that the leviathan will be a reaper, activates the if statement for
                # the reaper leviathan.
                try:
                    all_sprites_list.remove(reaper)
                except IndexError:
                    continue
                # tries to remove the previous reaper from all_sprites_list- if this is the first time this is looped
                # while the reaper is active, this will cause an indexerror, hence the try and except.
                levspeed = attributes[0]
                angle = attributes[1]
                # defines the speed and movement to the left or right each loop as the attributes returned by the
                # attributes function.
                reaper = Reaper(levxpos, levypos, leftorright)
                # defines the reaper class with the new attributes
                all_sprites_list.add(reaper)
                # adds the reaper to the all_sprites_list
                if leftorright == 0:
                    levxpos -= angle
                    # if the reaper is travelling left, subtracts the angle from the x position
                else:
                    levxpos += angle
                    # if the reaper is travelling right, adds the angle to the x position
                levypos -= levspeed
                # subtracts the leviathan's speed from the levypos variable
                if pygame.sprite.collide_circle_ratio(0.6)(reaper, seamoth):
                    # if the seamoth and reaper collide (their hitboxes are circles), begins the if statement to handle
                    # when you loose the game.
                    gamedisplay.blit(explosion, (xpos, ypos))
                    # blits the explosion under the seamoth sprite, to show the player that they exploded
                    if wait == 1:
                        leviathansactive = 0
                        deathvia = 'Reaper'
                        crashed = True
                    wait += 1
                    # waits one loop of the code so that the player will see the explosion before ending the game
                if levypos < 0 - 209 or levxpos < 0 - 300 or levxpos > display_width:
                    leviathansactive = 0
                    levxpos = random.randint(1, 500)
                    levypos = display_height
                    # if leviathan goes off the screen in any direction, despawns it to make room for a new leviathan
            elif attributes[2] == 'Ghost':
                try:
                    all_sprites_list.remove(ghost)
                except IndexError:
                    continue
                levspeed = attributes[0]
                angle = attributes[1]
                ghost = Ghost(levxpos, levypos, leftorright)
                all_sprites_list.add(ghost)
                if leftorright == 0:
                    levxpos -= angle
                else:
                    levxpos += angle
                levypos -= levspeed
                if pygame.sprite.collide_circle_ratio(0.5)(ghost, seamoth):
                    gamedisplay.blit(explosion, (xpos, ypos))
                    if wait == 1:
                        leviathansactive = 0
                        deathvia = 'Ghost'
                        crashed = True
                    wait += 1
                if levypos < 0 - 354 or levxpos < 0 - 620 or levxpos > display_width:
                    leviathansactive = 0
                    levxpos = random.randint(1, 500)
                    levypos = display_height
            # the entire if statement prior to this comment is almost identical to the if statement above it, except it
            # is for the other leviathan, the ghost. The only reason I didn't put it in a function is that you need to
            # call different classes, which meant I needed to write the whole thing again, with the only difference
            # being that every occurrence of the word 'reaper' or 'Reaper' is replaced with 'ghost' or 'Ghost'.
        if ypos > display_height - 46:
            ypos = 0
            background = getbackground(depth, random.randint(0, 3))
            willyoudie = 0
            leviathansactive = 0
            try:
                all_sprites_list.remove(reaper)
            except IndexError:
                continue
            try:
                all_sprites_list.remove(ghost)
            except IndexError:
                continue
            levxpos = random.randint(1, 500)
            levypos = display_height
            # when the player hits the bottom of the screen, despawns any active leviathan and resets them, also
            # teleporting the player to the top of the screen and getting a new background.
        if depth < 20:
            instruction1 = 'Use the Arrow keys to go Left and Right!'
            draw_text(gamedisplay, instruction1, 25, white, font_name, display_width/2, 75)
        if 25 < depth < 45:
            instruction2 = 'Use the Up and Down arrows to Accelerate and Decelerate!'
            draw_text(gamedisplay, instruction2, 25, white, font_name, display_width / 2, 75)
        # the past 2 if statements display the instructions while the player is still in the safe depth (0-50)
        depth += 1
        # adds 1 to depth for each iteration of the loop
        all_sprites_list.add(seamoth)
        # adds the seamoth to the sprites list
        all_sprites_list.draw(gamedisplay)
        # draws all the sprites in the all_sprites_list to the game display.
        draw_text(gamedisplay, str(depth), 40, white, font_name, display_width / 2, 25)
        # draws the depth onto the game display
        pygame.display.flip()
        clock.tick(60)
        # flips the display and ticks the clock by 60
    pygame.mixer.music.stop()
    # once the loop ends, stops the music
    savescore(depth)
    # saves the score to the highscore document
    you_dead(deathvia, depth)
    # calls the death screen function with the parameters for what killed you, and how deep you got.


'''
The following function is the final death screen function, where it displays the depth you got to, and plays the
roar sound effect of whichever leviathan killed you. You then press any button to continue, and it takes you back to
the starting screen, where you can try to play again.
'''


def you_dead(deathvia, depth):
    pygame.init()
    display_width = 960
    display_height = 540
    white = (255, 255, 255)
    # initializing pygame, setting the background size, and defining white
    reaperbackgrounds = ['Assets/Backgrounds/loadingscreen1.jpg',
                         'Assets/Backgrounds/loadingscreen2.jpg',
                         'Assets/Backgrounds/loadingscreen3.png']
    ghostbackgrounds = ['Assets/Backgrounds/loadingscreen4.jpg',
                        'Assets/Backgrounds/loadingscreen5.jpg',
                        'Assets/Backgrounds/loadingscreen6.png']
    # defining the backgrounds based on which leviathan killed you
    if deathvia == 'Reaper':
        background = pygame.image.load(random.choice(reaperbackgrounds))
    elif deathvia == 'Ghost':
        background = pygame.image.load(random.choice(ghostbackgrounds))
    else:
        background = pygame.image.load(random.choice(reaperbackgrounds))
    # getting the backgrounds based on what killed you
    title = pygame.image.load('Assets/General/Title.png')
    # loading the title image
    gamedisplay = pygame.display.set_mode((display_width, display_height))
    # setting the game display
    pygame.display.set_caption('Reaper')
    font_name = 'Helvetica'
    icon = pygame.image.load('Assets/General/alterra logo.png')
    pygame.display.set_icon(icon)
    # setting the caption, font name, and icon
    clock = pygame.time.Clock()
    crashed = False
    # defining the clock and the fact that we have not, in fact, crashed
    metressurvived = 'You survived ' + str(depth) + ' metres.'
    anybutton = 'Press any Button to Play Again'
    # defining two strings to be printed on the screen
    if deathvia == 'Reaper':
        roar('Reaper')
    else:
        roar('Ghost')
    # playing the roar of whichever leviathan killed you
    while not crashed:
        # loop that displays the menu
        gamedisplay.blit(background, (0, 0))
        gamedisplay.blit(title, (330, 100))
        # blitting the background and title to the game display
        draw_text(gamedisplay, metressurvived, 25, white, font_name, display_width / 2, 240)
        draw_text(gamedisplay, anybutton, 25, white, font_name, display_width / 2, 340)
        # drawing the text to the screen defined in the strings above
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                # if the user presses the red x, quits the code
            if event.type == pygame.KEYDOWN:
                crashed = True
                # if the user presses any button, quits the loop
        pygame.display.flip()
        # flips the display
        clock.tick(60)
        # ticks the clock by 60
    start_menu()
    # once the loop has ended, calls start_menu() again, restarting the whole process from the top


start_menu()
# calling the start_menu() function to begin the code
