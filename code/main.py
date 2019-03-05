import sys
import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from simple_objects import Objects as obj

rotate = False
rotateLeft = False;

az_degree = 0
el_degree = 20
radius = 50.0
rad = math.pi/180

width = 0
height = 0
aspect_ratio = 0

center = [0.0, 0.0, 0.0]

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
    glLoadIdentity()
    gluPerspective(45.0, aspect_ratio, 0.01, 100.0)
    gluLookAt(radius * math.sin(az_degree * rad),
              radius * math.sin(el_degree * rad),
              radius * math.cos(az_degree * rad),
              center[0], center[1], center[2],
              0.0, 1.0, 0.0)

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
    obj.draw_book_cases()

    alt = 50.0
    alt_rev = -5
    axis((0.0, 0.0, alt), (1.0, 0.0, 0.0)) # z to red
    axis((0.0, alt, 0.0), (0.0, 1.0, 0.0)) # y to green
    axis((alt, 0.0, 0.0), (0.0, 0.0, 1.0)) # x to blue
    axis((0.0, 0.0, alt_rev), (0.0, 0.0, 0.0)) # -z to black
    axis((0.0, alt_rev, 0.0), (0.0, 0.0, 0.0)) # -y to black
    axis((alt_rev, 0.0, 0.0), (0.0, 0.0, 0.0)) # -x to black

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

    center[0] = world_coords[0]/radius
    center[1] = -world_coords[1]/radius
    center[2] = world_coords[2]/radius


def mouse_motion(x, y):
    get_world_coords(x, y, verbose=0)
    glutPostRedisplay()


def mouse_click(button, state, x, y):
    if state != GLUT_DOWN:
        return
    get_world_coords(x, y)
    glutPostRedisplay()

def keyboard(key, x, y):
    global az_degree
    global el_degree
    global radius

    if not isinstance(key, int):
        key = key.decode("utf-8")

    if key == GLUT_KEY_DOWN:
        print("DOWN")
    elif key == GLUT_KEY_UP:
        print("UP")
    elif key == GLUT_KEY_LEFT:
        print("LEFT")
    elif key == GLUT_KEY_RIGHT:
        print("RIGHT")
    elif key == 'r':
        az_degree = (az_degree + 5) % 360
    elif key == 'R':
        az_degree = (az_degree - 5) % 360
    elif key == 'e':
        el_degree = (el_degree + 5) % 360
    elif key == 'E':
        el_degree = (el_degree - 5) % 360
    elif key == 'w':
        radius -= 3
    elif key == 's':
        radius += 3
    elif key == 'q':
        sys.exit()

    glutPostRedisplay()


# just for debug purposes :)
def axis(last_vertex, c):
    glColor(c)
    glBegin(GL_LINES)
    glVertex((0.0, 0.0, 0.0))
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
