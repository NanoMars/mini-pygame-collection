import pygame, noise, math

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Pygame Template")

class bug():
    def __init__(self):
        print("Bug created")
        

# Game loop
running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.flip()

pygame.quit()