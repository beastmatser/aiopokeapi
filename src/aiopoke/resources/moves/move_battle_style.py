from typing import Tuple

from ...utility.common_models import Name, NamedResource


class MoveBatteStyle(NamedResource):
    names: Tuple["Name", ...]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.names = tuple(Name(name_data) for name_data in data["names"])

    def __repr__(self) -> str:
        return f"<MoveBatteStyle id_={self.id_} name='{self.name}' names={self.names}>"
