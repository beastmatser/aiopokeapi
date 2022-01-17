from typing import Tuple
from typing import TYPE_CHECKING

from ....minimal_resources import MinimalResource
from ...utility import Description

if TYPE_CHECKING:
    from . import Stat


class Characteristic:
    description: str
    descriptions: Tuple["Description", ...]
    gene_modulo: int
    highest_stat: MinimalResource["Stat"]
    id_: int
    possible_values: Tuple[int, ...]

    def __init__(self, data) -> None:
        self.description = tuple(
            name_data["name"]
            for name_data in data["names"]
            if name_data["language"]["name"] == "en"
        )[0]
        self.descriptions = tuple(
            Description(description_data) for description_data in data["descriptions"]
        )
        self.gene_modulo = data["gene_modulo"]
        self.highest_stat = MinimalResource(data["highest_stat"])
        self.id_ = data["id"]
        self.possible_values = tuple(data["possible_values"])

    def __repr__(self) -> str:
        return (
            f"<Characteristic description='{self.description}' descriptions={self.descriptions} gene_modulo={self.gene_modulo} "
            f"id_={self.id_} possible_values={self.possible_values}>"
        )
