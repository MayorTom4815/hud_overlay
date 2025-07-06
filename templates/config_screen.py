from config import WINDOW, DEVICES
from pygame.surface import Surface
from pygame.time import Clock
from pygame.font import Font


class ConfigScreen:
    def __init__(self, screen: Surface, font: Font, clock:Clock = Clock()):
        self.screen = screen
        self.clock = clock
        self.font = font

    def render(self) -> int | DEVICES | None: ...

    def draw_centered_text(self, text, y=20) -> None:
        text = self.font.render(text, False, WINDOW.color_fg)
        self.screen.blit(
            text, text.get_rect(center=(self.screen.get_size()[0] // 2, y))
        )
