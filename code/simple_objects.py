from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from coordinates import Coordinates as c


class Objects():

    dnames = {
            0: 'background',
            1: 'floor',
            2: 'top',
            3: 'wall',
            4: 'door',
            5: 'chair'
            }

    def draw_floors():
        Objects.identify_object(1)
        for floor in c.floors:
            j = 0
            for f in floor:
                i = 0
                for face in f:
                    if ((j == 3) and (i == 0)):
                        glColor3fv((1, 1, 1))
                    else:
                        glColor3fv((0.70, 0.63, 0.45))
                    glBegin(GL_QUADS)
                    for vertex in face:
                        glVertex3fv(vertex)
                    glEnd()
                    i+=1
                j+=1

    def draw_tops():
        Objects.identify_object(2)
        for top in c.tops:
            glPushMatrix()
            glBegin(GL_TRIANGLES)
            for vertex in top:
                glColor3fv((0.5, 0.5, 0.5))
                glVertex3fv(vertex)
            glEnd()
            glPopMatrix()

    def draw_walls():
        Objects.identify_object(8)
        for wall in c.walls:
            j = 0
            for w in wall:
                i = 0
                for face in w:
                    if ((j == 0 or j == 2 or j == 3 or j == 5) and (i == 0)):
                        glColor3fv((1, 1, 1))
                    elif(j > 5):
                        glColor3fv((1, 1, 1))
                    else:
                        glColor3fv((1, 0.63, 0.48))
                    glBegin(GL_QUADS)
                    for vertex in face:
                        glVertex3fv(vertex)
                    glEnd()
                    i+=1
                j+=1

    def draw_doors():
        Objects.identify_object(4)
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
                glVertex3fv((x, y + h, 20.01))
                glVertex3fv((x, y, 20.01))

                glEnd()

    def draw_chairs():
        Objects.identify_object(5)
        for chair in c.chairs:
            colorx = 0.2
            for part in chair:
                colorx += 0.2
                for face in part:
                    glBegin(GL_QUADS)
                    for vertex in face:
                        glColor3fv((colorx, 0.0, 0.0))
                        glVertex3fv(vertex)
                    glEnd()

    def draw_tables():
        Objects.identify_object(6)
        for table in c.tables:
            colorx = 0.2
            for part in table:
                colorx += 0.2
                for face in part:
                    glBegin(GL_QUADS)
                    for vertex in face:
                        glColor3fv((colorx, 0.0, 0.0))
                        glVertex3fv(vertex)
                    glEnd()

    def draw_book_cases():
        Objects.identify_object(7)
        for bookcase in c.bookcases:
            i = 0
            colors = [(0.81, 0.66, 0.13), (0.67, 0.66, 0.62)]
            for part in bookcase:
                for face in part:
                    glBegin(GL_QUADS)
                    for vertex in face:
                        if (i <= 2):
                            glColor3fv(colors[0])
                        else:
                            glColor3fv(colors[1])
                        glVertex3fv(vertex)
                    glEnd()
                i += 1

    def identify_object(obj_id=None):
        glEnable(GL_STENCIL_TEST)
        glStencilOp(GL_KEEP, GL_KEEP, GL_REPLACE)
        glStencilFunc(GL_ALWAYS, obj_id, -1)
