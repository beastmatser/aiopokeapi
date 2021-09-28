from typing import List
from ...minimal_resources import MinimalStat
from ...utility import Description


class Characteristic:
    description: str
    descriptions: List["Description"]
    gene_modulo: int
    id_: int
    possible_values: List[int]

    def __init__(self, data) -> None:
        self.description = [
            name_data["name"]
            for name_data in data["names"]
            if name_data["language"]["name"] == "en"
        ][0]
        self.descriptions = [Description(description_data) for description_data in data["descriptions"]]
        self.gene_modulo = data["gene_modulo"]
        self.highest_stat = MinimalStat(data["highest_stat"])
        self.id_ = data["id"]
        self.possible_values = data["possible_values"]

    def __repr__(self) -> str:
        return (
            f"<Characteristic description='{self.description}' descriptions={self.descriptions} gene_modulo={self.gene_modulo} "
            f"id_={self.id_} possible_values={self.possible_values}>"
        )
