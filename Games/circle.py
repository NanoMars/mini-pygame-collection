import pygame
import sys
import math
import noise

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Circle")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

circle_x = screen_width // 2
circle_y = screen_height // 2
circle_radius = 35

angle = 45
base_speed = 100

clock = pygame.time.Clock()
last_time = pygame.time.get_ticks()

scale = 1.5
t = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)

    pygame.draw.circle(screen, red, (circle_x, circle_y), circle_radius)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    distance = math.sqrt((mouse_x - circle_x) ** 2 + (mouse_y - circle_y) ** 2)
    
    print(f"Distance from mouse to circle center: {distance}")

    current_time = pygame.time.get_ticks()
    delta_time = (current_time - last_time) / 1000.0
    last_time = current_time

    print(f"Delta time: {delta_time}")

    if distance <= circle_radius:
        print("Mouse is inside the circle")

        speed_factor = 1 - ((distance / circle_radius) / 2)
        speed = base_speed * speed_factor

        perlin_value = noise.pnoise1(t * scale)
        angle += perlin_value * 8
        radians = math.radians(angle)

        move_x = math.cos(radians) * speed * delta_time
        move_y = math.sin(radians) * speed * delta_time

        circle_x += move_x
        circle_y += move_y
        
        print(f"Circle position: ({circle_x}, {circle_y})")
        print(f"Movement X: {move_x}, Movement Y: {move_y}")

        t += delta_time
    else:
        circle_x += (screen_width // 2 - circle_x) * delta_time
        circle_y += (screen_height // 2 - circle_y) * delta_time
        
        print(f"Returning circle to center: ({circle_x}, {circle_y})")

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()