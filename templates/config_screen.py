from config import WINDOW, DEVICES
from pygame.surface import Surface
from pygame.time import Clock
from pygame.font import Font


class ConfigScreen:
    def __init__(self, screen: Surface, clock: Clock = Clock()):
        self.screen = screen
        self.clock = clock

        self.FONTS = dict(NORMAL=Font(None, 22), BUTTON=Font(None, 28))

    def render(self) -> int | DEVICES | None: ...

    def draw_centered_text(self, font: Font, text, y=30) -> None:
        text = font.render(text, False, WINDOW.color_fg)
        self.screen.blit(
            text, text.get_rect(center=(self.screen.get_size()[0] // 2, y))
        )
