import pygame
from pygame import Surface

from game_objects.tank.tank import Tank

from .interfaces import IApplicationState


class MainMenuState(IApplicationState):
    pass


class GameState(IApplicationState):
    def __init__(self):
        self.tanks: list[Tank] = [Tank()]
        self.x = 150
        self.y = 150
        self.move_up = 0

    def update(self, app) -> None:
        self.y += 1 * self.move_up * app.delta_time

    def render(self, delta_time: float, surface: Surface):
        for tank in self.tanks:
            surface.blit(tank.sprite, (self.x, self.y))

    def update_events(self, app, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.move_up = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.move_up = 0


class PauseState(IApplicationState):
    pass


class GameOverState(IApplicationState):
    pass
