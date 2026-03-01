from pathlib import Path

from pyray import Vector2

BUTTONS_POSITION: dict = {
    "LP": Vector2(195, 50),
    "MP": Vector2(265, 50),
    "HP": Vector2(335, 50),
    "LK": Vector2(195, 130),
    "MK": Vector2(265, 130),
    "HK": Vector2(335, 130),
}


DEFAULT_CONFIG = Path(".") / "default_config.toml"
PATH_CONFIG = Path.home() / ".HUDOverlay.toml"
WINDOW_HEIGHT = 175
WINDOW_WIDTH = 375
