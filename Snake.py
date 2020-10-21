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
import snake_part
import Menu
import os
import time
from random import randint
import sys


def init():
    screen = None
    pygame.init()

    snake = None
    imagebody = None

    imagehead = None
    foodimg = None

    foodx = None
    foody = None

    score = None
    skip = None
    gameon = None

    mainmenu = None
    wall = None


screen = None
pygame.init()

snake = None
imagebody = None

imagehead = None
foodimg = None

foodx = None
foody = None

score = None
skip = None
gameon = None

mainmenu = None
wall = None

k_prev = None


def loadscreen():
    global screen
    global mainmenu
    global imagehead
    pygame.display.init()
    pygame.display.set_caption("Snake")
    pygame.display.set_icon(
        pygame.image.load(
            os.path.join(
                "sprites",
                "head.bmp")))
    screen = pygame.display.set_mode((640, 640))
    mainmenu = Menu.menulist(
        200, 280, [
            "Without Walls", "With Walls"], 48, 48, screen)
    pygame.event.pump()


def gameendscreen():
    global screen
    global score
    global k_prev
    while True:
        font = pygame.font.Font("freesansbold.ttf", 48)
        screen.fill((255, 255, 255))
        scoreimg = font.render("You scored: " + str(score), 1, (0, 0, 0))
        screen.blit(scoreimg, (0, 240))
        pygame.display.flip()
        pygame.event.pump()
        k = pygame.key.get_pressed()
        if k[K_RETURN]:
            k_prev = k
            break

    return


def load():

    global imagebody
    global imagehead
    global foodimg

    global snake

    global foodx
    global foody

    global score

    global skip
    global gameon

    global wall

    score = 0

    snake = []

    imagehead = pygame.image.load(os.path.join("sprites", "head.bmp"))
    imagebody = pygame.image.load(os.path.join("sprites", "snake.bmp"))
    wall = pygame.image.load(os.path.join("sprites", "walls.bmp"))
    foodimg = pygame.image.load(os.path.join("sprites", "food.bmp"))
    head = snake_part.snakepart(320, 320, screen, imagehead, True, -1)
    snake.append(head)
    snake.append(snake_part.snakepart(320, 336, screen, imagebody, False, -1))
    snake.append(snake_part.snakepart(320, 352, screen, imagebody, False, -1))
    snake.append(snake_part.snakepart(320, 368, screen, imagebody, False, -1))

    foodx = randint(1, 38) * 16
    foody = randint(1, 38) * 16

    score = 0

    skip = 0
    gameon = True


def update(gamemode):
    global update_
    global screen
    global imagebody
    global snake
    global score
    global foodx, foody
    global skip
    global gameon
    keystate = pygame.key.get_pressed()
    if keystate[K_ESCAPE]:
        print("yes")
        return (False, score)
    if gameon:
        for i in range(len(snake) - 1, -1, -1):
            if not snake[i].head:
                snake[i].update(snake[i - 1].direc)
            elif snake[i].head:
                snake[i].update(keystate)

        if snake[0].x == foodx and snake[0].y == foody:
            foodx = randint(1, 38) * 16
            foody = randint(1, 38) * 16
            score += 1
            if snake[len(snake) - 1].direc == -1:
                print("eat")
                snake.append(
                    snake_part.snakepart(
                        snake[len(snake) - 1].x,
                        snake[len(snake) - 1].y + 16,
                        screen,
                        imagebody,
                        False,
                        -1,
                    )
                )
            elif snake[len(snake) - 1].direc == 1:
                print("eat")
                snake.append(
                    snake_part.snakepart(
                        snake[len(snake) - 1].x,
                        snake[len(snake) - 1].y - 16,
                        screen,
                        imagebody,
                        False,
                        1,
                    )
                )
            elif snake[len(snake) - 1].direc == -2:
                print("eat")
                snake.append(
                    snake_part.snakepart(
                        snake[len(snake) - 1].x + 16,
                        snake[len(snake) - 1].y,
                        screen,
                        imagebody,
                        False,
                        -2,
                    )
                )
            elif snake[len(snake) - 1].direc == -1:
                print("eat")
                snake.append(
                    snake_part.snakepart(
                        snake[len(snake) - 1].x - 16,
                        snake[len(snake) - 1].y,
                        screen,
                        imagebody,
                        False,
                        2,
                    )
                )
        for i in range(1, len(snake) - 1):
            if snake[0].x == snake[i].x and snake[0].y == snake[i].y:
                gameon = False
                print("oops")
                gameendscreen()
                return (False, score)
        if gamemode == 1:
            if (
                snake[0].x == 0
                or snake[0].x > 39 * 16
                or snake[0].y == 0
                or snake[0].y > 39 * 16
            ):
                gameon = False
                print("oops")
                gameendscreen()
                return (False, score)

    for q in pygame.event.get():
        if q.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.event.pump()
    return (True, score)


def draw(gamemode):
    global screen
    global foodimg
    global snake
    global score
    global wall
    screen.fill((255, 255, 255))
    for i in snake:
        i.render()
    if gamemode == 1:
        for x in range(0, 40):
            screen.blit(wall, (x * 16, 0))
            screen.blit(wall, (x * 16, 39 * 16))
        for y in range(1, 39):
            screen.blit(wall, (0, y * 16))
            screen.blit(wall, (39 * 16, y * 16))

    font = pygame.font.Font("freesansbold.ttf", 48)
    scoreimg = font.render(str(score), 1, (0, 0, 0))
    screen.blit(foodimg, (foodx, foody))
    screen.blit(scoreimg, (0, 0))
    pygame.display.flip()
    pygame.event.pump()


def gamestart(gamemode, scr):
    global gameon
    global screen
    screen = scr
    init()
    running = True
    load()
    kprev = pygame.key.get_pressed()
    prevtime = time.time()
    currenttime = time.time()
    fps = 30
    firstloop = True
    while running:
        if (currenttime - prevtime) > (1.0 / fps) or firstloop:
            prevtime = currenttime
            firstloop = False
            ret = update(gamemode)
            running = ret[0]
            score = ret[1]
            if not running:
                break
            draw(gamemode)

        else:
            currenttime = time.time()
    return ret[1]
