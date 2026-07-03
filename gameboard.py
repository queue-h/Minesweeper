import numpy as np

class GameBoard():
    global _board, _size, _NUM_BOMBS

    def __init__(self, size):
        if (not isinstance(size, int)) or size == 0:
            raise SyntaxError("Size must be a non-zero integer")
        self._size = size
        self._NUM_BOMBS = self._size * 5

    def generate_board(self):
        self._board = np.zeros((self._size, self._size)).astype(int)

        # set bombs
        bomb_list = self.get_bomb_list()
        for r in range(self._size):
            for c in range(self._size):
                # if location is in bombList, place a bomb (-1)
                temp_coord = (r, c)
                if temp_coord in bomb_list:
                    self._board[r][c] = -1

        # count number of nearby bombs
        for r in range(self._size):
            for c in range(self._size):
                if not self._board[r][c] == -1:
                    nearby_bombs = 0

                    # check top right, up, top left, right, left, bottom right, down, bottom left neighbors
                    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

                    # find boundary cell coords
                    for row_dir, col_dir in directions:
                        new_row, new_col = r + row_dir, c + col_dir

                        # check bounds
                        if 0 <= new_row < self._size and 0 <= new_col < self._size:
                            # check for bomb
                            if self._board[new_row][new_col] == -1:
                                nearby_bombs += 1
                    # document in cell
                    self._board[r][c] = nearby_bombs

        return self._board


    # get the locations of the bombs
    # if there's a library with a method that does this (there must be)
    # then I couldn't find it
    def get_bomb_list(self):
        # since the python set.add(x) function returns 'x' and not a boolean
        # there's really no difference between a list and a set
        bomb_list = set()

        # add NUM_BOMBS points to set
        for x in range(0, self._size):
            # get bomb coords
            x = np.random.randint(self._size)
            y = np.random.randint(self._size)
            coord = (x, y)
            # if the set already contains point (duplicate), deprecate x
            if coord in bomb_list:
                x -= 1
            else:
                bomb_list.add(coord)

        return bomb_list

# run
def main():
    board = GameBoard(10)
    board.generate_board()
    print(board)


