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
FRIC = -0.10
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
        # tracks state of player if jumping or not
        self.jumping = False

    def move(self):
        # keep constant acc of 0.5 in the downwards direction (gravity)
        self.acc = vec(0, 0.5)
        if abs(self.vel.x) > 0.3:
            self.running = True
        else:
            self.running = False

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > WIN_WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIN_WIDTH
        self.rect.midbottom = self.pos


    def gravity_check(self):
        # spritecollide takes 3 parameters, sprite being tested, sprite group to be tested against, and whether it kills the sprite or not
        # can check collisions against hundreds of sprites in a single function
        hits = pygame.sprite.spritecollide(player, ground_group, False)
        # checks to see if the character has vel in a downwards direcetion, if not he is on the ground and not falling
        if self.vel.y > 0:
            # if hits records a collision between player and ground
            if hits:
                lowest = hits[0]
                if self.pos.y < lowest.rect.bottom:
                    self.pos.y = lowest.rect.top + 1
                    self.vel.y = 0
                    self.jumping = False
    
    def update(self):
        pass

    def attack(self):
        pass

    def jump(self):
        self.rect.x += 1
        # check to see if player is touching ground
        hits = pygame.sprite.spritecollide(self, ground_group, False)

        self.rect.x -= 1
        
        # if touching ground and not jumping cause player to jump
        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = -12

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

background = Background()
ground = Ground()
# creates a sprite group for collisions
ground_group = pygame.sprite.Group()
# adds ground to the sprite group
ground_group.add(ground)
player = Player()

while True:
    player.gravity_check()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()
    
    background.render()
    ground.render()
    player.move()

    displaysurface.blit(player.image, player.rect)

    pygame.display.update()
    FPS_CLOCK.tick(FPS)

