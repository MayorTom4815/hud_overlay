# button_format_selector.py

import pygame
from config import COLOR_TEXT, SCREEN_WIDTH

def choose_button_format(screen):
    font = pygame.font.SysFont(None, 30)
    prompt = "Selecciona el formato de botones:"
    option1 = "Presiona [4] para 4 botones"
    option2 = "Presiona [6] para 6 botones"

    choosing = True
    while choosing:
        screen.fill((0, 0, 0))
        draw_centered_text(screen, font, prompt, y=25)
        draw_centered_text(screen, font, option1, y=80)
        draw_centered_text(screen, font, option2, y=125)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_4:
                    return 4
                elif event.key == pygame.K_6:
                    return 6

def draw_centered_text(screen, font, text, y):
    surface = font.render(text, True, COLOR_TEXT)
    rect = surface.get_rect(center=(SCREEN_WIDTH // 2, y))
    screen.blit(surface, rect)

