from Run_Game import *
from Button import *

# initialize pygame
pygame.init()
# set display width and height
screen_main = pygame.display.set_mode((800, 600))
BUTTON_START = Button(20.3, 20, 30, 40, (255, 153, 51), "Start")
BUTTON_START.draw(screen_main)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if BUTTON_START.is_clicked(mouse_pos):
                run_game()
                Screen_finish = pygame.display.set_mode((800, 600))
                BUTTON_START = Button(20.3, 20, 30, 40, (255, 153, 51), "Start")
                BUTTON_START.draw(Screen_finish)
