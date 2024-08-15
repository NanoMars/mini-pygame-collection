import pygame, noise, math

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Pygame Template")

class bug():
    def __init__(self, position):
        print("Bug created")
        self.direction = 0
        self.position = position
    def move(self):
        print("Bug moved")
        self.direction += 1
    def draw(self):
        x = self.position[0]
        y = self.position[1] 
        length = 5  
        angle = math.radians(self.direction) 

        end_x = x + length * math.cos(angle)
        end_y = y + length * math.sin(angle)

        pygame.draw.line(screen, (0, 0, 0), (x, y), (end_x, end_y), 1)
# Game loop
running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.flip()

pygame.quit()