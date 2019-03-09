import numpy as np
import sys
import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from simple_objects import Objects as obj

width = 0
height = 0
aspect_ratio = 0

rad = math.pi/180
radius = 5.0

eye_degree = [0, 20]  # in relation to center positon
center_degree = [180, 0]  # in relation to eye position
origin_centered = False

init_center = [0, 0, 0]

# debug
debug_vars = {'eye': None, 'ctr': None, 'last_key': None,
              'm' : None}

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glEnable(GL_DEPTH_TEST)


def reshape(w, h):
    global width
    global height
    global aspect_ratio

    width = float(w)
    height = float(h)
    aspect_ratio = width / height

    glViewport(0, 0, w, h)
    glMatrixMode(GL_MODELVIEW)

    update_view()


def update_view():
    #global eye
    #global ctr
    global debug_vars

    # center initial position in this frame
    cx, cy, cz = init_center
    # with init_center we set camera position
    eyex = cx + radius * math.sin(eye_degree[0] * rad)
    eyey = cy + radius * math.sin(eye_degree[1] * rad)
    eyez = cz + radius * math.cos(eye_degree[0] * rad)
    # we recalculate the center in case we changed its center_degree
    cx = eyex + radius * math.sin(center_degree[0] * rad)
    cy = eyey + radius * math.sin(center_degree[1] * rad)
    cz = eyez + radius * math.cos(center_degree[0] * rad)

    if origin_centered:
        eyex = 50 * math.sin(eye_degree[0] * rad)
        eyey = 50 * math.sin(eye_degree[1] * rad)
        eyez = 50 * math.cos(eye_degree[0] * rad)
        cx, cy, cz = 0, 0, 0

    # debug
    debug_vars['eye'] = (round(eyex, 3), round(eyey, 3), round(eyez, 3))
    debug_vars['ctr'] = (round(cx, 3), round(cy, 3), round(cz, 3))

    glLoadIdentity()
    gluPerspective(30.0, aspect_ratio, 0.01, 100.0)
    gluLookAt(eyex, eyey, eyez,
              cx, cy, cz,
              0.0, 1.0, 0.0)


def draw_scenario():

    update_view()

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT|GL_STENCIL_BUFFER_BIT)

    glPushMatrix()

    obj.draw_floors()
    obj.draw_tops()
    obj.draw_walls()
    obj.draw_doors()
#    obj.draw_chairs()
#    obj.draw_tables()
#    obj.draw_book_cases()
#
    # Debug
    alt = 50.0
    alt_rev = -5
    ctr = debug_vars['ctr']
    eye = debug_vars['eye']
    debug_axis(ctr, (ctr[0], ctr[1], alt), (1.0, 0.0, 0.0)) # z to red
    debug_axis(ctr, (ctr[0], alt, ctr[2]), (0.0, 1.0, 0.0)) # y to green
    debug_axis(ctr, (alt, ctr[1], ctr[2]), (0.0, 0.0, 1.0)) # x to blue
    debug_axis(ctr, (ctr[0], ctr[1], alt_rev), (1.0, 1.0, 0.0)) # -z to yellow
    debug_axis(ctr, (ctr[0], alt_rev, ctr[2]), (1.0, 0.0, 1.0)) # -y to pink
    debug_axis(ctr, (alt_rev, ctr[1], ctr[2]), (0.0, 1.0, 1.0)) # -x to cyan
    # line at (0,15,0)
    debug_axis((0,0,0),(0,15,0),(0.0,0.0,0.0))
    # line center to eye
    debug_axis(ctr, (eye[0], 0, eye[2]), (1.0, 1.0, 1.0))

    glPopMatrix()
    glutSwapBuffers()


def get_world_coords(x, y, verbose=1):

    color = glReadPixels(x, width - y - 1, 1, 1, GL_RGBA, GL_UNSIGNED_BYTE)
    depth = glReadPixels(x, width - y - 1, 1, 1, GL_DEPTH_COMPONENT, GL_FLOAT)
    index = glReadPixels(x, width - y - 1, 1, 1, GL_STENCIL_INDEX, GL_UNSIGNED_INT)

    # Screen space coords to world space coords
    wx = x
    wy = width - y - 1
    wz = depth[0][0]
    mvmat = glGetDoublev(GL_MODELVIEW_MATRIX)
    pmat = glGetDoublev(GL_PROJECTION_MATRIX)
    vmat = glGetIntegerv(GL_VIEWPORT)
    world_coords = gluUnProject(wx, wy, wz, mvmat, pmat, vmat)

    # Print everything
    if verbose:
        print("{}".format(10*'-'))
        #print(x, y, width, height)
        print("Color: ", [int(c) for c in color])
        print("Depth (0 is near): ", depth[0][0])
        print("Stencil: ", obj.dnames[index[0][0]])
        print("World coords: ", [round(wc, 3) for wc in world_coords])

    center_degree[0] = world_coords[0]/radius
    center_degree[1] = -world_coords[1]/radius
    center_degree[2] = world_coords[2]/radius


def mouse_motion(x, y):
    get_world_coords(x, y, verbose=0)
    glutPostRedisplay()


def mouse_click(button, state, x, y):
    if state != GLUT_DOWN:
        return
    get_world_coords(x, y)
    glutPostRedisplay()


def keyboard(key, x, y):
    global eye_degree
    global eye_degree
    global radius
    global center_degree
    global origin_centered
    global init_center
    global debug_vars

    if not isinstance(key, int):
        key = key.decode("utf-8")

    debug_info()
    if key != 'i':
        debug_vars['last_key'] = key

    inc_deg = 2
    inc_axis = 1

    if key == GLUT_KEY_DOWN:
        center_degree[1] = (center_degree[1] - inc_deg) % 360
        origin_centered = False
    elif key == GLUT_KEY_UP:
        center_degree[1] = (center_degree[1] + inc_deg) % 360
        origin_centered = False
    elif key == GLUT_KEY_LEFT:
        center_degree[0] = (center_degree[0] + inc_deg) % 360
        origin_centered = False
    elif key == GLUT_KEY_RIGHT:
        center_degree[0] = (center_degree[0] - inc_deg) % 360
        origin_centered = False
    elif key == 'r':
        origin_centered = True
        eye_degree[0] = (eye_degree[0] + inc_deg) % 360
    elif key == 'R':
        origin_centered = True
        eye_degree[0] = (eye_degree[0] - inc_deg) % 360
    elif key == 'e':
        eye_degree[1] = (eye_degree[1] + inc_deg) % 360
        origin_centered = False
    elif key == 'E':
        eye_degree[1] = (eye_degree[1] - inc_deg) % 360
        origin_centered = False
    elif key == 'w':
        if 90.0 <= center_degree[0] <= 270:
            init_center[2] -= inc_axis
            m, init_center[0] = get_new_center_x_from()
        else:
            init_center[2] += inc_axis
            m, init_center[0] = get_new_center_x_from(reverse=True)
        debug_vars['m'] = m
        origin_centered = False
    elif key == 's':
        if 90.0 <= center_degree[0] <= 270:
            init_center[2] += inc_axis
            m, init_center[0] = get_new_center_x_from()
        else:
            init_center[2] -= inc_axis
            m, init_center[0] = get_new_center_x_from(reverse=True)
        debug_vars['m'] = m
        origin_centered = False
    elif key == 'a':
        init_center[0] -= 1
        origin_centered = False
    elif key == 'd':
        init_center[0] += 1
        origin_centered = False
    elif key == 'i':
        debug_info()
    elif key == 'q':
        sys.exit()

    glutPostRedisplay()


def get_new_center_x_from(reverse=False):
    ctr = debug_vars['ctr']
    eye = debug_vars['eye']
    if not reverse:
        dx = (ctr[0] - eye[0])
        dy = (ctr[2] - eye[2])
    else:
        dx = (eye[0] - ctr[0])
        dy = (eye[2] - ctr[2])
    if dy == 0:
        m = 0
    else:
        m = dx/dy
    x = m * init_center[2]  # new_z
    return m, x

# just for debug purposes :)
def debug_axis(center, last_vertex, c):
    glColor(c)
    glBegin(GL_LINES)
    glVertex(center)
    glVertex(last_vertex)
    glEnd()


# just for debug purposes :)
def debug_info():
    spec_keys = [GLUT_KEY_DOWN, GLUT_KEY_UP, GLUT_KEY_LEFT, GLUT_KEY_RIGHT]
    key_names = ["DOWN", "UP", "LEFT", "RIGHT"]

    last_key = debug_vars['last_key']
    ctr = debug_vars['ctr']
    eye = debug_vars['eye']
    m = debug_vars['m']

    if isinstance(last_key, int):
        if last_key in spec_keys:
            last_key = key_names[spec_keys.index(last_key)]
            
    print('--- DEBUG START ---')
    print('last_key\t', last_key)
    print('radius \t\t', radius)
    print('inclination \t', m)
    print('center \t\t', ctr)
    print('center_degree \t', center_degree)
    print('eye    \t\t', eye)
    print('eye_degree \t', eye_degree)
    print('dist   \t\t', round(math.sqrt((eye[0] - ctr[0])**2 + 
                                         (eye[1] - ctr[1])**2 +
                                         (eye[2] - ctr[2])**2), 3))
    print('--- DEBUG END ---')


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
