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



class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.bgimage = pygame.image.load("resources/img/Background.png")
        self.bgY = 0
        self.bgX = 0

    def render(self):
        displaysurface.blit(self.bgimage, (self.bgX, self.bgY))

class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("resources/img/Ground.png")
        self.rect = self.image.get_rect(center = (350, 350))
    def render(self):
        displaysurface.blit(self.image, (self.rect.x, self.rect.y))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # load character image
        self.image = pygame.image.load("resources/img/Player_Sprite_R.png")
        # create interactable rectangle the size of character image
        self.rect = self.image.get_rect()

        # Position and direction
        self.vx = 0
        # use vector object created in first tutorial, 2 components, accessed in format self.pos.x and self.pos.y
        # self.pos = player position
        self.pos = vec((340, 240))
        # self.vel = player velocity
        self.vel = vec(0,0)
        # self.acc = player acceleration
        self.acc = vec(0,0)
        # current direction player is facing
        self.direction = "RIGHT"

    def move(self):
        pass
    
    def update(self):
        pass

    def attack(self):
        pass

    def jump(self):
        pass

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

background = Background()
ground = Ground()
player = Player()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

        if event.type == pygame.KEYDOWN:
            pass
    
    background.render()
    ground.render()
    # doesnt need to use render, playey.rect supplies coordinates for character
    displaysurface.blit(player.image, player.rect)

    pygame.display.update()
    FPS_CLOCK.tick(FPS)
