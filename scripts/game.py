import pygame
from scripts import consts
from scripts.tile import Tile
from scripts.window import Window


class Game:
    def __init__(self):
        self.window = Window()
        pygame.init()

    def main_loop(self):
        running = True
        while running:
            self.window.draw_game()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.flip()
