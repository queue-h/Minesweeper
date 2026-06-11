import unittest
from gameboard import GameBoard
from Player import Player
import numpy as np
import random

class test_uncover_zeroes(unittest.TestCase):

    player = Player()
    zero_indices = np.where(player._board==0)

    def setUp(self):
        # display initial board
        print(self.player._board)

    def test_uncover_zeroes(self):
        # choose random zero point
        starting_point = random.choice(self.zero_indices)

        self.player.uncover_zeroes(starting_point[0], starting_point[1])
        print(self.player)





