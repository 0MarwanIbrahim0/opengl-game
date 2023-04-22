import math
from OpenGL.GL import *
from OpenGL.raw.GLU import *


class Cylinder:
    def __init__(self, pos, size, speed, num_segments, radius):
        self.pos = pos
        self.size = size
        self.speed = speed
        self.num_segments = num_segments
        self.radius = radius
        # self.texture = texture

        self.vertices = []
        for i in range(self.num_segments):
            theta = 2.0 * math.pi * i / self.num_segments
            x = self.radius * math.cos(theta)
            y = self.radius * math.sin(theta)
            z = 0.5
            self.vertices.append((x, y, z))

        self.edges = []
        for i in range(self.num_segments):
            j = (i + 1) % self.num_segments
            self.edges.append((i, j))

    def draw(self):
        # glBindTexture(GL_TEXTURE_2D, self.texture)
        glPushMatrix()
        glColor3f(1.0, 1.0, 1.0)
        glTranslatef(self.pos[0], self.pos[1], self.pos[2])
        quad = gluNewQuadric()
        gluQuadricTexture(quad, GL_TRUE)
        gluCylinder(quad, self.size, self.size, 2 * self.size, self.num_segments, self.num_segments)
        glPopMatrix()

    def update(self):
        self.pos[1] -= self.speed
