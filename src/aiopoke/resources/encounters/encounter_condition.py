from typing import List
from ...minimal_resources import MinimalEncounterConditionValue
from ...utility.common_models import Name, NamedResource


class EncounterCondition(NamedResource):
    values: List["MinimalEncounterConditionValue"]
    names: List["Name"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.values = [
            MinimalEncounterConditionValue(encounter_condition_value)
            for encounter_condition_value in data["values"]
        ]
        self.names = [Name(name_data) for name_data in data["names"]]

    def __repr__(self) -> str:
        return f"<EncounterCondition id_={self.id_} name='{self.name}' names={self.names} values={self.values}>"
