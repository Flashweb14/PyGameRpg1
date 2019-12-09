import pygame


pygame.init()

WINDOW_WIDTH = 832
WINDOW_HEIGHT = 640

CELL_SIZE = 64

MAP_WIDTH = WINDOW_WIDTH // CELL_SIZE
MAP_HEIGHT = WINDOW_HEIGHT  // CELL_SIZE

S_PLAYER_FRONT = pygame.image.load("../resources/sprites/player/player_front.png")
S_WALL = pygame.image.load("../resources/sprites/map/tree.png")
S_FLOOR = pygame.image.load("../resources/sprites/map/grass.png")