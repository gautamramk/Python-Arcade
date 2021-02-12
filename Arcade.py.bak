import pygame
from pygame.locals import *
import Snake
import birds
import TTT
import Menu
import sys
import pickle
import os
import time

screen = None
k_prev = None
keystate = None


class scoreblock:
    box = pygame.image.load(os.path.join("Sprites", "Namebox.png"))
    boxs = pygame.image.load(os.path.join("Sprites", "Namebox-s.png"))
    font = pygame.font.Font(None, 64)

    def __init__(self, x, y, txt, sel, screen):
        self.txt = txt
        self.sel = sel
        self.x = x
        self.y = y
        self.screen = screen

    def swap(self):
        if self.sel:
            self.sel = False
        else:
            self.sel = True

    def draw(self):
        global screen
        ren = scoreblock.font.render(self.txt, 1, (0, 0, 0))
        if self.sel:
            self.screen.blit(scoreblock.boxs, (self.x, self.y))
        else:
            self.screen.blit(scoreblock.box, (self.x, self.y))
        self.screen.blit(ren, (self.x + 16, self.y + 16))

    def update(self, kprev, key):
        if (key[K_w] and kprev[K_w] == False) or (key[K_w] and kprev == None):
            if ord(self.txt) >= 90:
                self.txt = chr(65)
            else:
                self.txt = chr(ord(self.txt) + 1)
        elif (key[K_s] and kprev[K_s] == False) or (key[K_s] and kprev == None):
            if ord(self.txt) <= 65:
                self.txt = chr(90)
            else:
                self.txt = chr(ord(self.txt) - 1)


class scorescreen:
    def __init__(self, x, y, boxes, screen):
        self.x = x
        self.y = y
        self.boxes = boxes
        self.txtboxes = [
            scoreblock(x + i * 96, y, "A", False, screen) for i in range(boxes)
        ]
        self.txtboxes[0].selected = True
        self.selected = 0
        self.txtboxes[0].swap()

    def update(self, kprev, key):
        if (key[K_a] and kprev[K_a] == False) or (key[K_a] and kprev == None):
            self.txtboxes[self.selected].swap()
            if self.selected == 0:
                self.selected = self.boxes - 1
            else:
                self.selected -= 1
            self.txtboxes[self.selected].swap()
        elif (key[K_d] and kprev[K_d] == False) or (key[K_d] and kprev == None):
            self.txtboxes[self.selected].swap()
            if self.selected == self.boxes - 1:
                self.selected = 0
            else:
                self.selected += 1
            self.txtboxes[self.selected].swap()
        self.txtboxes[self.selected].update(kprev, key)
        self.text = ""
        for i in self.txtboxes:
            self.text += i.txt

    def draw(self):
        for box in self.txtboxes:
            box.draw()
            pygame.display.flip()
            pygame.event.pump()


def highscores(sc, mode):
    global screen
    if mode == 1:
        hf = open("snake.dat", "rb")
    elif mode == 2:
        hf = open("birds.dat", "rb")
    top = list(pickle.load(hf))
    print top
    check = False
    for i in top:
        if sc > i[1]:
            check = True
            print "yes"
    hf.close()

    if check:
        toshow = scorescreen(50, 50, 3, screen)
        prevtime = time.time()
        currenttime = time.time()
        fps = 30
        running = True
        while currenttime - prevtime < 0.25:
            currenttime = time.time()
        kprev = None
        while running:
            if (currenttime - prevtime) > (1.0 / fps):
                prevtime = currenttime
                screen.fill((128, 128, 128))
                toshow.draw()
                key = pygame.key.get_pressed()
                toshow.update(kprev, key)
                toshow.draw()
                kprev = key
                if key[K_RETURN]:
                    running = False
            else:
                currenttime = time.time()
        i = len(top)
        top.append(None)
        while top[i - 1][1] < sc and i > 0:
            top[i] = top[i - 1]
            i -= 1
        top[i] = (
            toshow.text,
            sc,
        )
        if len(top) > 5:
            del top[5]
        hf = open("temp.dat", "wb")
        pickle.dump(top, hf)
        hf.close()
        if mode == 1:
            os.remove("snake.dat")
            os.rename("temp.dat", "snake.dat")
        elif mode == 2:
            os.remove("birds.dat")
            os.rename("temp.dat", "birds.dat")
        for q in pygame.event.get():
            if q.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def highscorescr(screen):
    font = pygame.font.Font(None, 40)
    done = False
    hf = open("snake.dat", "rb")
    sn = list(pickle.load(hf))
    hf.close()
    hf = open("birds.dat", "rb")
    bd = list(pickle.load(hf))
    hf.close()
    prevtime = time.time()
    currenttime = time.time()
    while currenttime - prevtime < 1.0:
        currenttime = time.time()
    keys = pygame.key.get_pressed()
    while keys[K_SPACE] == False:
        keys = pygame.key.get_pressed()
        screen.fill((128, 128, 128))
        rnd = font.render("Snake", 1, (0, 0, 0))
        screen.blit(rnd, (20, 20))
        for i in range(5):
            rnd = font.render(sn[i][0] + " : " + str(sn[i][1]), 1, (0, 0, 0))
            screen.blit(rnd, (20, 80 + 40 * i))
        rnd = font.render("Birds", 1, (0, 0, 0))
        screen.blit(rnd, (20, 350))
        for i in range(5):
            rnd = font.render(bd[i][0] + " : " + str(bd[i][1]), 1, (0, 0, 0))
            screen.blit(rnd, (20, 380 + 40 * i))
        for q in pygame.event.get():
            if q.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()
        pygame.event.pump()
    print "Done"


def initialize():
    global screen
    pygame.display.init()
    pygame.display.set_caption("Arcade")
    screen = pygame.display.set_mode((640, 640))
    pygame.display.flip()
    pygame.event.pump()


def startgame(mode):
    global screen
    global k_prev
    if mode == 0:
        score = Snake.gamestart(1, screen)
        highscores(score, 1)
    elif mode == 1:
        TTT.gamestart(0, screen, keystate)
    elif mode == 2:
        score = birds.gamestart(screen)
        highscores(score, 2)
    elif mode == 3:
        highscorescr(screen)
    elif mode == 4:
        pygame.quit()
        sys.exit()
    screen = pygame.display.set_mode((640, 640))


def main():
    global k_prev
    global keystate
    running = True
    initialize()
    mainmenu = Menu.menulist(
        200,
        280,
        ["Snake", "Tic Tac Toe", "Flappy Birds", "Highscores", "Exit"],
        48,
        48,
        screen,
    )
    while running:
        screen.fill((128, 128, 128))
        keystate = pygame.key.get_pressed()
        mainmenu.update(keystate, k_prev)
        mainmenu.draw()
        if keystate[K_RETURN] and (
                k_prev[K_RETURN] == False or k_prev == None):
            startgame(mainmenu.getitem())
        pygame.display.flip()
        pygame.event.pump()
        k_prev = keystate
        for q in pygame.event.get():
            if q.type == pygame.QUIT:
                pygame.quit()
                exit()


main()
