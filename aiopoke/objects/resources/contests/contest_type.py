from typing import Tuple
from typing import TYPE_CHECKING

from ....minimal_resources import MinimalResource
from ...utility import Name
from ...utility import NamedResource

if TYPE_CHECKING:
    from ...resources.berries import BerryFlavor


class ContestType(NamedResource):
    berry_flavor: MinimalResource["BerryFlavor"]
    names: Tuple["ContestName", ...]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.berry_flavor = MinimalResource(data["berry_flavor"])
        self.names = tuple(ContestName(name_data) for name_data in data["names"])

    def __repr__(self) -> str:
        return f"<ContestType berry_flavor={self.berry_flavor} _id={self.id} name='{self.name}' names={self.names}>"


class ContestName(Name):
    color: str

    def __init__(self, data) -> None:
        super().__init__(data)
        self.color = data["color"]

    def __repr__(self) -> str:
        return f"<ContestName color='{self.color}' name='{self.name}' language={self.language}>"
