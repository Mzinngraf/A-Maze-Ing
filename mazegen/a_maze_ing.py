import sys
from parser import parser
from mazegen import MazeGenerator
from visual_display import Display
from bfs import solve_maze
from save_maze import save_maze

if __name__ == "__main__":
    maze_dict = parser()
    gen = MazeGenerator(maze_dict["width"], maze_dict["height"], maze_dict["entry"], maze_dict["exit"], maze_dict["perfect"], seed=maze_dict.get("seed", 0))
    maze = gen.generate()
    path = solve_maze(gen, maze)
    save_maze(gen, maze, path, maze_dict["output"])
    display = Display(gen, path)
    seed = maze_dict.get("seed", 0)
    while True:
        display.render()
        print("=== A-Maze-ing ===")
        print("1. Re-generate a new maze")
        print("2. Show/Hide path from entry to exit")
        print("3. Rotate maze colors")
        print("4. Quit")
        choice = input("Choice? (1-4): ")
        if choice == "1":
            seed += 1
            gen.seed = seed
            # random.seed(seed)
            maze = gen.generate()
            path = solve_maze(gen, maze)
            display.maze = gen
            display.path = path
            save_maze(gen, maze, path, maze_dict["output"])
        elif choice == "2":
            if display.show is False:
                display.show = True
            else:
                display.show = False
        elif choice == "3":
            if display.current_color != len(display.colors) - 1:
                display.current_color +=1
            else:
                display.current_color = 0
        elif choice == "4":
            sys.exit(0)