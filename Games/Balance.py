import pygame, math, random, subprocess

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Balance")

stick_spawned = False

countdown = 15

font = pygame.font.Font(None, 74)

game_path = "main.py"

class stick:
    def __init__ (self):
        self.length = 350
        self.x = pygame.mouse.get_pos()[0]
        self.y = (screen_height + self.length) // 2 + 50
        self.angle = random.choice([-math.pi / 1440, math.pi / 1440])
        self.last_update = 0.0
        self.last_mouse_update = pygame.mouse.get_pos()[0]
        self.acceleration = 0
        self.velocity = 0.0
        self.top_x = self.x
    def update(self):
        global stick_spawned, countdown
        time_passed = pygame.time.get_ticks() / 1000 - self.last_update
        self.angle = self.velocity  * time_passed + self.angle
        self.x = min(max(pygame.mouse.get_pos()[0], 0), screen_width)
        self.last_update = pygame.time.get_ticks() / 1000 
        
        
        #mouse_x = pygame.mouse.get_pos()[0] - self.last_mouse_update
        #self.last_mouse_update = mouse_x
        
        new_angle = (math.pi / 2 - math.acos(min(max((self.top_x - self.x) / self.length, -1), 1)) )
        self.angle = new_angle * 0.5 + self.angle * 0.5

        self.acceleration = (self.angle / (math.pi / 2)) * 10
        
        self.velocity += (self.acceleration) * time_passed 

        self.angle = max(-math.pi / 2, min(self.angle, math.pi / 2))
        self.top_x= self.x + self.length * math.cos(self.angle - math.pi / 2)
        
        if self.angle >= math.pi / 2 or self.angle <= -math.pi / 2:
            stick_spawned = False
            countdown = 15
        
    def draw(self):
        
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y), (self.x + self.length * math.cos(self.angle -math.pi / 2), self.y + self.length * math.sin(self.angle -math.pi / 2)), 5)
        



def update_countdown():
    global countdown
    countdown -= 1
    print(countdown)

    if countdown <= 0:
        subprocess.Popen(["python3", "-c", f"import game_opener; game_opener.open_game('{game_path}')"])
        pygame.quit()
        
        
def draw_countdown():
    countdown_text = font.render(str(countdown), True, pygame.Color('black'))
    screen.blit(countdown_text, ((screen.get_width() - countdown_text.get_width()) // 2, (screen.get_height() // 10) ))
        

countdown_timer = pygame.USEREVENT + 1
pygame.time.set_timer(countdown_timer, 1000)


button_rect = pygame.Rect((screen_width + 25) // 2, (screen_height - 350) // 2 + 50, 25, 350)

# Game loop
running = True
while running:
    screen.fill((255, 255, 255)) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos) and not stick_spawned:
                game_stick = stick()
                stick_spawned = True
        elif event.type == countdown_timer and stick_spawned:
            update_countdown()
    
    if not stick_spawned:
        pygame.draw.rect(screen, (0, 255, 0), button_rect)
    else:
        game_stick.update()
        game_stick.draw()
        draw_countdown()
        
    pygame.display.flip()

pygame.quit()