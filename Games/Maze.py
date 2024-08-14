import pygame
from random import choice

RES = WIDTH, HEIGHT = 1200, 900
TILE = 50
cols, rows = WIDTH // TILE, HEIGHT // TILE

pygame.init()
sc = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self.visited = False
    
    def draw_current_cell(self):
        x, y = self.x * TILE, self.y * TILE
        pygame.draw.rect(sc, pygame.Color('#f70067'), (x + 2, y + 2, TILE - 2, TILE - 2))
    
    def draw(self):
        x, y = self.x * TILE, self.y * TILE
        
        if self.visited:
            pygame.draw.rect(sc, pygame.Color('#1e1e1e'), (x, y, TILE, TILE))
        
        if self.walls['top']:
            pygame.draw.line(sc, pygame.Color('#1e4f5b'), (x, y), (x + TILE, y), 3)
        if self.walls['right']:
            pygame.draw.line(sc, pygame.Color('#1e4f5b'), (x + TILE, y), (x + TILE, y + TILE), 3)
        if self.walls['bottom']:
            pygame.draw.line(sc, pygame.Color('#1e4f5b'), (x + TILE, y + TILE), (x, y + TILE), 3)
        if self.walls['left']:
            pygame.draw.line(sc, pygame.Color('#1e4f5b'), (x, y + TILE), (x, y), 3)
            
    def check_cell(self, x, y):
        find_index = lambda x, y: x + y * cols
        if x < 0 or x >= cols or y < 0 or y >= rows:
            return None 
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
        
        return choice(neighbors) if neighbors else None
    
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
font = pygame.font.Font(None, 65)

grid_cells = [Cell(col, row) for row in range(rows) for col in range(cols)]
current_cell = grid_cells[0]
stack = []
colors, color = [], 40
mouse_pos = (0, 0)
game_state = 'loading'

def draw_loading_screen():
    text = font.render('Generating maze...', True, pygame.Color('black'))
    sc.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    
def draw_waiting_screen():
    pygame.draw.rect(sc, pygame.Color('black'), (0, 0, WIDTH, HEIGHT))
    pygame.draw.rect(sc, pygame.Color('red'), (WIDTH - TILE, HEIGHT - TILE, TILE, TILE))
    
    text = font.render('Place cursor on the red square', True, pygame.Color('white'))
    sc.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    

while True:
    sc.fill(pygame.Color('#a6d5e2'))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    [cell.draw() for cell in grid_cells]
    [pygame.draw.rect(sc, colors[i], (cell.x * TILE + 2, cell.y * TILE + 2, TILE - 4, TILE - 4), border_radius=8) for i, cell in enumerate(stack)] 

    mouse_pos = pygame.mouse.get_pos()
    
    if game_state == 'loading':
        draw_loading_screen()
        current_cell.visited = True
        current_cell.draw_current_cell()
        
        
        next_cell = current_cell.check_neighbors()
        
        
        
        
        if next_cell:
            next_cell.visited = True
            stack.append(current_cell)
            colors.append((min(color, 255), 0, 103))
            color += 1
            remove_walls(current_cell, next_cell)
            current_cell = next_cell 
        elif stack: 
            current_cell = stack.pop()
        else:
            game_state = 'waiting'
    
    if game_state == 'waiting':
        draw_waiting_screen()
        
        if mouse_pos[0] > (WIDTH - TILE) and mouse_pos[0] < (WIDTH) and mouse_pos[1] > HEIGHT - TILE and mouse_pos[1] < HEIGHT:
            game_state = 'playing'
                
    
        
    pygame.display.flip()
    clock.tick(30)