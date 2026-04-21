from json import load
from pathlib import Path
from typing import Any


class Configs:
    # ? Default config path
    __config_path: Path = Path.home() / ".HUDOverlay.json"
    __detaults: Path = Path("./default.json")
    data: dict[str, Any] = {}

    def __init__(self) -> None:
        if not self.__config_path.exists():
            self.__detaults.copy(self.__config_path)

        with open(str(self.__config_path), "rb") as file:
            self.data = load(file)
