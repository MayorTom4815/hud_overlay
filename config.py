# config.py

# Ventana
SCREEN_WIDTH = 350
SCREEN_HEIGHT = 150
FPS = 60

# Joystick
JOYSTICK_CENTER = (75, 75)
JOYSTICK_RADIUS = 50
JOYSTICK_STICK_LENGTH = 35

# Botón (radio constante)
BUTTON_RADIUS = 30

# Ruta para guardar bindings si se usa teclado
BINDINGS_PATH = "bindings.json"

# Filtro de nombre de dispositivo joystick
DEVICE_NAME_FILTER = ["joystick", "gamepad"]

# Colores
COLOR_BG = (0, 0, 0, 0)
COLOR_STICK = (100, 100, 100)
COLOR_STICK_KNOB = (0, 255, 0)
COLOR_BUTTON_INACTIVE = (80, 80, 80)
COLOR_BUTTON_ACTIVE = (0, 255, 0)
COLOR_TEXT = (255, 255, 255)

# -------------------------------
# CONFIGURACIÓN DINÁMICA
# -------------------------------

# Este valor se ajusta en tiempo de ejecución por main.py
BUTTON_FORMAT = 6  # Puede ser 4 o 6

def get_button_labels():
    if BUTTON_FORMAT == 4:
        return ["LP", "LK", "HP", "HK"]
    else:
        return ["LP", "MP", "HP", "LK", "MK", "HK"]

def get_icon_paths():
    return [
        "icons/lp.png", "icons/mp.png", "icons/hp.png",
        "icons/lk.png", "icons/mk.png", "icons/hk.png"
    ][:BUTTON_FORMAT]

def get_icon_paths():
    icon_map = {
        "LP": "icons/lp.png",
        "MP": "icons/mp.png",
        "HP": "icons/hp.png",
        "LK": "icons/lk.png",
        "MK": "icons/mk.png",
        "HK": "icons/hk.png",
    }
    return [icon_map[label] for label in get_button_labels()]

def get_button_positions():
    # Define 6 posiciones fijas
    full_positions = {
        "LP": (190, 40),
        "MP": (250, 40),
        "HP": (310, 40),
        "LK": (190, 110),
        "MK": (250, 110),
        "HK": (310, 110),
    }
    return [full_positions[label] for label in get_button_labels()]

