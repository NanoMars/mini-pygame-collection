import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen (width, height)
screen = pygame.display.set_mode((800, 600))

# Set the window title
pygame.display.set_caption('Pygame Template')

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the screen with a color (RGB)
    screen.fill((0, 0, 0))  # Black background

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()