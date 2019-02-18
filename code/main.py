import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from simple_objects import Objects as obj

x_move = 0
y_move = 0

def init():
    pygame.init()
    display = (1000, 700)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.01, 100)
    glTranslatef(0, 0, -40)
    glEnable(GL_DEPTH_TEST)

def draw_scenario():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    glTranslatef(x_move, y_move, 0)
    obj.draw_floors()
    obj.draw_walls()
    obj.draw_doors()

def event_ctrl(event):
    global x_move
    global y_move

    if (event.type == pygame.QUIT):
        pygame.quit()
        quit()

    if event.type == pygame.KEYDOWN:
        if (event.key == pygame.K_LEFT):
            x_move = 0.5
        if (event.key == pygame.K_RIGHT):
            x_move = -0.5
        if (event.key == pygame.K_UP):
            y_move = -0.5
        if (event.key == pygame.K_DOWN):
            y_move = 0.5

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
