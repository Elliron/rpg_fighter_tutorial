import pygame, sys, random
from pygame.locals import *
# from tkinter import filedialog
# from tkinter import *
# from config import *

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
        self.image = pygame.image.load("resources/img/Player_Sprite_R.png")
        self.rect = self.image.get_rect()

        self.vx = 0
        self.pos = vec((340, 240))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.direction = "RIGHT"
        self.SPEED = 3

    def move(self):
        # will set running to false if the player has slowed down to a certain extent
        # checks if the player is running, player will move forward even after taking hand off button
        if abs(self.vel.x) > 0.3:
            self.running = True
        else:
            self.running = False

        # gets keeys that are pressed
        pressed_keys = pygame.key.get_pressed()
        # accelerates player in direction of key press
        if pressed_keys[K_LEFT]:
            self.pos.x += -ACC
        if pressed_keys[K_RIGHT]:
            self.pos.x += ACC

        # Physics, equations of motion
        # acceleration calculated bassed off velocity and friction, position updated based off distance covered which is calculated based off acc and vel
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        # self.pos updates position with new values
        self.pos += self.vel + 0.5 * self.acc

        # warp character from one spot to another
        if self.pos.x > WIN_WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIN_WIDTH
        # updates rec with new position
        self.rect.midbottom = self.pos


        
    
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
    # call player movement
    player.move()

    displaysurface.blit(player.image, player.rect)

    pygame.display.update()
    FPS_CLOCK.tick(FPS)

