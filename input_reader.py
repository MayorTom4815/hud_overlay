import pygame
import config

def start_input_listener():
    match config.input_type:
        case config.DEVICES.KEYBOARD:
            listen_keyboard()

        # case config.DEVICES.JOYSTICK:
        #     listen_joystick(bindings)


# ---------------- TECLADO ----------------
def listen_keyboard() -> None:
    while True:
        pressed_keys = pygame.key.get_pressed()

        config.joystick_hud.dx = 0
        config.joystick_hud.dy = 0

        if pressed_keys[config.bindings[0][3]]:
            config.joystick_hud.dy -= 1

        elif pressed_keys[config.bindings[1][3]]:
            config.joystick_hud.dy += 1

        elif pressed_keys[config.bindings[2][3]]:
            config.joystick_hud.dx -= 1

        elif pressed_keys[config.bindings[3][3]]:
            config.joystick_hud.dx += 1

        if config.joystick_hud.dx != 0 and config.joystick_hud.dy != 0:
            config.joystick_hud.dx *= 0.7
            config.joystick_hud.dy *= 0.7

        for button in config.button_states.keys():
            state = config.button_states[button]

            if pressed_keys[state["bind"]]:
                state["state"] = True

            else:
                state["state"] = False


# ---------------- JOYSTICK ----------------
# def listen_joystick(bindings:list[tuple]):
#     dev = None
#     for path in evdev.list_devices():
#         d = InputDevice(path)
#         if any(name in d.name.lower() for name in DEVICE_NAME_FILTER):
#             dev = d
#             break

#     if not dev:
#         print("[ERROR] No se detectó joystick compatible.")
#         return

#     print(f"[INFO] Leyendo entradas desde: {dev.name}")

#     for event in dev.read_loop():
#         if event.type == ecodes.EV_ABS:
#             absevent = categorize(event)
#             if event.code == ecodes.ABS_X:
#                 input_state["stick"][0] = absevent.event.value / 128.0 - 1
#             elif event.code == ecodes.ABS_Y:
#                 input_state["stick"][1] = absevent.event.value / 128.0 - 1

#         elif event.type == ecodes.EV_KEY:
#             for i, label in enumerate(get_button_labels()):
#                 if event.code == bindings.get(label):
#                     input_state["buttons"][i] = event.value == 1
