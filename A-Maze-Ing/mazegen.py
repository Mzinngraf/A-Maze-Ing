import random
import sys

class MazeGrid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.cells = [[15 for col in range(self.width)]for row in range(self.height)]


class MazeGenerator:
    def __init__(self, width, height, entry, exit, perfect=True, seed=0):
        self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit
        self.perfect = perfect
        self.seed = seed
        random.seed(self.seed)
        self.basegrid = MazeGrid(self.height, self.width)
        self.fortytwo = []


    def generate(self):
        self.pattern()


    def pattern(self):
        if self.height >= 9 and self.width >= 8:
            fortytwopattern = [(0,0),(0,1),(0,2),(1,2),(2,2),(2,3),(2,4),(4,0),
                        (5,0),(6,0),(6,1),(4,2),(5,2),(6,2),(4,3),(4,4),(5,4),(6,4)]
            placed = []
            placex = int((self.width - 7) / 2)
            placey = int((self.height - 5) / 2)
            for (i,j) in fortytwopattern:
                placed.append((i + placex, j + placey))
            self.fortytwo = placed
            for (x, y) in self.fortytwo:
                self.basegrid.cells[y][x] = 16
        else:
            print("Maze too small to print 42 pattern")
            # gridtoosmall = input("Do you still want to print grid ? ")
            # if gridtoosmall == "yes":
            #     print(self.basegrid.cells)
            # else:
            #     sys.exit(1)


if __name__ == "__main__":
    gen = MazeGenerator(
        width=21, height=21,
        entry=(0,0), exit=(20,20),
        perfect=True, seed=42
    )
    gen.generate()
    for row in gen.basegrid.cells:
        print(f"{row}\n")