## MazeGenerator — Reusable Module

### Installation
```bash
make install
```

### Basic Example
```python
from mazegen import MazeGenerator, solve_maze

gen = MazeGenerator(width=10, height=10, entry=(0,0), exit=(9,9), perfect=True, seed=42)
maze = gen.generate()
path = solve_maze(maze, gen.entry, gen.exit, gen.width, gen.height)
```

### Custom Parameters
| Parameter | Type | Description |
|-----------|------|-------------|
| width | int | Number of columns (3–50) |
| height | int | Number of rows (3–50) |
| entry | Tuple[int,int] | (row, col) of the start cell |
| exit | Tuple[int,int] | (row, col) of the end cell |
| perfect | bool | True = no loops, False = ~15% walls removed |
| seed | int | RNG seed for reproducibility |

### Accessing the Maze Structure
```python
grid = gen.generate()
```

### Accessing the Solution
```python
path = solve_maze(maze, gen.entry, gen.exit, gen.width, gen.height)
```