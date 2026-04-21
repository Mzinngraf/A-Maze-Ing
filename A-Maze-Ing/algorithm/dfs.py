import random


def gen_maze(self):
    start_x, start_y = self.entry
    height = self.height
    width = self.width
    seed = self.seed
    perfect = self.perfect
    exit_x, exit_y = self.exit

    stack = [(start_x, start_y)]
    visited = set[(start_x, start_y)]

    directions = [
        (0, -1, 1, 2),
        (0, 1, 2, 1),
        (1, 0, 4, 8),
        (-1, 0, 8, 4)
    ]

    while stack:
        curr_x, curr_y = stack[-1]
        unvisited_walls = []
        for dx, dy, wall_curr, wall_next in directions:
            nx, ny = curr_x + dx, curr_y + dy
            if 0 <= nx < width and 0 <= ny < height and (nx, ny) not in visited:
                unvisited_walls.append((nx, ny, wall_curr, wall_next))
        if unvisited_walls:
            nx, ny, wall_curr, wall_next = random.choice(unvisited_walls)
            grid[curr_x][curr_y] -= wall_curr
            grid[ny][nx] -= wall_next
            visited.add(nx, ny)
            stack.append(nx, ny)
        else:
            stack.pop
        return grid
