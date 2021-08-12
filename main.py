import pygame, sys, random
from pygame.locals import *
# from tkinter import filedialog
# from tkinter import *
from config import *

pygame.init()

vec = pygame.math.Vector2
WIN_HEIGHT = 350
WIN_WIDTH = 700
ACC = 0.3
FRIC = -10
FPS = 60
FPS_CLOCK = pygame.time.Clock()
COUNT = 0

displaysurface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Glenns RPG Fighter Game Practice")



# main game classes
class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # background image to be used
        self.bgimage = pygame.image.load("resources/img/Background.png")
        # used later for scrolling background
        self.bgY = 0
        self.bgX = 0

    # display background on pygame window
    def render(self):
        displaysurface.blit(self.bgimage, (self.bgX, self.bgY))

class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # ground image to be used
        self.image = pygame.image.load("resources/img/Ground.png")
        # rectangle drawn around the image to make it interactable
        self.rect = self.image.get_rect(center = (350, 350))
    # draws image on the screen
    def render(self):
        displaysurface.blit(self.image, (self.rect.x, self.rect.y))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

# create objects for classes
background = Background()
ground = Ground()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

        if event.type == pygame.KEYDOWN:
            pass
    
    # draw images onto screen, order matters
    background.render()
    ground.render()

    # pygame updates and runs FPS at 60
    pygame.display.update()
    FPS_CLOCK.tick(FPS)
