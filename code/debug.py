import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from simple_objects import Objects as obj

def debug_axis(center, last_vertex, c):
    glColor(c)
    glBegin(GL_LINES)
    glVertex(center)
    glVertex(last_vertex)
    glEnd()


def debug_dist_e2c(ctr, eye):
    return round(math.sqrt(
        (eye[0] - ctr[0])**2 +
        (eye[1] - ctr[1])**2 +
        (eye[2] - ctr[2])**2), 3)


def debug_info(scene_vars):
    spec_keys = [GLUT_KEY_DOWN, GLUT_KEY_UP, GLUT_KEY_LEFT, GLUT_KEY_RIGHT]
    key_names = ["DOWN", "UP", "LEFT", "RIGHT"]

    last_key = scene_vars['last_key']

    if isinstance(last_key, int):
        if last_key in spec_keys:
            scene_vars['last_key'] = key_names[spec_keys.index(last_key)]

    print('--- DEBUG START ---')

    print('last_key\t', scene_vars['last_key'])
    print('radius \t\t', scene_vars['radius'])
    print('inclination \t', scene_vars['m'])
    print('init_center \t', scene_vars['init_center'])
    print('center \t\t', scene_vars['ctr'])
    print('center_degree \t', scene_vars['center_degree'])
    print('eye    \t\t', scene_vars['eye'])
    print('eye_degree \t', scene_vars['eye_degree'])
    print('dist   \t\t', debug_dist_e2c(scene_vars['ctr'], scene_vars['eye']))
                         
    print('--- DEBUG END ---')


# TODO: fix
def debug_world_coords(scene_vars, width, height, x, y, verbose=1):

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

