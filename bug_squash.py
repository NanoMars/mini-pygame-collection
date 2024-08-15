import pygame, noise, math, random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bug Squash")



class bug():
    def __init__(self, position):
        self.direction = random.randrange(0, 360)
        self.position = position
        self.last_time = pygame.time.get_ticks()
        self.speed = random.uniform(0.05, 0.5)
    def move(self):
        current_time = pygame.time.get_ticks()
        time_difference = current_time - self.last_time
        self.last_time = current_time

        rotation_speed = 2
        perlin_value = noise.pnoise2(self.position[0] * 0.1, self.position[1] * 0.1) 
        self.direction += rotation_speed * time_difference * perlin_value
        self.position = (
            self.position[0] + self.speed * time_difference * math.cos(math.radians(self.direction)),
            self.position[1] + self.speed * time_difference * math.sin(math.radians(self.direction))
        )
        
        if self.position[0] <= 0:
            self.direction = random.uniform(-90, 90)
        elif self.position[0] >= screen.get_width():
            self.direction = random.uniform(90, 360)
        elif self.position[1] <= 0:
            self.direction = random.uniform(0, 180)
        elif self.position[1] >= screen.get_height():
            self.direction = random.uniform(180, 360)

        
        
    def draw(self):
        x = self.position[0]
        y = self.position[1] 
        length = 5  
        angle = math.radians(self.direction) 

        end_x = x + length * math.cos(angle)
        end_y = y + length * math.sin(angle)

        pygame.draw.line(screen, (0, 0, 0), (x, y), (end_x, end_y), 1)
        

bugs = []

for i in range(random.randint(100, 500)):
    bugs.append(bug((random.randrange(0, screen.get_width()), random.randrange(0, screen.get_height()))))

# Game loop
running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            bugs = [bug for bug in bugs if math.hypot(bug.position[0] - mouse_pos[0], bug.position[1] - mouse_pos[1]) >= 50]
            print(len(bugs))
    
    for bug in bugs:
        bug.move()
        bug.draw()

    pygame.display.flip()

pygame.quit()