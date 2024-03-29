from game_objects.entity.objects import GameObject
from game_objects.utils.spritesheet import slice_sprite, SpriteSheet


class Tank(GameObject):
    def __init__(self):
        super().__init__(
            slice_sprite(
                SpriteSheet("../resources/Tiles.png"),
                (250, 705),
                (54, 79),
            )
        )
