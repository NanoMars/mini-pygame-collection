import pygame, math

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Balance")

class stick:
    def __init__ (self):
        self.length = 350
        self.x = pygame.mouse.get_pos()[0]
        self.y = (screen_height + self.length) // 2 + 50
        self.angle = 0.01
        self.last_update = 0.0
        self.last_mouse_update = pygame.mouse.get_pos()[0]
        self.acceleration = 0
        self.velocity = 0.0
        
    def update(self):
        time_passed = pygame.time.get_ticks() / 1000 - self.last_update
        self.last_update = pygame.time.get_ticks() / 1000 
        
        mouse_x = pygame.mouse.get_pos()[0] - self.last_mouse_update
        self.last_mouse_update = mouse_x
        
        self.acceleration = (self.angle / (math.pi / 2))
        
        self.velocity += self.acceleration * time_passed 
        
        self.angle += (self.velocity - mouse_x / 150) * time_passed
        self.angle = max(-math.pi / 2, min(self.angle, math.pi / 2))
        
        
        


        
        
    def draw(self):
        self.x = pygame.mouse.get_pos()[0]
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y), (self.x + self.length * math.cos(self.angle -math.pi / 2), self.y + self.length * math.sin(self.angle -math.pi / 2)), 5)
        

game_stick = stick()

# Game loop
running = True
while running:
    screen.fill((255, 255, 255)) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    game_stick.update()
    game_stick.draw()
    pygame.display.flip()

pygame.quit()