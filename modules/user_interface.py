import pygame
import sys
from pygame.locals import *
import heapq


class UserInterface:
    def __init__(self, Maze):
        pygame.init()

        size_of_each_block = 800 // len(Maze[0])

        window_width = size_of_each_block * len(Maze[0])
        window_height = size_of_each_block * len(Maze)

        # Set the title of the window
        pygame.display.set_caption('Maze Maker')

        size = (window_width, window_height)
        self.surface = pygame.display.set_mode(size)


        self.PathColor = (255, 255, 255)
        self.WallColor = (0, 0, 0)

        pygame.display.flip()

        self.draw_maze(Maze)

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

    def draw_maze(self, Maze):
        size_of_each_block = 800 // len(Maze[0])

        """
        Function that draws the maze.
        """
        for y in range(len(Maze)):
            for x in range(len(Maze[y])):
                if Maze[y][x] == '#':
                    pygame.draw.rect(self.surface, self.WallColor, (x * size_of_each_block, y * size_of_each_block, size_of_each_block, size_of_each_block))
                elif Maze[y][x] == ' ':
                    pygame.draw.rect(self.surface, self.PathColor, (x * size_of_each_block, y * size_of_each_block, size_of_each_block, size_of_each_block))
                elif Maze[y][x] == 'S':
                    pygame.draw.rect(self.surface, (0, 255, 0), (x * size_of_each_block, y * size_of_each_block, size_of_each_block, size_of_each_block))
                elif Maze[y][x] == 'E':
                    pygame.draw.rect(self.surface, (255, 0, 0), (x * size_of_each_block, y * size_of_each_block, size_of_each_block, size_of_each_block))
                elif Maze[y][x] == 'P':
                    pygame.draw.rect(self.surface, (0, 0, 255), (x * size_of_each_block, y * size_of_each_block, size_of_each_block, size_of_each_block))