# keymapper.py

import pygame
import json
import os
from config import (
    BINDINGS_PATH,
    COLOR_TEXT,
    SCREEN_WIDTH,
    get_button_labels
)

DIRECTIONS = ["Arriba", "Abajo", "Izquierda", "Derecha"]

def map_keys(screen):
    font = pygame.font.SysFont(None, 28)
    bindings = {}

    # Avisar si se va a reconfigurar
    formato = f"formato_{len(get_button_labels())}"
    print(f"[INFO] Configurando bindings para: {formato}")

    # Capturar direcciones y botones
    for name in DIRECTIONS + get_button_labels():
        key = wait_for_keypress(screen, font, f"Presiona una tecla para: {name}")
        bindings[name] = key

    formato = f"formato_{len(get_button_labels())}"

    if os.path.exists(BINDINGS_PATH):
        with open(BINDINGS_PATH, "r") as f:
            all_bindings = json.load(f)
    else:
        all_bindings = {}

    all_bindings[formato] = bindings

    with open(BINDINGS_PATH, "w") as f:
        json.dump(all_bindings, f, indent=4)

def wait_for_keypress(screen, font, message):
    waiting = True
    while waiting:
        screen.fill((0, 0, 0))
        draw_centered_text(screen, font, message, y=75)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                return event.key

def draw_centered_text(screen, font, text, y):
    surface = font.render(text, True, COLOR_TEXT)
    rect = surface.get_rect(center=(SCREEN_WIDTH // 2, y))
    screen.blit(surface, rect)

