import random
from modules.user_interface import UserInterface as UF
from modules.maze_generator import MazeGenerator as MG
from modules.maze_solver import MazeSolver as MS
import heapq
import sys

if __name__ == "__main__":
    MazeInit = MG(100, 100)
    Maze = MazeInit.generate_maze()
    starting_point = MazeInit.fetch_starting_point(Maze)
    ending_point = MazeInit.fetch_ending_point(Maze)
    
    MazeSolver = MS(Maze, starting_point, ending_point)
    SolvedMaze = MazeSolver.fetch_solved_maze()
    Draw_Maze = UF(SolvedMaze) 
    

