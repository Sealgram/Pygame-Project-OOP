# Imports:
import pygame, random, time, math
from multiprocessing import Process
tick = 0


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
    def __init__(self, x, y, move):
        super().__init__()
        self.imagemove1 = pygame.image.load('Assets/Sprites/Reaper Leviathan.png')
        self.imagemove1 = pygame.transform.scale(self.imagemove1, (300, 209))
        self.imagemove2 = pygame.transform.rotate(self.imagemove1, 20)
        if move:
            self.image = self.imagemove1
        else:
            self.image = self.imagemove2
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y, move):
        super().__init__()
        self.imagemove1 = pygame.image.load('Assets/Sprites/Ghost Leviathan.png')
        self.imagemove1 = pygame.transform.scale(self.imagemove1, (300, 209))
        self.imagemove2 = pygame.transform.rotate(self.imagemove1, 20)
        if move:
            self.image = self.imagemove1
        else:
            self.image = self.imagemove2
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


def leviathanchance(depth):
    if depth < 50:
        chance = 0
    elif 50 < depth < 150:
        chance = random.randint(0, 8)
    elif 150 < depth < 300:
        chance = random.randint(0, 5)
    elif 300 < depth < 450:
        chance = random.randint(0, 3)
    elif 450 < depth < 600:
        chance = random.randint(0, 2)
    elif depth > 600:
        chance = random.randint(0, 1)
    else:
        chance = random.randint(0, 1)
    return chance


def leviathanattributes(depth):
    angleseasy = [90, 80, 100]
    angleshard = [100, 80, 70, 120]
    speedseasy = [4, 6, 8]
    speedshard = [8, 10, 12, 15]
    if 50 < depth < 150:
        speed = random.choice(speedseasy)
        angle = random.choice(angleseasy)
        leviathantype = 'Reaper'
    elif 150 < depth < 300:
        speed = random.choice(speedseasy)
        angle = random.choice(angleseasy)
        leviathantype = 'Reaper'
    elif 300 < depth < 450:
        speed = random.choice(speedshard)
        angle = random.choice(angleshard)
        leviathantype = 'Reaper'
    elif 450 < depth < 600:
        speed = random.choice(speedshard)
        angle = random.choice(angleshard)
        leviathantype = 'Ghost'
    elif depth > 600:
        speed = random.choice(speedshard)
        angle = random.choice(angleshard)
        leviathantype = 'Ghost'
    else:
        speed = random.choice(speedshard)
        angle = random.choice(angleshard)
        leviathantype = 'Ghost'
    return [speed, angle, leviathantype]


def getscore():
    stored = open('Highscore', 'r')
    score = stored.read().strip()
    return score


def savescore(score):
    stored = open('Highscore', 'w')
    stored.write(score)


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
    backgrounds = ['Assets/Backgrounds/4. Fourth Depth 1.png',
                   'Assets/Backgrounds/4. Fourth Depth 2.png',
                   'Assets/Backgrounds/4. Fourth Depth 3.png']
    background = pygame.image.load(random.choice(backgrounds))
    background = pygame.transform.scale(background, (960, 540))
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
    iconsmall = pygame.transform.scale(icon, (100, 100))
    xpos = 10
    ypos = 100
    seamoth = Seamoth(xpos, ypos, True)
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(seamoth)
    clock = pygame.time.Clock()
    crashed = False
    lastkey = 0
    iteration = 0
    depth = 0
    speed = 10
    orientation = True
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
        if ypos > display_height - 46:
            ypos = 0
            iteration += 1
            if iteration == 4:
                iteration = 0
            background = getbackground(depth, iteration)
        if depth > 50:
            willyoudie = leviathanchance(depth)
        else:
            willyoudie = 0
        if willyoudie == 1:
            attributes = leviathanattributes(depth)


        if depth < 20:
            instruction1 = 'Use the Arrow keys to go Left and Right!'
            draw_text(gamedisplay, instruction1, 25, white, font_name, display_width/2, 75)
        if 25 < depth < 45:
            instruction2 = 'Use the Up and Down arrows to Accelerate and Decelerate!'
            draw_text(gamedisplay, instruction2, 25, white, font_name, display_width / 2, 75)
        depth += 0.4
        roundeddepth = math.ceil(depth)
        all_sprites_list.remove(seamoth)
        seamoth = Seamoth(xpos, ypos, orientation)
        all_sprites_list.add(seamoth)
        all_sprites_list.draw(gamedisplay)
        draw_text(gamedisplay, str(roundeddepth), 40, white, font_name, display_width / 2, 25)
        pygame.display.flip()
        clock.tick(60)
    savescore(depth)


start_menu()
