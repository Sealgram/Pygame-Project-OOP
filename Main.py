# Imports:
import pygame, random


class Seamoth(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('Assets/Sprites/seamoth.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 46))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


def getbackground(depth, iteration):
    depthpaths = open('BackgroundDirectories.txt')
    depthpathslist = depthpaths.readlines()
    if depth < 500:
        background =


def start_menu():
    pygame.init()
    display_width = 960
    display_height = 540
    backgrounds = ['Assets/Backgrounds/4. Fourth Depth 1.png',
                   'Assets/Backgrounds/4. Fourth Depth 2.png',
                   'Assets/Backgrounds/4. Fourth Depth 3.png']
    background = pygame.image.load(random.choice(backgrounds))
    background = pygame.transform.scale(background, (960, 540))
    title = pygame.image.load('Assets/Title Screen/Title.png')
    start = pygame.image.load('Assets/Title Screen/ClicktoStart.png')
    gamedisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Reaper')
    clock = pygame.time.Clock()
    crashed = False
    exitgame = False
    while not crashed:
        gamedisplay.blit(background, (0, 0))
        gamedisplay.blit(title, (330, 100))
        gamedisplay.blit(start, (350, 300))
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
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    background = pygame.image.load('Assets/water.png')
    background = pygame.transform.scale(background, (960, 540))
    background_rect = background.get_rect()
    background_size = background.get_size()
    gamedisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Reaper')
    xpos = 10
    ypos = 100
    seamoth = Seamoth(xpos, ypos)
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(seamoth)
    clock = pygame.time.Clock()
    crashed = False
    lastkey = 0
    backwidth, backheight = background_size
    y = 0
    x = 0
    y1 = +backheight
    x1 = 0
    while not crashed:
        gamedisplay.blit(background, background_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    lastkey = 0
                elif event.key == pygame.K_LEFT:
                    lastkey = 1
        if lastkey == 0:
            xpos += 10
        else:
            xpos -= 10
        if xpos > display_width - 80:
            lastkey = 1
        elif xpos < 0:
            lastkey = 0
        y1 -= 2
        y -= 2
        gamedisplay.blit(background, (x, y))
        gamedisplay.blit(background, (x1, y1))
        if y > backheight:
            y = +backheight
        if y1 > backheight:
            y1 = +backheight
        all_sprites_list.remove(seamoth)
        seamoth = Seamoth(xpos, ypos)
        all_sprites_list.add(seamoth)
        all_sprites_list.draw(gamedisplay)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


start_menu()
