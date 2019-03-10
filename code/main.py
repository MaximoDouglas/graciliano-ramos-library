import numpy as np
import sys
import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from simple_objects import Objects as obj
from debug import debug_axis, debug_info, debug_world_coords

width = 0
height = 0
aspect_ratio = 0

rad = math.pi/180
inc_deg = 1
inc_axis = 1

# TODO: put this in a dict
rot_eye_keys = ('r', 'R', 'e', 'E')
rot_ctr_keys = (GLUT_KEY_DOWN, GLUT_KEY_UP, GLUT_KEY_LEFT, GLUT_KEY_RIGHT)
nav_keys = ('w', 's', 'a', 'd')
lvl_keys = ('0', '1', '2')
cfg_keys = ('g', 'h', 'c', 'i', 'n', 'q')

scene_vars = {
        'eye': None, 'ctr': None,
        'eye_degree' : [0, 20], 'center_degree' : [180, 0],
        'origin_centered' : True, 'radius' : 5.0,
        'init_center' : [0, 0, 65],
        'last_key': None, 'm' : None,
        'debug': True}


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glEnable(GL_DEPTH_TEST)


# Reshape callback
def reshape(w, h):
    global width
    global height
    global aspect_ratio

    width = float(w)
    height = float(h)
    aspect_ratio = width / height

    glViewport(0, 0, w, h)
    glMatrixMode(GL_MODELVIEW)

    update_scene_params()
    update_view()


def update_view():
    eye = scene_vars['eye']
    ctr = scene_vars['ctr']

    glLoadIdentity()
    gluPerspective(30.0, aspect_ratio, 0.01, 100.0)
    gluLookAt(eye[0], eye[1], eye[2],
              ctr[0], ctr[1], ctr[2],
              0.0, 1.0, 0.0)


# Display and Idle func callback
def draw_scenario():

    update_view()

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT|GL_STENCIL_BUFFER_BIT)

    glPushMatrix()

    obj.draw_floors()
    obj.draw_tops()
    obj.draw_walls()
    obj.draw_doors()
    #obj.draw_chairs()
    #obj.draw_tables()
    #obj.draw_book_cases()

    ### debug start
    alt = 50.0
    alt_rev = -5
    ctr = scene_vars['ctr']
    eye = scene_vars['eye']
    debug_axis(ctr, (ctr[0], ctr[1], alt), (1.0, 0.0, 0.0)) # z to red
    debug_axis(ctr, (ctr[0], alt, ctr[2]), (0.0, 1.0, 0.0)) # y to green
    debug_axis(ctr, (alt, ctr[1], ctr[2]), (0.0, 0.0, 1.0)) # x to blue
    debug_axis(ctr, (ctr[0], ctr[1], alt_rev), (1.0, 1.0, 0.0)) # -z to yellow
    debug_axis(ctr, (ctr[0], alt_rev, ctr[2]), (1.0, 0.0, 1.0)) # -y to pink
    debug_axis(ctr, (alt_rev, ctr[1], ctr[2]), (0.0, 1.0, 1.0)) # -x to cyan
    debug_axis((0,0,0),(0,15,0),(0.0,0.0,0.0)) # line at (0,15,0)
    debug_axis(ctr, (eye[0], 0, eye[2]), (1.0, 1.0, 1.0)) # line center to eye
    ### debug end

    glPopMatrix()
    glutSwapBuffers()


def update_scene_params():
    global scene_vars

    # center initial position in this frame
    cx, cy, cz = scene_vars['init_center']
    # with init_center we set camera position
    eyex = cx + scene_vars['radius'] * math.sin(scene_vars['eye_degree'][0] * rad)
    eyey = cy + scene_vars['radius'] * math.sin(scene_vars['eye_degree'][1] * rad)
    eyez = cz + scene_vars['radius'] * math.cos(scene_vars['eye_degree'][0] * rad)
    # we recalculate the center in case we changed its center_degree
    cx = eyex + scene_vars['radius'] * math.sin(scene_vars['center_degree'][0] * rad)
    cy = eyey + scene_vars['radius'] * math.sin(scene_vars['center_degree'][1] * rad)
    cz = eyez + scene_vars['radius'] * math.cos(scene_vars['center_degree'][0] * rad)

    if scene_vars['origin_centered']:
        eyex = 70 * math.sin(scene_vars['eye_degree'][0] * rad)
        eyey = 70 * math.sin(scene_vars['eye_degree'][1] * rad)
        eyez = 70 * math.cos(scene_vars['eye_degree'][0] * rad)
        cx, cy, cz = 0, 0, 0

    # debug
    scene_vars['eye'] = (round(eyex, 3), round(eyey, 3), round(eyez, 3))
    scene_vars['ctr'] = (round(cx, 3), round(cy, 3), round(cz, 3))

    if scene_vars['debug']:
        lk = debug_info(scene_vars)
        scene_vars['last_key'] = lk


def kb_rot_eye(key):
    if key == 'r':
        scene_vars['eye_degree'][0] = (scene_vars['eye_degree'][0] + inc_deg) % 360
    elif key == 'R':
        scene_vars['eye_degree'][0] = (scene_vars['eye_degree'][0] - inc_deg) % 360
    elif key == 'e':
        scene_vars['eye_degree'][1] = (scene_vars['eye_degree'][1] + inc_deg) % 360
    elif key == 'E':
        scene_vars['eye_degree'][1] = (scene_vars['eye_degree'][1] - inc_deg) % 360


def kb_rot_ctr(key):
    # only if is not centered at origin
    if scene_vars['origin_centered']:
        pass
    elif key == GLUT_KEY_DOWN:
        scene_vars['center_degree'][1] = (scene_vars['center_degree'][1] - inc_deg) % 360
    elif key == GLUT_KEY_UP:
        scene_vars['center_degree'][1] = (scene_vars['center_degree'][1] + inc_deg) % 360
    elif key == GLUT_KEY_LEFT:
        scene_vars['center_degree'][0] = (scene_vars['center_degree'][0] + inc_deg) % 360
    elif key == GLUT_KEY_RIGHT:
        scene_vars['center_degree'][0] = (scene_vars['center_degree'][0] - inc_deg) % 360


def kb_nav_mov(key):
    # only if is not centered at origin
    if scene_vars['origin_centered']:
        pass
    elif key == 'w':
        if 90.0 <= scene_vars['center_degree'][0] <= 270:
            scene_vars['init_center'][2] -= inc_axis
            inc_x = math.sin(scene_vars['center_degree'][0] * rad)
            scene_vars['init_center'][0] += inc_x
        else:
            scene_vars['init_center'][2] += inc_axis
            inc_x = math.sin(scene_vars['center_degree'][0] * rad)
            scene_vars['init_center'][0] += inc_x
        scene_vars['m'] = math.tan(scene_vars['center_degree'][0] * rad)
    elif key == 's':
        if 90.0 <= scene_vars['center_degree'][0] <= 270:
            scene_vars['init_center'][2] += inc_axis
            inc_x = x = math.sin(scene_vars['center_degree'][0] * rad)
            scene_vars['init_center'][0] -= inc_x
        else:
            scene_vars['init_center'][2] -= inc_axis
            inc_x = x = math.sin(scene_vars['center_degree'][0] * rad)
            scene_vars['init_center'][0] -= inc_x
        scene_vars['m'] = math.tan(scene_vars['center_degree'][0] * rad)
    elif key == 'a':
        scene_vars['init_center'][0] -= inc_axis
    elif key == 'd':
        scene_vars['init_center'][0] += inc_axis


def kb_nav_to_lvl(key):
    if key == '0':
        scene_vars['init_center'][1] = 0
    elif key == '1':
        scene_vars['init_center'][1] = 4
    elif key == '2':
        scene_vars['init_center'][1] = 7


def kb_cfg(key):
    global inc_deg
    if key == 'h':
        inc_deg = 10
    elif key == 'g':
        inc_deg = 1
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

# Keyboard callback
def keyboard(key, x, y):
    global scene_vars

    if not isinstance(key, int):
        key = key.decode("utf-8")

    if key != 'i' and key != 'n':
        scene_vars['last_key'] = key

    # rotation keys that changes `eye_degree`
    if key in rot_eye_keys:
        scene_vars['origin_centered'] = True
        kb_rot_eye(key)
    # spec. keys that rotates center by changes in `center_degree``
    elif key in rot_ctr_keys:
        kb_rot_ctr(key)
    # navigation keys that changes the scene center (where camera is looking at)
    elif key in nav_keys:
        kb_nav_mov(key)
    elif key in lvl_keys:
        kb_nav_to_lvl(key)
    # config keys
    elif key in cfg_keys:
        kb_cfg(key)

    update_scene_params()

    glutPostRedisplay()


# Mouse callback
def mouse_motion(x, y):
    debug_world_coords(scene_vars, width, height, x, y, verbose=0)
    glutPostRedisplay()


# Mouse callback
def mouse_click(button, state, x, y):
    if state != GLUT_DOWN:
        return
    debug_world_coords(scene_vars, width, height, x, y)
    glutPostRedisplay()


# Callbacks registration
def register_callbacks():
    glutDisplayFunc(draw_scenario)
    glutIdleFunc(draw_scenario)
    #glutMouseFunc(mouse_click)
    #glutPassiveMotionFunc(mouse_motion)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(keyboard)
    glutReshapeFunc(reshape)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH | GLUT_STENCIL)
    glutInitWindowSize(1200, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Graciliano Ramos Library")
    init()
    register_callbacks()
    glutMainLoop()


main()
