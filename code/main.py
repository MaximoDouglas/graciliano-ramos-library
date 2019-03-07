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

# debug
eye = None
ctr = None

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
    global eye
    global ctr

    eyex = radius * math.sin(eye_degree[0] * rad)
    eyey = radius * math.sin(eye_degree[1] * rad)
    eyez = radius * math.cos(eye_degree[0] * rad)
    cx = radius * math.sin(center_degree[0] * rad) + eyex
    cy = radius * math.sin(center_degree[1] * rad) + eyey
    cz = radius * math.cos(center_degree[0] * rad) + eyez

    if origin_centered:
        eyex = 50 * math.sin(eye_degree[0] * rad)
        eyey = 50 * math.sin(eye_degree[1] * rad)
        eyez = 50 * math.cos(eye_degree[0] * rad)
        cx, cy, cz = 0, 0, 0

    # debug
    eye = (round(eyex, 3), round(eyey, 3), round(eyez, 3))
    ctr = (round(cx, 3), round(cy, 3), round(cz, 3))

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
    obj.draw_chairs()
    obj.draw_tables()
    obj.draw_book_cases()

    alt = 50.0
    alt_rev = -5
    axis(ctr, (ctr[0], ctr[1], alt), (1.0, 0.0, 0.0)) # z to red
    axis(ctr, (ctr[0], alt, ctr[2]), (0.0, 1.0, 0.0)) # y to green
    axis(ctr, (alt, ctr[1], ctr[2]), (0.0, 0.0, 1.0)) # x to blue
    axis(ctr, (ctr[0], ctr[1], alt_rev), (1.0, 1.0, 0.0)) # -z to yellow
    axis(ctr, (ctr[0], alt_rev, ctr[2]), (1.0, 0.0, 1.0)) # -y to pink
    axis(ctr, (alt_rev, ctr[1], ctr[2]), (0.0, 1.0, 1.0)) # -x to cyan
    # line at (0,15,0)
    axis((0,0,0),(0,15,0),(0.0,0.0,0.0))

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

    if not isinstance(key, int):
        key = key.decode("utf-8")

    print('--- distance eye to center_degree ---')
    print('radius ', radius)
    print('center ', ctr)
    print('eye    ', eye)
    print('dist   ', math.sqrt((eye[0] - ctr[0])**2 +
                               (eye[1] - ctr[1])**2 +
                               (eye[2] - ctr[2])**2))

    origin_centered = False

    if key == GLUT_KEY_DOWN:
        center_degree[1] = (center_degree[1] + 5) % 360
    elif key == GLUT_KEY_UP:
        center_degree[1] = (center_degree[1] - 5) % 360
    elif key == GLUT_KEY_LEFT:
        center_degree[0] = (center_degree[0] + 5) % 360
    elif key == GLUT_KEY_RIGHT:
        center_degree[0] = (center_degree[0] - 5) % 360
    elif key == 'r':
        origin_centered = True
        eye_degree[0] = (eye_degree[0] + 5) % 360
    elif key == 'R':
        origin_centered = True
        eye_degree[0] = (eye_degree[0] - 5) % 360
    elif key == 'e':
        eye_degree[1] = (eye_degree[1] + 5) % 360
    elif key == 'E':
        eye_degree[1] = (eye_degree[1] - 5) % 360
    elif key == 'w':
        radius -= 3
    elif key == 's':
        radius += 3
    elif key == 'q':
        sys.exit()

    glutPostRedisplay()


# just for debug purposes :)
def axis(center, last_vertex, c):
    glColor(c)
    glBegin(GL_LINES)
    glVertex(center)
    glVertex(last_vertex)
    glEnd()


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
