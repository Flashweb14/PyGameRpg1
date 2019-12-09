import pygame
from scripts import consts
from scripts.window import Window
from scripts.player import Player


class Game:
    def __init__(self):
        pygame.init()
        self.window = Window()
        self.player = Player(3, 3, consts.S_PLAYER_FRONT, self)

    def main_loop(self):
        running = True
        while running:
            self.window.draw_game()
            self.player.draw_self()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.player.move(0, -1)
                    if event.key == pygame.K_s:
                        self.player.move(0, 1)
                    if event.key == pygame.K_a:
                        self.player.move(-1, 0)
                    if event.key == pygame.K_d:
                        self.player.move(1, 0)
            pygame.display.flip()
