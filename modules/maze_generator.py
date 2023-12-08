import random

class MazeGenerator:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.camefrom = {}

    def generate_maze(self):
        """
        Generates a maze using the iterative backtracking algorithm.
        """
        maze = [['#']*self.width for _ in range(self.height)]
        self.iterative_backtracking(maze, 1, 1, self.width - 1, self.height - 1, self.width, self.height)
        return maze

    def iterative_backtracking(self, maze, start_x, start_y, end_x, end_y, width, height):
        """
        Function that generates a maze using the iterative backtracking algorithm.
        """
        stack = [(start_x, start_y)]

        while stack:
            x, y = stack[-1]
            maze[y][x] = ' '

            neighbors = [(x + dx, y + dy) for dx, dy in [(0, 2), (0, -2), (2, 0), (-2, 0)]]
            random.shuffle(neighbors)

            found = False
            for nx, ny in neighbors:
                if 0 < nx < width and 0 < ny < height and maze[ny][nx] == '#':
                    maze[(y + ny) // 2][(x + nx) // 2] = ' '
                    stack.append((nx, ny))
                    found = True
                    break

            if not found:
                stack.pop()

        maze[start_y][start_x] = 'S'
        maze[end_y][end_x] = 'E'

    def fetch_starting_point(self, maze):
        """
        Function that fetches the starting point of the maze.
        """
        for y in range(len(maze)):
            for x in range(len(maze[y])):
                if maze[y][x] == 'S':
                    return x, y
    
    def fetch_ending_point(self, maze):
        """
        Function that fetches the ending point of the maze.
        """
        for y in range(len(maze)):
            for x in range(len(maze[y])):
                if maze[y][x] == 'E':
                    return x, y
                