from typing import List
from typing import TYPE_CHECKING

from aiopoke.objects.utility import GenerationGameIndex
from aiopoke.objects.utility import Name
from aiopoke.objects.utility import NamedResource
from aiopoke.utils.resource import Resource

from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources.pokemon import Pokemon
    from aiopoke.objects.resources import (
        Generation,
        Move,
        MoveDamageClass,
    )


class NaturalGiftType(NamedResource):
    damage_relations: "TypeRelations"
    game_indices: List["GenerationGameIndex"]
    move_damage_class: MinimalResource["MoveDamageClass"]
    moves: List[MinimalResource["Move"]]
    names: List["Name"]
    past_damage_relations: List["PastTypeRelation"]
    pokemon: List["TypePokemon"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.damage_relations = TypeRelations(data["damage_relations"])
        self.game_indices = [
            GenerationGameIndex(game_indice_data)
            for game_indice_data in data["game_indices"]
        ]
        self.move_damage_class = MinimalResource(data["move_damage_class"])
        self.moves = [MinimalResource(move_data) for move_data in data["moves"]]
        self.names = [Name(name_data) for name_data in data["names"]]
        self.past_damage_relations = [
            PastTypeRelation(past_damage_relation_data)
            for past_damage_relation_data in data["past_damage_relations"]
        ]
        self.pokemon = [
            TypePokemon(pokemon_data) for pokemon_data in data["pokemon"]
        ]


class TypeRelations(Resource):
    double_damage_from: List[MinimalResource["NaturalGiftType"]]
    double_damage_to: List[MinimalResource["NaturalGiftType"]]
    half_damage_from: List[MinimalResource["NaturalGiftType"]]
    half_damage_to: List[MinimalResource["NaturalGiftType"]]
    no_damage_from: List[MinimalResource["NaturalGiftType"]]
    no_damage_to: List[MinimalResource["NaturalGiftType"]]

    def __init__(self, data) -> None:
        self.double_damage_from = [
            MinimalResource(natural_gift_type)
            for natural_gift_type in data["double_damage_from"]
        ]
        self.double_damage_to = [
            MinimalResource(natural_gift_type)
            for natural_gift_type in data["double_damage_to"]
        ]
        self.half_damage_from = [
            MinimalResource(natural_gift_type)
            for natural_gift_type in data["half_damage_from"]
        ]
        self.half_damage_to = [
            MinimalResource(natural_gift_type)
            for natural_gift_type in data["half_damage_to"]
        ]
        self.no_damage_from = [
            MinimalResource(natural_gift_type)
            for natural_gift_type in data["no_damage_from"]
        ]
        self.no_damage_to = [
            MinimalResource(natural_gift_type)
            for natural_gift_type in data["no_damage_to"]
        ]


class PastTypeRelation:
    damage_relations: "TypeRelations"
    generation: MinimalResource["Generation"]

    def __init__(self, data) -> None:
        self.damage_relations = TypeRelations(data["damage_relations"])
        self.generation = MinimalResource(data["generation"])


class TypePokemon(Resource):
    slot: int
    pokemon: MinimalResource["Pokemon"]

    def __init__(self, data) -> None:
        self.slot = data["slot"]
        self.pokemon = MinimalResource(data["pokemon"])
