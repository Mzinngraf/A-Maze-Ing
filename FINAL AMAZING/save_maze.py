from typing import List, Tuple


def save_maze(grid: List[List[int]],
              path: List[Tuple[int, int]],
              filename: str,
              entry: Tuple[int, int],
              exit: Tuple[int, int]) -> None:
    """
    Docstring for save_maze

    Saves the maze and solution path to a file.
    :param grid: 2D list of cell.
    :type grid: List[List[int]]
    :param path: Ordered (x, y) coordinates from entry to exit
    :type path: List[Tuple[int, int]]
    :param filename: Output .txt file
    :type filename: str
    """
    hex_chars = "0123456789ABCDEF"
    with open(filename, "w") as f:
        for row in grid:
            line = ""
            for cell in row:
                if cell == 16:
                    cell = 15
                i: int = int(cell) % 16
                line += hex_chars[i]
            f.write(line + "\n")
        f.write("\n")
        solution = ""
        f.write(f"{entry[1]},{entry[0]}\n")
        f.write(f"{exit[1]},{exit[0]}\n")
        for i in range(len(path) - 1):
            curr_x, curr_y = path[i]
            next_x, next_y = path[i + 1]
            if next_y < curr_y:
                solution += "N"
            if next_y > curr_y:
                solution += "S"
            if next_x < curr_x:
                solution += "W"
            if next_x > curr_x:
                solution += "E"
        f.write(solution + "\n")
