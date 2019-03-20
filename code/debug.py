from math import sqrt
from time import time

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import objects as obj

SPEC_KEYS = [GLUT_KEY_DOWN, GLUT_KEY_UP, GLUT_KEY_LEFT, GLUT_KEY_RIGHT]
KEY_NAMES = ["DOWN", "UP", "LEFT", "RIGHT"]


def fps(scene_vars):

    scene_vars['fps']['frames'] += 1
    frames = scene_vars['fps']['frames']
    last_time = scene_vars['fps']['last_time']
    if time() - last_time  >= 1:
        scene_vars['fps']['current'] = frames / (time() - last_time)
        scene_vars['fps']['frames'] = 0
        scene_vars['fps']['last_time'] = time()


def axis(ctr, eye):

    alt = 50.0
    alt_rev = -5
    __draw_axis(ctr, (ctr[0], ctr[1], alt), (1.0, 0.0, 0.0)) # z to red
    __draw_axis(ctr, (ctr[0], alt, ctr[2]), (0.0, 1.0, 0.0)) # y to green
    __draw_axis(ctr, (alt, ctr[1], ctr[2]), (0.0, 0.0, 1.0)) # x to blue
    __draw_axis(ctr, (ctr[0], ctr[1], alt_rev), (1.0, 1.0, 0.0)) # -z to yellow
    __draw_axis(ctr, (ctr[0], alt_rev, ctr[2]), (1.0, 0.0, 1.0)) # -y to pink
    __draw_axis(ctr, (alt_rev, ctr[1], ctr[2]), (0.0, 1.0, 1.0)) # -x to cyan
    __draw_axis((0,0,0),(0,15,0),(0.0,0.0,0.0)) # line at (0,15,0)
    __draw_axis(ctr, (eye[0], 0, eye[2]), (1.0, 1.0, 1.0)) # line center to eye
    ### debug end


def __draw_axis(center, last_vertex, c):

    glColor(c)
    glBegin(GL_LINES)
    glVertex(center)
    glVertex(last_vertex)
    glEnd()


def dist_e2c(ctr, eye):

    dist = round(sqrt(
                    (eye[0] - ctr[0])**2 +
                    (eye[1] - ctr[1])**2 +
                    (eye[2] - ctr[2])**2),
                 3)
    return dist


def scene_info(scene_vars):

    last_key = scene_vars['last_key']

    if isinstance(last_key, int):
        if last_key in SPEC_KEYS:
            last_key = KEY_NAMES[SPEC_KEYS.index(last_key)]

    print('--- DEBUG START ---')

    print('last_key\t', last_key)
    print('radius \t\t', scene_vars['radius'])
    print('inclination \t', scene_vars['m'])
    print('init_center \t', [round(x, 3) for x in scene_vars['init_center']])
    print('center \t\t', scene_vars['ctr'])
    print('center_degree \t', scene_vars['center_degree'])
    print('eye    \t\t', scene_vars['eye'])
    print('eye_degree \t', scene_vars['eye_degree'])
    print('origin_centered \t', scene_vars['origin_centered'])
    print('fps \t\t', scene_vars['fps']['current'])  # seems like vsync is enabled
    print('dist   \t\t', dist_e2c(scene_vars['ctr'], scene_vars['eye']))
                         
    print('--- DEBUG END ---')

    return last_key

