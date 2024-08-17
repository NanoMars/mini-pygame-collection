import pygame
import sys
import random
import subprocess

pygame.init()

grid_size = 12
square_size = 50

screen_width = grid_size * square_size
screen_height = grid_size * square_size
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flood")

white = (255, 255, 255)
colors = [(255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (128, 0, 128)]
grid = [[random.choice(colors) for _ in range(grid_size)] for _ in range(grid_size)]

def draw_grid():
    for r in range(grid_size):
        for c in range(grid_size):
            pygame.draw.rect(screen, grid[r][c], (c * square_size, r * square_size, square_size, square_size))

def fill(old_color, new_color, r, c):
    if r >= 0 and r < grid_size and c >= 0 and c < grid_size:
        if grid[r][c] == old_color:
            grid[r][c] = new_color
            fill(old_color, new_color, r-1, c)
            fill(old_color, new_color, r+1, c)
            fill(old_color, new_color, r, c-1)
            fill(old_color, new_color, r, c+1)

def check_win():
    for r in range(grid_size):
        for c in range(grid_size):
            if grid[r][c] != grid[0][0]:
                return False
    return True

game_path = 'main.py'

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row = y // square_size
            col = x // square_size
            current_color = grid[0][0]
            new_color = grid[row][col]
            if new_color != current_color:
                fill(current_color, new_color, 0, 0)
                if check_win():
                    subprocess.Popen(["python3", "-c", f"import game_opener; game_opener.open_game('{game_path}')"])
                    pygame.quit()
                    sys.exit()

    screen.fill(white)
    draw_grid()
    pygame.display.flip()

pygame.quit()
sys.exit()