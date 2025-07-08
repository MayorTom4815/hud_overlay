from templates import ConfigScreen
from config import DEVICES, WINDOW
import pygame

texts: list[str] = [
    "Selecciona el modo de entrada:",
    "Presiona [ T ] para TECLADO",
    "Presiona [ J ] para JOYSTICK",
]


class TypeInputScreen(ConfigScreen):
    def render(self) -> DEVICES:
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
                    exit()

                if event.type == pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_t:
                            return DEVICES.KEYBOARD

                        case pygame.K_j:
                            return DEVICES.JOYSTICK
