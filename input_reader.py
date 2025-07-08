import pygame
import config


def start_input_listener():
    match config.input_type:
        case config.DEVICES.KEYBOARD:
            config.button_states = {
                config.bindings[i][2]: {"bind": config.bindings[i][3], "state": False}
                for i in range(4, config.bindings.__len__())
            }

            listen_keyboard()

        case config.DEVICES.JOYSTICK:
            config.button_states = {
                config.bindings[i][2]: {"bind": config.bindings[i][3], "state": False}
                for i in range(config.bindings.__len__())
            }

            listen_joystick()


# * TECLADO
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


# * JOYSTICK
def listen_joystick() -> None:
    while True:
        control = config.JOYSTICKS[0]

        pressed_keys = [control.get_button(i) for i in range(control.get_numbuttons())]

        config.joystick_hud.dx = control.get_axis(0)
        config.joystick_hud.dy = control.get_axis(1)

        for button in config.button_states.keys():
            state = config.button_states[button]

            if pressed_keys[int(state["bind"])]:
                state["state"] = True

            else:
                state["state"] = False
