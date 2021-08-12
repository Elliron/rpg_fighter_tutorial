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

# might put in player class but tutorial said not to, outside of class it is global
# Run animation for the RIGHT
run_ani_R = [pygame.image.load("resources/img/Movement_Animations/Player_Sprite_R.png"), pygame.image.load("resources/img/Movement_Animations/Player_Sprite2_R.png"),
            pygame.image.load("resources/img/Movement_Animations/Player_Sprite3_R.png"),pygame.image.load("resources/img/Movement_Animations/Player_Sprite4_R.png"),
            pygame.image.load("resources/img/Movement_Animations/Player_Sprite5_R.png"),pygame.image.load("resources/img/Movement_Animations/Player_Sprite6_R.png"),
            pygame.image.load("resources/img/Movement_Animations/Player_Sprite_R.png")]

# Run animation for the LEFT
run_ani_L = [pygame.image.load("resources/img/Movement_Animations/Player_Sprite_L.png"), pygame.image.load("resources/img/Movement_Animations/Player_Sprite2_L.png"),
            pygame.image.load("resources/img/Movement_Animations/Player_Sprite3_L.png"),pygame.image.load("resources/img/Movement_Animations/Player_Sprite4_L.png"),
            pygame.image.load("resources/img/Movement_Animations/Player_Sprite5_L.png"),pygame.image.load("resources/img/Movement_Animations/Player_Sprite6_L.png"),
            pygame.image.load("resources/img/Movement_Animations/Player_Sprite_L.png")]

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
        self.jumping = False
        # standing and running, can add third mode of walking
        self.running = False
        # current frame of character being displayed
        self.move_frame = 0

    def move(self):
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
        hits = pygame.sprite.spritecollide(player, ground_group, False)
        if self.vel.y > 0:
            if hits:
                lowest = hits[0]
                if self.pos.y < lowest.rect.bottom:
                    self.pos.y = lowest.rect.top + 1
                    self.vel.y = 0
                    self.jumping = False
    
    def update(self):
        # return base frame if at end of movement sequence, resets frame to 0 if it reaches 6, we hve 7 frames starting at index 0
        # more frames look smoother
        if self.move_frame > 6:
            self.move_frame = 0
            return

        # move character to next frame if conditions are met, animations
        # checks to make sure characters arent jumping or standing still, only uses animations if character is moving
        if self.jumping == False and self.running == True:
            # direction player is moving
            if self.vel.x > 0:
                # image updating from animation dic
                self.image = run_ani_R[self.move_frame]
                # sets direction variable
                self.direction = "RIGHT"
            elif self.vel.x < 0:
                self.image = run_ani_L[self.move_frame]
                self.direction = "LEFT"
            self.move_frame += 1

        # returns to the base frame if standing still and incorrect frame is showing
        if abs(self.vel.x) < 0.2 and self.move_frame != 0:
            self.move_frame = 0
            if self.direction == "RIGHT":
                self.image = run_ani_R[self.move_frame]
            elif self.direction == "LEFT":
                self.image = run_ani_L[self.move_frame]

    def attack(self):
        pass

    def jump(self):
        self.rect.x += 1
        hits = pygame.sprite.spritecollide(self, ground_group, False)

        self.rect.x -= 1
        
        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = -12

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

background = Background()
ground = Ground()
ground_group = pygame.sprite.Group()
ground_group.add(ground)
player = Player()
Playergroup = pygame.sprite.Group()

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
    player.update()
    player.move()

    displaysurface.blit(player.image, player.rect)

    pygame.display.update()
    FPS_CLOCK.tick(FPS)

