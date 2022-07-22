from typing import Any, Dict, List

from aiopoke.objects.utility.common_models import Description, Name, NamedResource


class EncounterMethod(NamedResource):
    order: int
    names: List["Name"]

    def __init__(
        self, *, id: int, name: str, order: int, names: List[Dict[str, Any]]
    ) -> None:
        super().__init__(id=id, name=name)
        self.order = order
        self.names = [Name(**name) for name in names]
