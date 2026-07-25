from board import Board
import sys
import numpy as np
import pygame
from pygame.locals import *

# a game displays and manipulates a board
class Game:
    
    images = ["/icons/0_zero.png", "/icons/1_one.png", "/icons/2_two.png", "/icons/3_three.png",
              "/icons/4_four.png", "/icons/5_five.png", "/icons/6_six.png", "/icons/7_seven.png",
              "/icons/8_eight.png", "/icons/-1_bomb.png"]

    fps = 60
    fpsClock = pygame.time.Clock()

    def __init__(self, board_size):
        # create new board object
        self.board = Board(board_size)
        # is game running? (a bit of a misnomer--if the player loses, it switches to false)
        self.game = True

        pygame.init()
        # someday the screen will auto-adjust, but today is not that day
        self.screen_width, self.screen_height = 640, 480
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

    # if the player's first click is on a bomb, sucks to suckkkkk
    # ill fix it later
    def player_click(self, x, y):
        match self.board.get_status(x, y):
            # lose condition
            case -1:
                self.game = False
            # recursively uncover zeroes
            case 0:
                pass
            # uncover number
            # i don't know what this is supposed to be yet
            case _:
                pass

    def play_game(self):

        while True:
            self.screen.fill((0, 0, 0))

            # draw board
            for r in range(self.board.size):
                for c in range(self.board.size):
                    # underlying squares
                    pygame.draw.rect(self.screen, (255, 255, 255), self.board.get_rect(r, c))
                    # put text on top

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            # will check for player click and then pass to method somewhere here

            # Draw.

            pygame.display.flip()
            self.fpsClock.tick(self.fps)

    # flood-fill expose zeroes
    def uncover_zeroes(self, x, y):
        if self.board.get_rect(x, y) != 0:
            return
        else:
            self.display_board[x][y] = 0
        # search up
        if y - 1 >= 0 and self.display_board[x][y - 1] == '#':
            self.uncover_zeroes(x, y - 1)
        # search down
        if y + 1 < self.board.size and self.display_board[x][y + 1] == '#':
            self.uncover_zeroes(x, y + 1)
        # search left
        if x - 1 >= 0 and self.display_board[x - 1][y] == '#':
            self.uncover_zeroes(x - 1, y)
        # search right
        if x + 1 < self.board.size and self.display_board[x + 1][y] == '#':
            self.uncover_zeroes(x + 1, y)

    # print board

if __name__ == '__main__':
    g = Game(10)
    g.play_game()