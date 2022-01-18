from typing import Tuple
from typing import TYPE_CHECKING

from aiopoke.minimal_resources import MinimalResource
from aiopoke.objects.utility import Description
from aiopoke.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources.pokemon import Stat


class Characteristic(Resource):
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
