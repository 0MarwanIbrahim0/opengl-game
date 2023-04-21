import pygame


class HandleInput:
    def __init__(self, box_pos):
        self.box_pos = box_pos

    def handle(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_LEFT:
                    self.box_pos[0] -= 0.5
                elif event.key == pygame.K_RIGHT:
                    self.box_pos[0] += 0.5
                elif event.key == pygame.K_UP:
                    self.box_pos[2] -= 0.5
                elif event.key == pygame.K_DOWN:
                    self.box_pos[2] += 0.5
            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()
