from typing import List, Union
from ...minimal_resources import (
    MinimalNaturalGiftType,
    MinimalGeneration,
    MinimalMoveDamageClass,
    MinimalMove,
    MinimalPokemon
)
from ...utility import Name, NamedResource, GenerationGameIndex


class NaturalGiftType(NamedResource):
    damage_relations: "TypeRelations"
    game_indices: List["GenerationGameIndex"]
    move_damage_class: "MinimalMoveDamageClass"
    move: List["MinimalMove"]
    names: List["Name"]
    past_damage_relations: List["PastTypeRelation"]
    pokemon: List["TypePokemon"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.damage_relations = TypeRelations(data["damage_relations"])
        self.game_indices = [
            GenerationGameIndex(game_indice_data) for game_indice_data in data["game_indices"]
        ]
        self.move_damage_class = MinimalMoveDamageClass(data["move_damage_class"])
        self.moves = [MinimalMove(move_data) for move_data in data["moves"]]
        self.names = [Name(name_data) for name_data in data["names"]]
        self.past_damage_relations = [PastTypeRelation(past_damage_relation_data) for past_damage_relation_data in data["past_damage_relations"]]
        self.pokemon = [
            TypePokemon(pokemon_data) for pokemon_data in data["pokemon"]
        ]

    def __repr__(self) -> str:
        return (
            f"<NaturalGiftType damage_relations={self.damage_relations} game_indices={self.game_indices} id_={self.id_} "
            f"move_damage_class={self.move_damage_class} move={self.move} name='{self.name}' names={self.names} "
            f"past_damage_relations={self.past_damage_relations} pokemon={self.pokemon}>"
        )


class TypeRelations:
    double_damage_from: List["MinimalNaturalGiftType"]
    double_damage_to: List["MinimalNaturalGiftType"]
    half_damage_from: List["MinimalNaturalGiftType"]
    half_damage_to: List["MinimalNaturalGiftType"]
    no_damage_from: List["MinimalNaturalGiftType"]
    no_damage_to: List["MinimalNaturalGiftType"]

    def __init__(self, data) -> None:
        self.double_damage_from = [
            MinimalNaturalGiftType(natural_gift_type)
            for natural_gift_type in data["double_damage_from"]
        ]
        self.double_damage_to = [
            MinimalNaturalGiftType(natural_gift_type)
            for natural_gift_type in data["double_damage_to"]
        ]
        self.half_damage_from = [
            MinimalNaturalGiftType(natural_gift_type)
            for natural_gift_type in data["half_damage_from"]
        ]
        self.half_damage_to = [
            MinimalNaturalGiftType(natural_gift_type)
            for natural_gift_type in data["half_damage_to"]
        ]
        self.no_damage_from = [
            MinimalNaturalGiftType(natural_gift_type)
            for natural_gift_type in data["no_damage_from"]
        ]
        self.no_damage_to = [
            MinimalNaturalGiftType(natural_gift_type)
            for natural_gift_type in data["no_damage_to"]
        ]

    def __repr__(self) -> str:
        return (
            f"<DamageRelations double_damage_from={self.double_damage_from} double_damage_to={self.double_damage_from} "
            f"half_damage_from={self.half_damage_from} no_damage_from={self.no_damage_from} "
            f"no_damage_from={self.no_damage_from} no_damage_to={self.no_damage_to}>"
        )


class PastTypeRelation:
    damage_relations: "TypeRelations"
    generation: "MinimalGeneration"

    def __init__(self, data) -> None:
        self.damage_relations = TypeRelations(data["damage_relations"])
        self.generation = MinimalGeneration(data["generation"])

    def __repr__(self) -> str:
        return f"<PastTypeRelation damage_relations={self.damage_relations} generation={self.generation}>"


class TypePokemon:
    slot: int
    pokemon: "MinimalPokemon"

    def __init__(self, data) -> None:
        self.slot = data["slot"]
        self.pokemon = data["pokemon"]

    def __repr__(self) -> str:
        return f"<TypePokemon slot={self.slot} pokemon={self.pokemon}>"
