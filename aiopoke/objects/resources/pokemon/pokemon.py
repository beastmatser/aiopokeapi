from typing import Tuple
from typing import TYPE_CHECKING

from aiopoke.minimal_resources import MinimalResource
from aiopoke.objects.utility import NamedResource
from aiopoke.objects.utility import VersionEncounterDetail
from aiopoke.objects.utility import VersionGameIndex
from aiopoke.objects.utility.common_models.sprites import Sprites
from aiopoke.objects.resources.games.version_group import VersionGroupDetail

if TYPE_CHECKING:
    from aiopoke.objects.resources import (
        Generation,
        Item,
        LocationArea,
        MoveLearnMethod,
        Version,
        VersionGroup,
    )
    from aiopoke.objects.resources.pokemon import Ability, NaturalGiftType, PokemonForm, PokemonSpecies


class Pokemon(NamedResource):
    abilities: Tuple["PokemonAbility", ...]
    base_experience: int
    forms: Tuple[MinimalResource["PokemonForm"], ...]
    game_indices: Tuple["VersionGameIndex", ...]
    height: int
    items: Tuple["PokemonHeldItem", ...]
    is_default: bool
    location_area_encounters: Tuple["PokemonLocationArea", ...]
    moves: Tuple["PokemonMove", ...]
    order: int
    past_types: Tuple["PastType", ...]
    species: MinimalResource["PokemonSpecies"]
    sprites: "Sprites"
    stats: Tuple["PokemonStat", ...]
    types: Tuple["PokemonType", ...]
    weight: int

    def __init__(self, data) -> None:
        super().__init__(data)
        self.abilities = tuple(
            PokemonAbility(ability_data) for ability_data in data["abilities"]
        )
        self.base_experience = data["base_experience"]
        self.forms = tuple(MinimalResource(form_data) for form_data in data["forms"])
        self.game_indices = tuple(
            VersionGameIndex(game_indice_data)
            for game_indice_data in data["game_indices"]
        )
        self.height = data["height"]
        self.held_items = tuple(
            PokemonHeldItem(item_data) for item_data in data["held_items"]
        )
        self.is_default = data["is_default"]
        self.location_area_encounters = tuple(
            PokemonLocationArea(location_area_encounter_data)
            for location_area_encounter_data in data["location_area_encounters"]
        )
        self.moves = tuple(PokemonMove(move_data) for move_data in data["moves"])
        self.order = data["order"]
        self.past_types = tuple(
            PastType(past_type_data) for past_type_data in data["past_types"]
        )
        self.species = MinimalResource(data["species"])
        self.sprites = Sprites(data["sprites"])
        self.stats = tuple(PokemonStat(stat_data) for stat_data in data["stats"])
        self.types = tuple(PokemonType(type_data) for type_data in data["types"])
        self.weight = data["weight"]

    def __repr__(self) -> str:
        return (
            f"<Pokemon abilities={self.abilities} base_experience={self.base_experience} forms={self.forms} "
            f"game_indices={self.game_indices} height={self.height} id_={self.id} held_items={self.held_items} "
            f"is_default={self.is_default} location_area_encounters={self.location_area_encounters} moves={self.moves} name='{self.name}' "
            f"order={self.order} past_types={self.past_types} species={self.species} sprites={self.sprites} "
            f"stats={self.stats} types={self.types} weight={self.weight}>"
        )


class PokemonAbility:
    is_hidden: bool
    slot: int
    ability: MinimalResource["Ability"]

    def __init__(self, data) -> None:
        self.is_hidden = data["is_hidden"]
        self.slot = data["slot"]
        self.ability = MinimalResource(data["ability"])

    def __repr__(self) -> str:
        return f"<PokemonAbility is_hidden={self.is_hidden} slot={self.slot} pokemon={self.ability}>"


class PokemonType:
    slot: int
    type_: MinimalResource["NaturalGiftType"]

    def __init__(self, data) -> None:
        self.slot = data["slot"]
        self.type_ = MinimalResource(data["type"])

    def __repr__(self) -> str:
        return f"<PokemonType slot={self.slot} type_={self.type_}>"


class PokemonHeldItem:
    item: MinimalResource["Item"]
    version_details: Tuple["PokemonHeldItemVersion", ...]

    def __init__(self, data) -> None:
        self.item = MinimalResource(data["item"])
        self.version_details = tuple(
            PokemonHeldItemVersion(version_detail_data)
            for version_detail_data in data["version_details"]
        )

    def __repr__(self) -> str:
        return (
            f"<PokemonHeldItem item={self.item} version_details={self.version_details}>"
        )


class PokemonHeldItemVersion:
    rarity: int
    version: MinimalResource["Version"]

    def __init__(self, data) -> None:
        self.rarity = data["rarity"]
        self.version = MinimalResource(data["version"])

    def __repr__(self) -> str:
        return f"<PokemonHeldItemVersion rarity={self.rarity} version={self.version}>"


class PokemonMove:
    move: MinimalResource["Version"]
    version_group_details: Tuple["VersionGroupDetail", ...]

    def __init__(self, data) -> None:
        self.move = MinimalResource(data["move"])
        self.version_group_details = tuple(
            VersionGroupDetail(version_group_detail_data)
            for version_group_detail_data in data["version_group_details"]
        )

    def __repr__(self) -> str:
        return f"<PokemonMove move={self.move} version_group_details={self.version_group_details}>"


class PokemonMoveVersion:
    move_learn_method: MinimalResource["MoveLearnMethod"]
    version_group: MinimalResource["VersionGroup"]
    level_learned_at: int

    def __init__(self, data) -> None:
        self.move_learn_method = MinimalResource(data["move_learn_method"])
        self.version_group = MinimalResource(data["version_group"])
        self.level_learned_at = data["level_learned_at"]

    def __repr__(self) -> str:
        return f"<PokemonHeldItem move_learn_method={self.move_learn_method} version_group={self.version_group} level_learned_at={self.level_learned_at}>"


class PokemonStat:
    base_stat: int
    effort: int
    stat: MinimalResource["PokemonStat"]

    def __init__(self, data) -> None:
        self.base_stat = data["base_stat"]
        self.effort = data["effort"]
        self.stat = MinimalResource(data["stat"])

    def __repr__(self) -> str:
        return f"<PokemonStat base_stat={self.base_stat} effort={self.effort} stat={self.stat}>"


class PastType:
    generation: MinimalResource["Generation"]
    types: Tuple["PokemonType", ...]

    def __init__(self, data) -> None:
        self.generation = MinimalResource(data["generation"])
        self.types = tuple(PokemonType(type_data) for type_data in data["types"])

    def __repr__(self) -> str:
        return f"<PastType generation={self.generation} types={self.types}>"


class PokemonLocationArea:
    location_area: MinimalResource["LocationArea"]
    version_details: Tuple["VersionEncounterDetail", ...]

    def __init__(self, data) -> None:
        self.location_area = MinimalResource(data["location_area"])
        self.version_details = tuple(
            VersionEncounterDetail(version_detail_data)
            for version_detail_data in data["version_details"]
        )

    def __repr__(self) -> str:
        return f"<PokemonLocationArea location_area={self.location_area} version_details={self.version_details}>"
