from typing import List
from ...minimal_resources import MinimalEncounterCondition
from ...utility.common_models import Name, NamedResource


class EncounterConditionValue(NamedResource):
    condition: "MinimalEncounterCondition"
    names: List["Name"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.condition = MinimalEncounterCondition(data["condition"])
        self.names = [Name(name_data) for name_data in data["names"]]

    def __repr__(self) -> str:
        return f"<EncounterConditionValue condition={self.condition} id_={self.id_} name='{self.name}' names={self.names}>"
