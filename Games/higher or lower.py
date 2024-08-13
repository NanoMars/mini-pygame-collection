import pygame
import sys
import random

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("higher or lower")

white = (255, 255, 255)
black = (0, 0, 0)

font = pygame.font.SysFont(None, 55)
small_font = pygame.font.SysFont(None, 35)

lower_bound = 1
upper_bound = 100
guess = (lower_bound + upper_bound) // 2

running = True
game_over = False
tries = 0
changed_guess = False
out_of_bounds = None
intro_screen = True

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)


while running:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            
            if intro_screen:
                
                if event.key == pygame.K_SPACE:
                    intro_screen = False

            elif not game_over:
                
                if event.key == pygame.K_UP:
                    
                    if guess >= upper_bound:
                        changed_guess = True
                        game_over = True
                        
                    elif guess >= 100:
                        out_of_bounds = 'high'
                        game_over = True
                        
                    else:
                        lower_bound = guess + 1
                        tries += 1
                        
                    # print(f"Lower bound updated to: {lower_bound}")
                    # print(f"New guess: {guess}")

                if event.key == pygame.K_DOWN:
                    
                    if guess <= lower_bound:
                        changed_guess = True
                        game_over = True
                        
                    elif guess <= 1:
                        out_of_bounds = 'low'
                        game_over = True
                        
                    else:
                        upper_bound = guess - 1
                        tries += 1
                        
                    # print(f"Upper bound updated to: {upper_bound}")
                    # print(f"New guess: {guess}")

                if event.key == pygame.K_SPACE:
                    game_over = True
            
            guess = (lower_bound + upper_bound) // 2


    screen.fill(white)

    if intro_screen:
        draw_text(f"Think of a whole number between {lower_bound} & {upper_bound}", font, black, screen, screen_width // 2, screen_height // 2 - 30)
        draw_text("Once you have it, press Space", small_font, black, screen, screen_width // 2, screen_height // 2 + 30)
        
    elif game_over:
        
        if changed_guess:
            draw_text("Did you change your number?", font, black, screen, screen_width//2, screen_height//2)
            
        elif out_of_bounds == 'high':
            draw_text(f"You can't go higher than {upper_bound}!", font, black, screen, screen_width//2, screen_height//2)
            
        elif out_of_bounds == 'low':
            draw_text(f"You can't go lower than {lower_bound}!", font, black, screen, screen_width//2, screen_height//2)
            
        else:
            draw_text(f"Guessed it in {tries} tries!", font, black, screen, screen_width//2, screen_height//2)
            
    else:
        
        draw_text(f"Is it {guess}?", font, black, screen, screen_width//2, screen_height//2)
        draw_text("up = Higher, down = Lower, Space = Correct", small_font, black, screen, screen_width//2, screen_height//2 + 50)

    pygame.display.flip()

pygame.quit()
sys.exit()