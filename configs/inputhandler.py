from .enums import BUTTON_TYPE


class InputKeyboardHandler:
    last_key: set[str] = set()

    def press_key(self, key) -> None:
        self.last_key.add(self.key_to_str(key))

    def release_key(self, key) -> None:
        self.last_key.discard(self.key_to_str(key))

    def key_to_str(self, key) -> str:
        try:
            return key.char.lower()
        except AttributeError:
            return str(key).replace("key.", "").lower()

    def get_button(self, value: str) -> BUTTON_TYPE:
        for i in BUTTON_TYPE:
            if i.value == value:
                return i

        raise ValueError(f"{value} not is a memember of BUTTONS")
