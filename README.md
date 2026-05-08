# Building and Running Mazes using PyOpenGL

## Overview

This project is a Computer Graphics assignment implemented using **Python**, **PyOpenGL**, and **Pygame**.

The program:

- Generates a random rectangular maze
- Displays the maze dynamically while it is being created
- Solves the maze using a backtracking algorithm
- Visualizes:
  - A **red dot** for the current mouse position
  - **Blue dots** for dead-end cells

The project follows the assignment requirement of creating a proper maze where every cell is connected.

---

# Technologies Used

- Python 3
- PyOpenGL
- Pygame

---

# Maze Representation

The maze is represented using two 2D arrays:

```python
northWall[ROWS][COLS]
eastWall[ROWS][COLS]
```

 # Maze generation algorithm

The maze is generated using a stack-based Depth first search (DFS) algorithm.

STEPS:

1. Start with all walls intact.
2. Place an invisible mouse in a random cell.
3. Check neighboring unvisited cells.
4. Randomly choose one neighbor.
5. Remove the wall between the current cell and chosen cell.
6. Push the current cell onto a stack.
7. Move to the chosen cell.
8. Continue until trapped.
9. Backtrack using the stack.
10. Repeat until all cells are visited.

This guarantees that all cells are connected.

```

# Maze Solving Algorithm

The maze is solved using a **backtracking algorithm**.

## Steps

1. Start from the start cell.

2. Move randomly to valid neighboring cells.

3. Store previous positions on a stack.

4. If a dead end is reached:
   - Mark the cell blue
   - Pop from the stack to backtrack

5. Continue until the end cell is reached.
```

# Bonus Features

The project also implements the bonus challenge from the assignment.

## Added Features

- Random extra walls are removed with a 1 in 20 chance
- This creates cycles inside the maze
- The maze is no longer a perfect tree
- Start and end positions are placed inside the maze interior

This makes solving more difficult and defeats the simple wall-following strategy.

# Visual Features

| Color | Meaning |
| ----- | ------- |
| White | Maze walls |
| Red | Current mouse position |
| Blue | Dead-end cells |

---

# File Structure

```text id="aqg8wx"
computer-graphics/
│
├── start.py
└── README.md
```

# Project Features

- Dynamic maze generation
- Randomized maze structure
- Stack-based DFS generation
- Backtracking maze solver
- OpenGL rendering
- Dead-end visualization
- Interior start and end positions
- Bonus cycle generation