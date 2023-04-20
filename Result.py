import pygame
from OpenGL.GL import *


class Draw:

    def draw_text(text, font_size, color, x, y, z):
        font = pygame.font.SysFont("Arial", font_size)
        text_surface = font.render(str(text), True, color, (0, 0, 0))
        text_data = pygame.image.tostring(text_surface, "RGBA", True)
        glRasterPos3d(x, y, z)
        glDrawPixels(text_surface.get_width(), text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)
