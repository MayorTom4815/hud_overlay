from dataclasses import dataclass, field

from pyray import Vector2

from .enums import BUTTONS, DEVICE_TYPE


@dataclass
class Button:
    position: Vector2 = Vector2()
    key: int = 4
    type: BUTTONS = BUTTONS.LOW_KICK
    active: bool = False


@dataclass
class Device:
    type: DEVICE_TYPE = DEVICE_TYPE.KEYBOARD
    joystick: Vector2 = Vector2()
    buttons: dict[str, list[Button]] = field(default_factory=dict)
