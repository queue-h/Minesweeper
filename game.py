from tile import Tile
from board import Board
import sys
import pygame
from pygame.locals import *

# a game displays and manipulates a board
class Game:


    fps = 60
    fpsClock = pygame.time.Clock()
    tile_size = Tile.tile_size

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
                self.board.get_tile(x, y).is_revealed = True
                self.board.uncover_zeroes(x, y)
            case _:
                self.board.get_tile(x, y).is_revealed = True

    def set_image(self, image, r, c):
        image = pygame.transform.scale(image, (self.tile_size, self.tile_size))
        self.screen.blit(image, self.board.get_rect(r, c))

    def play_game(self):

        while True:
            self.screen.fill((0, 0, 0))

            # draw board
            for r in range(self.board.size):
                for c in range(self.board.size):
                    # check if tile has been revealed, then choose appropriate image
                    if self.board.get_tile(r, c).is_revealed:
                        self.set_image(self.board.get_image(r, c), r, c)
                    else:
                        self.set_image(Tile.blank, r, c)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                # handle mouse click
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    tile_clicked = self.board.determine_tile_click(mouse_x, mouse_y)

                    if tile_clicked is not None:
                        # left click means flip tile
                        if event.button == 1:
                            self.player_click(tile_clicked[0], tile_clicked[1])
                        # right click means flag image
                        if event.button == 3:
                            self.set_image("flag", tile_clicked[0], tile_clicked[1])

            pygame.display.flip()
            self.fpsClock.tick(self.fps)


if __name__ == '__main__':
    g = Game(10)
    g.play_game()