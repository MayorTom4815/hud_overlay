# input_selector.py

import pygame
from config import COLOR_TEXT, SCREEN_WIDTH, SCREEN_HEIGHT

def choose_input_mode(screen):
    font = pygame.font.SysFont(None, 28)
    prompt = "Selecciona el modo de entrada:"
    option1 = "Presiona [T] para TECLADO"
    option2 = "Presiona [J] para JOYSTICK"

    choosing = True
    while choosing:
        screen.fill((0, 0, 0))
        draw_centered_text(screen, font, prompt, y=25)
        draw_centered_text(screen, font, option1, y=80)
        draw_centered_text(screen, font, option2, y=120)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    return "teclado"
                elif event.key == pygame.K_j:
                    return "joystick"

def draw_centered_text(screen, font, text, y):
    surface = font.render(text, True, COLOR_TEXT)
    rect = surface.get_rect(center=(SCREEN_WIDTH // 2, y))
    screen.blit(surface, rect)

