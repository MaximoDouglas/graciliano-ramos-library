
import numpy as np

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image


def gen_texture_id(obj, id, px='28'):
    folder = 'textures/'
    #filename = f"{folder}{obj}_{id}_{px}.png"
    filename = "{}{}_{}_{}.png".format(folder, obj, id, px)
    texture_id = read_texture(filename)
    return texture_id
 

def read_image_data(filename):
    img = Image.open(filename)
    img_data = np.array(list(img.getdata()), np.int8)
    return img_data, img.size


def read_texture(filename):

    texture_id = glGenTextures(1)  # return 1 texture name

    # Will these remain the same?
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)  # pname, param

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)  # repeat in s when done, if needed
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)  # repeat in t when done, if needed
    #glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)  # repeat in s when done, if needed
    #glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)  # repeat in t when done, if needed
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)  # how to upsample?
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)  # how to downsample?

    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)

    img_data, dims = read_image_data(filename)

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA,
                 dims[0], dims[1], 0,
                 GL_RGBA, GL_UNSIGNED_BYTE, img_data)

    return texture_id

