from Button import *

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 500
screen_height = 500

# Create screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set font
font = pygame.font.SysFont('Arial', 30)

button = Button(100, 200, 150, 50, (0, 255, 0), "Start")
# Set button dimensions and position
button_width = 150
button_height = 50
# Set button state
button_state = False
# Game loop
running = True
while running:

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.is_clicked(event.pos):
                button_state = True
            # Check if mouse click is within button rect

    # Draw button on screen
    button.draw(screen)
    # Update screen
    pygame.display.update()

    # Open new window if button is clicked
    if button_state:
        # Create new screen
        new_screen = pygame.display.set_mode((screen_width, screen_height))

        # Set background color
        new_screen.fill((255, 255, 255))

        # Draw text on new screen
        new_text = font.render("New screen!", True, (0, 0, 0))
        new_text_rect = new_text.get_rect(center=new_screen.get_rect().center)
        new_screen.blit(new_text, new_text_rect)

        # Update new screen
        pygame.display.flip()

        # Reset button state
        button_state = False

# Quit Pygame
pygame.quit()
