import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Text or Color Game")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 74)

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
texts = ["Red", "Green", "Blue", "Yellow"]

text = random.choice(texts)
text_color = random.choice(colors)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    text_surface = font.render(text, True, text_color)
    screen.blit(text_surface, (350, 250))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()