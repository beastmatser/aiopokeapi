from typing import Any
from typing import Dict
from typing import List
from typing import TYPE_CHECKING
from typing import Optional

from aiopoke.objects.resources.games.version_group import VersionGroupDetail
from aiopoke.objects.utility import NamedResource
from aiopoke.objects.utility import VersionEncounterDetail
from aiopoke.objects.utility import VersionGameIndex
from aiopoke.objects.utility.common_models.sprites import Sprites
from aiopoke.utils.minimal_resources import MinimalResource
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources import (
        Generation,
        Item,
        LocationArea,
        MoveLearnMethod,
        Version,
        VersionGroup,
    )
    from aiopoke.objects.resources.pokemon import (
        Ability,
        NaturalGiftType,
        PokemonForm,
        PokemonSpecies,
    )


class Pokemon(NamedResource):
    abilities: List["PokemonAbility"]
    base_experience: int
    cries: "PokemonCries"
    forms: List[MinimalResource["PokemonForm"]]
    game_indices: List["VersionGameIndex"]
    held_items: List["PokemonHeldItem"]
    height: int
    is_default: bool
    location_area_encounters: List["PokemonLocationArea"]
    moves: List["PokemonMove"]
    order: int
    past_abilities: List["PastAbility"]
    past_stats: List["PastStat"]
    past_types: List["PastType"]
    species: MinimalResource["PokemonSpecies"]
    sprites: "Sprites"
    stats: List["PokemonStat"]
    types: List["PokemonType"]
    weight: int

    def __init__(
        self,
        *,
        id: int,
        name: str,
        abilities: List[Dict[str, Any]],
        base_experience: int,
        cries: Dict[str, Any],
        forms: List[Dict[str, Any]],
        game_indices: List[Dict[str, Any]],
        height: int,
        held_items: List[Dict[str, Any]],
        is_default: bool,
        location_area_encounters: List[Dict[str, Any]],
        moves: List[Dict[str, Any]],
        order: int,
        past_abilities: List[Dict[str, Any]],
        past_stats: List[Dict[str, Any]],
        past_types: List[Dict[str, Any]],
        species: Dict[str, Any],
        sprites: Dict[str, Any],
        stats: List[Dict[str, Any]],
        types: List[Dict[str, Any]],
        weight: int,
    ) -> None:
        super().__init__(id=id, name=name)
        self.abilities = [PokemonAbility(**ability) for ability in abilities]
        self.base_experience = base_experience
        self.cries = PokemonCries(**cries)
        self.forms = [MinimalResource(**form) for form in forms]
        self.game_indices = [
            VersionGameIndex(**game_index) for game_index in game_indices
        ]
        self.height = height
        self.held_items = [PokemonHeldItem(**held_item) for held_item in held_items]
        self.is_default = is_default
        self.location_area_encounters = [
            PokemonLocationArea(**location_area_encounter)
            for location_area_encounter in location_area_encounters
        ]
        self.moves = [PokemonMove(**move) for move in moves]
        self.order = order
        self.past_abilities = [
            PastAbility(**past_ability) for past_ability in past_abilities
        ]
        self.past_stats = [PastStat(**past_stat) for past_stat in past_stats]
        self.past_types = [PastType(**past_type) for past_type in past_types]
        self.species = MinimalResource(**species)
        self.sprites = Sprites(sprites)
        self.stats = [PokemonStat(**stat) for stat in stats]
        self.types = [PokemonType(**type_) for type_ in types]
        self.weight = weight


class PokemonAbility(Resource):
    is_hidden: bool
    slot: int
    ability: Optional[MinimalResource["Ability"]]

    def __init__(
        self,
        *,
        is_hidden: bool,
        slot: int,
        ability: Dict[str, Any],
    ) -> None:
        self.is_hidden = is_hidden
        self.slot = slot
        self.ability = MinimalResource(**ability) if ability is not None else None


class PokemonCries(Resource):
    latest: str
    legacy: Optional[str]

    def __init__(self, *, latest: str, legacy: Optional[str]) -> None:
        self.latest = latest
        self.legacy = legacy


class PokemonType(Resource):
    slot: int
    type: MinimalResource["NaturalGiftType"]

    def __init__(
        self,
        *,
        slot: int,
        type: Dict[str, Any],
    ) -> None:
        self.slot = slot
        self.type = MinimalResource(**type)


class PokemonHeldItem(Resource):
    item: MinimalResource["Item"]
    version_details: List["PokemonHeldItemVersion"]

    def __init__(
        self,
        *,
        item: Dict[str, Any],
        version_details: List[Dict[str, Any]],
    ) -> None:
        self.item = MinimalResource(**item)
        self.version_details = [
            PokemonHeldItemVersion(**version_detail)
            for version_detail in version_details
        ]


class PokemonHeldItemVersion(Resource):
    rarity: int
    version: MinimalResource["Version"]

    def __init__(
        self,
        *,
        rarity: int,
        version: Dict[str, Any],
    ) -> None:
        self.rarity = rarity
        self.version = MinimalResource(**version)


class PokemonMove(Resource):
    move: MinimalResource["Version"]
    version_group_details: List["VersionGroupDetail"]

    def __init__(
        self,
        *,
        move: Dict[str, Any],
        version_group_details: List[Dict[str, Any]],
    ) -> None:
        self.move = MinimalResource(**move)
        self.version_group_details = [
            VersionGroupDetail(**version_group_detail)
            for version_group_detail in version_group_details
        ]


class PokemonMoveVersion(Resource):
    move_learn_method: MinimalResource["MoveLearnMethod"]
    version_group: MinimalResource["VersionGroup"]
    level_learned_at: int

    def __init__(
        self,
        *,
        move_learn_method: Dict[str, Any],
        version_group: Dict[str, Any],
        level_learned_at: int,
    ) -> None:
        self.move_learn_method = MinimalResource(**move_learn_method)
        self.version_group = MinimalResource(**version_group)
        self.level_learned_at = level_learned_at


class PokemonStat(Resource):
    base_stat: int
    effort: int
    stat: MinimalResource["PokemonStat"]

    def __init__(
        self,
        *,
        base_stat: int,
        effort: int,
        stat: Dict[str, Any],
    ) -> None:
        self.base_stat = base_stat
        self.effort = effort
        self.stat = MinimalResource(**stat)


class PastAbility(Resource):
    abilities: List["PokemonAbility"]
    generation: MinimalResource["Generation"]

    def __init__(
        self, *, abilities: List[Dict[str, Any]], generation: Dict[str, Any]
    ) -> None:
        self.ability = [PokemonAbility(**ability) for ability in abilities]
        self.generation = MinimalResource(**generation)


class PastStat(Resource):
    generation: MinimalResource["Generation"]
    stats: List["PokemonStat"]

    def __init__(
        self, *, generation: Dict[str, Any], stats: List[Dict[str, Any]]
    ) -> None:
        self.generation = MinimalResource(**generation)
        self.stats = [PokemonStat(**stat) for stat in stats]


class PastType(Resource):
    generation: MinimalResource["Generation"]
    types: List["PokemonType"]

    def __init__(
        self,
        *,
        generation: Dict[str, Any],
        types: List[Dict[str, Any]],
    ) -> None:
        self.generation = MinimalResource(**generation)
        self.types = [PokemonType(**type_) for type_ in types]


class PokemonLocationArea(Resource):
    location_area: MinimalResource["LocationArea"]
    version_details: List["VersionEncounterDetail"]

    def __init__(
        self,
        *,
        location_area: Dict[str, Any],
        version_details: List[Dict[str, Any]],
    ) -> None:
        self.location_area = MinimalResource(**location_area)
        self.version_details = [
            VersionEncounterDetail(**version_detail)
            for version_detail in version_details
        ]
