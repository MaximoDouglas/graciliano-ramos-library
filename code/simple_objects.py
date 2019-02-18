from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from coordinates import Coordinates as c

class Objects():

    def draw_ground():
        glBegin(GL_QUADS)
        for vertex in c.ground0:
            glColor3fv((1, 1, 0.8))
            glVertex3fv(vertex)
        glEnd()

    def draw_walls():
        for wall in c.walls:
            glBegin(GL_QUADS)
            for vertex in wall:
                glColor3fv((1, 0.8, 0.8))
                glVertex3fv(vertex)
            glEnd()
