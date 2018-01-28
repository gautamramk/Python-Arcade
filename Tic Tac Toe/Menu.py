import pygame
from pygame.locals import *

class menulist():
    items = []
    fontsize = 0
    spacing = 0
    x = 0
    y = 0
    screen = None
    selected = 0
    

    def __init__(self,xl,yl,li,sp,fs,s):
        self.items = li
        self.x = xl
        self.y = yl
        self.spacing = sp
        self.fontsize = fs
        self.screen = s
        

    def update(self,k,k_prev):
        
        if k[K_w] == True and k_prev[K_w] == False:
            if self.selected == 0:
                self.selected = len(self.items)-1
            else:
                self.selected -= 1
            oldstate = k

        elif k[K_s] == True and k_prev[K_s] == False:
            if self.selected == len(self.items)-1:
                self.selected = 0
            else:
                self.selected += 1
            oldstate = k
            
    def getitem(self):
        return self.selected
    def draw(self):
        font = pygame.font.Font(None,self.fontsize)
        itemnumber = 0
        for l in self.items:
            if itemnumber == self.selected:
                lname = font.render(l,1,(128,128,0))
            else:
                lname = font.render(l,1,(0,0,0))
            self.screen.blit(lname,(self.x,self.y + self.spacing*itemnumber))
            itemnumber += 1

