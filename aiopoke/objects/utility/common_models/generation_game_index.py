from typing import TYPE_CHECKING, Any, Dict

from aiopoke.utils.minimal_resources import MinimalResource
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources import Generation


class GenerationGameIndex(Resource):
    game_index: int
    generation: MinimalResource["Generation"]

    def __init__(self, *, game_index: int, generation: Dict[str, Any]) -> None:
        self.game_index = game_index
        self.generation = MinimalResource(**generation)
