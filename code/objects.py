from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from coordinates import Coordinates as c

from functools import partial

open_main_door = False


def draw_object(draw_obj, obj_texture_id):

    if obj_texture_id is not None:
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, obj_texture_id) # target, texture
        draw_obj()
        glDisable(GL_TEXTURE_2D)
    else:
        draw_obj()


# ----------------------------------------------------------------- FLOORS METHODS BEGIN
def draw_floors():

    for floor in c.floors:  # there are 4 floors
        j = 0
        for f in floor:  # there are 6 faces for each floor
            i = 0
            for face in f:  # there are 4 vertices for each face
                if ((j == 3) and (i == 0)):
                    glColor3fv((1, 1, 1))
                else:
                    glColor3fv((0.70, 0.63, 0.45))
                glBegin(GL_QUADS)
                for t, vertex in enumerate(face):  # there are 3 literals in each vertex
                    glTexCoord2fv((vertex[0], vertex[2]))
                    glVertex3fv(vertex)  # here we have vertex = (x, y, z)
                glEnd()
                i+=1
            j+=1
# ----------------------------------------------------------------- FLOORS METHODS END

# ----------------------------------------------------------------- TOPS METHODS BEGIN
def draw_tops():

    for top in c.tops:
        glPushMatrix()
        glBegin(GL_TRIANGLES)
        for vertex in top:
            glColor3fv((0.5, 0.5, 0.5))
            glTexCoord2fv((vertex[0], vertex[2]))
            glVertex3fv(vertex)
        glEnd()
        glPopMatrix()
# ----------------------------------------------------------------- TOPS METHODS END

# ----------------------------------------------------------------- WALLS METHODS BEGIN
def draw_walls():
    texcoords = [(0,0),(40,0),(40,10),(0,10)]

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
                for t, vertex in enumerate(face):
                    glTexCoord2fv(texcoords[t])
                    glVertex3fv(vertex)
                glEnd()
                i+=1
            j+=1
# ----------------------------------------------------------------- WALLS METHODS END

# ----------------------------------------------------------------- FRONT METHODS BEGIN
def draw_front():

    glColor3fv((0.5, 0.5, 0.5))
    for piece in c.front:
        for face in piece:
            glBegin(GL_QUADS)
            for vertex in face:
                glTexCoord3fv(vertex)
                glVertex3fv(vertex)
            glEnd()
# ----------------------------------------------------------------- FRONT METHODS END

# ----------------------------------------------------------------- DOORS METHODS BEGIN
def open_doors():
    global open_main_door
    open_main_door = True


def close_doors():
    global open_main_door
    open_main_door = False


def __draw_main_left_door(door):
    glPushMatrix()
    # door left low corner is (-0.75, 0, 20)
    glTranslatef(-0.75, 0, 20)
    glRotatef(-75, 0, 1, 0)
    glTranslatef(0.75, 0, -20.0)
    glBegin(GL_POLYGON)

    for vertex in door.get_left_door():
        glColor3fv((0, 0, 1))
        glTexCoord2fv((vertex[0], vertex[1]))
        glVertex3fv(vertex)

    glEnd()
    glPopMatrix()


def __draw_main_right_door(door):

    glPushMatrix()
    # door left low corner is (-0.75, 0, 20)
    glTranslatef(0.75, 0, 20)
    glRotatef(75, 0, 1, 0)
    glTranslatef(-0.75, 0, -20.0)
    glBegin(GL_POLYGON)

    for vertex in door.get_right_door():
        glColor3fv((0, 0, 1))
        glTexCoord2fv((vertex[0], vertex[1]))
        glVertex3fv(vertex)

    glEnd()
    glPopMatrix()


def _draw_main_door(lvl, ctr):
    door = c.doors_objects[lvl][ctr]

    __draw_main_left_door(door)
    __draw_main_right_door(door)


def _draw_other_doors(lvl, ctr):

    glBegin(GL_POLYGON)

    for vertex in c.doors_objects[lvl][ctr].get_door():
        glColor3fv((0, 0, 1))
        glTexCoord2fv((vertex[0], vertex[1]))
        glVertex3fv(vertex)

    glEnd()


def draw_doors():
    draw_door_func = None
    for lvl in c.levels:
        for ctr in c.centers:
            if lvl == ctr and open_main_door:
                draw_door_func = _draw_main_door
            else:
                draw_door_func = _draw_other_doors

            draw_door_func(lvl, ctr)
# ----------------------------------------------------------------- DOORS METHODS END


# ----------------------------------------------------------------- CHAIRS METHODS BEGIN
def draw_chairs():
    for i, chair in enumerate(c.chairs):
        glPushMatrix()

        glTranslatef(c.c_coordsT[i][0], c.c_coordsT[i][1], c.c_coordsT[i][2])

        if(i >= 4 and i <= 6):
            glRotatef(90, 0, 1, 0)
        elif(i >= 7 and i <= 9):
            glRotatef(-90, 0, 1, 0)
        elif(i >= 10 and i <= 13):
            glRotatef(180, 0, 1, 0)

        colorx = 0.2
        for part in chair:
            colorx += 0.2
            for face in part:
                glBegin(GL_QUADS)
                for vertex in face:
                    glColor3fv((colorx, 0.0, 0.0))
                    glVertex3fv(vertex)
                glEnd()
        glPopMatrix()

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
# ----------------------------------------------------------------- CHAIRS METHODS END

# ----------------------------------------------------------------- TABLE METHODS BEGIN
def draw_tables():
    for i, table in enumerate(c.tables):
        glPushMatrix()

        glTranslatef(c.ct_coordsT[i][0], c.ct_coordsT[i][1], c.ct_coordsT[i][2])

        colorx = 0.2
        for part in table:
            colorx += 0.2
            for face in part:
                glBegin(GL_QUADS)
                for vertex in face:
                    glColor3fv((colorx, 0.0, 0.0))
                    glVertex3fv(vertex)
                glEnd()
        glPopMatrix()

# ----------------------------------------------------------------- TABLE METHODS END

# ----------------------------------------------------------------- BOOKCASES METHODS BEGIN
def draw_book_cases():
    for i, bookcase in enumerate(c.bookcases):
        glPushMatrix()

        glTranslatef(c.cbc_coordsT[i][0], c.cbc_coordsT[i][1], c.cbc_coordsT[i][2])

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

        glPopMatrix()

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
# ----------------------------------------------------------------- BOOKCASES METHODS END
