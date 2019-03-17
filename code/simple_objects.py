from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from coordinates import Coordinates as c

open_main_door = False

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
        for _, wall in enumerate(c.walls):
            j = 0
            for w in wall:
                i = 0
                for face in w:
                    if ((j == 0 or j == 2 or j == 3 or j == 5) and (i == 0)):
                        glColor3fv((1, 1, 1))
                    elif(j > 7):
                        glColor3fv((1, 1, 1))
                    else:
                        glColor3fv((1, 0.63, 0.48))

                    glBegin(GL_QUADS)
                    for vertex in face:
                        glVertex3fv(vertex)
                    glEnd()
                    i+=1
                j+=1

    def draw_front():
        Objects.identify_object(9)
        glColor3fv((0, 0, 0))
        for piece in c.front:
            for face in piece:
                glBegin(GL_QUADS)
                for vertex in face:
                    glVertex3fv(vertex)
                glEnd()

    def open_doors():
        global open_main_door
        open_main_door = True

    def close_doors():
        global open_main_door
        open_main_door = False

    def draw_doors(texture_id):
        Objects.identify_object(4)
        for lvl in c.levels:
            for ctr in c.centers:
                if lvl == ctr and open_main_door:
                    door = c.doors_objects[0][0]
                    glPushMatrix()
                    # door left low corner is (-0.75, 0, 20)
                    glTranslatef(-0.75, 0, 20)
                    glRotatef(-45, 0, 1, 0)
                    glTranslatef(-0.75, 0, -20.0)
                    glBegin(GL_POLYGON)

                    for vertex in door.get_left_door():
                        glColor3fv((0, 0, 1))
                        glVertex3fv(vertex)

                    glEnd()
                    glPopMatrix()
                    glPushMatrix()
                    # door left low corner is (-0.75, 0, 20)
                    glTranslatef(0.75, 0, 20)
                    glRotatef(45, 0, 1, 0)
                    glTranslatef(-0.75, 0, -20.0)
                    glBegin(GL_POLYGON)
                    for vertex in door.get_right_door():
                        glColor3fv((0, 0, 1))
                        glVertex3fv(vertex)
                    glEnd()
                    glPopMatrix()
                else:
                    glEnable(GL_TEXTURE_2D)
                    glBindTexture(GL_TEXTURE_2D, texture_id) # target, texture

                    glBegin(GL_POLYGON)

                    for vertex in c.doors_objects[lvl][ctr].get_door():
                        glColor3fv((0, 0, 1))
                        glTexCoord3fv(vertex)
                        glVertex3fv(vertex)

                    glEnd()
                    glDisable(GL_TEXTURE_2D)


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

        for chair in c.chairs2:
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

        for bookcase in c.bookcases2:
            i = 0
            colors = [(0, 0.5, 0)]
            for part in bookcase:
                for face in part:
                    glBegin(GL_QUADS)
                    for vertex in face:
                        glColor3fv(colors[0])
                        glVertex3fv(vertex)
                    glEnd()
                i += 1

    def identify_object(obj_id=None):
        glEnable(GL_STENCIL_TEST)
        glStencilOp(GL_KEEP, GL_KEEP, GL_REPLACE)
        glStencilFunc(GL_ALWAYS, obj_id, -1)
