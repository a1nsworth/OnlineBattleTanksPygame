import pygame
from pygame import Surface

from game_objects.interfaces.engine_objects import IRenderable, IUpdatable
from typing import TypeAlias


PygameColor: TypeAlias = (
    pygame.Color | int | str | tuple[int, int, int] | tuple[int, int, int, int]
)


class Window(IUpdatable, IRenderable):
    def __init__(
        self,
        width: int,
        height: int,
        title: str,
        bg_color: PygameColor,
    ):
        self._surface = pygame.display.set_mode(
            (height, width),
        )
        pygame.display.set_caption(title)
        self._bg_color = bg_color

    @property
    def bg_color(self):
        return self._bg_color

    @bg_color.setter
    def bg_color(self, value: PygameColor):
        self._bg_color = value

    @property
    def surface(self) -> Surface:
        return self._surface

    def update(self) -> None:
        pass

    def render(self) -> None:
        self._surface.fill(self.bg_color)
