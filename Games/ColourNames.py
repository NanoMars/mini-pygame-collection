import pygame

pygame.init()

# Define colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

running = True
while running:  # Main loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(RED)  # Example: Filling the screen with red
    pygame.display.flip()
    clock.tick(60)

pygame.quit()