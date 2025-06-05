# input_reader.py

import pygame
import json
import time
import evdev
from evdev import InputDevice, categorize, ecodes

from config import (
    BINDINGS_PATH, DEVICE_NAME_FILTER, get_button_labels
)

JOYSTICK_BINDINGS_PATH = "joystick_bindings.json"

# Estado compartido leído por el HUD
input_state = {
    "stick": [0, 0],  # dx, dy
    "buttons": [False] * len(get_button_labels())
}

bindings = {}

def start_input_listener(mode):
    global bindings

    if mode == "teclado":
        with open(BINDINGS_PATH, "r") as f:
            bindings_all = json.load(f)
            formato = f"formato_{len(get_button_labels())}"
            bindings = bindings_all[formato]
        listen_keyboard()
    elif mode == "joystick":
        with open(JOYSTICK_BINDINGS_PATH, "r") as f:
            all_bindings = json.load(f)
            formato = f"formato_{len(get_button_labels())}"
            bindings = all_bindings[formato]
        listen_joystick(bindings)

# ---------------- TECLADO ----------------
def listen_keyboard():
    while True:
        keys = pygame.key.get_pressed()

        dx = dy = 0
        if keys[bindings["Izquierda"]]:
            dx -= 1
        if keys[bindings["Derecha"]]:
            dx += 1
        if keys[bindings["Arriba"]]:
            dy -= 1
        if keys[bindings["Abajo"]]:
            dy += 1

        if dx != 0 and dy != 0:
            dx *= 0.7
            dy *= 0.7

        input_state["stick"] = [dx, dy]

        for i, name in enumerate(get_button_labels()):
            input_state["buttons"][i] = keys[bindings[name]]

        time.sleep(0.01)

# ---------------- JOYSTICK ----------------
def listen_joystick(bindings):
    dev = None
    for path in evdev.list_devices():
        d = InputDevice(path)
        if any(name in d.name.lower() for name in DEVICE_NAME_FILTER):
            dev = d
            break

    if not dev:
        print("[ERROR] No se detectó joystick compatible.")
        return

    print(f"[INFO] Leyendo entradas desde: {dev.name}")

    for event in dev.read_loop():
        if event.type == ecodes.EV_ABS:
            absevent = categorize(event)
            if event.code == ecodes.ABS_X:
                input_state["stick"][0] = absevent.event.value / 128.0 - 1
            elif event.code == ecodes.ABS_Y:
                input_state["stick"][1] = absevent.event.value / 128.0 - 1

        elif event.type == ecodes.EV_KEY:
            for i, label in enumerate(get_button_labels()):
                if event.code == bindings.get(label):
                    input_state["buttons"][i] = event.value == 1

