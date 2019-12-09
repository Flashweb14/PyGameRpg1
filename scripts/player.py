from scripts.object import Object
from scripts.utilities import translate_coords


class Player(Object):
    def __init__(self, x, y, sprite, game):
        super().__init__(x, y, sprite)
        self.game = game

    def draw_self(self):
        self.game.window.main_surface.blit(self.sprite, translate_coords((self.x, self.y), self.game.window.cell_size))

    def move(self, delta_x, delta_y):
        if not self.game.window.map[self.x + delta_x][self.y + delta_y].block_path:
            self.x += int(delta_x)
            self.y += int(delta_y)
