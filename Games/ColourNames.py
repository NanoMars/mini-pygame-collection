import pygame, math, random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Text or Color Game")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 74)

colours = [["Red", (255, 0, 0)], ["Green", (0, 255, 0)], ["Blue", (0, 0, 255)], ["Yellow", (255, 255, 0)]]
texts = ["Red", "Green", "Blue", "Yellow"]

mode = 'text'

score = 5

class coloured_text:
    def __init__(self):
        self.text = random.choice(texts)
        self.colour = random.choice(colours)

    def draw(self, screen):
        text_surface = font.render(self.text, True, self.colour[1])
        screen.blit(text_surface, ((screen.get_width() - text_surface.get_width()) // 2, screen.get_height() // 2))


def draw_mode():
    text = font.render(f"Mode: {mode}", True, pygame.Color('black'))
    screen.blit(text, ((screen.get_width() - text.get_width()) // 2, (screen.get_height() // 2) - 100))
    
def check_correct(input):
    if mode == 'text':
        if input == current_text.text:
            return True
        else:
            return False
    else:
        if input == current_text.colour[0]:
            return True
        else:
            return False
        
def act_score(correct):
    if correct:
        score -= 1
    else:
        score = 5
        countdown = 5

    
countdown = 5

def draw_countdown():
    countdown_text = font.render(str(countdown), True, pygame.Color('black'))
    screen.blit(countdown_text, ((screen.get_width() - countdown_text.get_width()) // 2, (screen.get_height() // 2) + 100))

def update_countdown():
    global countdown
    countdown -= 1

    if countdown <= 0:
        act_score(False)

countdown_timer = pygame.USEREVENT + 1
pygame.time.set_timer(countdown_timer, 1000)

current_text = coloured_text()

def draw_triangle(screen, colour, center, size, angle):
    angle = math.radians(angle)

    half_size = size / 2
    point1 = (
        center[0] + math.cos(angle) * half_size,
        center[1] - math.sin(angle) * half_size
    )
    point2 = (
        center[0] + math.cos(angle + 2 * math.pi / 3) * half_size,
        center[1] - math.sin(angle + 2 * math.pi / 3) * half_size
    )
    point3 = (
        center[0] + math.cos(angle + 4 * math.pi / 3) * half_size,
        center[1] - math.sin(angle + 4 * math.pi / 3) * half_size
    )

    pygame.draw.polygon(screen, colour, [point1, point2, point3])
    
def draw_triangles():
    center = (screen.get_width() - 75, screen.get_height() - 75)
    for i in range (4):
        angle = math.radians((i * 90))
        new_x = center[0] + math.cos(angle) * 40
        new_y = center[1] - math.sin(angle) * 40
        draw_triangle(screen, colours[i][1], (new_x, new_y), 50, i * 90)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print(check_correct("Green"))
            elif event.key == pygame.K_DOWN:
                print(check_correct("Yellow"))
            elif event.key == pygame.K_LEFT:
                print(check_correct("Blue"))
            elif event.key == pygame.K_RIGHT:
                print(check_correct("Red"))
                

    screen.fill((255, 255, 255))
    
    current_text.draw(screen)
    
    draw_mode()
    draw_triangles()
    draw_countdown()

        
        
    for event in pygame.event.get():
        if event.type == countdown_timer:
            update_countdown()
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()