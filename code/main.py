from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from simple_objects import Objects as obj

degree = 0
rotate = False
rotateLeft = False;

def init():
	glClearColor(0.0, 0.0, 0.0, 0.0)
	glEnable(GL_DEPTH_TEST)

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluPerspective(45, w/h, 0.01, 100)
    gluLookAt(0.0, 12.0, 30.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);

def rotacionate():
    global degree

    if(rotate):
        if (rotateLeft):
            degree = (degree + 1) % 360
        else:
            degree = (degree - 1) % 360

def draw_scenario():

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    rotacionate()

    glPushMatrix();
    glRotatef(degree, 0.0, 1.0, 0.0);
    obj.draw_floors()
    obj.draw_walls()
    obj.draw_doors()
    glPopMatrix()

    glutSwapBuffers()

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

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(1200, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Graciliano Ramos Library")

    init()
    glutDisplayFunc(draw_scenario)
    glutMouseFunc(OnMouseClick)
    glutIdleFunc(draw_scenario)
    glutReshapeFunc(reshape)
    glutMainLoop()

main()
