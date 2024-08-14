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
    def check_cell(self, x, y):
        find_index = lambda x, y: x + y * cols
        if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
            return False
        return grid_cells[find_index(x, y)]
    def check_neighbors(self):
        neighbors = []
        top = self.check_cell(self.x, self.y - 1)
        right = self.check_cell(self.x + 1, self.y)
        bottom = self.check_cell(self.x, self.y + 1)
        left = self.check_cell(self.x - 1, self.y)
        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if left and not left.visited:
            neighbors.append(left)
            
def remove_walls(current, next):
    dx = current.x - next.x
    if dx == 1:
        current.walls['left'] = False
        next.walls['right'] = False
    elif dx == -1:
        current.walls['right'] = False
        next.walls['left'] = False
    dy = current.y - next.y
    if dy == 1:
        current.walls['top'] = False
        next.walls['bottom'] = False
    elif dy == -1:
        current.walls['bottom'] = False
        next.walls['top'] = False
        
            
grid_cells = [Cell(col,row) for row in range(rows) for col in range(cols)]
current_cell = grid_cells[0]
stack = []


    

running = True
while running:
    sc.fill (pygame.Color(255,255,255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    next_cell = current_cell.check_neighbors()
    if next_cell:
        next_cell.visited = True
        dx = current_cell.x - next_cell.x
        dy = current_cell.y - next_cell.y

        if dx == 1:
            current_cell.walls['left'] = False
            next_cell.walls['right'] = False
        elif dx == -1:
            current_cell.walls['right'] = False
            next_cell.walls['left'] = False
        if dy == 1:
            current_cell.walls['top'] = False
            next_cell.walls['bottom'] = False
        elif dy == -1:
            current_cell.walls['bottom'] = False
            next_cell.walls['top'] = False
        current_cell = next_cell
        
    
    pygame.display.flip()
    clock.tick(60)