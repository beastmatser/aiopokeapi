from typing import TYPE_CHECKING

from aiopoke.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources import Generation


class GenerationGameIndex:
    game_index: int
    generation: MinimalResource["Generation"]

    def __init__(self, data) -> None:
        self.game_index = data["game_index"]
        self.generation = MinimalResource(data["generation"])

    def __repr__(self) -> str:
        return f"<GenerationGameIndex game_index='{self.game_index}' generation={self.generation}>"
