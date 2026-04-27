*This project has been created as part of the 42 curriculum by <mmourao-> and <limelo-c>.*

A-Maze-ing: This is the way

Description

This project is a Maze Generator and Solver. It reads a simple text file to know how big the maze should be, builds it using a "smart" random logic so every area is reachable, and then finds the fastest way out. It’s a great way to see how computer algorithms can "think" through a puzzle.

Instructions

1. Setup

We use Poetry to keep things organized. Open your terminal and run:
Bash

poetry install

2. How to Run

To create a maze, just point the program to your configuration file:
Bash

poetry run python a_maze_ing.py config.txt

3. Checking your code

We used Mypy to make sure our variables are correct and Flake8 to keep the code clean:
Bash

poetry run mypy .
poetry run flake8 .

4. How to Run in virtual environment

To run in a virtual environment, run these commands:

python3 -m venv venv

source venv/bin/activate

make install

make dist

make run

or to view the files created : ls dist

Config File Format

The config.txt file is like a "instruction manual" for the program. It looks like this:

    WIDTH / HEIGHT: How many blocks wide and tall.

    ENTRY / EXIT: Where you start and where you finish.

    PERFECT: If True, there is only one path. If False, we break extra walls to add loops.

    OUTPUT_FILE: Where to save the finished maze.

Technical Choices
Generation: Recursive Backtracking

Think of this like a person exploring a dark cave with a ball of string. They move randomly to new rooms; if they get stuck, they follow the string back (backtrack) until they find a new path to explore.

    Why? It makes cool, long, and winding paths that look like real mazes.

Solving: BFS (Breadth-First Search)

This algorithm works like a ripple in a pond. It explores every possible direction at the same time, one step at a time.

    Why? Because it explores everything equally, it is guaranteed to find the shortest path possible.

Reusable Code

    The Grid System: The way we store the walls using numbers (1, 2, 4, 8) can be used for any top-down tile game.

    The Parser: The code that reads the text file can be easily moved to another project to read different settings.

Team and Project Management

    Role: I (mmourao-) handled the algorithms, parser and the output file.

    The Parser: I started by making a "bulletproof" parser. I added strict checks so that even if someone puts wrong data in the config file, the code won't crash.

    Generation (DFS): I learned about Depth-First Search (the "cave explorer"). I used this logic to carve out the paths and make sure the maze looks interesting.

    Solving (BFS): I added the Breadth-First Search (the "ripple" logic). This makes sure the program always finds the absolute shortest path to the exit.

    Output: I created the hex-encoding system so the maze is saved correctly in the .txt file.

    What went well: The algorithms were nice and I liked the way it was transfered to code.

    What could be better: I’d like to add a way to see the maze being built in real-time like an animation.

    Role : I (limelo-c) handled the main, the visual display and the generation of maze.

    The A_Maze_ing: It's the heart of the project, linking all the different files in order to work together. We can also find the different choices of the user input making the whole project work as intended.

    the Mazegen: Creates the basegrid which is a list of a list full of closed cells (value 15), afterwards generates a maze using the DFS algorithm. 
    It also creates a "42" pattern that will be centered in the maze. It also handles special cases such as, a maze too small to generate the pattern and an entry/exit within the "42" limits.

    The Visual_Display: Displays the maze taking into account the basegrid, the cells created in the maze generator

    What went well: The generation of the maze went quite easily as well as the 42 pattern.

    What could be better: I would've liked for the visual display have more options. 

Resources

    Algorithms: https://www.geeksforgeeks.org/dsa/depth-first-search-or-dfs-for-a-graph/
                https://www.geeksforgeeks.org/dsa/breadth-first-search-or-bfs-for-a-graph/

    Python Typing: Used to make the code easier for others to read.

    AI Usage: Usage throughout the process:

        Helped understanding some concepts such as DFS and BFS algorithms.

        Helped understanding how (x, y) values worked as they were inverted.

        Helped understanding how to link the bits logic with the walls logic.

        Helped writing this READme