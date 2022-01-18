from typing import List
from typing import TYPE_CHECKING

from aiopoke.objects.utility import Description
from aiopoke.utils.resource import Resource

from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources.pokemon import Stat


class Characteristic(Resource):
    descriptions: List["Description"]
    gene_modulo: int
    highest_stat: MinimalResource["Stat"]
    id_: int
    possible_values: List[int]

    def __init__(self, data) -> None:
        self.descriptions = [
            Description(description_data) for description_data in data["descriptions"]
        ]
        self.gene_modulo = data["gene_modulo"]
        self.highest_stat = MinimalResource(data["highest_stat"])
        self.id_ = data["id"]
        self.possible_values = data["possible_values"]
