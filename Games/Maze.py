import pygame
from random import choice

RES = WIDTH, HEIGHT = 800, 600
TILE = 50
cols, rows = WIDTH // TILE, HEIGHT // TILE

pygame.init()
sc = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.walls = {
            'top': True,
            'right': True,
            'bottom': True,
            'left': True
        }
    def draw(self):
        x, y = self.x * TILE, self.y * TILE
        if self.visited:
            pygame.draw.line(sc, pygame.Color('1e1e1e'), (x, y, TILE, TILE))
            
        if self.walls['top']:
            pygame.draw.line(sc, pygame.Color('1e4f5b'), (x, y), (x + TILE, y), 3) 
        if self.walls['right']:
            pygame.draw.line(sc, pygame.Color('1e4f5b'), (x + TILE, y), (x + TILE, y + TILE), 3)
        if self.walls['bottom']:
            pygame.draw.line(sc, pygame.Color('1e4f5b'), (x + TILE, y + TILE), (x, y + TILE), 3)
        if self.walls['left']:
            pygame.draw.line(sc, pygame.Color('1e4f5b'), (x, y + TILE), (x, y), 3)
            
    def draw_current_cell(self):
        x, y = self.x * TILE, self.y * TILE
        pygame.draw.rect(sc, pygame.Color('f70067'), (x + 2, y + 2, TILE - 2, TILE - 2))   
            
grid_cells = [Cell(col,row) for row in range(rows) for col in range(cols)]
current_cell = grid_cells[0]
stack = []


    

running = True
while running:
    sc.fill (pygame.Color(255,255,255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.flip()
    clock.tick(60)