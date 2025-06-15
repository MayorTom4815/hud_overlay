# joystick_mapper.py

import pygame
import json
import evdev
import select
from evdev import InputDevice, ecodes, util
from config import get_button_labels, COLOR_TEXT, SCREEN_WIDTH

JOYSTICK_BINDINGS_PATH = "joystick_bindings.json"

def map_joystick_buttons(screen):
    font = pygame.font.SysFont(None, 32)
    labels = get_button_labels()  # ✅ Solo LP, LK, HP, HK si formato_4

    # Buscar primer joystick disponible
    dev = None
    for path in evdev.list_devices():
        d = InputDevice(path)
        if "joystick" in d.name.lower() or "gamepad" in d.name.lower():
            dev = d
            dev.grab()
            break

    if not dev:
        print("[ERROR] No se encontró joystick.")
        return

    print(f"[INFO] Usando joystick: {dev.name}")

    bindings = {}

    for label in labels:
        prompt = f"Presiona el botón para: {label}"
        waiting = True
        while waiting:
            screen.fill((0, 0, 0))
            draw_centered_text(screen, font, prompt, y=150)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            r, _, _ = select.select([dev], [], [], 0.01)
            if dev in r:
                for event in dev.read():
                    if event.type == ecodes.EV_KEY and event.value == 1:
                        bindings[label] = event.code
                        print(f"[OK] {label} → code {event.code}")
                        waiting = False
                        break

    # Guardar en archivo por formato
    formato = f"formato_{len(get_button_labels())}"

    try:
        with open(JOYSTICK_BINDINGS_PATH, "r") as f:
            all_bindings = json.load(f)
    except:
        all_bindings = {}

    all_bindings[formato] = bindings

    with open(JOYSTICK_BINDINGS_PATH, "w") as f:
        json.dump(all_bindings, f, indent=4)

    print(f"[OK] Mapeo de joystick guardado en '{JOYSTICK_BINDINGS_PATH}'")
    dev.ungrab()

def draw_centered_text(screen, font, text, y):
    surface = font.render(text, True, COLOR_TEXT)
    rect = surface.get_rect(center=(SCREEN_WIDTH // 2, y))
    screen.blit(surface, rect)

