import pygame
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

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0, COLS, 0, ROWS, -1, 1)

glMatrixMode(GL_MODELVIEW)

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

    draw_maze()

    pygame.display.flip()
    pygame.time.wait(10)
