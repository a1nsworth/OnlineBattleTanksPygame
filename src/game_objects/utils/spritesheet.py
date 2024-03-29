import pygame
from pygame import Surface


class SpriteSheet:
    def __init__(self, path: str):
        self._image = pygame.image.load(path).convert()
        self._path = path

    @property
    def image(self) -> Surface:
        return self._image

    @property
    def path(self) -> str:
        return self._path


def slice_sprite(
    sprite_sheet: SpriteSheet,
    xy: tuple[float, float],
    wh: tuple[float, float],
) -> Surface:
    sprite = pygame.Surface((wh[0], wh[1]))
    sprite.set_colorkey((0, 0, 0))
    sprite.blit(sprite_sheet.image, (0, 0), (*xy, *wh))
    return sprite
