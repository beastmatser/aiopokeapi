from typing import Tuple

from aiopoke.objects.utility.common_models import Name
from aiopoke.objects.utility.common_models import NamedResource


class MoveBatteStyle(NamedResource):
    names: Tuple["Name", ...]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.names = tuple(Name(name_data) for name_data in data["names"])
