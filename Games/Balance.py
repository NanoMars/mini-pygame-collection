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
        self.angle = 2
        
        
    def update(self):
        time_passed = pygame.time.get_ticks() / 1000 
        self.angle *= time_passed
        self.angle = min(max(self.angle, -90), 90)
        
    def draw(self):
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y), (self.x + self.length * math.cos(math.radians(self.angle - 90)), self.y + self.length * math.sin(math.radians(self.angle - 90))), 5)
        

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