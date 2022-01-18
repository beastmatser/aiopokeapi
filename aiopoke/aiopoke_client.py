from typing import Union

from aiopoke.http_client import HttpClient
from aiopoke.objects.resources import (
    Ability,
    Berry,
    BerryFirmness,
    BerryFlavor,
    Characteristic,
    ContestEffect,
    ContestType,
    EggGroup,
    EncounterCondition,
    EncounterConditionValue,
    EncounterMethod,
    EvolutionChain,
    EvolutionTrigger,
    Gender,
    Generation,
    GrowthRate,
    Item,
    ItemAttribute,
    ItemCategory,
    ItemFlingEffect,
    ItemPocket,
    Location,
    LocationArea,
    Machine,
    Move,
    MoveAilment,
    MoveBatteStyle,
    MoveCategory,
    MoveDamageClass,
    MoveLearnMethod,
    MoveTarget,
    NaturalGiftType,
    Nature,
    PalParkArea,
    PokeathlonStat,
    Pokedex,
    Pokemon,
    PokemonColor,
    PokemonForm,
    PokemonHabitat,
    PokemonShape,
    PokemonSpecies,
    Region,
    Stat,
    SuperContestEffect,
    Version,
    VersionGroup,
)
from aiopoke.objects.utility import Sprite
from aiopoke.objects.utility.language import Language
from aiopoke.utils import Cache, Url, cache

ENDPOINTS = {
    "ability",
    "berry",
    "berry-firmness",
    "berry-flavor",
    "characteristic",
    "contest-effect",
    "contest-type",
    "egg-group",
    "encounter-condition",
    "encounter-condition-value",
    "encounter-method",
    "evolution-chain",
    "evolution-trigger",
    "gender",
    "generation",
    "growth-rate",
    "item",
    "item-attribute",
    "item-category",
    "item-fling-effect",
    "item-pocket",
    "language",
    "location",
    "location-area",
    "machine",
    "move",
    "move-ailment",
    "move-battle-style",
    "move-category",
    "move-damage-class",
    "move-learn-method",
    "move-target",
    "nature",
    "pal-park-area",
    "pokeathlon-stat",
    "pokedex",
    "pokemon",
    "pokemon-color",
    "pokemon-form",
    "pokemon-habitat",
    "pokemon-shape",
    "pokemon-species",
    "region",
    "stat",
    "super-contest-effect",
    "type",
    "version",
    "version-group",
}


class AiopokeClient:
    http: HttpClient
    _cache: Cache

    def __init__(self, *, session=None) -> None:
        self.http = HttpClient(session=session)
        self._cache = Cache()
        Url.link(self)
        Sprite.link(self)

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        await self.close()

    async def close(self):
        await self.http.close()

    @cache("ability")
    async def get_ability(self, name_or_id) -> Ability:
        data = await self.http.get(f"ability/{name_or_id}")
        return Ability(**data)

    @cache("berry")
    async def get_berry(self, name_or_id) -> Berry:
        data = await self.http.get(f"berry/{name_or_id}")
        return Berry(**data)

    @cache("berry-flavor")
    async def get_berry_flavor(self, name_or_id) -> BerryFlavor:
        data = await self.http.get(f"berry-flavor/{name_or_id}")
        return BerryFlavor(**data)

    @cache("berry-firmness")
    async def get_berry_firmness(self, name_or_id) -> BerryFirmness:
        data = await self.http.get(f"berry-firmness/{name_or_id}")
        return BerryFirmness(**data)

    @cache("characteristic")
    async def get_characteristic(self, name_or_id) -> Characteristic:
        data = await self.http.get(f"characteristic/{name_or_id}")
        return Characteristic(**data)

    @cache("contest-effect")
    async def get_contest_effect(self, id_) -> ContestEffect:
        data = await self.http.get(f"contest-effect/{id_}")
        return ContestEffect(**data)

    @cache("contest-type")
    async def get_contest_type(self, name_or_id) -> ContestType:
        data = await self.http.get(f"contest-type/{name_or_id}")
        return ContestType(**data)

    @cache("egg-group")
    async def get_egg_group(self, name_or_id) -> EggGroup:
        data = await self.http.get(f"egg-group/{name_or_id}")
        return EggGroup(**data)

    @cache("encounter-condition")
    async def get_encounter_condition(self, name_or_id) -> EncounterCondition:
        data = await self.http.get(f"encounter-condition/{name_or_id}")
        return EncounterCondition(**data)

    @cache("encounter-condition-value")
    async def get_encounter_condition_value(
        self, name_or_id
    ) -> EncounterConditionValue:
        data = await self.http.get(f"encounter-condition-value/{name_or_id}")
        return EncounterConditionValue(**data)

    @cache("encounter-method")
    async def get_encounter_method(self, name_or_id) -> EncounterMethod:
        data = await self.http.get(f"encounter-method/{name_or_id}")
        return EncounterMethod(**data)

    @cache("evolution-chain")
    async def get_evolution_chain(self, id_) -> EvolutionChain:
        data = await self.http.get(f"evolution-chain/{id_}")
        return EvolutionChain(**data)

    @cache("evolution-trigger")
    async def get_evolution_trigger(self, id_) -> EvolutionTrigger:
        data = await self.http.get(f"evolution-trigger/{id_}")
        return EvolutionTrigger(**data)

    @cache("gender")
    async def get_gender(self, name_or_id) -> Gender:
        data = await self.http.get(f"gender/{name_or_id}")
        return Gender(**data)

    @cache("generation")
    async def get_generation(self, name_or_id) -> Generation:
        data = await self.http.get(f"generation/{name_or_id}")
        return Generation(**data)

    @cache("growth-rate")
    async def get_growth_rate(self, name_or_id) -> GrowthRate:
        data = await self.http.get(f"growth-rate/{name_or_id}")
        return GrowthRate(**data)

    @cache("item")
    async def get_item(self, name_or_id) -> Item:
        data = await self.http.get(f"item/{name_or_id}")
        return Item(**data)

    @cache("item-attribute")
    async def get_item_attribute(self, name_or_id) -> ItemAttribute:
        data = await self.http.get(f"item-attribute/{name_or_id}")
        return ItemAttribute(**data)

    @cache("item-category")
    async def get_item_category(self, name_or_id) -> ItemCategory:
        data = await self.http.get(f"item-category/{name_or_id}")
        return ItemCategory(**data)

    @cache("item-fling-effect")
    async def get_item_fling_effect(self, name_or_id) -> ItemFlingEffect:
        data = await self.http.get(f"item-fling-effect/{name_or_id}")
        return ItemFlingEffect(**data)

    @cache("item-pocket")
    async def get_item_pocket(self, name_or_id) -> ItemPocket:
        data = await self.http.get(f"item-pocket/{name_or_id}")
        return ItemPocket(**data)

    @cache("language")
    async def get_language(self, name_or_id: Union[str, int]) -> Language:
        data = await self.http.get(f"language/{name_or_id}")
        return Language(**data)

    @cache("location")
    async def get_location(self, name_or_id) -> Location:
        data = await self.http.get(f"location/{name_or_id}")
        return Location(**data)

    @cache("location-area")
    async def get_location_area(self, name_or_id) -> LocationArea:
        data = await self.http.get(f"location-area/{name_or_id}")
        return LocationArea(**data)

    @cache("machine")
    async def get_machine(self, name_or_id) -> Machine:
        data = await self.http.get(f"machine/{name_or_id}")
        return Machine(**data)

    @cache("move")
    async def get_move(self, name_or_id) -> Move:
        data = await self.http.get(f"move/{name_or_id}")
        return Move(**data)

    @cache("move-ailment")
    async def get_move_ailment(self, name_or_id) -> MoveAilment:
        data = await self.http.get(f"move-ailment/{name_or_id}")
        return MoveAilment(**data)

    @cache("move-battle-style")
    async def get_move_battle_style(self, name_or_id) -> MoveBatteStyle:
        data = await self.http.get(f"move-battle-style/{name_or_id}")
        return MoveBatteStyle(**data)

    @cache("move-category")
    async def get_move_category(self, name_or_id) -> MoveCategory:
        data = await self.http.get(f"move-category/{name_or_id}")
        return MoveCategory(**data)

    @cache("move-damage-class")
    async def get_move_damage_class(self, name_or_id) -> MoveDamageClass:
        data = await self.http.get(f"move-damage-class/{name_or_id}")
        return MoveDamageClass(**data)

    @cache("move-learn-method")
    async def get_move_learn_method(self, name_or_id) -> MoveLearnMethod:
        data = await self.http.get(f"move-learn-method/{name_or_id}")
        return MoveLearnMethod(**data)

    @cache("move-target")
    async def get_move_target(self, name_or_id) -> MoveTarget:
        data = await self.http.get(f"move-target/{name_or_id}")
        return MoveTarget(**data)

    @cache("nature")
    async def get_nature(self, name_or_id) -> Nature:
        data = await self.http.get(f"nature/{name_or_id}")
        return Nature(**data)

    @cache("pal-park-area")
    async def get_pal_park_area(self, name_or_id) -> PalParkArea:
        data = await self.http.get(f"pal-park-area/{name_or_id}")
        return PalParkArea(**data)

    @cache("pokeathlon-stat")
    async def get_pokeathlon_stat(self, name_or_id) -> PokeathlonStat:
        data = await self.http.get(f"pokeathlon-stat/{name_or_id}")
        return PokeathlonStat(**data)

    @cache("pokedex")
    async def get_pokedex(self, name_or_id) -> Pokedex:
        data = await self.http.get(f"pokedex/{name_or_id}")
        return Pokedex(**data)

    @cache("pokemon")
    async def get_pokemon(self, name_or_id) -> Pokemon:
        data = await self.http.get(f"pokemon/{name_or_id}")
        data["location_area_encounters"] = await self.http.get(
            f"pokemon/{data['id']}/encounters"
        )
        return Pokemon(**data)

    @cache("pokemon-color")
    async def get_pokemon_color(self, name_or_id) -> PokemonColor:
        data = await self.http.get(f"pokemon-color/{name_or_id}")
        return PokemonColor(**data)

    @cache("pokemon-form")
    async def get_pokemon_form(self, name_or_id) -> PokemonForm:
        data = await self.http.get(f"pokemon-form/{name_or_id}")
        return PokemonForm(**data)

    @cache("pokemon-habitat")
    async def get_pokemon_habitat(self, name_or_id) -> PokemonHabitat:
        data = await self.http.get(f"pokemon-habitat/{name_or_id}")
        return PokemonHabitat(**data)

    @cache("pokemon-shape")
    async def get_pokemon_shape(self, name_or_id) -> PokemonShape:
        data = await self.http.get(f"pokemon-shape/{name_or_id}")
        return PokemonShape(**data)

    @cache("pokemon-species")
    async def get_pokemon_species(self, name_or_id) -> PokemonSpecies:
        data = await self.http.get(f"pokemon-species/{name_or_id}")
        return PokemonSpecies(**data)

    @cache("region")
    async def get_region(self, name_or_id) -> Region:
        data = await self.http.get(f"region/{name_or_id}")
        return Region(**data)

    @cache("stat")
    async def get_stat(self, name_or_id) -> Stat:
        data = await self.http.get(f"stat/{name_or_id}")
        return Stat(**data)

    @cache("super-contest-effect")
    async def get_super_contest_effect(self, name_or_id) -> SuperContestEffect:
        data = await self.http.get(f"super-contest-effect/{name_or_id}")
        return SuperContestEffect(**data)

    @cache("type")
    async def get_type(self, name_or_id) -> NaturalGiftType:
        data = await self.http.get(f"type/{name_or_id}")
        return NaturalGiftType(**data)

    @cache("version")
    async def get_version(self, name_or_id) -> Version:
        data = await self.http.get(f"version/{name_or_id}")
        return Version(**data)

    @cache("version-group")
    async def get_version_group(self, name_or_id) -> VersionGroup:
        data = await self.http.get(f"version-group/{name_or_id}")
        return VersionGroup(**data)
