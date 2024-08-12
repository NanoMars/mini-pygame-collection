import pygame, sys, random, os
from pygame.locals import *
pygame.init()
 
# Colours
BACKGROUND = (255, 255, 255)
 
# Game Setup
FPS = 60
fps_clock = pygame.time.Clock()

pygame.display.set_caption('My Game!')
font = pygame.font.Font(None, 36)



class Label:
    def __init__ (self, filename):
        self.color = (0, 0, 0) 
        
        if filename.endswith(".py"):
            modified_filename = filename[:-3]
        self.text = modified_filename
        self.rendered_text = font.render(self.text, True, self.color)
        
    def draw(self, screen, position):
        screen.blit(self.rendered_text, position)

max_width = 0
games_folder = 'Games'
games_list = []
labels = []

if not os.path.exists(games_folder): # make the games folder if it doesn't exist
  os.makedirs(games_folder)
  
for filename in os.listdir(games_folder): # get all the games in the games folder
    games_list.append(filename)
    labels.append(Label(filename))
    
    if filename.endswith(".py"):
        modified_filename = filename[:-3]
    
    rendered_text = font.render(modified_filename, True, (0, 0, 0))
    text_width = rendered_text.get_width()
    
    # Compare widths to find the longest
    if text_width > max_width:
        max_width = text_width
    
TEXT_SPACING = 37

SCREEN_WIDTH = max_width + 20
SCREEN_HEIGHT = ((len(labels) - 1) * TEXT_SPACING)
 
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

list_velocity = 20
list_position = 0
 
# The main function that controls the game  
  # The main game loop
running = True
while running :
    # Get inputs
    for event in pygame.event.get() :
        if event.type == QUIT :
            pygame.quit()
            sys.exit()

    # Processing
    # This section will be built out later

    # Render elements of the game
    SCREEN.fill(BACKGROUND)

    list_position += list_velocity
    list_velocity = list_velocity * 0.995

    for label in labels:
        label_y_pos = (((labels.index(label) * TEXT_SPACING) + list_position) % (SCREEN_HEIGHT + 37)) - 37
        if label_y_pos > SCREEN_HEIGHT:
            # move this label to the front of the list
            print("label off screen")
        label.draw(SCREEN, (10, label_y_pos))

    pygame.display.update()
    fps_clock.tick(FPS)
