from game_objects.interfaces.engine_objects import IRenderable, IUpdatable


class GameField(IRenderable, IUpdatable):
    def __init__(self, width: int, height: int):
        pass

    def render(self, *args, **kwargs) -> None:
        pass

    def update(self, *args, **kwargs) -> None:
        pass
