from mazegen import MazeGenerator

class Display:
    def __init__(self, entry, exit, maze, show, color= "eeeeee", path=None):
        self.entry = entry
        self.exit = exit
        self.maze = maze
        self.path = path
        self.show = show
        self.color = color