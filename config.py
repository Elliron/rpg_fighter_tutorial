import pygame

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