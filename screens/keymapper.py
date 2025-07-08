import config
from templates import ConfigScreen
import pygame


class MappingScreen(ConfigScreen):
    def wait_for_keypress(
        self, button: config.BUTTONS, event_type
    ) -> tuple[str, str, int]:
        while True:
            self.screen.fill(config.WINDOW.color_bg)
            self.draw_centered_text(
                self.FONTS["NORMAL"],
                f"Seleccione la tecla para el boton {button.value}",
                50,
            )
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                elif event.type == event_type:
                    return event.key if event_type == pygame.KEYDOWN else event.button

    def render(self) -> None:
        temp_binding: list[tuple] = []

        match config.input_type:
            case config.DEVICES.KEYBOARD:
                for button in config.BUTTONS_FORMATS[config.button_format]:
                    temp_binding.append(
                        (
                            config.input_type.value,
                            config.button_format,
                            button.value,
                            self.wait_for_keypress(button, pygame.KEYDOWN),
                        )
                    )

            case config.DEVICES.JOYSTICK:
                bformat = config.BUTTONS_FORMATS[config.button_format]

                if config.JOYSTICKS.__len__() > 0:
                    for i in range(4, bformat.__len__()):
                        temp_binding.append(
                            (
                                config.input_type.value,
                                config.button_format,
                                bformat[i].value,
                                str(
                                    self.wait_for_keypress(
                                        bformat[i], pygame.JOYBUTTONDOWN
                                    )
                                ),
                            )
                        )
                else:
                    print("[Error] No hay controles disponibles")

        config.saver.write_bindings(temp_binding)
