# Note That all comments are referencing the line/lines directly above them. Block comments reference the functions
# and classes directly below them.

import pygame, random, time
# imports needed modules into the game
leviathansactive = 0
# global variable is defined for how many leviathans (the enemy) are active in my game.


'''
The below class is created for my player sprite, the seamoth
'''


class Seamoth(pygame.sprite.Sprite):
    def __init__(self, x, y, orientation):
        super().__init__()
        self.imageleft = pygame.image.load('Assets/Sprites/seamoth.png').convert_alpha()
        self.imageleft = pygame.transform.scale(self.imageleft, (80, 46))
        self.imageright = pygame.transform.flip(self.imageleft, True, False)
        if orientation:
            self.image = self.imageright
        else:
            self.image = self.imageleft
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


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


def leviathanattributes(depth):
    angleseasy = [0, 2, 4]
    angleshard = [6, 8, 12]
    speedseasy = [6, 10, 14]
    speedshard = [16, 18, 20]
    levtypes1 = ['Reaper', 'Reaper', 'Ghost']
    levtypes2 = ['Ghost', 'Ghost', 'Reaper']
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


def roar(roartype):
    reaper_roar = pygame.mixer.Sound("Assets/SoundEffects/Reaper Roar.wav")
    ghost_roar = pygame.mixer.Sound("Assets/SoundEffects/Ghost Roar.wav")
    if roartype == 'Reaper':
        pygame.mixer.Sound.play(reaper_roar)
        pygame.mixer.music.stop()
    elif roartype == 'Ghost':
        pygame.mixer.Sound.play(ghost_roar)
        pygame.mixer.music.stop()


def getscore():
    stored = open('Highscore', 'r')
    score = stored.read().strip()
    return int(score)


def savescore(score):
    scoresaved = getscore()
    if score > scoresaved:
        stored = open('Highscore', 'w')
        stored.write(str(score))


def getbackground(depth, iteration):
    depthpaths = open('BackgroundDirectories', "r")
    depthpathslist = depthpaths.read()
    depthpathslist = depthpathslist.split("?")
    bglist = []
    for i in depthpathslist:
        bglist.append(i.split("\n"))
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
    background = pygame.transform.scale(background, (960, 540))
    return background


def draw_text(surf, text, size, white, font_name, x, y):
    font = pygame.font.SysFont(font_name, size)
    text_surface = font.render(text, True, white)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def start_menu():
    pygame.init()
    display_width = 960
    display_height = 540
    white = (255, 255, 255)
    backgrounds = ['Assets/Backgrounds/loadingscreen1.jpg',
                   'Assets/Backgrounds/loadingscreen2.jpg',
                   'Assets/Backgrounds/loadingscreen3.png',
                   'Assets/Backgrounds/loadingscreen4.jpg']
    background = pygame.image.load(random.choice(backgrounds))
    pygame.mixer.music.load('Assets/SoundEffects/Salutations.mp3')
    pygame.mixer.music.play(-1)
    title = pygame.image.load('Assets/General/Title.png')
    start = pygame.image.load('Assets/General/ClicktoStart.png')
    highscore = pygame.image.load('Assets/General/Highscore.png')
    gamedisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Reaper')
    font_name = 'Helvetica'
    icon = pygame.image.load('Assets/General/alterra logo.png')
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()
    crashed = False
    exitgame = False
    while not crashed:
        gamedisplay.blit(background, (0, 0))
        gamedisplay.blit(title, (330, 100))
        gamedisplay.blit(start, (350, 300))
        gamedisplay.blit(highscore, (285, 200))
        draw_text(gamedisplay, str(getscore()) + ' metres', 25, white, font_name, 650, 240)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
                exitgame = True
            if event.type == pygame.KEYDOWN:
                crashed = True
                exitgame = False
        pygame.display.flip()
        clock.tick(60)
    maingame(exitgame)


def maingame(exitgame):
    global leviathansactive
    if exitgame:
        exit()
    pygame.init()
    display_width = 960
    display_height = 540
    gamedisplay = pygame.display.set_mode((display_width, display_height))
    white = (255, 255, 255)
    background = pygame.image.load('Assets/backgrounds/1. First Depth 1.png')
    background = pygame.transform.scale(background, (960, 540))
    pygame.display.set_caption('Reaper')
    font_name = 'Helvetica'
    icon = pygame.image.load('Assets/General/alterra logo.png')
    pygame.display.set_icon(icon)
    explosion = pygame.image.load('Assets/General/explosion.png')
    iconsmall = pygame.transform.scale(icon, (100, 100))
    pygame.mixer.music.load('Assets/SoundEffects/Abandon Ship.mp3')
    pygame.mixer.music.play(-1)
    xpos = 10
    ypos = 100
    seamoth = Seamoth(xpos, ypos, True)
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(seamoth)
    clock = pygame.time.Clock()
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
    while not crashed:
        gamedisplay.blit(background, (0, 0))
        gamedisplay.blit(iconsmall, (5, 5))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    lastkey = 0
                    orientation = True
                elif event.key == pygame.K_LEFT:
                    lastkey = 1
                    orientation = False
                elif event.key == pygame.K_UP:
                    speed += 2.5
                elif event.key == pygame.K_DOWN:
                    speed -= 2.5
        if speed > 15:
            speed = 15
        elif speed < 5:
            speed = 5
        if lastkey == 0:
            xpos += speed
        else:
            xpos -= speed
        ypos += 5
        if xpos > display_width - 80:
            lastkey = 1
            orientation = False
        elif xpos < 0:
            lastkey = 0
            orientation = True
        all_sprites_list.remove(seamoth)
        seamoth = Seamoth(xpos, ypos, orientation)
        if leviathansactive == 0:
            leftorright = random.randint(0, 1)
            attributes = leviathanattributes(depth)
            levxpos = random.randint(1, 500)
            if depth > 50:
                willyoudie = leviathanchance(depth)
        if willyoudie == 1:
            leviathansactive = 1
            if attributes[2] == 'Reaper':
                try:
                    all_sprites_list.remove(reaper)
                except IndexError:
                    continue
                levspeed = attributes[0]
                angle = attributes[1]
                reaper = Reaper(levxpos, levypos, leftorright)
                all_sprites_list.add(reaper)
                if leftorright == 0:
                    levxpos -= angle
                else:
                    levxpos += angle
                levypos -= levspeed
                if pygame.sprite.collide_circle_ratio(0.5)(reaper, seamoth):
                    gamedisplay.blit(explosion, (xpos, ypos))
                    time.sleep(0.5)
                    leviathansactive = 0
                    deathvia = 'Reaper'
                    crashed = True
                if levypos < 0 - 209 or levxpos < 0 - 300 or levxpos > display_width:
                    leviathansactive = 0
                    levxpos = random.randint(1, 500)
                    levypos = display_height
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
                    time.sleep(0.5)
                    leviathansactive = 0
                    deathvia = 'Ghost'
                    crashed = True
                if levypos < 0 - 354 or levxpos < 0 - 620 or levxpos > display_width:
                    leviathansactive = 0
                    levxpos = random.randint(1, 500)
                    levypos = display_height
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
        if depth < 20:
            instruction1 = 'Use the Arrow keys to go Left and Right!'
            draw_text(gamedisplay, instruction1, 25, white, font_name, display_width/2, 75)
        if 25 < depth < 45:
            instruction2 = 'Use the Up and Down arrows to Accelerate and Decelerate!'
            draw_text(gamedisplay, instruction2, 25, white, font_name, display_width / 2, 75)
        depth += 1
        all_sprites_list.add(seamoth)
        all_sprites_list.draw(gamedisplay)
        draw_text(gamedisplay, str(depth), 40, white, font_name, display_width / 2, 25)
        pygame.display.flip()
        clock.tick(60)
    pygame.mixer.music.stop()
    savescore(depth)
    you_dead(deathvia, depth)


def you_dead(deathvia, depth):
    pygame.init()
    display_width = 960
    display_height = 540
    white = (255, 255, 255)
    reaperbackgrounds = ['Assets/Backgrounds/loadingscreen1.jpg',
                         'Assets/Backgrounds/loadingscreen2.jpg',
                         'Assets/Backgrounds/loadingscreen3.png']
    ghostbackgrounds = ['Assets/Backgrounds/loadingscreen4.jpg',
                        'Assets/Backgrounds/loadingscreen5.jpg',
                        'Assets/Backgrounds/loadingscreen6.png']
    if deathvia == 'Reaper':
        background = pygame.image.load(random.choice(reaperbackgrounds))
    elif deathvia == 'Ghost':
        background = pygame.image.load(random.choice(ghostbackgrounds))
    else:
        background = pygame.image.load(random.choice(reaperbackgrounds))
    title = pygame.image.load('Assets/General/Title.png')
    gamedisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Reaper')
    font_name = 'Helvetica'
    icon = pygame.image.load('Assets/General/alterra logo.png')
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()
    crashed = False
    metressurvived = 'You survived ' + str(depth) + ' metres.'
    anybutton = 'Press any Button to Play Again'
    fullstop = False
    if deathvia == 'Reaper':
        roar('Reaper')
    else:
        roar('Ghost')
    while not crashed:
        gamedisplay.blit(background, (0, 0))
        gamedisplay.blit(title, (330, 100))
        draw_text(gamedisplay, metressurvived, 25, white, font_name, display_width / 2, 240)
        draw_text(gamedisplay, anybutton, 25, white, font_name, display_width / 2, 340)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
                fullstop = True
            if event.type == pygame.KEYDOWN:
                crashed = True
                fullstop = False
        pygame.display.flip()
        clock.tick(60)
    if fullstop:
        exit()
    else:
        start_menu()


start_menu()
