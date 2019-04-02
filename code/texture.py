
import numpy as np

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image


def gen_texture_id(obj, id, px='28'):
    folder = 'textures/{}'.format(obj)
    #filename = f"{folder}{obj}_{id}_{px}.png"
    filename = "{}/{}_{}.png".format(folder, id, px)
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

    borderColor = (1.0, 1.0, 1.0, 1.0)
    glTexParameterfv(GL_TEXTURE_2D, GL_TEXTURE_BORDER_COLOR, borderColor)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)  # repeat in s when done, if needed
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)  # repeat in t when done, if needed
    #glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_BORDER)  # repeat in s when done, if needed
    #glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_BORDER)  # repeat in t when done, if needed
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)  # how to upsample?
    #glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)  # how to downsample?
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)  # how to upsample?

    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)

    img_data, dims = read_image_data(filename)

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB,
                 dims[0], dims[1], 0,
                 GL_RGB, GL_UNSIGNED_BYTE, img_data)

    glGenerateMipmap(GL_TEXTURE_2D)

    return texture_id

