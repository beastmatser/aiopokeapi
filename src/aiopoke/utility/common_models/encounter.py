from typing import List
from ...minimal_resources import MinimalEncounterMethod, MinimalEncounterConditionValue


class Encounter:
    min_level: int
    max_level: int
    condition_values: List["MinimalEncounterConditionValue"]
    chance: int
    method: "MinimalEncounterMethod"

    def __init__(self, data) -> None:
        self.min_level = data["min_level"]
        self.max_level = data["max_level"]
        self.condition_values = [
            MinimalEncounterConditionValue(condition_value_data)
            for condition_value_data in data["condition_values"]
        ]
        self.chance = data["chance"]
        self.method = MinimalEncounterMethod(data["method"])

    def __repr__(self) -> str:
        return (
            f"<Encounter min_level={self.min_level} max_level={self.max_level} condition_values={self.condition_values} "
            f"chance={self.chance} method={self.method}>"
        )
