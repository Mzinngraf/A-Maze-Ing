import random
import sys
from typing import List, Tuple, Set


class MazeGrid:
    """
    Docstring for MazeGrid

    2D grid of cells (15 default value for all walls set)
    """
    def __init__(self, height: int, width: int):
        """
        Docstring for __init__

        :param height: Number of rows
        :type height: int
        :param width: Number of columns
        :type width: int
        """
        self.height = height
        self.width = width
        self.cells: List[List[int]] = [
            [15 for col in range(self.width)]
            for row in range(self.height)
        ]


class MazeGenerator:
    """
    Docstring for MazeGenerator

    Generates a maze using DFS algorithm
    """
    def __init__(self, width: int, height: int, entry: Tuple[int, int],
                 exit: Tuple[int, int], perfect: bool, seed: int = 0):
        """
        Docstring for __init__

        :param width: Number of columns
        :type width: int
        :param height: Number of rows
        :type height: int
        :param entry: (row, col) of entry cell
        :type entry: Tuple[int, int]
        :param exit: (row, col) of exit cell
        :type exit: Tuple[int, int]
        :param perfect: boolean determining a perfect maze or not
        :type perfect: bool
        :param seed: random seed
        :type seed: int
        """
        self.width: int = width
        self.height: int = height
        self.entry: Tuple[int, int] = entry
        self.exit: Tuple[int, int] = exit
        self.perfect: bool = perfect
        self.seed: int = seed
        random.seed(self.seed)
        self.basegrid: MazeGrid = MazeGrid(self.height, self.width)
        self.fortytwo: List[Tuple[int, int]] = []

    def generate(self) -> List[List[int]]:
        """
        Docstring for generate

        Reserts grid and carves maze thanks to DFS algorithm
        :return: 2D list of cells representing the generated maze
        :rtype: List[List[int]]
        """
        self.basegrid = MazeGrid(self.height, self.width)
        self.pattern()
        entry_y, entry_x = self.entry
        height: int = self.height
        width: int = self.width
        rando = random.Random(self.seed)
        exit_y, exit_x = self.exit

        stack: List[Tuple[int, int]] = [(entry_x, entry_y)]
        visited: Set[Tuple[int, int]] = {(entry_x, entry_y)}

        directions: List[Tuple[int, int, int, int]] = [
            (0, -1, 1, 4),
            (1, 0, 2, 8),
            (0, 1, 4, 1),
            (-1, 0, 8, 2)
        ]
        while stack:
            curr_x, curr_y = stack[-1]
            unvisited_walls: List[Tuple[int, int, int, int]] = []
            for dx, dy, wall_curr, wall_next in directions:
                nx, ny = curr_x + dx, curr_y + dy
                if (
                    0 <= nx < width and 0 <= ny < height
                    and (nx, ny)not in visited
                    and (nx, ny) not in self.fortytwo
                ):
                    unvisited_walls.append((nx, ny, wall_curr, wall_next))
            if unvisited_walls:
                nx, ny, wall_curr, wall_next = rando.choice(unvisited_walls)
                self.basegrid.cells[curr_y][curr_x] -= wall_curr
                self.basegrid.cells[ny][nx] -= wall_next
                visited.add((nx, ny))
                stack.append((nx, ny))
            else:
                stack.pop()
        if self.perfect is False:
            for _ in range(int((height*width) * 0.2)):
                rx: int = rando.randint(0, width - 2)
                ry: int = rando.randint(0, height - 1)
                if self.basegrid.cells[ry][rx] & 2:
                    self.basegrid.cells[ry][rx] -= 2
                    self.basegrid.cells[ry][rx + 1] -= 8
        return self.basegrid.cells

    def pattern(self) -> None:
        """
        Docstring for pattern

        Embeds a 42 pattern into the center of the grid and marking cells
        as 16. Exits if entry or exit are initiated in the pattern and
        prints a message if the maze is too small and prints the grid without
        pattern
        """
        entry_y, entry_x = self.entry
        exit_y, exit_x = self.exit
        if self.height >= 7 and self.width >= 9:
            fortytwopattern: List[Tuple[int, int]] = [
                (0, 0), (0, 1), (0, 2), (1, 2), (2, 2),
                (2, 3), (2, 4), (4, 0), (5, 0), (6, 0),
                (6, 1), (4, 2), (5, 2), (6, 2), (4, 3),
                (4, 4), (5, 4), (6, 4)
                ]
            placed: List[Tuple[int, int]] = []
            placex: int = int((self.width - 7) / 2)
            placey: int = int((self.height - 5) / 2)
            for (i, j) in fortytwopattern:
                placed.append((i + placex, j + placey))
            self.fortytwo = placed
            for (x, y) in self.fortytwo:
                self.basegrid.cells[y][x] = 16
            if (entry_x, entry_y) in self.fortytwo:
                print("Entry values in 42 pattern, please run again")
                sys.exit(1)
            if (exit_x, exit_y) in self.fortytwo:
                print("Exit values in 42 pattern, please run again")
                sys.exit(1)
        else:
            print("Maze too small to print 42 pattern")
