# config.py

# Ventana
SCREEN_WIDTH = 375
SCREEN_HEIGHT = 250
FPS = 60

# Joystick
JOYSTICK_CENTER = (75, 125)
JOYSTICK_RADIUS = 50
JOYSTICK_STICK_LENGTH = 30

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
        "LP": (200, 100),
        "MP": (260, 100),
        "HP": (320, 100),
        "LK": (200, 160),
        "MK": (260, 160),
        "HK": (320, 160),
    }
    return [full_positions[label] for label in get_button_labels()]

