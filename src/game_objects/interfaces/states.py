from abc import ABC, abstractmethod

import pygame
from pygame import Surface


class IApplicationState(ABC):
    @abstractmethod
    def update(self, app: "Application") -> None:
        pass

    @abstractmethod
    def render(self, surface: Surface) -> None:
        pass

    @abstractmethod
    def update_events(self, app: "Application", event: pygame.event.Event) -> None:
        pass
