import unittest
from gameboard import GameBoard
from Player import Player
import numpy as np
import random

class test_uncover_zeroes(unittest.TestCase):

    # create object (everything must go through self.player)
    player = Player()

    # find the coordinates of all the zeroes
    zeroes_x, zeroes_y = np.where(player._board==0)
    zero_indices = set(zip(zeroes_x, zeroes_y))

    def setUp(self):
        # display initial board
        print(self.player._board)

    def test_uncover_zeroes(self):
        # choose random zero point
        starting_point = random.choice(list(self.zero_indices))

        # uncover zeroes and pull out indices for testing
        self.player.uncover_zeroes(starting_point[0], starting_point[1])
        uncovered_zeroes_x, uncovered_zeroes_y = np.where(self.player.display_board==0)
        uncovered_zeroes = set(zip(uncovered_zeroes_x, uncovered_zeroes_y))

        # assert all uncovered zeroes are in original list
        self.assertTrue(uncovered_zeroes.issubset(self.zero_indices))

        # this does not check for false negatives (zeroes that should have been uncovered, but weren't)





