import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


class Display:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # create the display surface
        self.surface = pygame.display.set_mode((self.width, self.height), DOUBLEBUF | OPENGL)
        # set up the OpenGL perspective projection
        gluPerspective(45, (self.width / self.height), 0.1, 50.0)
        # set up the initial position and orientation of the camera
        glTranslatef(0.0, 0.0, -5.0)
        glRotatef(30, 60, 60, 10)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
