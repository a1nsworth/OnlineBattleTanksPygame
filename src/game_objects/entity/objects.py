from pygame import Surface
from pygame.sprite import Sprite


class GameObject(Sprite):
    def __init__(self, sprite: Surface | None):
        super().__init__()
        self.sprite: Surface | None = sprite

    def render(self, surface: Surface, position: tuple[float, float]):
        surface.blit(self.sprite, position)
