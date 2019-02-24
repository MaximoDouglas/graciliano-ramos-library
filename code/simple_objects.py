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

    def draw_tops():
        for top in c.tops:
            glPushMatrix()
            glBegin(GL_TRIANGLES)
            for vertex in top:
                glColor3fv((0.5, 0.5, 0.5))
                glVertex3fv(vertex)
            glEnd()
            glPopMatrix()

    def draw_walls():
        for wall in c.walls:
            glBegin(GL_QUADS)
            for vertex in wall:
                glColor3fv((1, 0.7, 0.7))
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
        for y in c.levels:
            for x in c.centers:
                glBegin(GL_LINES)
                glColor3fv((0, 0, 0))

                h = 2.5
                if x == 0 and y == 0: h = 2.75
                glVertex3fv((x, y + h, 8.01))
                glVertex3fv((x, y, 8.01))

                glEnd()

    def draw_chairs():
        for chair in c.chairs:
            for part in chair:
                for face in part:
                    glBegin(GL_QUADS)
                    for vertex in face:
                        glColor3fv((0.2, 0.0, 0.0))
                        glVertex3fv(vertex)
                    glEnd()
