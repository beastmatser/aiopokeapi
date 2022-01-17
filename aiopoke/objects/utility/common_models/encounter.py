from typing import Tuple
from typing import TYPE_CHECKING

from aiopoke.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from ...resources import EncounterConditionValue, EncounterMethod


class Encounter:
    min_level: int
    max_level: int
    condition_values: Tuple[MinimalResource["EncounterConditionValue"], ...]
    chance: int
    method: MinimalResource["EncounterMethod"]

    def __init__(self, data) -> None:
        self.min_level = data["min_level"]
        self.max_level = data["max_level"]
        self.condition_values = tuple(
            MinimalResource(condition_value_data)
            for condition_value_data in data["condition_values"]
        )
        self.chance = data["chance"]
        self.method = MinimalResource(data["method"])

    def __repr__(self) -> str:
        return (
            f"<Encounter min_level={self.min_level} max_level={self.max_level} condition_values={self.condition_values} "
            f"chance={self.chance} method={self.method}>"
        )
