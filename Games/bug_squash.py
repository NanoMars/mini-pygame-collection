import pygame, noise, math, random, subprocess, os

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bug Squash")

game_path = "main.py"

class Blood():
    def __init__(self, position):
        self.position = position
        self.radius = 4
        self.opacity = 175
        self.last_time = pygame.time.get_ticks()
        self.duration = 1000
    def draw(self):
        Blood_surface = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(Blood_surface, (255, 0, 0, int(self.opacity)), (self.radius, self.radius), self.radius)
        screen.blit(Blood_surface, (self.position[0] - self.radius, self.position[1] - self.radius))
    def update(self):
        current_time = pygame.time.get_ticks()
        time_difference = current_time - self.last_time
        self.last_time = current_time
        self.opacity = max(0, self.opacity - 175 * time_difference / self.duration)
        self.radius = max(0, self.radius + 3 * time_difference / self.duration)
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
    
        
bloods = []
bugs = []

for i in range(random.randint(700, 1500)):
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
            removed_bugs = [bug for bug in bugs if math.hypot(bug.position[0] - mouse_pos[0], bug.position[1] - mouse_pos[1]) < 50]
            bugs = [bug for bug in bugs if bug not in removed_bugs]
            for bug in removed_bugs:
                bloods.append(Blood(bug.position))
            if bugs == []:
                parent_dir = os.path.dirname(os.getcwd())

                if os.name == "nt":
                    subprocess.Popen(["python", "-c", f"import game_opener; game_opener.open_game(r'{game_path}')"], cwd=parent_dir)
                else:
                    subprocess.Popen(["python3", "-c", f"import game_opener; game_opener.open_game('{game_path}')"], cwd=parent_dir)
                pygame.quit()
    
    for bug in bugs:
        bug.move()
        bug.draw()

    for blood in bloods:
        blood.draw()
        blood.update()
        print(len(bloods))
        if blood.opacity == 0:
            bloods.remove(blood)
    
    pygame.display.flip()

pygame.quit()