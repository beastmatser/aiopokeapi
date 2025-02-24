import asyncio

from typing import Union

from aiopoke.http_client import HttpClient
from aiopoke.objects.resources import Ability
from aiopoke.objects.resources import Berry
from aiopoke.objects.resources import BerryFirmness
from aiopoke.objects.resources import BerryFlavor
from aiopoke.objects.resources import Characteristic
from aiopoke.objects.resources import ContestEffect
from aiopoke.objects.resources import ContestType
from aiopoke.objects.resources import EggGroup
from aiopoke.objects.resources import EncounterCondition
from aiopoke.objects.resources import EncounterConditionValue
from aiopoke.objects.resources import EncounterMethod
from aiopoke.objects.resources import EvolutionChain
from aiopoke.objects.resources import EvolutionTrigger
from aiopoke.objects.resources import Gender
from aiopoke.objects.resources import Generation
from aiopoke.objects.resources import GrowthRate
from aiopoke.objects.resources import Item
from aiopoke.objects.resources import ItemAttribute
from aiopoke.objects.resources import ItemCategory
from aiopoke.objects.resources import ItemFlingEffect
from aiopoke.objects.resources import ItemPocket
from aiopoke.objects.resources import Location
from aiopoke.objects.resources import LocationArea
from aiopoke.objects.resources import Machine
from aiopoke.objects.resources import Move
from aiopoke.objects.resources import MoveAilment
from aiopoke.objects.resources import MoveBatteStyle
from aiopoke.objects.resources import MoveCategory
from aiopoke.objects.resources import MoveDamageClass
from aiopoke.objects.resources import MoveLearnMethod
from aiopoke.objects.resources import MoveTarget
from aiopoke.objects.resources import NaturalGiftType
from aiopoke.objects.resources import Nature
from aiopoke.objects.resources import PalParkArea
from aiopoke.objects.resources import PokeathlonStat
from aiopoke.objects.resources import Pokedex
from aiopoke.objects.resources import Pokemon
from aiopoke.objects.resources import PokemonColor
from aiopoke.objects.resources import PokemonForm
from aiopoke.objects.resources import PokemonHabitat
from aiopoke.objects.resources import PokemonShape
from aiopoke.objects.resources import PokemonSpecies
from aiopoke.objects.resources import Region
from aiopoke.objects.resources import Stat
from aiopoke.objects.resources import SuperContestEffect
from aiopoke.objects.resources import Version
from aiopoke.objects.resources import VersionGroup
from aiopoke.objects.utility import Sprite
from aiopoke.objects.utility.language import Language
from aiopoke.utils import Cache
from aiopoke.utils import cache
from aiopoke.utils import Url


class MetaClient(type):
    def __new__(cls, name, bases, clsdict):
        for key, value in clsdict.items():
            if not hasattr(value, "__qualname__"):
                continue

            if key.startswith("get") and value.__qualname__.startswith("AiopokeClient"):
                endpoint = value.__name__.split("get_")[1].replace("_", "-")
                clsdict[key] = cache(endpoint, value)

        return super().__new__(cls, name, bases, clsdict)


class AiopokeClient(metaclass=MetaClient):
    http: HttpClient
    _cache: Cache

    def __init__(self, *, session=None, base_url="https://pokeapi.co/api/v2") -> None:
        self.http = HttpClient(session=session, base_url=base_url)
        self._cache = Cache()
        Url.link(self)
        Sprite.link(self)

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        await self.close()

    async def close(self):
        await self.http.close()

    async def get_ability(self, name_or_id: Union[str, int]) -> Ability:
        data = await self.http.get(f"ability/{name_or_id}")
        return Ability(**data)

    async def get_berry(self, name_or_id: Union[str, int]) -> Berry:
        data = await self.http.get(f"berry/{name_or_id}")
        return Berry(**data)

    async def get_berry_flavor(self, name_or_id: Union[str, int]) -> BerryFlavor:
        data = await self.http.get(f"berry-flavor/{name_or_id}")
        return BerryFlavor(**data)

    async def get_berry_firmness(self, name_or_id: Union[str, int]) -> BerryFirmness:
        data = await self.http.get(f"berry-firmness/{name_or_id}")
        return BerryFirmness(**data)

    async def get_characteristic(self, id: int) -> Characteristic:
        data = await self.http.get(f"characteristic/{id}")
        return Characteristic(**data)

    async def get_contest_effect(self, id: int) -> ContestEffect:
        data = await self.http.get(f"contest-effect/{id}")
        return ContestEffect(**data)

    async def get_contest_type(self, name_or_id: Union[str, int]) -> ContestType:
        data = await self.http.get(f"contest-type/{name_or_id}")
        return ContestType(**data)

    async def get_egg_group(self, name_or_id: Union[str, int]) -> EggGroup:
        data = await self.http.get(f"egg-group/{name_or_id}")
        return EggGroup(**data)

    async def get_encounter_condition(
        self, name_or_id: Union[str, int]
    ) -> EncounterCondition:
        data = await self.http.get(f"encounter-condition/{name_or_id}")
        return EncounterCondition(**data)

    async def get_encounter_condition_value(
        self, name_or_id
    ) -> EncounterConditionValue:
        data = await self.http.get(f"encounter-condition-value/{name_or_id}")
        return EncounterConditionValue(**data)

    async def get_encounter_method(
        self, name_or_id: Union[str, int]
    ) -> EncounterMethod:
        data = await self.http.get(f"encounter-method/{name_or_id}")
        return EncounterMethod(**data)

    async def get_evolution_chain(self, id: int) -> EvolutionChain:
        data = await self.http.get(f"evolution-chain/{id}")
        return EvolutionChain(**data)

    async def get_evolution_trigger(self, id: int) -> EvolutionTrigger:
        data = await self.http.get(f"evolution-trigger/{id}")
        return EvolutionTrigger(**data)

    async def get_gender(self, name_or_id: Union[str, int]) -> Gender:
        data = await self.http.get(f"gender/{name_or_id}")
        return Gender(**data)

    async def get_generation(self, name_or_id: Union[str, int]) -> Generation:
        data = await self.http.get(f"generation/{name_or_id}")
        return Generation(**data)

    async def get_growth_rate(self, name_or_id: Union[str, int]) -> GrowthRate:
        data = await self.http.get(f"growth-rate/{name_or_id}")
        return GrowthRate(**data)

    async def get_item(self, name_or_id: Union[str, int]) -> Item:
        data = await self.http.get(f"item/{name_or_id}")
        return Item(**data)

    async def get_item_attribute(self, name_or_id: Union[str, int]) -> ItemAttribute:
        data = await self.http.get(f"item-attribute/{name_or_id}")
        return ItemAttribute(**data)

    async def get_item_category(self, name_or_id: Union[str, int]) -> ItemCategory:
        data = await self.http.get(f"item-category/{name_or_id}")
        return ItemCategory(**data)

    async def get_item_fling_effect(
        self, name_or_id: Union[str, int]
    ) -> ItemFlingEffect:
        data = await self.http.get(f"item-fling-effect/{name_or_id}")
        return ItemFlingEffect(**data)

    async def get_item_pocket(self, name_or_id: Union[str, int]) -> ItemPocket:
        data = await self.http.get(f"item-pocket/{name_or_id}")
        return ItemPocket(**data)

    async def get_language(self, name_or_id: Union[str, int]) -> Language:
        data = await self.http.get(f"language/{name_or_id}")
        return Language(**data)

    async def get_location(self, name_or_id: Union[str, int]) -> Location:
        data = await self.http.get(f"location/{name_or_id}")
        return Location(**data)

    async def get_location_area(self, name_or_id: Union[str, int]) -> LocationArea:
        data = await self.http.get(f"location-area/{name_or_id}")
        return LocationArea(**data)

    async def get_machine(self, id: int) -> Machine:
        data = await self.http.get(f"machine/{id}")
        return Machine(**data)

    async def get_move(self, name_or_id: Union[str, int]) -> Move:
        data = await self.http.get(f"move/{name_or_id}")
        return Move(**data)

    async def get_move_ailment(self, name_or_id: Union[str, int]) -> MoveAilment:
        data = await self.http.get(f"move-ailment/{name_or_id}")
        return MoveAilment(**data)

    async def get_move_battle_style(
        self, name_or_id: Union[str, int]
    ) -> MoveBatteStyle:
        data = await self.http.get(f"move-battle-style/{name_or_id}")
        return MoveBatteStyle(**data)

    async def get_move_category(self, name_or_id: Union[str, int]) -> MoveCategory:
        data = await self.http.get(f"move-category/{name_or_id}")
        return MoveCategory(**data)

    async def get_move_damage_class(
        self, name_or_id: Union[str, int]
    ) -> MoveDamageClass:
        data = await self.http.get(f"move-damage-class/{name_or_id}")
        return MoveDamageClass(**data)

    async def get_move_learn_method(
        self, name_or_id: Union[str, int]
    ) -> MoveLearnMethod:
        data = await self.http.get(f"move-learn-method/{name_or_id}")
        return MoveLearnMethod(**data)

    async def get_move_target(self, name_or_id: Union[str, int]) -> MoveTarget:
        data = await self.http.get(f"move-target/{name_or_id}")
        return MoveTarget(**data)

    async def get_nature(self, name_or_id: Union[str, int]) -> Nature:
        data = await self.http.get(f"nature/{name_or_id}")
        return Nature(**data)

    async def get_pal_park_area(self, name_or_id: Union[str, int]) -> PalParkArea:
        data = await self.http.get(f"pal-park-area/{name_or_id}")
        return PalParkArea(**data)

    async def get_pokeathlon_stat(self, name_or_id: Union[str, int]) -> PokeathlonStat:
        data = await self.http.get(f"pokeathlon-stat/{name_or_id}")
        return PokeathlonStat(**data)

    async def get_pokedex(self, name_or_id: Union[str, int]) -> Pokedex:
        data = await self.http.get(f"pokedex/{name_or_id}")
        return Pokedex(**data)

    async def get_pokemon(self, name_or_id: Union[str, int]) -> Pokemon:
        tasks = [
            self.http.get(f"pokemon/{name_or_id}"),
            self.http.get(f"pokemon/{name_or_id}/encounters"),
        ]
        results = await asyncio.gather(*tasks)
        data = results[0]
        data["location_area_encounters"] = results[1]
        return Pokemon(**data)

    async def get_pokemon_color(self, name_or_id: Union[str, int]) -> PokemonColor:
        data = await self.http.get(f"pokemon-color/{name_or_id}")
        return PokemonColor(**data)

    async def get_pokemon_form(self, name_or_id: Union[str, int]) -> PokemonForm:
        data = await self.http.get(f"pokemon-form/{name_or_id}")
        return PokemonForm(**data)

    async def get_pokemon_habitat(self, name_or_id: Union[str, int]) -> PokemonHabitat:
        data = await self.http.get(f"pokemon-habitat/{name_or_id}")
        return PokemonHabitat(**data)

    async def get_pokemon_shape(self, name_or_id: Union[str, int]) -> PokemonShape:
        data = await self.http.get(f"pokemon-shape/{name_or_id}")
        return PokemonShape(**data)

    async def get_pokemon_species(self, name_or_id: Union[str, int]) -> PokemonSpecies:
        data = await self.http.get(f"pokemon-species/{name_or_id}")
        return PokemonSpecies(**data)

    async def get_region(self, name_or_id: Union[str, int]) -> Region:
        data = await self.http.get(f"region/{name_or_id}")
        return Region(**data)

    async def get_stat(self, name_or_id: Union[str, int]) -> Stat:
        data = await self.http.get(f"stat/{name_or_id}")
        return Stat(**data)

    async def get_super_contest_effect(
        self, name_or_id: Union[str, int]
    ) -> SuperContestEffect:
        data = await self.http.get(f"super-contest-effect/{name_or_id}")
        return SuperContestEffect(**data)

    async def get_type(self, name_or_id: Union[str, int]) -> NaturalGiftType:
        data = await self.http.get(f"type/{name_or_id}")
        return NaturalGiftType(**data)

    async def get_version(self, name_or_id: Union[str, int]) -> Version:
        data = await self.http.get(f"version/{name_or_id}")
        return Version(**data)

    async def get_version_group(self, name_or_id: Union[str, int]) -> VersionGroup:
        data = await self.http.get(f"version-group/{name_or_id}")
        return VersionGroup(**data)
