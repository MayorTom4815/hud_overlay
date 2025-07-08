from config import WINDOW, BUTTONS_POSITION
import config

from templates import ConfigScreen
import pygame


def render_button(
    screen, font, pos: list[int] = [0, 0], text: str = "", pressed: bool = False
) -> None:
    color = (0, 0, 255) if not pressed else (255, 0, 0)
    font.set_bold(True)

    cir = pygame.draw.circle(screen, color, pos, 30)
    label = font.render(text, True, WINDOW.color_fg)

    screen.blit(label, label.get_rect(center=cir.center))


def render_jostick(screen):
    center_x, center_y = (75, 85)
    base_radius = 50
    stick_length = 40

    dx = config.joystick_hud.dx
    dy = config.joystick_hud.dy

    # ? Normalizar diagonal
    if dx != 0 and dy != 0:
        dx *= 1
        dy *= 1

    end_x = int(center_x + dx * stick_length)
    end_y = int(center_y + dy * stick_length)

    pygame.draw.circle(screen, (100, 100, 100), (center_x, center_y), base_radius)

    pygame.draw.line(screen, (0, 0, 0), (center_x, center_y), (end_x, end_y), 6)
    pygame.draw.circle(screen, (180, 180, 180), (end_x, end_y), 12)


class RenderInput(ConfigScreen):
    def render(self) -> None:
        while True:
            self.screen.fill(WINDOW.color_bg)
            keys = pygame.key.get_pressed()

            render_jostick(self.screen)
            for button in config.button_states.keys():
                state = config.button_states[button]

                render_button(
                    self.screen,
                    self.FONTS["NORMAL"],
                    BUTTONS_POSITION[button],
                    button,
                    state["state"],
                )

                if keys[state["bind"]]:
                    render_button(
                        self.screen,
                        self.FONTS["BUTTON"],
                        BUTTONS_POSITION[button],
                        button,
                        state["state"],
                    )

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            pygame.display.flip()
            self.clock.tick(WINDOW.fps)
