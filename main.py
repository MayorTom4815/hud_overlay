from screens import ChoosingButtonsScreen, TypeInputScreen, MappingScreen, RenderInput
from os import environ

from input_reader import start_input_listener
from threading import Thread

import config
import pygame


def main():
    # * Screen Settings
    screen = pygame.display.set_mode(config.WINDOW.size, pygame.NOFRAME)
    pygame.display.set_caption("Arcade HUD Overlay")

    # * Init Configs
    config.JOYSTICKS = [
        pygame.joystick.Joystick(joy) for joy in range(pygame.joystick.get_count())
    ]

    # * Program start
    config.button_format = ChoosingButtonsScreen(screen).render()
    config.input_type = TypeInputScreen(screen).render()

    if not config.saver.read_controller():
        config.saver.write_controller()
        MappingScreen(screen).render()

    config.bindings = config.saver.read_bindings()
    Thread(target=start_input_listener, daemon=True).start()
    RenderInput(screen).render()


if __name__ == "__main__":
    environ["SDL_VIDEO_WINDOW_POS"] = "20,780"

    # ! Si quieres reiniciar todo, debes descomentar la siguiente linea antes de iniciar el programa
    # ! y despues comentala otra vez.

    # config.saver.delete_all()

    pygame.init()
    main()
