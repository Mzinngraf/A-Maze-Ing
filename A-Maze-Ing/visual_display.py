from mazegen import MazeGenerator

class Display:
    def __init__(self, show=False, color= "white", path=None):
        # self.entry = entry
        # self.exit = exit
        # self.maze = maze
        self.path = path
        self.show = show
        self.color = color
        self.maze = gen


    def render(self):
        gridwidth = 2 * self.maze.width + 1
        gridheight = 2 * self.maze.height + 1
        grid = [["_" for col in range(gridwidth)] for row in range(gridheight)]
        for maze_y in range(self.maze.height):
            for maze_x in range(self.maze.width):
                cellval = self.maze.basegrid.cells[maze_y][maze_x]
                if cellval & 1 == 1:
                    pass
                elif cellval & 2 == 2:
                    print("|")
                elif cellval & 4 == 4:
                    print("_")
                elif cellval & 8 == 8:
                    print("|")
                # print(cellval, end=" ")
        for row in grid:
            print("".join(row))
        # for (maze_x, maze_y) in grid:
        #     if (2 * maze_x + 1, 2 *maze_y + 1) == (gridwidth, gridheight):
        #         print(" ")



if __name__ == "__main__":
    gen = MazeGenerator(
        width=5, height=5,
        entry=(0,0), exit=(39,29),
        perfect=True, seed=42
    )
    gen.generate()
    display = Display(gen)
    display.render()
