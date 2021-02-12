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


class menulist:
    items = []
    fontsize = 0
    spacing = 0
    x = 0
    y = 0
    screen = None
    selected = 0

    def __init__(self, xl, yl, li, sp, fs, s):
        self.items = li
        self.x = xl
        self.y = yl
        self.spacing = sp
        self.fontsize = fs
        self.screen = s

    def update(self, k, k_prev):

        if k[K_w] and k_prev[K_w] == False:
            if self.selected == 0:
                self.selected = len(self.items) - 1
            else:
                self.selected -= 1
            oldstate = k

        elif k[K_s] and k_prev[K_s] == False:
            if self.selected == len(self.items) - 1:
                self.selected = 0
            else:
                self.selected += 1
            oldstate = k

    def getitem(self):
        return self.selected

    def draw(self):
        font = pygame.font.Font("freesansbold.ttf", self.fontsize)
        itemnumber = 0
        for l in self.items:
            if itemnumber == self.selected:
                lname = font.render(l, 1, (128, 128, 0))
            else:
                lname = font.render(l, 1, (0, 0, 0))
            self.screen.blit(
                lname, (self.x, self.y + self.spacing * itemnumber))
            itemnumber += 1
