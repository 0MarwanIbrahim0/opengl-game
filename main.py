from Run_Game import *
from Button import *

# initialize pygame
pygame.init()
# set display width and height
screen_main = pygame.display.set_mode((800, 600))
Background = pygame.image.load("Backound.png")
screen_main.blit(Background, (0, 0))
BUTTON_START = Button(350, 600 / 2, 100, 50, (255, 153, 51), "Start")
BUTTON_START.draw(screen_main)
BUTTON_QUIT = Button(350, 400, 100, 50, (255, 153, 51), "Quit")
BUTTON_QUIT.draw(screen_main)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            screen_finish = pygame.display.set_mode((800, 600))
            screen_finish.blit(Background, (0, 0))
            BUTTON_START.draw(screen_finish)
            BUTTON_QUIT.draw(screen_finish)
            if BUTTON_START.is_clicked(mouse_pos):
                run_game()
            elif BUTTON_QUIT.is_clicked(mouse_pos):
                pygame.quit()
                quit()
