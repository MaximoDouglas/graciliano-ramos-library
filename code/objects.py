import numpy as np

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from functools import partial

from coordinates import Coordinates as c

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
    #texcoords = [(0,0),(40,0),(40,10),(0,10)]

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

                texcoords = __get_tex_coords_from(face)

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

    for t, vertex in enumerate(door.get_left_door()):
        #glColor3fv((0, 0, 1))
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

    for t, vertex in enumerate(door.get_right_door()):
        #glColor3fv((0, 0, 1))
        glTexCoord2fv((vertex[0], vertex[1]))
        glVertex3fv(vertex)

    glEnd()
    glPopMatrix()


def _draw_main_door(lvl, ctr):
    door = c.doors_objects[lvl][ctr]

    __draw_main_left_door(door)
    __draw_main_right_door(door)


def _draw_other_doors(lvl, ctr):

    glPushMatrix()

    if lvl == 10 and ctr == 0:
        glTranslatef(0.0, -10.0, -20.0)
        glScalef(0.5, 0.5, 0.5)
        glTranslatef(0.0, 30.0, 56.4)

    glBegin(GL_POLYGON)

    for vertex in c.doors_objects[lvl][ctr].get_door():
        glColor3fv((0, 0, 1))
        glTexCoord2fv((vertex[0], vertex[1]))
        glVertex3fv(vertex)

    glEnd()
    glPopMatrix()



def draw_doors():
    draw_door_func = None
    for lvl in c.levels:
        for ctr in c.centers:
            if lvl == ctr and open_main_door:
                draw_door_func = _draw_main_door
            else:
                draw_door_func = _draw_other_doors

            if lvl == 10:
                if ctr != 0:
                    continue

            draw_door_func(lvl, ctr)
# ----------------------------------------------------------------- DOORS METHODS END


# ----------------------------------------------------------------- CHAIRS METHODS BEGIN
def draw_chairs():
    for i, chair in enumerate(c.chairs):
        glPushMatrix()

        glTranslatef(c.c_coordsT[i][0], c.c_coordsT[i][1], c.c_coordsT[i][2])

        if(i >= 6 and i <= 11):
            glRotatef(90, 0, 1, 0)
        elif(i >= 12 and i <= 16):
            glRotatef(-90, 0, 1, 0)
        elif(i >= 17 and i <= 21):
            glRotatef(180, 0, 1, 0)

        colorx = 0.2
        for part in chair:
            colorx += 0.2
            for face in part:
                glBegin(GL_QUADS)
                for vertex in face:
                    glColor3fv((colorx, 0.0, 0.0))
                    glTexCoord2fv((vertex[0], vertex[1]))
                    glVertex3fv(vertex)
                glEnd()
        glPopMatrix()

    for ind, chair in enumerate(c.chairs2):
        glPushMatrix()

        glTranslatef(c.c2_coordsT[ind][0], c.c2_coordsT[ind][1], c.c2_coordsT[ind][2])
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
                texcoords = __get_tex_coords_from(face)
                glBegin(GL_QUADS)
                for t, vertex in enumerate(face):
                    glColor3fv((0.5 * colorx, 0.0, 0.0))
                    #glTexCoord2fv((vertex[0], vertex[1]))
                    glTexCoord2fv(texcoords[t])
                    glVertex3fv(vertex)
                glEnd()
        glPopMatrix()

# ----------------------------------------------------------------- TABLE METHODS END

# ----------------------------------------------------------------- BOOKCASES METHODS BEGIN
def draw_book_cases_center_sides():
    for ind, bookcase in enumerate(c.bookcases):
        glPushMatrix()

        glTranslatef(c.cbc_coordsT[ind][0], c.cbc_coordsT[ind][1], c.cbc_coordsT[ind][2])
        if (ind >= 2 and ind <= 17):
            glRotatef(90, 0, 1, 0)

        i = 0
        colors = [(0.81, 0.66, 0.13), (0.67, 0.66, 0.62)]
        for part in bookcase:
            for face in part:
                texcoords = __get_tex_coords_from(face)
                glBegin(GL_QUADS)
                for t, vertex in enumerate(face):
                    if (i <= 2):
                        glColor3fv(colors[0])
                    else:
                        glColor3fv(colors[1])
                    glTexCoord2fv(texcoords[t])
                    glVertex3fv(vertex)
                glEnd()
            i += 1

        glPopMatrix()


def draw_book_cases_corners():
    for ind2, bookcase in enumerate(c.bookcases2):
        glPushMatrix()

        glTranslatef(c.cbc2_coordsT[ind2][0], c.cbc2_coordsT[ind2][1], c.cbc2_coordsT[ind2][2])
        i = 0
        colors = [(0, 0.5, 0)]
        for part in bookcase:
            for face in part:
                texcoords = __get_tex_coords_from(face)
                glBegin(GL_QUADS)
                for t, vertex in enumerate(face):
                    #glColor3fv(colors[0])
                    glTexCoord2fv(texcoords[t])
                    glVertex3fv(vertex)
                glEnd()
            i += 1
        glPopMatrix()
# ----------------------------------------------------------------- BOOKCASES METHODS END

# utils
def __get_tex_coords_from(face, from_obj=None):
    def dist(u, v):
        diff = np.asarray(u) - np.asarray(v)
        return np.linalg.norm(diff)

    if from_obj == 'door':
        f = list(face[1:])
        f.append(face[0])
        face = tuple(f)

    v1, v2, v3, v4 = face
    s1 = 0
    s2 = dist(v1, v2)
    t1 = 0
    t2 = dist(v2, v3)
    tc = [(s1,t1),(s2,t1),(s2,t2),(s1,t2)]

    return tc
