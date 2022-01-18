from typing import TYPE_CHECKING, List

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

    def __init__(self, data) -> None:
        self.min_level = data["min_level"]
        self.max_level = data["max_level"]
        self.condition_values = [
            MinimalResource(condition_value_data)
            for condition_value_data in data["condition_values"]
        ]
        self.chance = data["chance"]
        self.method = MinimalResource(data["method"])
