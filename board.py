from tile import Tile
import numpy.random as random

# a board holds and manipulates tiles
class Board:
    # i want to add ability to set board size, but i don't want to fuck with anything else right now
    def __init__(self, size):
        if (not isinstance(size, int)) or size == 0:
            raise SyntaxError("Size must be a non-zero integer")
        self.size = size

        self.matrix = [] # put it here instead of in create_tiles so its global
        # populates self.matrix with objects
        self.create_tiles()

        # set tile statuses (bomb, number of surrounding bombs)
        self.bomb_freq = 0.15 # idk
        self.set_statuses()

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
                # make sure tile is not a bomb
                if not self.matrix[r][c] == -1:
                    # placeholder
                    nearby_bombs = 0

                    # check top right, up, top left, right, left, bottom right, down, bottom left neighbors
                    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

                    # search all the boundary cells
                    # (its a little pythonic, but this does work)
                    for row_dir, col_dir in directions:
                        new_row, new_col = r + row_dir, c + col_dir

                        # check bounds
                        if 0 <= new_row < self.size and 0 <= new_col < self.size:
                            # check for bomb
                            if self.matrix[new_row][new_col] == -1:
                                nearby_bombs += 1 # increment count if there is a bomb
                    # update tile
                    self.matrix[r][c].set_status(nearby_bombs)


    # set_statuses helper method
    # determine where the bombs are
    def set_bombs(self):
        for r in range(self.size):
            for c in range(self.size):
                # generate a random number, and if it is less than bomb_freq, change tile status to bomb (-1)
                if random.random() < self.bomb_freq:
                    self.matrix[r][c].set_status(-1)

    # return status of the tile
    def get_status(self, r, c):
        return self.matrix[r][c].status

    def get_rect(self, r, c):
        return self.matrix[r][c].rect

    def get_tile(self, r, c):
        return self.matrix[r][c]


def main():
    board = Board(8)

if __name__ == '__main__':
    main()