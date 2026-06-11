from ctypes.wintypes import SIZE
from unittest import case

from gameboard import GameBoard
import numpy as np

class Player:
    board_size = 10
    # create new gameboard object
    _board = GameBoard(board_size)
    # is game running?
    _game = True
    # board the player sees
    display_board = np.full((board_size, board_size), '#')

    def __init__(self):
        # generate the board
        self._board = self._board.generate_board()

    # if the player's first click is on a bomb, sucks to suck
    # ill fix it later
    def player_click(self, x, y):
        match self._board[x][y]:
            # lose condition
            case -1:
                _game = False
            # recursively uncover zeroes
            case 0:
                pass
            # uncover number
            case _:
                self.display_board[x][y] = self._board[x][y]

    def uncover_zeroes(self, x, y):
        if self._board[x][y] != 0:
            return
        else:
            self.display_board[x][y] = 0
        # search up
        if y - 1 >= 0 and self._board[x][y - 1] == '#':
            return self.uncover_zeroes(x, y - 1)
        # search down
        if y + 1 < self.board_size and self._board[x][y + 1] == '#':
            return self.uncover_zeroes(x, y + 1)
        # search left
        if x - 1 >= 0 and self._board[x - 1][y] == '#':
            return self.uncover_zeroes(x - 1, y)
        # search right
        if x + 1 < self.board_size and self._board[x + 1][y] == '#':
            return self.uncover_zeroes(x + 1, y)

        return

    # print board
    def __str__(self):
        board_str = ""
        for r in range(self.board_size):
            for c in range(self.board_size):
                board_str += str(self.display_board[r][c]) + "  "
            board_str += "\n"
        return board_str