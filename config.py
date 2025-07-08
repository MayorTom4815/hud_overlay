from dataclasses import dataclass
from os.path import expanduser
from enum import Enum

from save_manager import SaverManager
from pygame.joystick import Joystick

#---------------------
#     Constantes
#---------------------
# ! ¡No tocar!

class DIRECCTIONS(Enum):
    UP = "arriba"
    DOWN = "abajo"
    LEFT = "izquierda"
    RIGHT = "derecha"


class BUTTONS(Enum):
    LOW_PUNCH = "LP"
    MEDIUM_PUNCH = "MP"
    HIGH_PUNCH = "HP"

    LOW_KICK = "LK"
    MEDIUM_KICK = "MK"
    HIGH_KICK = "HK"


class DEVICES(Enum):
    JOYSTICK = "joystick"
    KEYBOARD = "keyboard"


@dataclass
class STICK:
    dx: float = 0
    dy: float = 0


@dataclass
class WINDOW:
    color_bg = (0, 0, 0, 0)
    color_fg = (255, 255, 255)
    size: tuple = (375, 175)
    fps: int = 60



BUTTONS_FORMATS: dict = {
    4: [
        DIRECCTIONS.UP,
        DIRECCTIONS.DOWN,
        DIRECCTIONS.LEFT,
        DIRECCTIONS.RIGHT,
        BUTTONS.LOW_PUNCH,
        BUTTONS.HIGH_PUNCH,
        BUTTONS.LOW_KICK,
        BUTTONS.HIGH_KICK,
    ],
    6: [
        DIRECCTIONS.UP,
        DIRECCTIONS.DOWN,
        DIRECCTIONS.LEFT,
        DIRECCTIONS.RIGHT,
        BUTTONS.LOW_KICK,
        BUTTONS.MEDIUM_KICK,
        BUTTONS.HIGH_KICK,
        BUTTONS.LOW_PUNCH,
        BUTTONS.MEDIUM_PUNCH,
        BUTTONS.HIGH_PUNCH,
    ],
}


BUTTONS_POSITION: dict = {
    "LP": (195, 50),
    "MP": (265, 50),
    "HP": (335, 50),
    "LK": (195, 130),
    "MK": (265, 130),
    "HK": (335, 130),
}

JOYSTICKS: list[Joystick] = []

# * Ruta del guardado
# ? Puedes modificar esto:
BINDINGS_PATH: str = expanduser("~/.bindings.db")

#--------------------
#      Valores
#--------------------

saver: SaverManager = SaverManager(BINDINGS_PATH)
input_type: DEVICES = DEVICES.KEYBOARD
button_format: int = 0

joystick_hud: STICK = STICK()
bindings: list[tuple] = []

button_states: dict = {}
