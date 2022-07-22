from typing import TYPE_CHECKING, Any, Dict, List

from aiopoke.objects.utility import Description
from aiopoke.utils.minimal_resources import MinimalResource
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources.pokemon import Stat


class Characteristic(Resource):
    descriptions: List["Description"]
    gene_modulo: int
    highest_stat: MinimalResource["Stat"]
    id: int
    possible_values: List[int]

    def __init__(
        self,
        *,
        descriptions: List[Dict[str, Any]],
        gene_modulo: int,
        highest_stat: Dict[str, Any],
        id: int,
        possible_values: List[int]
    ) -> None:
        self.descriptions = [Description(**description) for description in descriptions]
        self.gene_modulo = gene_modulo
        self.highest_stat = MinimalResource(**highest_stat)
        self.id = id
        self.possible_values = possible_values
