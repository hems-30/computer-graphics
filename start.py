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

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0, COLS, 0, ROWS, -1, 1)

glMatrixMode(GL_MODELVIEW)

def draw_grid():
    glColor3f(1, 1, 1)
    glLineWidth(2)

    glBegin(GL_LINES)

    for i in range(COLS + 1):
        x = i * CELL_SIZE
        glVertex2f(x, 0)
        glVertex2f(x, ROWS * CELL_SIZE)

    for j in range(ROWS + 1):
        y = j * CELL_SIZE
        glVertex2f(0, y)
        glVertex2f(COLS * CELL_SIZE, y)

    glEnd()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    draw_grid()

    pygame.display.flip()
    pygame.time.wait(10)
