import sys
import pygame
from pygame.locals import *
from Player import Player

class Game:
    def __init__(self, width, height):
        pygame.init()
        self.fps = 60
        self.fpsClock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((width, height))
        # everything must go through self.player
        self.player = Player()

    def create_tiles(self):
        num_tiles = self.player.board_size # var name is misleading, this is the number of tiles per side
        tile_size = 40
        buffer = 10

        for r in range(buffer, (num_tiles * tile_size) + buffer, tile_size + buffer):
            for c in range(buffer, (num_tiles * tile_size) + buffer, tile_size + buffer):
                rect = pygame.Rect(r, c, tile_size, tile_size)
                pygame.draw.rect(self.screen, 200, rect)


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
    game.play_game()

if __name__ == '__main__':
    main()