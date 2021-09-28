from typing import List
from ...minimal_resources import MinimalBerry
from ...utility import Name, NamedResource


class BerryFirmness(NamedResource):
    berries: List["MinimalBerry"]
    names: List["Name"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.berries = [MinimalBerry(berry_data) for berry_data in data["berries"]]
        self.names = [Name(name_data) for name_data in data["names"]]

    def __repr__(self) -> str:
        return f"<BerryFirmness berries={self.berries} id_={self.id_} name='{self.name}' names={self.names}>"
