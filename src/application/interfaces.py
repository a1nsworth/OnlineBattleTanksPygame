from __future__ import annotations

from abc import ABC, abstractmethod
import pygame
from pygame import Surface

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .application import Application


class IApplicationState(ABC):
    @abstractmethod
    def update(self, app: Application) -> None:
        pass

    @abstractmethod
    def render(self, delta_time: float, surface: Surface) -> None:
        pass

    @abstractmethod
    def update_events(self, app: Application, event: pygame.event.Event) -> None:
        pass
