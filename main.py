import pygame, sys, random, os
from pygame.locals import *
pygame.init()

# Colours
BACKGROUND = (255, 255, 255)

FONT_SIZE = 36

# Game Setup
FPS = 60
fps_clock = pygame.time.Clock()

pygame.display.set_caption('My Game!')
font = pygame.font.Font(None, FONT_SIZE)


class Label:
    def __init__(self, filename):
        self.color = (0, 0, 0)
        if filename.endswith(".py"):
            self.text = filename[:-3]
        else:
            self.text = filename
        self.rendered_text = font.render(self.text, True, self.color)

    def draw(self, screen, position):
        screen.blit(self.rendered_text, position)


max_width = 0
games_folder = 'Games'
games_list = []
labels = []

if not os.path.exists(games_folder):  # make the games folder if it doesn't exist
    os.makedirs(games_folder)

for filename in os.listdir(games_folder):  # get all the games in the games folder
    games_list.append(filename)
    labels.append(Label(filename))

    if filename.endswith(".py"):
        modified_filename = filename[:-3]
    else:
        modified_filename = filename

    rendered_text = font.render(modified_filename, True, (0, 0, 0))
    text_width = rendered_text.get_width()

    # Compare widths to find the longest
    if text_width > max_width:
        max_width = text_width

SCREEN_WIDTH = max_width + 20
SCREEN_HEIGHT = ((len(labels) - 1) * FONT_SIZE)

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

list_velocity = 7.5
list_position = random.random() * SCREEN_HEIGHT

RECT_HEIGHT = FONT_SIZE
RECT_WIDTH = SCREEN_WIDTH
RECT_COLOR = (255, 0, 255)

rect_x = 0
rect_y = (SCREEN_HEIGHT - RECT_HEIGHT) // 2

centered_rect = pygame.Rect(rect_x, rect_y, RECT_WIDTH, RECT_HEIGHT)

running = True
while running:
    # Get inputs
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Render elements of the game
    SCREEN.fill(BACKGROUND)

    list_position += list_velocity
    list_velocity = list_velocity * 0.996

    pygame.draw.rect(SCREEN, RECT_COLOR, centered_rect)

    min_distance = float('inf')
    closest_label = None

    for index, label in enumerate(labels):
        label_y_pos = (((index * FONT_SIZE) + list_position) % (SCREEN_HEIGHT + FONT_SIZE)) - FONT_SIZE
        label.draw(SCREEN, (10, label_y_pos))

        center_y = (SCREEN_HEIGHT / 2)
        distance = abs(label_y_pos - center_y)

        if distance < min_distance:
            min_distance = distance
            closest_label = label

    if list_velocity < 0.1:
        if closest_label is not None:
            print(f"The closest label to the center is: {closest_label.text}")

    pygame.display.update()
    fps_clock.tick(FPS)