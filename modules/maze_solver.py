import heapq

class MazeSolver:
    def __init__(self, maze, starting_point, ending_point):
        self.maze = maze
        self.starting_point = starting_point
        self.ending_point = ending_point
        self.camefrom = {}
        self.path = []
        self.path_cost = 0
        self.path_found = False
    
    def a_star(self, maze, start, end):
        """
        Function that finds the shortest path from the starting point to the ending point.
        """
        frontier = []
        heapq.heappush(frontier, (0, start))
        self.camefrom[start] = None
        cost_so_far = {}
        cost_so_far[start] = 0

        while frontier:
            current = heapq.heappop(frontier)[1]

            if current == end:
                self.path_found = True
                break

            for next in self.neighbors(maze, current):
                new_cost = cost_so_far[current] + 1
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + self.heuristic(end, next)
                    heapq.heappush(frontier, (priority, next))
                    self.camefrom[next] = current

        if self.path_found:
            self.path_cost = cost_so_far[end]
            self.path = self.reconstruct_path(self.camefrom, start, end)

    def heuristic(self, a, b):
        """
        Function that calculates the heuristic.
        """
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    def neighbors(self, maze, current):
        """
        Function that finds the neighbors of the current node.
        """
        x, y = current
        neighbors = [(x + dx, y + dy) for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]]
        return [next for next in neighbors if 0 <= next[0] < len(maze[0]) and 0 <= next[1] < len(maze) and maze[next[1]][next[0]] != '#']
    
    def reconstruct_path(self, camefrom, start, end):
        """
        Function that reconstructs the path from the starting point to the ending point.
        """
        current = end
        path = []
        while current != start:
            path.append(current)
            current = camefrom[current]
        path.append(start)
        path.reverse()
        return path
    
    def fetch_solved_maze(self):
        """
        Function that fetches the solved maze.
        """
        solved_maze = self.a_star(self.maze, self.starting_point, self.ending_point)
        if self.path_found:
            for x, y in self.path:
                self.maze[y][x] = 'P'
            return self.maze
        else:
            return None