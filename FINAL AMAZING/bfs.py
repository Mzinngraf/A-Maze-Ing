from typing import List, Tuple, Dict, Optional, Deque, Set
from collections import deque


def solve_maze(grid: List[List[int]],
               entry: Tuple[int, int],
               exit: Tuple[int, int],
               width: int,
               height: int) -> List[Tuple[int, int]]:
    """
    Docstring for solve_maze

    BFS solver from entry to exit on the maze grid
    :param grid: 2D list of cells encoding walls and cell state
    :type grid: List[List[int]]
    :return: Ordered list of (x, y) coordinates from entry to exit
            or an empty list if unsolvable
    :rtype: List[Tuple[int, int]]
    """
    start_y, start_x = entry
    exit_y, exit_x = exit

    q: Deque[Tuple[int, int]] = deque([(start_x, start_y)])
    visited: Set[Tuple[int, int]] = {(start_x, start_y)}
    way: Dict[tuple[int, int], Optional[Tuple[int, int]]] = {
        (start_x, start_y): None
        }

    directions: List[Tuple[int, int, int, int]] = [
        (0, -1, 1, 4),
        (1, 0, 2, 8),
        (0, 1, 4, 1),
        (-1, 0, 8, 2)
    ]
    found: bool = False
    while q:
        curr_x, curr_y = q.popleft()
        if (curr_x, curr_y) == (exit_x, exit_y):
            found = True
            break
        for dx, dy, wall, wall_next in directions:
            nx, ny = curr_x + dx, curr_y + dy
            if 0 <= nx < width and 0 <= ny < height:
                if grid[ny][nx] == 16:
                    continue
                if not (grid[curr_y][curr_x] & wall) and \
                    not (grid[ny][nx] & wall_next) and \
                        (nx, ny) not in visited:
                    visited.add((nx, ny))
                    way[(nx, ny)] = (curr_x, curr_y)
                    q.append((nx, ny))
    path: List[Tuple[int, int]] = []
    if found:
        curr: Optional[Tuple[int, int]] = (exit_x, exit_y)
        while curr is not None:
            path.append(curr)
            curr = way.get(curr)
        return path[::-1]
    return []
