'''THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE AND
NON-INFRINGEMENT. IN NO EVENT SHALL THE COPYRIGHT HOLDERS OR ANYONE
DISTRIBUTING THE SOFTWARE BE LIABLE FOR ANY DAMAGES OR OTHER LIABILITY,
WHETHER IN CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''

# Bitcoin Cash (BCH)   qpz32c4lg7x7lnk9jg6qg7s4uavdce89myax5v5nuk
# Ether (ETH) -        0x843d3DEC2A4705BD4f45F674F641cE2D0022c9FB
# Litecoin (LTC) -     Lfk5y4F7KZa9oRxpazETwjQnHszEPvqPvu
# Bitcoin (BTC) -      34L8qWiQyKr8k4TnHDacfjbaSqQASbBtTd

# contact :- github@jamessawyer.co.uk



import pygame
from pygame.locals import *
import os
import time
import random

birdimg = None
wallimg = None
screen = None


def gamestart():
    global birdimg
    global wallimg

    birdimg = pygame.image.load(os.path.join("Images", "Bird.bmp"))
    wallimg = pygame.image.load(os.path.join("Images", "Wall.bmp"))


def update(xpos, ypos, wall):
    global screen
    global birdimg
    global wallimg
    screen.fill((255, 255, 255))
    screen.blit(birdimg, (368, ypos))
    if wall[0] is not None:
        screen.blit(wallimg, (300 - xpos, wall[0] - 400))
        screen.blit(wallimg, (300 - xpos, wall[0] + 64))
    screen.blit(wallimg, (800 - xpos, wall[1] - 400))
    screen.blit(wallimg, (800 - xpos, wall[1] + 64))
    pygame.display.flip()
    pygame.event.pump()


def loop():
    score = 0
    k = pygame.key.get_pressed()
    f = True
    kprev = pygame.key.get_pressed()
    prevtime = time.time()
    currenttime = time.time()
    fps = 30
    xpos = 0.0
    ypos = 300.0
    yvel = 0
    g = 100
    walllist = []
    walllist.extend([None, random.randint(100, 236), random.randint(100, 236)])
    gameon = True
    while gameon:
        if (currenttime - prevtime) > (1.0 / fps) or f:
            k = pygame.key.get_pressed()
            f = False
            if xpos >= 434 and xpos <= 500:
                if ypos <= walllist[1] or ypos >= walllist[1] + 32:
                    gameon = False
            if k[K_SPACE] and kprev[K_SPACE] == False:
                yvel -= 100 if yvel > -50 else 0
            xpos += 200 / fps
            yvel += g / fps
            ypos += yvel / fps
            kprev = k

            update(xpos, ypos, walllist)
            prevtime = currenttime
            kprev = k
            currenttime = time.time()

            if xpos >= 500:
                xpos = 0
                walllist[0] = walllist[1]
                walllist[1] = walllist[2]
                walllist[2] = random.randint(100, 150)
                score += 1
                print(score)
        else:
            currenttime = time.time()
    print(ypos)
    print(walllist[1])
    while True:
        continue


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
        k = pygame.key.get_pressed()
        if k[K_SPACE]:
            gamestart()
            loop()
        for q in pygame.event.get():
            if q.type == pygame.QUIT:
                pygame.quit()
                running = False
        pygame.event.pump()


main()
