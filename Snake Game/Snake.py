import pygame
from pygame.locals import *
import snake_part
import Menu
import os
import time
from random import randint

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
    pygame.display.set_icon(pygame.image.load(os.path.join("sprites","head.bmp")))
    screen = pygame.display.set_mode((640,640))
    mainmenu = Menu.menulist(200,280,["Without Walls","With Walls"],48,48,screen)
    pygame.event.pump()

def gameendscreen():
    global screen
    global score
    global k_prev
    while True:
        font = pygame.font.Font("freesansbold.ttf",48)
        screen.fill((255,255,255))
        scoreimg = font.render("You scored: "+str(score),1,(0,0,0))
        screen.blit(scoreimg,(0,240))
        pygame.display.flip()
        pygame.event.pump()
        k = pygame.key.get_pressed()
        if k[K_RETURN] == True:
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
    
    
    
    
    imagehead = pygame.image.load(os.path.join("sprites","head.bmp"))
    imagebody = pygame.image.load(os.path.join("sprites","snake.bmp"))
    wall = pygame.image.load(os.path.join("sprites","wall.bmp"))
    foodimg = pygame.image.load(os.path.join("sprites","food.bmp"))
    head = snake_part.snakepart(320,320,screen,imagehead,True,-1)
    snake.append(head)
    snake.append(snake_part.snakepart(320,336,screen,imagebody,False,-1))
    snake.append(snake_part.snakepart(320,352,screen,imagebody,False,-1))
    snake.append(snake_part.snakepart(320,368,screen,imagebody,False,-1))
    
    foodx = randint(1,38)*16
    foody = randint(1,38)*16
    
    score = 0

    skip = 0
    gameon = True

def update(gamemode):
    global update_
    global screen
    global imagebody
    global snake
    global score
    global foodx,foody
    global skip
    global gameon
    keystate = pygame.key.get_pressed()
    if keystate[K_ESCAPE] == True:
        print "yes"
        return False
    if gameon:
        for i in range(len(snake)-1,-1,-1):
            if snake[i].head == False:
                snake[i].update(snake[i-1].direc)
            elif snake[i].head == True:
                snake[i].update(keystate)
                
        if snake[0].x == foodx and snake[0].y == foody:
            foodx = randint(1,38)*16
            foody = randint(1,38)*16
            score += 1
            if snake[len(snake)-1].direc == -1:
                print "eat"
                snake.append(snake_part.snakepart(snake[len(snake)-1].x,snake[len(snake)-1].y+16,screen,imagebody,False,-1))
            elif snake[len(snake)-1].direc == 1:
                print "eat"
                snake.append(snake_part.snakepart(snake[len(snake)-1].x,snake[len(snake)-1].y-16,screen,imagebody,False,1))
            elif snake[len(snake)-1].direc == -2:
                print "eat"
                snake.append(snake_part.snakepart(snake[len(snake)-1].x+16,snake[len(snake)-1].y,screen,imagebody,False,-2))
            elif snake[len(snake)-1].direc == -1:
                print "eat"
                snake.append(snake_part.snakepart(snake[len(snake)-1].x-16,snake[len(snake)-1].y,screen,imagebody,False,2))
        for i in range(1,len(snake)-1):
            if snake[0].x == snake[i].x and snake[0].y == snake[i].y:
                gameon = False
                print "oops"
                gameendscreen()
                return False
        if gamemode == 1:
            if snake[0].x == 0 or snake[0].x > 39*16 or snake[0].y == 0 or snake[0].y > 39*16:
                gameon = False
                print "oops"
                gameendscreen()
                return False
        
    for q in pygame.event.get():
        if q.type == pygame.QUIT:
            pygame.quit()
            return False
    
    pygame.event.pump()
    return True

def draw(gamemode):
    global screen
    global foodimg
    global snake
    global score
    global wall
    screen.fill((255,255,255))
    for i in snake:
        i.render()
    if gamemode == 1:
        for x in range(0,40):
            screen.blit(wall,(x*16,0))
            screen.blit(wall,(x*16,39*16))
        for y in range(1,39):
            screen.blit(wall,(0,y*16))
            screen.blit(wall,(39*16,y*16))
       
    font = pygame.font.Font("freesansbold.ttf",48)
    scoreimg = font.render(str(score),1,(0,0,0))
    screen.blit(foodimg,(foodx,foody))
    screen.blit(scoreimg,(0,0))
    pygame.display.flip()
    pygame.event.pump()


def gamestart(gamemode):
    global gameon
    init()
    running = True
    load()
    kprev = pygame.key.get_pressed()
    prevtime = time.time()
    currenttime = time.time()
    fps = 30
    firstloop=True
    while running == True:
        if (currenttime - prevtime) > (1.0/fps) or firstloop == True:
            prevtime = currenttime
            firstloop = False
            running = update(gamemode)
            if not running:
                break
            draw(gamemode)
            
        else:
            currenttime = time.time()
    
def main():
    global gameon
    global screen
    global mainmenu
    global k_prev
    running = True
    loadscreen()
    skip = 0
    while running == True:
        
        screen.fill((128,128,128))
        keystate = pygame.key.get_pressed()
        font = pygame.font.Font("freesansbold.ttf",72)
        instfont = pygame.font.Font("freesansbold.ttf",24)
        titleimg = font.render("Snake",1,(0,0,0))
        inst = instfont.render("Use wasd for movement and enter to select option.",1,(0,0,0))
        screen.blit(titleimg,(220,100))
        screen.blit(inst,(0,500))
        mainmenu.update(keystate,k_prev)
        mainmenu.draw()
        if keystate[K_RETURN] and k_prev[K_RETURN] == False :
            gamestart(mainmenu.getitem())
        for q in pygame.event.get():
            if q.type == pygame.QUIT:
                pygame.quit()
                running = False
        pygame.display.flip()
        pygame.event.pump()
        k_prev = keystate
            
        
        
main()
