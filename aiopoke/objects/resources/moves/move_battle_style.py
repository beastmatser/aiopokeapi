from typing import List

from aiopoke.objects.utility.common_models import Name
from aiopoke.objects.utility.common_models import NamedResource


class MoveBatteStyle(NamedResource):
    names: List["Name"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.names = [Name(name_data) for name_data in data["names"]]
