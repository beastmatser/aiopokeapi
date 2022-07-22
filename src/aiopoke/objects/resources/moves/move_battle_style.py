from typing import Any, Dict, List

from aiopoke.objects.utility.common_models import Name, NamedResource


class MoveBatteStyle(NamedResource):
    names: List["Name"]

    def __init__(self, *, id: int, name: str, names: List[Dict[str, Any]]) -> None:
        super().__init__(id=id, name=name)
        self.names = [Name(**name) for name in names]
