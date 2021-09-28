from typing import List
from ...minimal_resources import MinimalBerryFlavor
from ...utility import Name, NamedResource


class ContestType(NamedResource):
    berry_flavor: "MinimalBerryFlavor"
    names: List["ContestName"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.berry_flavor = MinimalBerryFlavor(data["berry_flavor"])
        self.names = [ContestName(name_data) for name_data in data["names"]]

    def __repr__(self) -> str:
        return f"<ContestType berry_flavor={self.berry_flavor} _id={self.id_} name='{self.name}' names={self.names}>"


class ContestName(Name):
    color: str

    def __init__(self, data) -> None:
        super().__init__(data)
        self.color = data["color"]

    def __repr__(self) -> str:
        return f"<ContestName color='{self.color}' name='{self.name}' language={self.language}>"
