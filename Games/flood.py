import pygame
import sys
import random

pygame.init()

grid_size = 12
square_size = 50

screen_width = grid_size * square_size
screen_height = grid_size * square_size
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flood Game")

white = (255, 255, 255)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (128, 0, 128)]
grid = [[random.choice(colors) for _ in range(grid_size)] for _ in range(grid_size)]

def draw_grid():
    for r in range(grid_size):
        for c in range(grid_size):
            pygame.draw.rect(screen, grid[r][c], (c * square_size, r * square_size, square_size, square_size))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)
    draw_grid()
    pygame.display.flip()

pygame.quit()
sys.exit()