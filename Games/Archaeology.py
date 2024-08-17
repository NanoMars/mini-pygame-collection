import pygame, sys, random, math, subprocess


# Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Archaeology')

game_path = "main.py"

prize_size = 0

dig_site_x = random.randint(0, screen.get_width())
dig_site_y = random.randint(0, screen.get_height())
dig_site_radius = 60

click_count = 0

def draw_triangle(surface, color, center, size):
        height = math.sqrt(3) / 2 * size
        points = [
            (center[0], center[1] - height / 2), 
            (center[0] - size / 2, center[1] + height / 2),
            (center[0] + size / 2, center[1] + height / 2) ]
        pygame.draw.polygon(surface, color, points)

def draw_circle(surface, color, center, radius, opacity):
    temp_surface = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
    pygame.draw.circle(temp_surface, (*color, opacity), (radius, radius), radius)
    surface.blit(temp_surface, (center[0] - radius, center[1] - radius))
    
def draw_prize(surface, color, position, size):
    height = math.sqrt(3) / 2 * size
    
    top_center = (position[0], position[1] - height / 2)
    bottom_left_center = (position[0] - size / 2, position[1] + height / 2)
    bottom_right_center = (position[0] + size / 2, position[1] + height / 2)
    
    draw_triangle(surface, color, top_center, size)
    draw_triangle(surface, color, bottom_left_center, size)
    draw_triangle(surface, color, bottom_right_center, size)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            distance = math.sqrt((mouse_x - dig_site_x) ** 2 + (mouse_y - dig_site_y) ** 2)
            if distance <= dig_site_radius:
                click_count += 1
    
    screen.fill((235, 203, 164))
    
    draw_circle(screen, (56, 33, 4), (dig_site_x, dig_site_y), dig_site_radius, min(click_count * 12.75, 255))

    if click_count * 12.75 >= 255:
        prize_size += 1
        draw_prize(screen, (255, 255, 0), (dig_site_x, dig_site_y), prize_size)
        
        if prize_size > screen.get_width():
            print("You found the treasure!")
            if os.name == "nt":
                subprocess.Popen(["python", "-c", f"import game_opener; game_opener.open_game(r'{game_path}')"], cwd=r"d:\documents\Developer\mini-pygame-collection")
            else:
                subprocess.Popen(["python3", "-c", f"import game_opener; game_opener.open_game('{game_path}')"], cwd=r"d:\documents\Developer\mini-pygame-collection")
            pygame.quit()
            sys.exit()

    pygame.display.flip()

pygame.quit()
sys.exit()