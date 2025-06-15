# main.py

import pygame
import threading
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "libs"))
import config  # Necesario para mutar config.BUTTON_FORMAT
import json
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from button_format_selector import choose_button_format
from input_selector import choose_input_mode
# Preguntar por formato de botones
from keymapper import map_keys
from joystick_mapper import map_joystick_buttons
from input_reader import start_input_listener, input_state
from hud_renderer import draw_hud, load_icons
BINDINGS_PATH = "bindings.json"

def main():
    # Inicializar Pygame
    pygame.init()
    os.environ['SDL_VIDEO_WINDOW_POS'] = "100,100"
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)
    pygame.display.set_caption("Arcade HUD Overlay")
    button_count = choose_button_format(screen)
    config.BUTTON_FORMAT = button_count
    load_icons() # Cargar íconos depués de iniciar la pantalla
    input_mode = choose_input_mode(screen)
    clock = pygame.time.Clock()

    # Selección de modo de entrada
    if input_mode == "teclado":
        try:
            with open(BINDINGS_PATH, "r") as f:
                data = json.load(f)
                formato = f"formato_{button_count}"
                if formato not in data:
                    print(f"[WARN] No hay bindings para {formato}. Se pedirá configuración.")
                    map_keys(screen)
        except Exception as e:
            print(f"[ERROR] bindings.json inválido: {e}")
            map_keys(screen)
    if input_mode == "joystick":
        try:
            with open("joystick_bindings.json", "r") as f:
                all_bindings = json.load(f)
                formato = f"formato_{button_count}"
                if formato not in all_bindings:
                    print(f"[WARN] No hay bindings de joystick para {formato}. Se pedirá configuración.")
                    map_joystick_buttons(screen)
        except Exception as e:
            print(f"[ERROR] joystick_bindings.json inválido o faltante: {e}")
            map_joystick_buttons(screen)

    # Iniciar hilo de lectura de entradas
    threading.Thread(target=start_input_listener, args=(input_mode,), daemon=True).start()

    # Bucle principal
    running = True
    while running:
        screen.fill((0, 0, 0, 0))  # Fondo "transparente"
        draw_hud(screen, input_state)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

