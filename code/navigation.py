import math
import sys

from OpenGL.GLUT import GLUT_KEY_DOWN
from OpenGL.GLUT import GLUT_KEY_UP
from OpenGL.GLUT import GLUT_KEY_RIGHT
from OpenGL.GLUT import GLUT_KEY_LEFT

import objects as obj


def kb_rot_eye(key, scene_vars):

    if key == 'r':
        scene_vars['eye_degree'][0] = (scene_vars['eye_degree'][0] + scene_vars['inc_deg']) % 360
    elif key == 'R':
        scene_vars['eye_degree'][0] = (scene_vars['eye_degree'][0] - scene_vars['inc_deg']) % 360
    elif key == 'e':
        scene_vars['eye_degree'][1] = (scene_vars['eye_degree'][1] + scene_vars['inc_deg']) % 360
    elif key == 'E':
        scene_vars['eye_degree'][1] = (scene_vars['eye_degree'][1] - scene_vars['inc_deg']) % 360


def kb_rot_ctr(key, scene_vars):

    # only if is not centered at origin
    if scene_vars['origin_centered']:
        pass
    elif key == GLUT_KEY_DOWN:
        scene_vars['center_degree'][1] = (scene_vars['center_degree'][1] - scene_vars['inc_deg']) % 360
    elif key == GLUT_KEY_UP:
        scene_vars['center_degree'][1] = (scene_vars['center_degree'][1] + scene_vars['inc_deg']) % 360
    elif key == GLUT_KEY_LEFT:
        scene_vars['center_degree'][0] = (scene_vars['center_degree'][0] + scene_vars['inc_deg']) % 360
    elif key == GLUT_KEY_RIGHT:
        scene_vars['center_degree'][0] = (scene_vars['center_degree'][0] - scene_vars['inc_deg']) % 360


def kb_rot_eye(key, scene_vars):

    if key == 'r':
        scene_vars['eye_degree'][0] = (scene_vars['eye_degree'][0] + scene_vars['inc_deg']) % 360
    elif key == 'R':
        scene_vars['eye_degree'][0] = (scene_vars['eye_degree'][0] - scene_vars['inc_deg']) % 360
    elif key == 'e':
        scene_vars['eye_degree'][1] = (scene_vars['eye_degree'][1] + scene_vars['inc_deg']) % 360
    elif key == 'E':
        scene_vars['eye_degree'][1] = (scene_vars['eye_degree'][1] - scene_vars['inc_deg']) % 360


def kb_rot_ctr(key, scene_vars):

    # only if is not centered at origin
    if scene_vars['origin_centered']:
        pass
    elif key == GLUT_KEY_DOWN:
        scene_vars['center_degree'][1] = (scene_vars['center_degree'][1] - scene_vars['inc_deg']) % 360
    elif key == GLUT_KEY_UP:
        scene_vars['center_degree'][1] = (scene_vars['center_degree'][1] + scene_vars['inc_deg']) % 360
    elif key == GLUT_KEY_LEFT:
        scene_vars['center_degree'][0] = (scene_vars['center_degree'][0] + scene_vars['inc_deg']) % 360
    elif key == GLUT_KEY_RIGHT:
        scene_vars['center_degree'][0] = (scene_vars['center_degree'][0] - scene_vars['inc_deg']) % 360


def kb_rot_eye(key, scene_vars):

    if key == 'r':
        scene_vars['eye_degree'][0] = (scene_vars['eye_degree'][0] + scene_vars['inc_deg']) % 360
    elif key == 'R':
        scene_vars['eye_degree'][0] = (scene_vars['eye_degree'][0] - scene_vars['inc_deg']) % 360
    elif key == 'e':
        scene_vars['eye_degree'][1] = (scene_vars['eye_degree'][1] + scene_vars['inc_deg']) % 360
    elif key == 'E':
        scene_vars['eye_degree'][1] = (scene_vars['eye_degree'][1] - scene_vars['inc_deg']) % 360


def kb_rot_ctr(key, scene_vars):

    # only if is not centered at origin
    if scene_vars['origin_centered']:
        pass
    elif key == GLUT_KEY_DOWN:
        scene_vars['center_degree'][1] = (scene_vars['center_degree'][1] - scene_vars['inc_deg']) % 360
    elif key == GLUT_KEY_UP:
        scene_vars['center_degree'][1] = (scene_vars['center_degree'][1] + scene_vars['inc_deg']) % 360
    elif key == GLUT_KEY_LEFT:
        scene_vars['center_degree'][0] = (scene_vars['center_degree'][0] + scene_vars['inc_deg']) % 360
    elif key == GLUT_KEY_RIGHT:
        scene_vars['center_degree'][0] = (scene_vars['center_degree'][0] - scene_vars['inc_deg']) % 360


def kb_nav_mov(key, scene_vars):

    # only if is not centered at origin
    if scene_vars['origin_centered']:
        return

    cd = scene_vars['center_degree'][0]

    # inc in degree
    dir = {'w': 0, 'a': 90, 's': 180, 'd': 270}

    # cd gives the angle of the center in ref. to z+
    # angle_move adjusts the angle by the movement I will perform
    # If I look to the center at 180 degrees and move to the right,
    #    I need to adjust the angle by -90 (or 270) degrees.
    # If I move left, 
    #    I adjust by 90. 
    # If I move back,
    #    I adjust by 180.
    angle_move = (dir[key] + cd) % 360
    iwsin = math.sin(math.radians(angle_move))
    iwcos = math.cos(math.radians(angle_move))

    scene_vars['init_center'][2] += iwcos
    scene_vars['init_center'][0] += iwsin

    scene_vars['m'] = math.tan(math.radians(scene_vars['center_degree'][0]))


def kb_nav_to_lvl(key, scene_vars):

    if key == '0':
        scene_vars['init_center'][1] = 0
    elif key == '1':
        scene_vars['init_center'][1] = 4
    elif key == '2':
        scene_vars['init_center'][1] = 7
    elif key == 'o':
        obj.open_doors()
    elif key == 'O':
        obj.close_doors()


def kb_cfg(key, scene_vars):

    if key == 'h':
        scene_vars['inc_deg'] = 10
    elif key == 'g':
        scene_vars['inc_deg'] = 1
    elif key == 'c' and not scene_vars['origin_centered']:
        if scene_vars['init_center'][2] == 0:
            scene_vars['init_center'][2] = 65
        else:
            scene_vars['init_center'][2] = 0
    elif key == 'i':
        scene_vars['debug'] = ~scene_vars['debug']
    elif key == 'n':
        scene_vars['origin_centered'] = False
    elif key == 'q':
        sys.exit()

