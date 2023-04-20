import random

from Bottle import *
from Result import *
from box import *
from Display import *
from Handle_Input import *

# initialize pygame
pygame.init()
# set display width and height
Display(800, 600)
# set up the game variables
score = 0
missed = 0

box_pos = [0, -3.5, -5]
box_size = 1
box = Box(box_pos, box_size)

num_segments = 20
radius = 0.5
bottle_pos = [random.uniform(-3, 3), 2, -1]
bottle_size = 0.5
bottle_speed = 0.005
bottle = Cylinder(bottle_pos, bottle_size, bottle_speed, num_segments, radius)

# BUTTON_START = Button(-1.3, 0, 50, 50, (255, 153, 51), "Start")
Draw.draw_text('Press (Space) To Start', 72, (255, 0, 0), -1.9, 0, 0)
pygame.display.flip()

while True:
    running = False
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                quit()

            elif event.key == pygame.K_r:
                running = True
                missed, score = 0, 0
        # pygame.display.update()
        while running:
            # handle events
            controls = HandleInput(box_pos)
            controls.handle()
            # clear the screen and depth buffer
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            # Draw the Box
            box.draw()
            # update the bottle position
            bottle.update()
            bottle_pos[1] -= bottle_speed

            # if the bottle falls off the screen, generate a new one and increase missed count
            if bottle_pos[1] < -3:
                bottle_pos = [random.uniform(-3, 3), 2, -5]
                missed += 1

            # check for collision with the box
            if (box_pos[0] - box_size < bottle_pos[0] < box_pos[0] + box_size) and (
                    box_pos[1] - box_size < bottle_pos[1] < box_pos[1] + box_size) and (
                    box_pos[2] - box_size < bottle_pos[2] < box_pos[2] + box_size):
                bottle_pos = [random.uniform(-3, 3), 2, -5]
                score += 1

            # draw the bottle
            bottle = Cylinder(bottle_pos, bottle_size, bottle_speed, num_segments, radius)
            bottle.draw()

            Draw.draw_text(f"Score: {score}", 32, (0, 255, 0), 10, 0.9, -10)
            Draw.draw_text(f"Missed: {missed}", 32, (255, 0, 0), -2, 0.9, -10)
            # update the display
            pygame.display.flip()
            if missed == 3:
                glTranslatef(0.0, 0.0, 0.0)
                glRotatef(0, 0, 0, 0)
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                # display the game over message
                Draw.draw_text(f"Score: {score}", 32, (0, 255, 0), 10, 0.9, -10)
                Draw.draw_text('GAME OVER', 72, (255, 0, 0), -1.3, 0, 0)
                Draw.draw_text('Click Q to Quit Or R to Try again', 30, (255, 0, 0), -1.3, -1.5, 0)
                pygame.display.flip()
                running = False
