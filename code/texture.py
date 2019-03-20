
import numpy as np

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image


def read_texture(filename):

    img = Image.open(filename)
    img_data = np.array(list(img.getdata()), np.int8)

    texture_id = glGenTextures(1)  # return 1 texture name

    # Will these remain the same?
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)  # pname, param

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)  # repeat in s when done, if needed
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)  # repeat in t when done, if needed
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)  # how to upsample?
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)  # how to downsample?

    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA,
                 img.size[0], img.size[1], 0,
                 GL_RGBA, GL_UNSIGNED_BYTE, img_data)

    return texture_id

