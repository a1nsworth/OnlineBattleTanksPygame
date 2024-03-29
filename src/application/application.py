import pygame
from pygame.time import Clock

from application.window import Window
from .states import GameState, IApplicationState
from game_objects.interfaces.engine_objects import IUpdatableRenderableUpdatableEvents
from network import container


class Application(IUpdatableRenderableUpdatableEvents):
    MAX_FPS: int = 60

    def __init__(self, window: Window):
        pygame.init()
        self._window = window

        self.state: IApplicationState = GameState()
        self._clinet = container.client_singleton()
        self._clock: Clock = pygame.time.Clock()
        self._delta_time: float = 0

    @property
    def delta_time(self):
        return self._delta_time

    def update_delta_time(self):
        self._delta_time = self._clock.tick(Application.MAX_FPS)

    def render(self, delta_time: float) -> None:
        self._window.render()
        self.state.render(delta_time, self._window.surface)

    def update(self, delta_time: float) -> None:
        self._window.update()
        self.state.update(self)
        pygame.display.flip()

    def update_events(self, delta_time: float) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self._clinet.close()
                exit()
            self.state.update_events(self, event)

    def run(self):
        while True:
            self.update(1)
            self.render(1)
            self.update_events(1)
            self.update_delta_time()
