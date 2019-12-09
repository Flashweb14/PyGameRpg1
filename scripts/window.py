import pygame
from scripts.tile import Tile
from scripts import consts
from scripts.utilities import translate_coords


class Window:
    def __init__(self, cell_size=64, width=832, height=640):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.map_width = self.width // self.cell_size
        self.map_height = self.height // self.cell_size
        self.main_surface = pygame.display.set_mode((self.width, self.height))
        self.map = self.map_create()

    def map_create(self):
        map = [[Tile(False) for i in range(self.map_height)] for j in range(self.map_width)]
        map[2][2].block_path = True
        return map

    def draw_game(self):
        self.main_surface.fill(pygame.Color('gray'))
        self.draw_map()
     #   self.main_surface.blit(consts.S_PLAYER_FRONT, translate_coords((0, 0), 64))

    def draw_map(self):
        for x in range(len(self.map)):
            for y in range(len(self.map[x])):
                if self.map[x][y].block_path:
                    self.main_surface.blit(consts.S_WALL, (x * self.cell_size, y * self.cell_size))
                else:
                    self.main_surface.blit(consts.S_FLOOR, (x * self.cell_size, y * self.cell_size))
