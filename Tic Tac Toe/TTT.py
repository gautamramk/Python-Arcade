import pygame
import os
from pygame.locals import *
import time
import Menu
import random

screen = None
naughtpic = None
crosspic = None
boardpic = None
highlight = None
keys = None


def gameover(board):
    # columns
    win = True
    for row in range(0, 3):
        win = True
        if board[row][0] == 0:
            win = False
        else:

            for column in range(0, 3):
                if board[row][column] == board[row][0]:
                    pass
                else:
                    win = False
        if win:
            return [True, board[row][0]]

    # rows
    win = True
    for column in range(0, 3):
        win = True
        if board[0][column] == 0:
            win = False
        else:

            for row in range(0, 3):
                if board[row][column] == board[0][column]:
                    pass
                else:
                    win = False
        if win:
            return [True, board[0][column]]
    # major diagonal
    if board[0][0] != 0:
        win = True
        for row in range(0, 3):
            if board[row][row] != board[0][0]:
                win = False
        if win:
            return [True, board[0][0]]

    # minor diagonal
    if board[0][2] != 0:
        win = True
        for row in range(0, 3):
            if board[row][2 - row] != board[0][2]:
                win = False
        if win:
            return [True, board[0][2]]

    # board full
    over = True
    for row in range(0, 3):
        for column in range(0, 3):
            if board[row][column] == 0:
                over = False
    if over:
        return [True, 0]
    return [False, 0]


def initialize():
    pygame.init()
    global boardpic
    global naughtpic
    global crosspic
    global screen
    global highlight
    boardpic = pygame.image.load(os.path.join("Sprites", "Board.png"))
    naughtpic = pygame.image.load(os.path.join("Sprites", "Naught.png"))
    crosspic = pygame.image.load(os.path.join("Sprites", "Cross.png"))
    highlight = pygame.image.load(os.path.join("Sprites", "Highlight.png"))
    pygame.display.init()
    pygame.display.set_caption("Tic Tac Toe")
    screen = pygame.display.set_mode((640, 640))
    pygame.display.flip()
    pygame.event.pump()


def nextpos(board, curpos):
    check = False
    while check == False:
        if board[curpos / 3][curpos % 3] != 0:
            curpos = (curpos + 1) % 9
        else:
            check = True
    return curpos


def compthink(board, comp):

    for i in range(3):
        for j in range(3):
            trialboard = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            for m in range(3):
                for n in range(3):
                    trialboard[m][n] = board[m][n]

            if trialboard[i][j] == 0:
                trialboard[i][j] = comp
                print("tryin")
                c = gameover(trialboard)
                print(trialboard)
                if c[0] and c[1] == comp:
                    print("win")
                    return 3 * i + j
    for i in range(3):
        for j in range(3):
            trialboard = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            for m in range(3):
                for n in range(3):
                    trialboard[m][n] = board[m][n]
            if trialboard[i][j] == 0:
                trialboard[i][j] = -comp
                c = gameover(trialboard)
                if c[0] and c[1] == -comp:
                    print("block")
                    return 3 * i + j
    counter = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                counter += 1
    rplace = random.randint(0, counter - 1)
    print(rplace)
    counter = 0
    for i in range(9):
        if board[i / 3][i % 3] == 0:
            if counter == rplace:
                print("play")
                return i
            else:
                counter += 1


def playcomp():
    keys[1] = keys[0]
    global keys
    global screen
    global boardpic
    global crosspic
    global naughtpic
    global highlight
    firstloop = True
    times = []
    times.append(time.time())
    times.append(time.time())
    gamechoose = True
    signchoice = Menu.menulist(
        100, 400, [
            "I choose X", "I choose O"], 48, 48, screen)
    fps = 20
    comp = 0
    while gamechoose:
        if times[0] - times[1] >= (1.0 / fps) or firstloop:
            screen.fill((128, 128, 128))
            times[1] = times[0]
            keys[0] = pygame.key.get_pressed()
            firstloop = False
            signchoice.update(keys[0], keys[1])
            signchoice.draw()
            if keys[0][K_RETURN] and keys[1][K_RETURN] == False:
                if signchoice.getitem() == 1:
                    comp = -1
                    gamechoose = False
                elif signchoice.getitem() == 0:
                    comp = 1
                    gamechoose = False
            pygame.display.flip()
            pygame.event.pump()
            keys[1] = keys[0]
        for q in pygame.event.get():
            if q.type == pygame.QUIT:
                pygame.quit()
        times[0] = time.time()

    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    curpos = 0
    running = True
    while running:
        if times[0] - times[1] >= (1.0 / fps) or firstloop:
            screen.fill((128, 128, 128))
            times[1] = times[0]
            keys[0] = pygame.key.get_pressed()
            firstloop = False
            screen.blit(boardpic, (100, 100))
            screen.blit(
                highlight,
                (
                    100 + curpos % 3 * 80 + (5 * (curpos % 3)),
                    100 + (curpos / 3) * 80 + (5 * (curpos / 3)),
                ),
            )
            if keys[0][K_d] and keys[1][K_d] == False:
                curpos = nextpos(board, (curpos + 1) % 9)
            elif keys[0][K_a] and keys[1][K_a] == False:
                curpos = nextpos(board, (curpos - 1) % 9)
            elif keys[0][K_w] and keys[1][K_w] == False:
                curpos = nextpos(board, (curpos - 3) % 9)
            elif keys[0][K_s] and keys[1][K_s] == False:
                curpos = nextpos(board, (curpos + 3) % 9)

            if keys[0][K_RETURN] and keys[1][K_RETURN] == False:
                if comp == 1:
                    board[curpos / 3][curpos % 3] = -1
                elif comp == -1:
                    board[curpos / 3][curpos % 3] = 1
                c = gameover(board)
                if c[0] and c[1] == -comp:
                    print("You win")
                    running = False
                elif c[0] and c[1] == 0:
                    print("Draw")
                    running = False
                else:
                    cplay = compthink(board, comp)
                    board[cplay / 3][cplay % 3] = comp
                    curpos = nextpos(board, (curpos + 1) % 9)
            for i in range(3):
                for j in range(3):
                    if board[i][j] == -1:
                        screen.blit(
                            crosspic, (100 + j * 80 + j * 5, 100 + i * 80 + i * 5))
                    elif board[i][j] == +1:
                        screen.blit(
                            naughtpic, (100 + j * 80 + j * 5, 100 + i * 80 + i * 5))
            c = gameover(board)
            if c[0]:
                if c[1] == comp:
                    print("Computer wins.")
                    running = False
                    winner = comp
                elif c[1] == -comp:
                    print("You win.")
                    winner = -comp
                    running = False
                elif c[1] == 0:
                    print("Draw")
                    running = False
                    winner = 0

            pygame.display.flip()
            pygame.event.pump()
            keys[1] = keys[0]
            for q in pygame.event.get():
                if q.type == pygame.QUIT:
                    pygame.quit()
        times[0] = time.time()
    q = False
    c = 0
    t = time.time()
    screen.fill((128, 128, 128))
    font = pygame.font.Font(None, 60)
    if winner == comp:
        txt = font.render("Computer Wins", 1, (0, 0, 0))
    elif winner == -comp:
        txt = font.render("Player Wins", 1, (0, 0, 0))
    else:
        txt = font.render("Draw", 1, (0, 0, 0))
    screen.blit(txt, (50, 50))
    pygame.display.flip()
    pygame.event.pump()
    while q == False:
        if time.time() - t > 1.0:

            k = pygame.key.get_pressed()
            if k[K_RETURN]:
                print("True")
                q = True
        pygame.event.pump()


def gamestart(mode):
    global keys
    global screen
    if mode == 0:
        playcomp()


def main():
    global screen
    global keys
    initialize()
    running = True
    firstloop = True
    gamechoice = Menu.menulist(
        100, 400, [
            "Play Against Computer", "Play Against Human"], 48, 48, screen)
    times = []
    keys = []
    keys.append(None)
    keys.append(None)
    times.append(time.time())
    times.append(time.time())
    fps = 60
    while running:
        if times[0] - times[1] >= (1.0 / fps) or firstloop:
            times[1] = times[0]
            keys[0] = pygame.key.get_pressed()

            firstloop = False
            screen.fill((128, 128, 128))
            gamechoice.update(keys[0], keys[1])
            gamechoice.draw()
            if keys[0][K_RETURN] and keys[1][K_RETURN] == False:
                gamestart(gamechoice.getitem())
            keys[1] = keys[0]
            pygame.display.flip()
            pygame.event.pump()
        for q in pygame.event.get():
            if q.type == pygame.QUIT:
                pygame.quit()
                running = False
        times[0] = time.time()


main()
