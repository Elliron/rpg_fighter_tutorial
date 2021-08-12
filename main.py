import pygame, sys, random
from pygame.locals import *
# tkinter is used for creating new windows
# from tkinter import filedialog
# from tkinter import *
from config import *

# initialize pygame
pygame.init()

# Declare variables in program, this will go in config
vec = pygame.math.Vector2
# window height and width
WIN_HEIGHT = 350
WIN_WIDTH = 700
# acceleration and friction for creating physics in game
ACC = 0.3
FRIC = -10
# frames per second, how many times the game loop runs in a single second
FPS = 60
# clock object when used with FPS limits game loop to 60 frames per second
FPS_CLOCK = pygame.time.Clock()
# not sure what count is for  yet
COUNT = 0

# creates display for game surface
displaysurface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
# changes window title from default to the new title
pygame.display.set_caption("Glenns RPG Fighter Game Practice")

# main game classes
class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


while True:
    for event in pygame.event.get():
        # will run when the close window button is clicked
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # for events that occur upon clicking the left mouse button
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

        # event handling for a range of different key presses
        if event.type == pygame.KEYDOWN:
            pass