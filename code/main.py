from time import time
from math import sin
from math import cos
from math import radians

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import debug
import navigation as nav
import objects as obj
import texture as tex


width = 0
height = 0
aspect_ratio = 0

kb_keys = {
        'rot_eye' : ('r', 'R', 'e', 'E'),
        'rot_ctr' : (GLUT_KEY_DOWN, GLUT_KEY_UP, GLUT_KEY_LEFT, GLUT_KEY_RIGHT),
        'nav' : ('w', 's', 'a', 'd'),
        'lvl' : ('0', '1', '2', 'o', 'O'),
        'cfg' : ('g', 'h', 'c', 'i', 'n', 'q', 't')
        }

scene_vars = {
        'init_center' : [0, 0, 32.12], 'eye': None, 'ctr': None,
        'eye_degree' : [0, 20], 'center_degree' : [180, 0],
        'radius' : 5.0, 'm' : None,
        'inc_deg': 1, 'inc_axis': 1,
        'origin_centered' : True,
        'last_key': None, 'show_axis': False, 'debug': True,
        'fps' : {
                 'frames': 0, 'last_time' : time(), 'current' : 0,
                 'enable': True
                 },
        'spf' : 0
        }

# global for texture
textures = {'door': None}


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)

    # Bloco para iluminação ambiente ---------------
    luzAmbiente   = [0.5, 0.5, 0.5, 1]
    posicaoLuz    = [0.0, 1000.0, 0.0, 0.1]

    # Habilita o modelo de colorização de Gouraud
    glShadeModel(GL_SMOOTH)

    # Ativa o uso da luz ambiente
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, luzAmbiente)

    # Define os parâmetros da luz de número 0
    glLightfv(GL_LIGHT0, GL_AMBIENT, luzAmbiente)
    glLightfv(GL_LIGHT0, GL_POSITION, posicaoLuz)

    # Habilita a definição da cor do material a partir da cor corrente
    glEnable(GL_COLOR_MATERIAL)

    # Habilita o uso de iluminação
    glEnable(GL_LIGHTING)

    # Habilita a luz de número 0
    glEnable(GL_LIGHT0)
    # Fim do bloco para iluminação ambiente ---------------

    # Habilita o depth-buffering
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
    obj.draw_doors(textures['door'])
    obj.draw_chairs()
    obj.draw_tables()
    obj.draw_book_cases()
    obj.draw_front()

    ### debug start
    if scene_vars['show_axis']:
        debug.axis(scene_vars['ctr'], scene_vars['eye'])

    if scene_vars['fps']['enable']:
        debug.fps(scene_vars)

    glPopMatrix()
    glutSwapBuffers()


def update_scene_params():

    ed_radians_0 = radians(scene_vars['eye_degree'][0])
    ed_radians_1 = radians(scene_vars['eye_degree'][1])
    cd_radians_0 = radians(scene_vars['center_degree'][0])
    cd_radians_1 = radians(scene_vars['center_degree'][1])

    # center initial position in this frame
    cx, cy, cz = scene_vars['init_center']
    # with init_center we set camera position
    eyex = cx + scene_vars['radius'] * sin(ed_radians_0)
    eyey = cy + scene_vars['radius'] * sin(ed_radians_1)
    eyez = cz + scene_vars['radius'] * cos(ed_radians_0)
    # we recalculate the center in case we changed its center_degree
    cx = eyex + scene_vars['radius'] * sin(cd_radians_0)
    cy = eyey + scene_vars['radius'] * sin(cd_radians_1)
    cz = eyez + scene_vars['radius'] * cos(cd_radians_0)

    if scene_vars['origin_centered']:
        eyex = 70 * sin(ed_radians_0)
        eyey = 70 * sin(ed_radians_1)
        eyez = 70 * cos(ed_radians_0)
        cx, cy, cz = 0, 0, 0

    # debug
    scene_vars['eye'] = (round(eyex, 3), round(eyey, 3), round(eyez, 3))
    scene_vars['ctr'] = (round(cx, 3), round(cy, 3), round(cz, 3))

    if scene_vars['debug']:
        lk = debug.scene_info(scene_vars)
        scene_vars['last_key'] = lk


# Keyboard callback
def keyboard(key, x, y):

    if not isinstance(key, int):
        key = key.decode("utf-8")

    if key != 'i' and key != 'n':
        scene_vars['last_key'] = key

    if key in kb_keys['rot_eye']:
        # rotation keys that changes `eye_degree`
        scene_vars['origin_centered'] = True
        nav.kb_rot_eye(key, scene_vars)
    elif key in kb_keys['rot_ctr']:
        # spec. keys that rotates center by changes in `center_degree``
        nav.kb_rot_ctr(key, scene_vars)
    elif key in kb_keys['nav']:
        # navigation keys that changes the scene center (where camera is looking at)
        nav.kb_nav_mov(key, scene_vars)
    elif key in kb_keys['lvl']:
        nav.kb_nav_to_lvl(key, scene_vars)
    elif key in kb_keys['cfg']:
        # config keys
        nav.kb_cfg(key, scene_vars)

    update_scene_params()

    glutPostRedisplay()


# Callbacks' registration
def register_callbacks():

    glutDisplayFunc(draw_scenario)
    #glutIdleFunc(draw_scenario)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(keyboard)
    glutReshapeFunc(reshape)


def register_textures():
    global textures

    texture_id = tex.read_texture('textures/door_1_28x28.png')
    textures['door'] = texture_id


def main():

    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH | GLUT_STENCIL)
    glutInitWindowSize(1200, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Graciliano Ramos Library")

    init()
    register_callbacks()
    register_textures()

    glutMainLoop()


main()
