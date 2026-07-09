import enum
import sys
import pygame
from pygame.locals import *
from Player import Player

class Tile:
    # tile size and buffer might need to be passed in to account for changing window sizes
    # but that's a later problem
    tile_size = 40
    buffer = 10

    # every tile must have an x and y based on board location, x and y graphical location (independently calculated),
    # size (global for now), buffer (global for now), and a status (-1 = tile is bomb, [0, 8] = num of surrounding bombs)
    def __init__(self, x, y, board):
        self.board_x = x
        self.board_y = y
        self.status = board[x, y]
        self.screen_x, self.screen_y = self.get_screen_coord()

    def get_rect(self):
        return pygame.Rect(self.screen_x, self.screen_y, self.tile_size, self.tile_size)

    def get_screen_coord(self):
        return (self.board_x * self.tile_size) + self.buffer, (self.board_y * self.tile_size) + self.buffer

class Game:
    # i want to add ability to set board size, but i don't want to fuck with anything else right now
    def __init__(self, width, height):
        # set up pygame
        pygame.init()
        self.fps = 60
        self.fpsClock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((width, height))
        # everything must go through self.player
        self.player = Player()
        self.board = self.player._board

    def create_tiles(self):
        # i think i will probably need a matrix of tiles
        # i might want to refactor the gameboard class
        # shit


        # num_tiles = self.player.board_size # var name can be misleading, this is the number of tiles per side
        #
        # for r in range(buffer, (num_tiles * tile_size) + buffer, tile_size + buffer):
        #     for c in range(buffer, (num_tiles * tile_size) + buffer, tile_size + buffer):
        #         rect = pygame.Rect(r, c, tile_size, tile_size)
        #         pygame.draw.rect(self.screen, 200, rect)

        button = pygame.Rect(5, 5, 20, 20) # this is a trial button, to see if i can do it with one before i try 100
        b = pygame.draw.rect(self.screen, (255, 255, 255), button)
        pygame.display.flip() # i don't know what this does

        # loop to check for mouse action and its position
        # figure out how to check if the mouse has clicked on a button--this is going to be
        # a huge pain in the ass for no reason
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # if mouse is pressed get position of cursor
                    pos = pygame.mouse.get_pos()
                    ## check if cursor is on button
                    if b.collidepoint(pos):
                        ## exit ##
                        return

    def play_game(self):
        # Game loop.
        while True:
            self.screen.fill((255, 255, 255))
            self.create_tiles()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            # left click (uncover point)
            if pygame.mouse.get_pressed(num_buttons = 3)[0]:
                pass


            # right click (place flag)
            if pygame.mouse.get_pressed(num_buttons = 3)[1]:
                pass

            # Update

            # Draw

            # increment time
            pygame.display.flip()
            self.fpsClock.tick(self.fps)

def main():
    game = Game(640, 480)
    game.create_tiles()

if __name__ == '__main__':
    main()