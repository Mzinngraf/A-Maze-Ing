def save_maze(self, grid, path, filename):
    hex_chars = "0123456789ABCDEF"
    with open(filename, "w") as f:
        for row in grid:
            line = ""
            for cell in row:
                if cell == 16:
                    cell = 15
                i = int(cell) % 16
                line += hex_chars[i]
            f.write(line + "\n")
        f.write("\n")
        solution = ""
        f.write(f"{self.entry[1]},{self.entry[0]}\n")
        f.write(f"{self.exit[1]},{self.exit[0]}\n")
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
