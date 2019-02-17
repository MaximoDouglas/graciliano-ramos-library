import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

x_move = 0
y_move = 0

wall_verteces = (
    (-5, -2.1, 10),
    (-5, 3.1, 10),
    (-5, 3.1, 5),
    (-5, -2.1, 5)
)

ground_verteces = (
    (-10, -2.1, 20),
    (10, -2.1, 20),
    (-10, -2.1, -300),
    (10, -2.1, -300)
)

def init():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.01, 100)
    glTranslatef(0, 0, -40)
    glEnable(GL_DEPTH_TEST)

def draw_ground():
    glBegin(GL_QUADS)
    for vertex in ground_verteces:
        glColor3fv((0, 0.5, 0.5))
        glVertex3fv(vertex)
    glEnd()

def draw_wall():
    glBegin(GL_QUADS)
    for vertex in wall_verteces:
        glColor3fv((0, 0.5, 0.0))
        glVertex3fv(vertex)
    glEnd()

def draw_scenario():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    glTranslatef(x_move, y_move, 0)
    draw_ground()
    draw_wall()

def event_ctrl(event):
    global x_move
    global y_move

    if (event.type == pygame.QUIT):
        pygame.quit()
        quit()

    if event.type == pygame.KEYDOWN:
        if (event.key == pygame.K_LEFT):
            x_move = 0.2
        if (event.key == pygame.K_RIGHT):
            x_move = -0.2
        if (event.key == pygame.K_UP):
            y_move = 0.2
        if (event.key == pygame.K_DOWN):
            y_move = -0.2

    if event.type == pygame.KEYUP:
        if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
            x_move = 0
        if (event.key == pygame.K_UP or event.key == pygame.K_DOWN):
            y_move = 0

    #Zoom in and zoom out
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 4:
            glScalef(1.1, 1.1, 1.1)
        if event.button == 5:
            glScalef(0.9, 0.9, 0.9)

def main():
    init()

    while True:
        draw_scenario()
        pygame.display.flip()
        pygame.time.wait(10)

        for event in pygame.event.get():
            event_ctrl(event)

main()
