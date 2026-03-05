from pynput.keyboard import Listener
from tomllib import load
from typing import Any

import pyray as rl
from pyray import ConfigFlags, Vector2

from configs.dataclasses import Button, Device
from configs.enums import BUTTONS, DEVICE_TYPE
from configs.const import (
    BUTTONS_POSITION,
    DEFAULT_CONFIG,
    PATH_CONFIG,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
)

# * ==================
# *        VARS
# * ==================
config_data: dict[str, Any] = {}
device: Device = Device()
current_type = False
last_key = set()
running = True

def get_button(value: str) -> BUTTONS:
    for i in BUTTONS:
        if i.value == value:
            return i

    raise ValueError(f"{value} not is a member of BUTTONS")

def key_to_str(key) -> str:
    try:
        return key.char.lower()

    except AttributeError:
        return str(key).replace("key.", "").lower()

def press_key(key) -> None:
    global last_key
    last_key.add(key_to_str(key))

def release_key(key) -> None:
    global last_key
    last_key.discard(key_to_str(key))

# * INIT
def init_overlay() -> None:
    global device, config_data, current_style

    if not PATH_CONFIG.exists():
        DEFAULT_CONFIG.copy(PATH_CONFIG)

    with open(str(DEFAULT_CONFIG), "rb") as file:
        config_data = load(file)
        assert config_data.__len__() != 0, "Error while try to parse the config file"

    device = Device(
        type=(
            DEVICE_TYPE.JOYSTICK
            if rl.is_gamepad_available(config_data["general"]["default_gamepad"])
            else DEVICE_TYPE.KEYBOARD
        )
    )

    for type in DEVICE_TYPE:
        device.buttons[type.value] = []

        for i in config_data[type.value]["buttons"]:
            current = config_data[type.value]["buttons"][i]
            btn = Button(
                BUTTONS_POSITION[i],
                current,
                get_button(i),
            )

            device.buttons[type.value].append(btn)

# * UPDATE
def update_overlay() -> None:
    global device, config_data, current_type, last_key

    if rl.is_key_pressed(config_data["keyboard"]["change_cast"]):
        device.type = DEVICE_TYPE.KEYBOARD if current_type else DEVICE_TYPE.JOYSTICK
        current_type = not current_type

    if device.type is DEVICE_TYPE.JOYSTICK:
        device.joystick = rl.Vector2(
            rl.get_gamepad_axis_movement(
                config_data["general"]["default_gamepad"],
                rl.GamepadAxis.GAMEPAD_AXIS_LEFT_X,
            ),
            rl.get_gamepad_axis_movement(
                config_data["general"]["default_gamepad"],
                rl.GamepadAxis.GAMEPAD_AXIS_LEFT_Y,
            ),
        )

        for btn in device.buttons["joystick"]:
            if rl.is_gamepad_button_down(0, btn.key):
                btn.active = True
                continue

            btn.active = False

    else:
        device.joystick = Vector2()
        if {config_data["keyboard"]["directions"]["up"]} <= last_key:
            device.joystick.y = -1

        if {config_data["keyboard"]["directions"]["down"]} <= last_key:
            device.joystick.y = 1

        if {config_data["keyboard"]["directions"]["left"]} <= last_key:
            device.joystick.x = -1

        if {config_data["keyboard"]["directions"]["right"]} <= last_key:
            device.joystick.x = 1



        for btn in device.buttons["keyboard"]:
            if {btn.key} <= last_key:
                btn.active = True
                continue

            btn.active = False

# * DRAW
def draw_overlay() -> None:
    global running

    gamepad_position = rl.Vector2(75, 85)
    gamepad_radius = 55
    end_v = rl.Vector2(
        gamepad_position.x + device.joystick.x * gamepad_radius,
        gamepad_position.y + device.joystick.y * gamepad_radius,
    )

    rl.begin_drawing()
    rl.clear_background(rl.BLANK)

    rl.draw_text(f"Casting: {device.type.value}", 0, 0, 12, rl.WHITE)
    if rl.gui_button((WINDOW_WIDTH - 25, 0, 25, 25), "X"):
        running = False        

    # ? Drawing jostick base
    rl.draw_circle_v(gamepad_position, gamepad_radius, rl.DARKBLUE)
    rl.draw_circle_v(gamepad_position, 22, rl.BLACK)
    rl.draw_line_ex(gamepad_position, end_v, 20, rl.SKYBLUE)
    rl.draw_circle_v(end_v, gamepad_radius // 2, rl.SKYBLUE)


    # ? Drawing buttons
    for btn in device.buttons[device.type.value]:
        if not btn.active:
            rl.draw_circle_v(btn.position, 25, rl.DARKBROWN)
            rl.draw_circle_v(btn.position, 20, rl.RED)

        else:
            rl.draw_circle_v(btn.position, 25, rl.DARKGREEN)
            rl.draw_circle_v(btn.position, 20, rl.GREEN)

        mesure_label = rl.measure_text(btn.type.value, 18)
        rl.draw_text(
            btn.type.value,
            int(btn.position.x) - mesure_label // 2,
            int(btn.position.y) - mesure_label // 2,
            18,
            rl.WHITE,
        )

    rl.end_drawing()

if __name__ == "__main__":
    rl.set_config_flags(ConfigFlags.FLAG_WINDOW_TRANSPARENT)
    rl.init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "HUD OVERLAY")
    rl.set_window_position( rl.get_monitor_width(0) - WINDOW_WIDTH, rl.get_monitor_height(0) - WINDOW_HEIGHT)
    rl.set_window_state(ConfigFlags.FLAG_WINDOW_UNDECORATED | ConfigFlags.FLAG_WINDOW_TOPMOST)
    rl.set_target_fps(60)

    keyboard_listener:Listener = Listener(on_press=press_key, on_release=release_key)

    init_overlay()
    keyboard_listener.start()
    while running:
        update_overlay()
        draw_overlay()

    keyboard_listener.stop()
    rl.close_window()
