from typing import TYPE_CHECKING, Any, Dict, List

from aiopoke.objects.utility import GenerationGameIndex, Name, NamedResource
from aiopoke.utils.minimal_resources import MinimalResource
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources import Generation, Move, MoveDamageClass
    from aiopoke.objects.resources.pokemon import Pokemon


class NaturalGiftType(NamedResource):
    damage_relations: "TypeRelations"
    game_indices: List["GenerationGameIndex"]
    generation: MinimalResource["Generation"]
    move_damage_class: MinimalResource["MoveDamageClass"]
    moves: List[MinimalResource["Move"]]
    names: List["Name"]
    past_damage_relations: List["PastTypeRelation"]
    pokemon: List["TypePokemon"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        damage_relations: Dict[str, Any],
        game_indices: List[Dict[str, Any]],
        generation: Dict[str, Any],
        move_damage_class: Dict[str, Any],
        moves: List[Dict[str, Any]],
        names: List[Dict[str, Any]],
        past_damage_relations: List[Dict[str, Any]],
        pokemon: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.damage_relations = TypeRelations(**damage_relations)
        self.game_indices = [
            GenerationGameIndex(**game_index) for game_index in game_indices
        ]
        self.generation = MinimalResource(**generation)
        self.move_damage_class = MinimalResource(**move_damage_class)
        self.moves = [MinimalResource(**move) for move in moves]
        self.names = [Name(**name) for name in names]
        self.past_damage_relations = [
            PastTypeRelation(**past_damage_relation)
            for past_damage_relation in past_damage_relations
        ]
        self.pokemon = [TypePokemon(**pokemon) for pokemon in pokemon]


class TypeRelations(Resource):
    double_damage_from: List[MinimalResource["NaturalGiftType"]]
    double_damage_to: List[MinimalResource["NaturalGiftType"]]
    half_damage_from: List[MinimalResource["NaturalGiftType"]]
    half_damage_to: List[MinimalResource["NaturalGiftType"]]
    no_damage_from: List[MinimalResource["NaturalGiftType"]]
    no_damage_to: List[MinimalResource["NaturalGiftType"]]

    def __init__(
        self,
        *,
        double_damage_from: List[Dict[str, Any]],
        double_damage_to: List[Dict[str, Any]],
        half_damage_from: List[Dict[str, Any]],
        half_damage_to: List[Dict[str, Any]],
        no_damage_from: List[Dict[str, Any]],
        no_damage_to: List[Dict[str, Any]],
    ) -> None:
        self.double_damage_from = [
            MinimalResource(**type_data) for type_data in double_damage_from
        ]
        self.double_damage_to = [
            MinimalResource(**type_data) for type_data in double_damage_to
        ]
        self.half_damage_from = [
            MinimalResource(**type_data) for type_data in half_damage_from
        ]
        self.half_damage_to = [
            MinimalResource(**type_data) for type_data in half_damage_to
        ]
        self.no_damage_from = [
            MinimalResource(**type_data) for type_data in no_damage_from
        ]
        self.no_damage_to = [MinimalResource(**type_data) for type_data in no_damage_to]


class PastTypeRelation:
    damage_relations: "TypeRelations"
    generation: MinimalResource["Generation"]

    def __init__(
        self,
        *,
        damage_relations: Dict[str, Any],
        generation: Dict[str, Any],
    ) -> None:
        self.damage_relations = TypeRelations(**damage_relations)
        self.generation = MinimalResource(**generation)


class TypePokemon(Resource):
    slot: int
    pokemon: MinimalResource["Pokemon"]

    def __init__(self, *, slot: int, pokemon: Dict[str, Any]) -> None:
        self.slot = slot
        self.pokemon = MinimalResource(**pokemon)
