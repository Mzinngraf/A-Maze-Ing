from mazegen import MazeGenerator
import sys
import random

class Compass:
    def __init__(self, cellval):
        self.north = cellval & 1 == 1
        self.east = cellval & 2 == 2
        self.south = cellval & 4 == 4
        self.west = cellval & 8 == 8
        self.cellval = cellval


class Display:
    def __init__(self, maze, path=None, show=False):
        self.maze = maze
        self.path = path if path else []
        self.show = show
        self.colors = ["37", "35", "34"]
        self.current_color = 0

    def render(self):
        for maze_y in range(self.maze.height):
            for maze_x in range(self.maze.width):
                cellval = self.maze.basegrid.cells[maze_y][maze_x]
                direction = Compass(cellval)
                print(f"\033[{self.colors[self.current_color]}m+\033[0m", end="")
                if maze_y == 0 or direction.north \
                or (maze_x, maze_y) in self.maze.fortytwo \
                or (maze_x, maze_y - 1) in self.maze.fortytwo:
                    print(f"\033[{self.colors[self.current_color]}m───\033[0m", end="")
                else:
                    print("   ", end="")
            print(f"\033[{self.colors[self.current_color]}m+\033[0m")

            for maze_x in range(self.maze.width):
                cellval = self.maze.basegrid.cells[maze_y][maze_x]
                direction = Compass(cellval)
                if maze_x == 0 or direction.west \
                or (maze_x, maze_y) in self.maze.fortytwo \
                or (maze_x - 1, maze_y) in self.maze.fortytwo:
                    print(f"\033[{self.colors[self.current_color]}m|\033[0m", end="")
                else:
                    print(" ", end="")
                pos = (maze_x, maze_y)
                current_posyx = (maze_y, maze_x)
                if pos in self.maze.fortytwo:
                    print(" ✹ ", end="")
                elif current_posyx == self.maze.entry:
                    print(" ▶ ", end="")
                elif current_posyx == self.maze.exit:
                    print(" ⚑ ", end="")
                elif self.show and pos in self.path:
                    print(" ▹ ", end="")
                else:
                    print("   ", end="")
            print(f"\033[{self.colors[self.current_color]}m|\033[0m")
        for maze_x in range(self.maze.width):
            cellval = self.maze.basegrid.cells[maze_y][maze_x]
            direction = Compass(cellval) 
            print(f"\033[{self.colors[self.current_color]}m+\033[0m", end="")
            print(f"\033[{self.colors[self.current_color]}m───\033[0m", end="")
        print(f"\033[{self.colors[self.current_color]}m+\033[0m")
