from OpenGL.GL import *


class Box:
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        self.vertices = (
            (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1), (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1))
        self.edges = ((0, 1), (0, 3), (0, 4), (1, 2), (1, 5), (2, 3), (2, 6), (3, 7), (4, 5), (4, 7), (5, 6), (6, 7))
        self.colors = [
            (1, 0, 0),  # red
            (0, 1, 0),  # green
            (0, 0, 1),  # blue
            (1, 1, 0),  # yellow
            (1, 0, 1),  # magenta
            (0, 1, 1),  # cyan
            (1, 1, 1),  # white
            (0, 0, 0),  # black
        ]

    def draw(self):
        glPushMatrix()
        glTranslatef(self.pos[0], self.pos[1], self.pos[2])
        glBegin(GL_QUADS)
        for i, edge in enumerate(self.edges):
            # glColor3fv(self.colors[i])
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
        glEnd()
        glPopMatrix()
