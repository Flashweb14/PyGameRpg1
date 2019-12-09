import pygame
from scripts import consts
from scripts.tile import Tile


def map_create():
    map = [[Tile(False) for i in range(consts.MAP_HEIGHT)] for j in range(consts.MAP_WIDTH)]
    map[0][0].block_path = True
    return map


def draw_game():
    global MAIN_SURFACE

    MAIN_SURFACE.fill(pygame.Color('gray'))

    draw_map(GAME_MAP)

    MAIN_SURFACE.blit(consts.S_PLAYER_FRONT, (400, 300))

    pygame.display.flip()

def draw_map(map):
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y].block_path:
                MAIN_SURFACE.blit(consts.S_WALL, (x * consts.CELL_SIZE, y * consts.CELL_SIZE))
            else:
                MAIN_SURFACE.blit(consts.S_FLOOR, (x * consts.CELL_SIZE, y * consts.CELL_SIZE))

def game_main_loop():
    running = True

    while running:
        draw_game()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


def game_init():
    global MAIN_SURFACE
    global GAME_MAP

    pygame.init()
    MAIN_SURFACE = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

    GAME_MAP = map_create()


if __name__ == '__main__':
    game_init()
    game_main_loop()