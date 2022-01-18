from typing import List, Dict, Any

from aiopoke.objects.utility.common_models import Description, Name, NamedResource


class EncounterMethod(NamedResource):
    descriptions: List["Description"]
    order: int
    names: List["Name"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        order: int,
        descriptions: List[Dict[str, Any]],
        names: List[Dict[str, Any]]
    ) -> None:
        super().__init__(id=id, name=name)
        self.order = order
        self.descriptions = [Description(**description) for description in descriptions]
        self.names = [Name(**name) for name in names]
