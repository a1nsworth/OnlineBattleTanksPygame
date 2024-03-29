from abc import ABC, abstractmethod


class IUpdatable(ABC):
    @abstractmethod
    def update(self, delta_time: float) -> None:
        pass


class IRenderable(ABC):
    @abstractmethod
    def render(self, delta_time: float) -> None:
        pass


class IUpdatableEvents(ABC):
    @abstractmethod
    def update_events(self, delta_time: float) -> None:
        pass


class IUpdatableRenderableUpdatableEvents(
    IUpdatable, IRenderable, IUpdatableEvents, ABC
):
    pass
