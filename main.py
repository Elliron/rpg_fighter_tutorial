import pygame, sys, random, math
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

run_ani_R = [pygame.image.load("resources/img/Movement_Animations/Player_Sprite_R.png"), pygame.image.load("resources/img/Movement_Animations/Player_Sprite2_R.png"),
            pygame.image.load("resources/img/Movement_Animations/Player_Sprite3_R.png"),pygame.image.load("resources/img/Movement_Animations/Player_Sprite4_R.png"),
            pygame.image.load("resources/img/Movement_Animations/Player_Sprite5_R.png"),pygame.image.load("resources/img/Movement_Animations/Player_Sprite6_R.png"),
            pygame.image.load("resources/img/Movement_Animations/Player_Sprite_R.png")]

run_ani_L = [pygame.image.load("resources/img/Movement_Animations/Player_Sprite_L.png"), pygame.image.load("resources/img/Movement_Animations/Player_Sprite2_L.png"),
            pygame.image.load("resources/img/Movement_Animations/Player_Sprite3_L.png"),pygame.image.load("resources/img/Movement_Animations/Player_Sprite4_L.png"),
            pygame.image.load("resources/img/Movement_Animations/Player_Sprite5_L.png"),pygame.image.load("resources/img/Movement_Animations/Player_Sprite6_L.png"),
            pygame.image.load("resources/img/Movement_Animations/Player_Sprite_L.png")]

attack_ani_R = [pygame.image.load("resources/img/Attack_Animations/Player_Attack_R.png"), pygame.image.load("resources/img/Attack_Animations/Player_Attack_R.png"),
                pygame.image.load("resources/img/Attack_Animations/Player_Attack2_R.png"),pygame.image.load("resources/img/Attack_Animations/Player_Attack2_R.png"),
                pygame.image.load("resources/img/Attack_Animations/Player_Attack3_R.png"),pygame.image.load("resources/img/Attack_Animations/Player_Attack3_R.png"),
                pygame.image.load("resources/img/Attack_Animations/Player_Attack4_R.png"),pygame.image.load("resources/img/Attack_Animations/Player_Attack4_R.png"),
                pygame.image.load("resources/img/Attack_Animations/Player_Attack5_R.png"),pygame.image.load("resources/img/Attack_Animations/Player_Attack5_R.png"),
                pygame.image.load("resources/img/Attack_Animations/Player_Attack_R.png")]
 
attack_ani_L = [pygame.image.load("resources/img/Attack_Animations/Player_Attack_L.png"), pygame.image.load("resources/img/Attack_Animations/Player_Attack_L.png"),
                pygame.image.load("resources/img/Attack_Animations/Player_Attack2_L.png"),pygame.image.load("resources/img/Attack_Animations/Player_Attack2_L.png"),
                pygame.image.load("resources/img/Attack_Animations/Player_Attack3_L.png"),pygame.image.load("resources/img/Attack_Animations/Player_Attack3_L.png"),
                pygame.image.load("resources/img/Attack_Animations/Player_Attack4_L.png"),pygame.image.load("resources/img/Attack_Animations/Player_Attack4_L.png"),
                pygame.image.load("resources/img/Attack_Animations/Player_Attack5_L.png"),pygame.image.load("resources/img/Attack_Animations/Player_Attack5_L.png"),
                pygame.image.load("resources/img/Attack_Animations/Player_Attack_L.png")]

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

        # position and direction
        self.vx = 0
        self.pos = vec((340, 240))
        self.vel = vec(0,0)
        self.acc = vec(0,0)

        # movement
        self.direction = "RIGHT"
        self.jumping = False
        self.running = False
        self.move_frame = 0
        # Combat
        self.attacking = False
        # cooldown between attacks
        self.cooldown = False
        self.attack_frame = 0

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
        if self.move_frame > 6:
            self.move_frame = 0
            return

        if self.jumping == False and self.running == True:
            if self.vel.x > 0:
                self.image = run_ani_R[self.move_frame]
                self.direction = "RIGHT"
            elif self.vel.x < 0:
                self.image = run_ani_L[self.move_frame]
                self.direction = "LEFT"
            self.move_frame += 1

        if abs(self.vel.x) < 0.2 and self.move_frame != 0:
            self.move_frame = 0
            if self.direction == "RIGHT":
                self.image = run_ani_R[self.move_frame]
            elif self.direction == "LEFT":
                self.image = run_ani_L[self.move_frame]

    def correction(self):
        if self.attack_frame == 1:
            self.pos.x -= 20
        if self.attack_frame == 10:
            self.pos.x += 20


    def attack(self):
        if self.attack_frame > 10:
            self.attack_frame = 0
            self.attacking = False

        if self.direction == "RIGHT":
            self.image = attack_ani_R[self.attack_frame]
        elif self.direction == "LEFT":
            self.correction()
            self.image = attack_ani_L[self.attack_frame]

        self.attack_frame += 1

    def player_hit(self):
        hits = pygame.sprite.spritecollide(self, Enemygroup, False)
        if self.cooldown == False:
            self.cooldown = True # enable the cooldown
            pygame.time.set_timer(hit_cooldown, 1000) # resets cooldown in 1 second

            pygame.display.update()

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
        self.image = pygame.image.load("resources/img/Enemy.png")
        self.rect = self.image.get_rect()
        self.pos = vec(0,0)
        self.vel = vec(0,0)
        self.direction = random.randint(0,1)
        self.vel.x = random.randint(2,6) / 2
        if self.direction == 0:
            self.pos.x = 0
            self.pos.y = 235
        if self.direction == 1:
            self.pos.x = 700
            self.pos.y = 235
    
    def move(self):
        if self.pos.x >= (WIN_WIDTH - 20):
            self.direction = 1
        elif self.pos.x <= 0:
            self.direction = 0

        if self.direction == 0:
            self.pos.x += self.vel.x
        if self.direction == 1:
            self.pos.x -= self.vel.x
        
        self.rect.center = self.pos

    def update(self):
        # check for collision with player
        hits = pygame.sprite.spritecollide(self, Playergroup, False)

        # activates if player is attacking and collision
        if hits and player.attacking == True:
            self.kill()
            print("enemy hit")
        
        # if collision with player not attacking, call "hit" function, lets player know they have been hit
        elif hits and player.attacking == False:
            player.player_hit()
            print("you got hit")

    def render(self):
        displaysurface.blit(self.image, (self.pos.x, self.pos.y))

background = Background()
ground = Ground()
ground_group = pygame.sprite.Group()
ground_group.add(ground)

enemy = Enemy()
Enemygroup = pygame.sprite.Group()
Enemygroup.add(enemy)

player = Player()
Playergroup = pygame.sprite.Group()
Playergroup.add(player)

# event that we created that can be used in game loop
hit_cooldown = pygame.USEREVENT + 1

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

            if event.key == pygame.K_RETURN:
                if player.attacking == False:
                    player.attack()
                    player.attacking = True

        if event.type == hit_cooldown:
            player.cooldown = False
            pygame.time.set_timer(hit_cooldown, 0)
    
    background.render()
    ground.render()
    # create and move enemy
    enemy.render()
    enemy.move()

    player.update()
    if player.attacking == True:
        player.attack()
    player.move()


    displaysurface.blit(player.image, player.rect)


    pygame.display.update()
    FPS_CLOCK.tick(FPS)

