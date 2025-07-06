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

    font = pygame.font.SysFont(pygame.font.get_default_font(), 22)

    # * Init Configs
    config.JOYSTICKS = [
        pygame.joystick.Joystick(joy) for joy in range(pygame.joystick.get_count())
    ]

    # * Program start
    config.button_format = ChoosingButtonsScreen(screen, font).render()
    config.input_type = TypeInputScreen(screen, font).render()

    if not config.saver.read_controller():
        config.saver.write_controller()
        MappingScreen(screen, font).render()

    config.bindings = config.saver.read_bindings()
    config.button_states = {
        config.bindings[i][2]: {"bind": config.bindings[i][3], "state": False}
        for i in range(4, config.bindings.__len__())
    }

    Thread(target=start_input_listener, daemon=True).start()
    RenderInput(screen, font).render()


if __name__ == "__main__":
    environ["SDL_VIDEO_WINDOW_POS"] = "20,780"

    # ! if you want to restart all, uncomment the next line before to run the program
    # ! then comment it again after to close the program.

    # config.saver.delete_all()

    pygame.init()
    main()
