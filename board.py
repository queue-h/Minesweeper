import pygame
from pygame.locals import *

from tile import Tile
import numpy.random as random

# a board holds and manipulates tiles
class Board:
    # i want to add ability to set board size, but i don't want to fuck with anything else right now
    def __init__(self, size):
        if (not isinstance(size, int)) or size == 0:
            raise SyntaxError("Size must be a non-zero integer")
        self.size = size
        self.buffer = size // 10

        self.matrix = [] # put it here instead of in create_tiles so its global
        # populates self.matrix with objects
        self.create_tiles()

        # set tile statuses (bomb, number of surrounding bombs)
        self.bomb_freq = 0.2 # idk
        self.set_statuses()

        for r in range(len(self.matrix)):
            for c in range(len(self.matrix)):
             print(self.get_status(r, c), end = " ")
             print()

    def create_tiles(self):
        for r in range(self.size):
            temp_row = []
            for c in range(self.size):
                # zero is a placeholder
                # i think i will need to set status post-init
                temp_row.append(Tile(r, c))
            self.matrix.append(temp_row)

    def set_statuses(self):
        self.set_bombs()

        # count number of nearby bombs
        for r in range(self.size):
            for c in range(self.size):
                num_bombs = 0
                tile = self.matrix[r][c]
                # make sure is not a bomb
                if tile.status != -1:
                    # check top right, up, top left, right, left, bottom right, down, bottom left neighbors
                    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

                    # search all the boundary cells
                    # (its a little pythonic, but this does work)
                    for row_dir, col_dir in directions:
                        new_row, new_col = r + row_dir, c + col_dir

                        # check bounds
                        if 0 <= new_row < self.size and 0 <= new_col < self.size:
                            # check new space is a bomb
                            new_tile = self.matrix[new_row][new_col]
                            if new_tile.status == -1:
                                num_bombs += 1 # increment count if there is a bomb
                    # update tile
                    tile.set_status(num_bombs)


    # set_statuses helper method
    # determine where the bombs are
    def set_bombs(self):
        num_bombs = 0
        for r in range(self.size):
            for c in range(self.size):
                # generate a random number, and if it is less than bomb_freq, change tile status to bomb (-1)
                if random.random() < self.bomb_freq:
                    self.matrix[r][c].set_status(-1)

    # flood-fill expose zeroes
    def uncover_zeroes(self, x, y):
        if self.matrix[x][y].status == 0:
            self.matrix[x][y].is_revealed = True
        else:
            return
        # search up
        if y - 1 >= 0 and not self.matrix[x][y - 1].is_revealed:
            self.uncover_zeroes(x, y - 1)
        # search down
        if y + 1 < self.size and not self.matrix[x][y + 1].is_revealed:
            self.uncover_zeroes(x, y + 1)
        # search left
        if x - 1 >= 0 and not self.matrix[x - 1][y].is_revealed:
            self.uncover_zeroes(x - 1, y)
        # search right
        if x + 1 < self.size and not self.matrix[x + 1][y].is_revealed:
            self.uncover_zeroes(x + 1, y)

    def determine_tile_click(self, x, y):
        for r in range(self.size):
            for c in range(self.size):
                # it needs a rect to collide with, so we'll just make a point-sized rect
                # this really seems like the wrong solution
                mouse_rect = Rect(x - 1, y - 1, 2, 2)
                tile_rect = self.matrix[r][c].rect

                if pygame.Rect.colliderect(mouse_rect, tile_rect):
                    return r, c
        return None

    # convenience methods
    def get_status(self, r, c):
        return self.matrix[r][c].status

    def get_rect(self, r, c):
        return self.matrix[r][c].rect

    def get_image(self, r, c):
        tile = self.matrix[r][c]
        if tile.is_revealed:
            return tile.true_image
        return tile.blank

    def get_tile(self, r, c):
        return self.matrix[r][c]

    def get_blank(self):
        return self.matrix[0][0].blank



if __name__ == '__main__':
    board = Board(8)

