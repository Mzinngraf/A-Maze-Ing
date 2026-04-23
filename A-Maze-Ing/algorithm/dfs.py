import random


def gen_maze(self, grid):
    start_y, start_x = self.entry
    height = self.height
    width = self.width
    rando = random.Random(self.seed)
    exit_x, exit_y = self.exit

    stack = [(start_x, start_y)]
    visited = {(start_x, start_y)}

    directions = [
        (0, -1, 1, 4),#N
        (1, 0, 2, 8),#L
        (0, 1, 4, 1),#S
        (-1, 0, 8, 2)#O
    ]

    while stack:
        curr_x, curr_y = stack[-1]
        unvisited_walls = []
        for dx, dy, wall_curr, wall_next in directions:
            nx, ny = curr_x + dx, curr_y + dy
            if 0 <= nx < width and 0 <= ny < height and (nx, ny) not in visited:
                unvisited_walls.append((nx, ny, wall_curr, wall_next))
        if unvisited_walls:
            nx, ny, wall_curr, wall_next = rando.choice(unvisited_walls)
            grid[curr_y][curr_x] -= wall_curr
            grid[ny][nx] -= wall_next
            visited.add((nx, ny))
            stack.append((nx, ny))
        else:
            stack.pop()
    if self.perfect is False:
        rx = rando.randint(0, width - 2)
        ry = rando.randint(0, height - 1)
        if grid[ry][rx] & 2:
            grid[ry][rx] -= 2
            grid[ry][rx + 1] -= 8
    return grid
