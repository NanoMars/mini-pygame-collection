import pygame, sys, random, math


# Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Archaeology')

dig_site_x = random.randint(0, screen.get_width())
dig_site_y = random.randint(0, screen.get_height())
dig_site_radius = 60

click_count = 0

def draw_circle(surface, color, center, radius, opacity):
    temp_surface = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
    pygame.draw.circle(temp_surface, (*color, opacity), (radius, radius), radius)
    surface.blit(temp_surface, (center[0] - radius, center[1] - radius))

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
                print(f"Clicked on the dig site! Click count: {click_count}")
    
    screen.fill((235, 203, 164))
    
    draw_circle(screen, (56, 33, 4), (dig_site_x, dig_site_y), dig_site_radius, min(click_count * 12.75, 255))

    pygame.display.flip()

pygame.quit()
sys.exit()