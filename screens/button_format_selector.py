from templates import ConfigScreen
from config import WINDOW
import pygame

texts: list[str] = [
    "Selecciona el formato de los botones:",
    "Presiona [ 4 ] para 4 botones",
    "Presiona [ 6 ] para 6 botones",
]


class ChoosingButtonsScreen(ConfigScreen):
    def render(self) -> int:
        self.screen.fill(WINDOW.color_bg)
        while True:
            ypos = 50

            for i in texts:
                self.draw_centered_text(self.FONTS["NORMAL"], i, ypos)
                ypos += 30

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_4:
                            return 4

                        case pygame.K_6:
                            return 6
