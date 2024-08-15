import pygame, noise, math

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Pygame Template")



class bug():
    def __init__(self, position):
        print("Bug created")
        self.direction = 0
        self.position = position
        self.last_time = pygame.time.get_ticks()
    def move(self):
        print("Bug moved")
        current_time = pygame.time.get_ticks()
        time_difference = current_time - self.last_time
        self.last_time = current_time

        rotation_speed = 2
        perlin_value = noise.pnoise2(self.position[0] * 0.1, self.position[1] * 0.1)  # Use pnoise2 for 2D noise
        self.direction += rotation_speed * time_difference * perlin_value
        speed = 0.05
        self.position = (
            self.position[0] + speed * time_difference * math.cos(math.radians(self.direction)),
            self.position[1] + speed * time_difference * math.sin(math.radians(self.direction))
        )
    def draw(self):
        x = self.position[0]
        y = self.position[1] 
        length = 5  
        angle = math.radians(self.direction) 

        end_x = x + length * math.cos(angle)
        end_y = y + length * math.sin(angle)

        pygame.draw.line(screen, (0, 0, 0), (x, y), (end_x, end_y), 1)
        

bugs = []

bugs.append(bug((400, 300)))

# Game loop
running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    

    bugs[0].move()
    bugs[0].draw()
    pygame.display.flip()

pygame.quit()