import pygame, math

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Balance")

class stick:
    def __init__ (self):
        self.length = 350
        self.x = screen_width // 2
        self.y = (screen_height + self.length) // 2 + 50
        self.angle = 0
        self.last_update = 0.0
        self.gravity = 9.8
        self.acceleration = self.gravity / self.length
        self.velocity = 0.0
        
    def update(self):
        time_passed = pygame.time.get_ticks() / 1000
        self.last_update = pygame.time.get_ticks() / 1000 
        self.velocity = self.acceleration * time_passed
        self.angle = 1/2 * self.acceleration *(pygame.time.get_ticks() / 1000) ** 2
        print(pygame.time.get_ticks() / 1000)
        
        
    def draw(self):
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y), (self.x + self.length * math.cos(self.angle), self.y + self.length * math.sin(self.angle)), 5)
        

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