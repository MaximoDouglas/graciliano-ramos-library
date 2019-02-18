from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from coordinates import Coordinates as c

class Objects():

    def draw_floors():
        for floor in c.floors:
            glBegin(GL_QUADS)
            for vertex in floor:
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

    def draw_doors():

        for door in c.doors:
            glBegin(GL_POLYGON)
            for vertex in door:
                glColor3fv((0, 0, 1))
                glVertex3fv(vertex)
            glEnd()

        # --- DRAW LINE TO SEPARETE DOORS (THIS WILL BE DELETED WHEN ADDED THE OPEN_DOORS FUNC)
        for x in c.centers:
            glBegin(GL_LINES)
            glColor3fv((0, 0, 0))

            h = 2.5
            if x == 0: h = 2.75
            glVertex3fv((x, h, 8.01))
            glVertex3fv((x, 0, 8.01))

            glEnd()
