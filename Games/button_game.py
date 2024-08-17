import pygame, sys, subprocess, os


pygame.init()

game_path = "main.py"

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Button game")

# Set up the game clock
clock = pygame.time.Clock()

# Define colors (RGB)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
width = 200

def draw_button (height):
    button_angle = 80
    x = (screen_width - width) // 2
    y = screen_height / 2 - height + 65
    pygame.draw.ellipse(screen, red, (x, screen_height / 2 + 65 - (button_angle / 2), width, button_angle))
    pygame.draw.rect(screen, red, (x, y, width, height))
    pygame.draw.ellipse(screen, (255,75,75), (x, y + -button_angle / 2, width, button_angle))
    
    
cursor_pos = pygame.mouse.get_pos()
default_button_height = 100
button_height = default_button_height
clicks_to_go = 100
button_clicked = False

font = pygame.font.SysFont(None, 72)
    
def calculate_clicked():
    global button_height, clicks_to_go, button_clicked
    x = (screen_width - width) // 2
    y = screen_height / 2 - default_button_height + 65
    new_button_height = max(min(default_button_height - (cursor_pos[1] - y), default_button_height), 5)
    
    if cursor_pos[0] > x and cursor_pos[0] < x + width:
        button_height = new_button_height
        
    if new_button_height == 100:
        button_clicked = False
    if new_button_height <= 10 and button_clicked == False:
        button_clicked = True
        clicks_to_go -= 1

    
    




# Main game loop
running = True
while running:
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    cursor_pos = pygame.mouse.get_pos()

    y = screen_height / 2 - default_button_height + 65
    draw_button(button_height)
    calculate_clicked()
    
    # Move the code inside the main game loop
    clicks_text = font.render(f"{clicks_to_go}", True, black)
    screen.blit(clicks_text, (screen_width // 2 - clicks_text.get_width() // 2, 20))
    
    if clicks_to_go == 0:
        running = False
        if os.name == "nt":
            subprocess.Popen(["python", "-c", f"import game_opener; game_opener.open_game(r'{game_path}')"], cwd=r"d:\documents\Developer\mini-pygame-collection")
        else:
            subprocess.Popen(["python3", "-c", f"import game_opener; game_opener.open_game('{game_path}')"], cwd=r"d:\documents\Developer\mini-pygame-collection")
        
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
sys.exit()