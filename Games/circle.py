import pygame, sys, math, noise, subprocess, os

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

center_x = circle_x
center_y = circle_y

hover_timer_start = 15
hover_timer = hover_timer_start
hover_time_survived = 0
hover_timer_active = True
cooldown_timer = 0
cooldown_duration = 0.5
font = pygame.font.Font(None, 74)

game_path = "main.py"

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)

    pygame.draw.circle(screen, red, (circle_x, circle_y), circle_radius)

    mouse_x, mouse_y = pygame.mouse.get_pos()

    distance = math.sqrt((mouse_x - circle_x) ** 2 + (mouse_y - circle_y) ** 2)
    
    # Debugging: Check if the distance calculation is working correctly
    print(f"Distance from mouse to circle center: {distance}")

    current_time = pygame.time.get_ticks()
    delta_time = (current_time - last_time) / 1000.0
    last_time = current_time

    # Debugging: Check the time between frames to ensure it’s consistent
    print(f"Delta time: {delta_time}")

    if cooldown_timer > 0:
        cooldown_timer -= delta_time
        cooldown_timer = max(cooldown_timer, 0)
        
        # Debugging: Ensure the cooldown timer is decrementing as expected
        print(f"Cooldown timer: {cooldown_timer}")

    if distance <= circle_radius and cooldown_timer == 0:
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
        
        # Debugging: Check the circle's position and movement values
        print(f"Circle position: ({circle_x}, {circle_y})")
        print(f"Movement X: {move_x}, Movement Y: {move_y}")

        t += delta_time

        if hover_timer_active:
            hover_timer -= delta_time
            if hover_timer <= 0:
                hover_timer_active = False
                hover_timer = 0
                
                # Debugging: Confirm when the hover timer ends
                print("Hover timer ended.")
        else:
            hover_time_survived += delta_time
            
            # Debugging: Track how long the circle has survived after hover timer ends
            print(f"Hover time survived: {hover_time_survived}")

    else:
        if distance > circle_radius and cooldown_timer == 0:
            print("Mouse is outside the circle")
            cooldown_timer = cooldown_duration
            
            # Debugging: Confirm the cooldown started after the mouse left the circle
            print("Cooldown started.")

            if hover_timer <= 0 or hover_time_survived > 0:
                print("Launching the game...")
                if os.name == "nt":
                    subprocess.Popen(["python", "-c", f"import game_opener; game_opener.open_game(r'{game_path}')"], cwd=r"d:\documents\Developer\mini-pygame-collection")
                else:
                    subprocess.Popen(["python3", "-c", f"import game_opener; game_opener.open_game('{game_path}')"], cwd=r"d:\documents\Developer\mini-pygame-collection")
                running = False

            hover_timer = hover_timer_start
            hover_timer_active = True
            hover_time_survived = 0

        circle_x += (center_x - circle_x) * delta_time
        circle_y += (center_y - circle_y) * delta_time
        
        # Debugging: Track the circle's return to center
        print(f"Returning circle to center: ({circle_x}, {circle_y})")

    if circle_x - circle_radius < 0 or circle_x + circle_radius > screen_width:
        angle = 180 - angle
        
        # Debugging: Verify angle adjustment when hitting screen bounds
        print("Circle hit horizontal screen bounds. Adjusting angle.")

    if circle_y - circle_radius < 0 or circle_y + circle_radius > screen_height:
        angle = -angle
        
        # Debugging: Verify angle adjustment when hitting screen bounds
        print("Circle hit vertical screen bounds. Adjusting angle.")

    if hover_timer_active:
        timer_text = font.render(f"{int(hover_timer)}", True, black)
    else:
        timer_text = font.render(f"+{int(hover_time_survived)}", True, black)

    timer_rect = timer_text.get_rect(center=(screen_width // 2, 50))
    screen.blit(timer_text, timer_rect)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()