import pygame
import random
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

window_size = (600, 600)
pygame.display.set_mode(window_size, DOUBLEBUF | OPENGL)
glViewport(0, 0, 600, 600)   # define drawing area
glClearColor(0, 0, 0, 1)     # black background

ROWS = 20
COLS = 20
CELL_SIZE = 1

northWall = [[1 for _ in range(COLS)] for _ in range(ROWS)]
eastWall  = [[1 for _ in range(COLS)] for _ in range(ROWS)]

visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0, COLS, 0, ROWS, -1, 1)

glMatrixMode(GL_MODELVIEW)

stack = []

current_row = 0
current_col = 0

visited[current_row][current_col] = True

def get_neighbors(r, c):
    neighbors = []

    if r > 0 and not visited[r - 1][c]:
        neighbors.append((r - 1, c))  # up

    if r < ROWS - 1 and not visited[r + 1][c]:
        neighbors.append((r + 1, c))  # down

    if c > 0 and not visited[r][c - 1]:
        neighbors.append((r, c - 1))  # left

    if c < COLS - 1 and not visited[r][c + 1]:
        neighbors.append((r, c + 1))  # right

    return neighbors

def remove_walls(r1, c1, r2, c2):
    if r1 == r2: # Horizontal movement
        if c1 < c2: eastWall[r1][c1] = 0 # Moving East
        else: eastWall[r2][c2] = 0       # Moving West
    elif c1 == c2: # Vertical movement
        if r1 < r2: northWall[r1][c1] = 0 # Moving North (Up)
        else: northWall[r2][c2] = 0       # Moving South (Down)

def generate_maze_step():
    global current_row, current_col

    neighbors = get_neighbors(current_row, current_col)

    if neighbors:
        next_cell = random.choice(neighbors)

        stack.append((current_row, current_col))

        remove_walls(current_row, current_col, next_cell[0], next_cell[1])

        current_row, current_col = next_cell
        visited[current_row][current_col] = True

    elif stack:
        current_row, current_col = stack.pop()

def draw_maze():
    glColor3f(1, 1, 1)
    glLineWidth(2)

    glBegin(GL_LINES)

    for i in range(ROWS):
        for j in range(COLS):

            x = j * CELL_SIZE
            y = i * CELL_SIZE

            # Draw north wall
            if northWall[i][j] == 1:
                glVertex2f(x, y + CELL_SIZE)
                glVertex2f(x + CELL_SIZE, y + CELL_SIZE)

            # Draw east wall
            if eastWall[i][j] == 1:
                glVertex2f(x + CELL_SIZE, y)
                glVertex2f(x + CELL_SIZE, y + CELL_SIZE)

    # Draw left border
    for i in range(ROWS):
        glVertex2f(0, i * CELL_SIZE)
        glVertex2f(0, (i + 1) * CELL_SIZE)

    # Draw bottom border
    for j in range(COLS):
        glVertex2f(j * CELL_SIZE, 0)
        glVertex2f((j + 1) * CELL_SIZE, 0)

    glEnd()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    generate_maze_step()
    draw_maze()
    

    pygame.display.flip()
    pygame.time.wait(10)
