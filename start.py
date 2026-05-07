import pygame
import random
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

window_size = (600, 600)
pygame.display.set_mode(window_size, DOUBLEBUF | OPENGL)
glViewport(0, 0, 600, 600)   
glClearColor(0, 0, 0, 1)     

ROWS = 20
COLS = 20
CELL_SIZE = 1

northWall = [[1 for _ in range(COLS)] for _ in range(ROWS)]
eastWall  = [[1 for _ in range(COLS)] for _ in range(ROWS)]

visited = [[False for _ in range(COLS)] for _ in range(ROWS)]


start = (0, 0)
end = (ROWS - 1, COLS - 1)

solved_path = set()
dead_cells = set()

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0, COLS, 0, ROWS, -1, 1)

glMatrixMode(GL_MODELVIEW)

stack = []

current_row = 0
current_col = 0
visited[current_row][current_col] = True

maze_finished = False # Flag to ensure maze completes before solving

def get_neighbors(r, c):
    neighbors = []
    if r > 0 and not visited[r - 1][c]:
        neighbors.append((r - 1, c)) 
    if r < ROWS - 1 and not visited[r + 1][c]:
        neighbors.append((r + 1, c))  
    if c > 0 and not visited[r][c - 1]:
        neighbors.append((r, c - 1))  
    if c < COLS - 1 and not visited[r][c + 1]:
        neighbors.append((r, c + 1)) 
    return neighbors

def remove_walls(r1, c1, r2, c2):
    if r1 == r2: 
        if c1 < c2: eastWall[r1][c1] = 0 
        else: eastWall[r2][c2] = 0       
    elif c1 == c2: 
        if r1 < r2: northWall[r1][c1] = 0 
        else: northWall[r2][c2] = 0       

def generate_maze_step():
    global current_row, current_col, maze_finished

    neighbors = get_neighbors(current_row, current_col)

    if neighbors:
        next_cell = random.choice(neighbors)
        stack.append((current_row, current_col))
        remove_walls(current_row, current_col, next_cell[0], next_cell[1])
        current_row, current_col = next_cell
        visited[current_row][current_col] = True
    elif stack:
        current_row, current_col = stack.pop()
    else:
        maze_finished = True 

solver_stack = []
solver_visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

solver_row, solver_col = start
solver_visited[solver_row][solver_col] = True
solver_stack.append(start)

def can_move(r1, c1, r2, c2):
    if c2 > c1: # moving right
        return eastWall[r1][c1] == 0
    if c2 < c1: # moving left
        return eastWall[r1][c2] == 0
    if r2 > r1: # moving up
        return northWall[r1][c1] == 0
    if r2 < r1: # moving down
        return northWall[r2][c2] == 0
    return False

def solver_neighbors(r, c):
    moves = []
    directions = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
    for nr, nc in directions:
        if 0 <= nr < ROWS and 0 <= nc < COLS:
            if not solver_visited[nr][nc]:
                if can_move(r, c, nr, nc):
                    moves.append((nr, nc))
    return moves

def solve_step():
    global solver_row, solver_col

    if not maze_finished or (solver_row, solver_col) == end:
        return

    moves = solver_neighbors(solver_row, solver_col)
    solver_visited[solver_row][solver_col] = True

    if moves:
       
        next_cell = random.choice(moves)
        solver_stack.append((solver_row, solver_col))
        solver_row, solver_col = next_cell
    else:
        
        dead_cells.add((solver_row, solver_col))
        if solver_stack:
            solver_row, solver_col = solver_stack.pop()

def draw_solver():
    glPointSize(8)
    glBegin(GL_POINTS)
    

    glColor3f(0, 0, 1) 
    for r, c in dead_cells:
        glVertex2f(c + 0.5, r + 0.5)

    
    glColor3f(1, 0, 0)
    glVertex2f(solver_col + 0.5, solver_row + 0.5)
    
    glEnd()

def draw_maze():
    glColor3f(1, 1, 1)
    glLineWidth(2)
    glBegin(GL_LINES)
    for i in range(ROWS):
        for j in range(COLS):
            x = j * CELL_SIZE
            y = i * CELL_SIZE
            if northWall[i][j] == 1:
                glVertex2f(x, y + CELL_SIZE)
                glVertex2f(x + CELL_SIZE, y + CELL_SIZE)
            if eastWall[i][j] == 1:
                glVertex2f(x + CELL_SIZE, y)
                glVertex2f(x + CELL_SIZE, y + CELL_SIZE)
    # Left and Bottom borders
    for i in range(ROWS):
        glVertex2f(0, i * CELL_SIZE); glVertex2f(0, (i + 1) * CELL_SIZE)
    for j in range(COLS):
        glVertex2f(j * CELL_SIZE, 0); glVertex2f((j + 1) * CELL_SIZE, 0)
    glEnd()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    if not maze_finished:
        generate_maze_step()
    else:
        solve_step()

    draw_maze()
    draw_solver()

    pygame.display.flip()
    pygame.time.wait(20) 
