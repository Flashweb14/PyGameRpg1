import pygame


class Window:
    def __init__(self, width=832, height=640):
        self.width = width
        self.height = height
        self.main_window = pygame.display.set_mode((self.width, self.height))