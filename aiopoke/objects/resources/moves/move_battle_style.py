from typing import List, Dict, Any

from aiopoke.objects.utility.common_models import Name, NamedResource


class MoveBatteStyle(NamedResource):
    names: List["Name"]

    def __init__(self, *, names: List[Dict[str, Any]]) -> None:
        self.names = [Name(**name) for name in names]
