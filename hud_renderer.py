# hud_renderer.py

import pygame
import os

from config import (
    JOYSTICK_CENTER, JOYSTICK_RADIUS, JOYSTICK_STICK_LENGTH,
    BUTTON_RADIUS, get_icon_paths, get_button_positions,
    COLOR_STICK, COLOR_STICK_KNOB, COLOR_BUTTON_ACTIVE, COLOR_BUTTON_INACTIVE
)

# Carga de íconos al iniciar
icons = []

def load_icons():
    global icons
    icons = []
    for path in get_icon_paths():
        if os.path.exists(path):
            image = pygame.image.load(path).convert_alpha()
            image = pygame.transform.scale(image, (BUTTON_RADIUS * 2, BUTTON_RADIUS * 2))
            icons.append(image)
        else:
            print(f"[WARN] Ícono no encontrado: {path}")
            icons.append(None)

def draw_hud(screen, state):
    draw_stick(screen, state["stick"])
    draw_buttons(screen, state["buttons"])

def draw_stick(screen, vec):
    center_x, center_y = JOYSTICK_CENTER
    base_radius = JOYSTICK_RADIUS
    stick_length = JOYSTICK_STICK_LENGTH

    dx = vec[0]
    dy = vec[1]

    # Normalizar diagonal
    if dx != 0 and dy != 0:
        dx *= 1
        dy *= 1

    end_x = int(center_x + dx * stick_length)
    end_y = int(center_y + dy * stick_length)

    # Base
    pygame.draw.circle(screen, (100, 100, 100), (center_x, center_y), base_radius)  # Gris oscuro

    # Palanca
    pygame.draw.line(screen, (0, 0, 0), (center_x, center_y), (end_x, end_y), 6)  # Negra
    pygame.draw.circle(screen, (180, 180, 180), (end_x, end_y), 12)  # Gris claro

def draw_buttons(screen, button_states):
    positions = get_button_positions()
    for i, pos in enumerate(positions):
        icon = icons[i]
        pressed = button_states[i]

        if icon:
            rect = icon.get_rect(center=pos)
            screen.blit(icon, rect)
            if pressed:
                pygame.draw.circle(screen, COLOR_BUTTON_ACTIVE, pos, BUTTON_RADIUS, 3)
        else:
            color = COLOR_BUTTON_ACTIVE if pressed else COLOR_BUTTON_INACTIVE
            pygame.draw.circle(screen, color, pos, BUTTON_RADIUS)

