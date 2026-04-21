from dataclasses import dataclass, field

from pyray import Vector2

from .enums import BUTTON_TYPE, DEVICE_TYPE


@dataclass
class Button:
    position: tuple[int, int]
    keys: tuple[str, int]
    type: BUTTON_TYPE
    active: bool = False


@dataclass
class Device:
    type: DEVICE_TYPE = DEVICE_TYPE.KEYBOARD
    joystick: Vector2 = Vector2()
    buttons: list[Button] = field(default_factory=list)
