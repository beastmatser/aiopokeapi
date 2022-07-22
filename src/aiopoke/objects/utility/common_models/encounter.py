from typing import TYPE_CHECKING, Any, Dict, List

from aiopoke.utils.minimal_resources import MinimalResource
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources import EncounterConditionValue, EncounterMethod


class Encounter(Resource):
    min_level: int
    max_level: int
    condition_values: List[MinimalResource["EncounterConditionValue"]]
    chance: int
    method: MinimalResource["EncounterMethod"]

    def __init__(
        self,
        *,
        min_level: int,
        max_level: int,
        condition_values: List[Dict[str, Any]],
        chance: int,
        method: Dict[str, Any],
    ):
        self.min_level = min_level
        self.max_level = max_level
        self.condition_values = [
            MinimalResource(**condition_value) for condition_value in condition_values
        ]
        self.chance = chance
        self.method = MinimalResource(**method)
