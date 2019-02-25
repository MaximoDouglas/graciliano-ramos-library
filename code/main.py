import sys
import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from simple_objects import Objects as obj

rotate = False
rotateLeft = False;

degree = 0
radius = 50.0
rad = math.pi/180

width = 0
height = 0
aspect_ratio = 0


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
    glLoadIdentity()
    gluPerspective(45, aspect_ratio, 0.01, 100)
    gluLookAt(30.0, 30.0, 30.0, 0.0, 0.5, 0.0, 0.0, 1.0, 0.0);


def navigate():
    glLoadIdentity()
    gluPerspective(45.0, aspect_ratio, 0.01, 100.0)
    gluLookAt(radius * math.sin(degree * rad), 0, radius * math.cos(degree * rad),
               0.0, 0.5, 0.0,
               0.0, 1.0, 0.0)


def draw_scenario():

	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

	glPushMatrix()

	obj.draw_floors()
	obj.draw_tops()
	obj.draw_walls()
	obj.draw_doors()
	obj.draw_chairs()

	glPopMatrix()
	glutSwapBuffers()


# TODO: implement in `navigate`
def OnMouseClick(button, state, x, y):
    global rotate
    global rotateLeft

    if button == GLUT_LEFT_BUTTON:
        rotate = True
        rotateLeft = True
    if button == GLUT_RIGHT_BUTTON:
        rotate = True
        rotateLeft = False
    if button == GLUT_MIDDLE_BUTTON:
        rotate = False


def keyboard(key, x, y):
    global degree
    global radius

    key = key.decode("utf-8")

    if key == 'r':
        degree = (degree + 5) % 360
        navigate()
    elif key == 'R':
        degree = (degree - 5) % 360
        navigate()
    elif key == 'w':
        radius -= 3
        navigate()
    elif key == 's':
        radius += 3
        navigate()
    elif key == 'q':
        sys.exit()

    glutPostRedisplay()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(1200, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Graciliano Ramos Library")
    init()
    glutDisplayFunc(draw_scenario)
    glutKeyboardFunc(keyboard)
    glutIdleFunc(draw_scenario)
    glutMouseFunc(OnMouseClick)
    glutReshapeFunc(reshape)
    glutMainLoop()


main()

