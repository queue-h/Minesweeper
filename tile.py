import pygame

class Tile:
    class Tile:
        # tile size and buffer might need to be passed in to account for changing window sizes
        # but that's a later problem
        tile_size = 40
        buffer = 10

        # every tile must have an x and y based on board location, x and y graphical location (independently calculated),
        # size (global for now), buffer (global for now), and a status (-1 = tile is bomb, [0, 8] = num of surrounding bombs)
        def __init__(self, x, y, status):
            self.board_x = x
            self.board_y = y
            self.status = status
            # rectangle object to be drawn in the Game class
            self.screen_x, self.screen_y = self.get_screen_coord()
            self.rect = self.get_rect()

        def get_rect(self):
            return pygame.Rect(self.screen_x, self.screen_y, self.tile_size, self.tile_size)

        def get_screen_coord(self):
            return (self.board_x * self.tile_size) + self.buffer, (self.board_y * self.tile_size) + self.buffer