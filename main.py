import pyray as rl
from pynput.keyboard import Listener
from pyray import ConfigFlags, Vector2

from configs import *

# * VARS
input_handler = InputKeyboardHandler()
config: Configs = Configs()
device: Device = Device()
current_type = False
running = True


# * INIT
def init_overlay() -> None:
    global device

    for type in BUTTON_TYPE:
        btn = Button(
            config.data["buttons_position"][type.value],
            config.data["keys"]["buttons"][type.value],
            type,
        )

        device.buttons.append(btn)


# * UPDATE
def update_overlay() -> None:
    global device, current_type

    if rl.is_key_pressed(config.data["keys"]["change_cast"]):
        device.type = DEVICE_TYPE.KEYBOARD if current_type else DEVICE_TYPE.JOYSTICK
        current_type = not current_type

    match device.type:
        case DEVICE_TYPE.JOYSTICK:
            device.joystick = rl.Vector2(
                rl.get_gamepad_axis_movement(
                    config.data["default_gamepad"],
                    rl.GamepadAxis.GAMEPAD_AXIS_LEFT_X,
                ),
                rl.get_gamepad_axis_movement(
                    config.data["default_gamepad"],
                    rl.GamepadAxis.GAMEPAD_AXIS_LEFT_Y,
                ),
            )

        case DEVICE_TYPE.KEYBOARD:
            device.joystick = Vector2()
            if {config.data["keys"]["directions"]["up"]} <= input_handler.last_key:
                device.joystick.y = -1
            if {config.data["keys"]["directions"]["down"]} <= input_handler.last_key:
                device.joystick.y = 1
            if {config.data["keys"]["directions"]["left"]} <= input_handler.last_key:
                device.joystick.x = -1
            if {config.data["keys"]["directions"]["right"]} <= input_handler.last_key:
                device.joystick.x = 1

    for btn in device.buttons:
        if {btn.keys[current_type]} <= input_handler.last_key:
            btn.active = True
            continue

        btn.active = False


# * DRAW
def draw_overlay() -> None:
    global running
    end_v = rl.Vector2(
        config.data["gamepad_position"][0]
        + device.joystick.x * config.data["gamepad_radius"],
        config.data["gamepad_position"][1]
        + device.joystick.y * config.data["gamepad_radius"],
    )

    rl.begin_drawing()
    rl.clear_background(rl.BLANK)

    rl.draw_text(f"Casting: {device.type.value}", 0, 0, 12, rl.WHITE)
    if rl.gui_button((config.data["window_size"][0] - 25, 0, 25, 25), "X"):
        running = False

    # ? Drawing jostick base
    rl.draw_circle_lines_v(
        config.data["gamepad_position"],
        config.data["gamepad_radius"],
        rl.WHITE,
    )
    rl.draw_circle_v(
        end_v,
        config.data["gamepad_radius"] // 2,
        rl.WHITE,
    )

    # ? Drawing buttons
    for btn in device.buttons:
        mesure_label = rl.measure_text(btn.type.value, 18)

        rl.draw_circle_lines_v(btn.position, 25, rl.WHITE)
        if btn.active:
            rl.draw_circle_v(
                btn.position,
                20,
                rl.WHITE,
            )

        rl.draw_text(
            btn.type.value,
            int(btn.position[0]) - mesure_label // 2,
            int(btn.position[1]) - mesure_label // 2,
            18,
            (rl.BLACK if btn.active else rl.WHITE),
        )

    rl.end_drawing()


if __name__ == "__main__":
    rl.set_config_flags(
        ConfigFlags.FLAG_WINDOW_TRANSPARENT
        | ConfigFlags.FLAG_WINDOW_UNDECORATED
        | ConfigFlags.FLAG_WINDOW_TOPMOST
    )
    rl.init_window(
        config.data["window_size"][0],
        config.data["window_size"][1],
        "PyHUD Overay",
    )
    rl.set_target_fps(60)

    rl.set_window_position(
        rl.get_monitor_width(0) - config.data["window_size"][0],
        rl.get_monitor_height(0) - config.data["window_size"][1],
    )

    keyboard_listener: Listener = Listener(
        on_press=input_handler.press_key,
        on_release=input_handler.release_key,
    )

    init_overlay()
    keyboard_listener.start()
    while running:
        update_overlay()
        draw_overlay()

    keyboard_listener.stop()
    rl.close_window()
