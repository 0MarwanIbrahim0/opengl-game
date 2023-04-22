from OpenGL.GL import *
from Texture import *


class Box:
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        self.vertices = (
            (-1, -1, -1),
            (1, -1, -1),
            (1, 1, -1),
            (-1, 1, -1),
            (-1, -1, 1),
            (1, -1, 1),
            (1, 1, 1),
            (-1, 1, 1)
        )
        self.tex_coords = (
            (0, 0),
            (1, 0),
            (1, 1),
            (0, 1)
        )
        self.faces = ((0, 1, 2, 3),
                      (3, 2, 6, 7),
                      (7, 6, 5, 4),
                      (4, 5, 1, 0),
                      (1, 5, 6, 2),
                      (4, 0, 3, 7)
                      )
        self.colors = [
            (1, 0, 0),  # red
            (0, 1, 0),  # green
            (0, 0, 1),  # blue
            (1, 1, 0),  # yellow
            (1, 0, 1),  # magenta
            (0, 1, 1),  # cyan
            (1, 1, 1),  # white
            (0, 0, 0),  # black
            (1, 0, 0),  # red
            (0, 1, 0),  # green
            (0, 0, 1),  # blue
            (1, 1, 0),  # yellow
            (1, 0, 1),  # magenta
            (0, 1, 1),  # cyan
            (1, 1, 1),  # white
            (0, 0, 0),  # black
        ]

    def draw(self,texture):
        load_texture(texture)
        glPushMatrix()
        glTranslatef(self.pos[0], self.pos[1], self.pos[2])
        glBegin(GL_QUADS)
        for face in self.faces:
            for vertex, tex_coord in zip(face, self.tex_coords):
                glTexCoord2f(tex_coord[0], tex_coord[1])
                glVertex3fv(self.vertices[vertex])
        glEnd()
        glPopMatrix()
