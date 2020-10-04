import pygame
from pygame.locals import *
import os
import time
import random

birdimg = None
wallimg = None
screen = None
bgimg1 = None
bgimg2 = None
bgimg1_x = 0
bgimg2_x = 0
day = random.randint(1, 2)


def gamestart():
    global birdimg
    global wallimg
    global bgimg1
    global bgimg2
    global bgimg1_x
    global bgimg2_x

    birdimg = pygame.image.load(os.path.join("Images", "Bird.bmp"))
    wallimg = pygame.image.load(os.path.join("Images", "Wall.bmp"))
    if day == 1:
        bgimg1 = pygame.image.load(os.path.join("Images", "BGM.png"))
        bgimg2 = pygame.image.load(os.path.join("Images", "BGM.png"))
    else:
        bgimg1 = pygame.image.load(os.path.join("Images", "BGN.png"))
        bgimg2 = pygame.image.load(os.path.join("Images", "BGN.png"))
    bgimg1_x = 0
    bgimg2_x = bgimg1.get_width()


def update(xpos, ypos, wall, score):
    global screen
    global birdimg
    global wallimg
    global bgimg1
    global bgimg2
    screen.fill((255, 255, 255))
    screen.blit(bgimg1, (bgimg1_x, 0))
    screen.blit(bgimg2, (bgimg2_x, 0))
    # screen.blit(bgimg,(0,0))

    screen.blit(birdimg, (368, ypos))
    if wall[0] is not None:
        screen.blit(wallimg, (300 - xpos, wall[0] - 400))
        screen.blit(wallimg, (300 - xpos, wall[0] + 64))
    screen.blit(wallimg, (800 - xpos, wall[1] - 400))
    screen.blit(wallimg, (800 - xpos, wall[1] + 64))
    font = pygame.font.Font(None, 60)
    r = font.render("Score is:" + str(score), 1, (255, 255, 255))
    screen.blit(r, (500, 10))
    pygame.display.flip()
    pygame.event.pump()


def loop():
    global bgimg1_x
    global bgimg2_x
    score = 0

    k = pygame.key.get_pressed()
    f = True
    kprev = pygame.key.get_pressed()
    prevtime = time.time()
    currenttime = time.time()
    fps = 30
    xpos = 0.0
    ypos = 150.0
    yvel = 0
    g = 500
    walllist = []
    walllist.extend([None, random.randint(100, 280), random.randint(100, 280)])
    gameon = True
    while gameon:
        if (currenttime - prevtime) > (1.0 / fps) or f:
            k = pygame.key.get_pressed()
            f = False
            if xpos >= 434 and xpos <= 500:
                if ypos <= walllist[1] or ypos >= walllist[1] + 40:
                    gameon = False
            if k[K_SPACE] and kprev[K_SPACE] == False:
                yvel -= 200 if yvel > -50 else 0
            xpos += 200 / fps
            yvel += g / fps
            ypos += yvel / fps
            kprev = k

            update(xpos, ypos, walllist, score)
            bgimg1_x -= 2
            bgimg2_x -= 2

            if bgimg1_x == -1 * bgimg1.get_width():
                bgimg1_x = bgimg2_x + bgimg2.get_width()
            if bgimg2_x == -1 * bgimg2.get_width():
                bgimg2_x = bgimg1_x + bgimg1.get_width()
            prevtime = currenttime
            kprev = k
            currenttime = time.time()

            if xpos >= 500:
                xpos = 0
                walllist[0] = walllist[1]
                walllist[1] = walllist[2]
                walllist[2] = random.randint(100, 150)
                score += 1
                print score
        else:
            currenttime = time.time()
    print ypos
    print walllist[1]
    q = False
    c = 0
    t = time.time()
    screen.fill((128, 128, 128))
    font = pygame.font.Font(None, 60)
    txt = font.render("You scored:" + str(score), 1, (0, 0, 0))
    screen.blit(txt, (50, 50))
    pygame.display.flip()
    pygame.event.pump()
    while q == False:
        if time.time() - t > 1.0:

            k = pygame.key.get_pressed()
            if k[K_RETURN]:
                print "True"
                q = True
        pygame.event.pump()
    return None


def main():
    global screen
    pygame.init()
    pygame.display.init()
    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption("Birds")
    screen.fill((255, 255, 255))
    pygame.display.flip()
    running = True
    while running:
        screen.fill((255, 255, 255))
        k = pygame.key.get_pressed()
        if k[K_SPACE]:
            gamestart()
            loop()
        for q in pygame.event.get():
            if q.type == pygame.QUIT:
                pygame.quit()
                running = False
        pygame.display.flip()
        pygame.event.pump()


main()
