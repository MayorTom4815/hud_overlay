from enum import Enum


class DEVICE_TYPE(Enum):
    JOYSTICK = "joystick"
    KEYBOARD = "keyboard"


class BUTTON_TYPE(Enum):
    # * punch
    LOW_PUNCH = "LP"
    MEDIUM_PUNCH = "MP"
    HIGH_PUNCH = "HP"
    # * kick
    LOW_KICK = "LK"
    MEDIUM_KICK = "MK"
    HIGH_KICK = "HK"
