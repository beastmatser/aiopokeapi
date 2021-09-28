import aiohttp
from typing import Any, Callable, Dict, Optional, Union


from .cache import Cache, cache
from .resources import (
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
from .utility.language import Language

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
    __instance: Optional["AiopokeClient"] = None

    session: Optional["aiohttp.ClientSession"]

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, *, session=None) -> None:
        self.session = session
        self._cache = Cache()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, exc_traceback):
        await self._close()

    async def _close(self):
        if self.session is None:
            return

        await self.session.close()

    def build(self, endpoint: str, data: Dict[str, Any]) -> Any:
        """Returns a constructed object via json-formatted data"""
        build_map: Dict[str, Callable[[Dict[str, Any]], Any]] = {
            "ability": lambda data: Ability(data),
            "berry": lambda data: Berry(data),
            "berry-firmness": lambda data: BerryFirmness(data),
            "berry-flavor": lambda data: BerryFlavor(data),
            "characteristic": lambda data: Characteristic(data),
            "contest-effect": lambda data: ContestEffect(data),
            "contest-type": lambda data: ContestType(data),
            "egg-group": lambda data: EggGroup(data),
            "encounter-condition": lambda data: EncounterCondition(data),
            "encounter-condition-value": lambda data: EncounterConditionValue(data),
            "encounter-method": lambda data: EncounterMethod(data),
            "evolution-chain": lambda data: EvolutionChain(data),
            "evolution-trigger": lambda data: EvolutionTrigger(data),
            "gender": lambda data: Gender(data),
            "generation": lambda data: Generation(data),
            "growth-rate": lambda data: GrowthRate(data),
            "item": lambda data: Item(data),
            "item-attribute": lambda data: ItemAttribute(data),
            "item-category": lambda data: ItemCategory(data),
            "item-fling-effect": lambda data: ItemFlingEffect(data),
            "item-pocket": lambda data: ItemPocket(data),
            "language": lambda data: Language(data),
            "location": lambda data: Location(data),
            "location-area": lambda data: LocationArea(data),
            "machine": lambda data: Machine(data),
            "move": lambda data: Move(data),
            "move-ailment": lambda data: MoveAilment(data),
            "move-battle-style": lambda data: MoveBatteStyle(data),
            "move-category": lambda data: MoveCategory(data),
            "move-damage-class": lambda data: MoveDamageClass(data),
            "move-learn-method": lambda data: MoveLearnMethod(data),
            "move-target": lambda data: MoveTarget(data),
            "nature": lambda data: Nature(data),
            "pal-park-area": lambda data: PalParkArea(data),
            "pokeathlon-stat": lambda data: PokeathlonStat(data),
            "pokedex": lambda data: Pokedex(data),
            "pokemon": lambda data: Pokemon(data),
            "pokemon-color": lambda data: PokemonColor(data),
            "pokemon-form": lambda data: PokemonForm(data),
            "pokemon-habitat": lambda data: PokemonHabitat(data),
            "pokemon-shape": lambda data: PokemonShape(data),
            "pokemon-species": lambda data: PokemonSpecies(data),
            "region": lambda data: Region(data),
            "stat": lambda data: Stat(data),
            "super-contest-effect": lambda data: SuperContestEffect(data),
            "type": lambda data: NaturalGiftType(data),
            "version": lambda data: Version(data),
            "version-group": lambda data: VersionGroup(data),
        }
        return build_map[endpoint](data)

    @cache
    async def _fetch(self, endpoint: str, name_or_id: Union[str, int]) -> Dict[str, Any]:
        endpoint = endpoint.lower().replace(" ", "-")
        if endpoint not in ENDPOINTS:
            raise ValueError(f"'{endpoint}' is not a valid endpoint")

        if self.session is None:
            self.session = aiohttp.ClientSession()

        url = f"https://pokeapi.co/api/v2/{endpoint}/{name_or_id}"
        async with self.session.get(url) as response:
            try:
                data: Dict[str, Any] = await response.json()
            except aiohttp.ContentTypeError:
                raise ValueError(f"An invalid value for '{endpoint}' was passed in")

        return data

    async def fetch_ability(self, name_or_id) -> Ability:
        data = await self._fetch("ability", name_or_id)
        return Ability(data)

    async def fetch_berry(self, name_or_id) -> Berry:
        data = await self._fetch("berry", name_or_id)
        return Berry(data)

    async def fetch_berry_flavor(self, name_or_id) -> BerryFlavor:
        data = await self._fetch("berry-flavor", name_or_id)
        return BerryFlavor(data)

    async def fetch_berry_firmness(self, name_or_id) -> BerryFirmness:
        data = await self._fetch("berry-firmness", name_or_id)
        return BerryFirmness(data)

    async def fetch_characteristic(self, name_or_id) -> Characteristic:
        data = await self._fetch("characteristic", name_or_id)
        return Characteristic(data)

    async def fetch_contest_effect(self, id_) -> ContestEffect:
        data = await self._fetch("contest-effect", id_)
        return ContestEffect(data)

    async def fetch_contest_type(self, name_or_id) -> ContestType:
        data = await self._fetch("contest-type", name_or_id)
        return ContestType(data)

    async def fetch_egg_group(self, name_or_id) -> EggGroup:
        data = await self._fetch("egg-group", name_or_id)
        return EggGroup(data)

    async def fetch_encounter_condition(self, name_or_id) -> EncounterCondition:
        data = await self._fetch("encounter-condition", name_or_id)
        return EncounterCondition(data)

    async def fetch_encounter_condition_value(
        self, name_or_id
    ) -> EncounterConditionValue:
        data = await self._fetch("encounter-condition-value", name_or_id)
        return EncounterConditionValue(data)

    async def fetch_encounter_method(self, name_or_id) -> EncounterMethod:
        data = await self._fetch("encounter-method", name_or_id)
        return EncounterMethod(data)

    async def fetch_evolution_chain(self, id_) -> EvolutionChain:
        data = await self._fetch("evolution-chain", id_)
        return EvolutionChain(data)

    async def fetch_evolution_trigger(self, id_) -> EvolutionTrigger:
        data = await self._fetch("evolution-trigger", id_)
        return EvolutionTrigger(data)

    async def fetch_gender(self, name_or_id) -> Gender:
        data = await self._fetch("gender", name_or_id)
        return Gender(data)

    async def fetch_generation(self, name_or_id) -> Generation:
        data = await self._fetch("generation", name_or_id)
        return Generation(data)

    async def fetch_growth_rate(self, name_or_id) -> GrowthRate:
        data = await self._fetch("growth-rate", name_or_id)
        return GrowthRate(data)

    async def fetch_item(self, name_or_id) -> Item:
        data = await self._fetch("item", name_or_id)
        return Item(data)

    async def fetch_item_attribute(self, name_or_id) -> ItemAttribute:
        data = await self._fetch("item-attribute", name_or_id)
        return ItemAttribute(data)

    async def fetch_item_category(self, name_or_id) -> ItemCategory:
        data = await self._fetch("item-category", name_or_id)
        return ItemCategory(data)

    async def fetch_item_fling_effect(self, name_or_id) -> ItemFlingEffect:
        data = await self._fetch("item-fling-effect", name_or_id)
        return ItemFlingEffect(data)

    async def fetch_item_pocket(self, name_or_id) -> ItemPocket:
        data = await self._fetch("item-pocket", name_or_id)
        return ItemPocket(data)

    async def fetch_location(self, name_or_id) -> Location:
        data = await self._fetch("location", name_or_id)
        return Location(data)

    async def fetch_location_area(self, name_or_id) -> LocationArea:
        data = await self._fetch("location-area", name_or_id)
        return LocationArea(data)

    async def fetch_machine(self, name_or_id) -> Machine:
        data = await self._fetch("machine", name_or_id)
        return Machine(data)

    async def fetch_move(self, name_or_id) -> Move:
        data = await self._fetch("move", name_or_id)
        return Move(data)

    async def fetch_move_ailment(self, name_or_id) -> MoveAilment:
        data = await self._fetch("move-ailment", name_or_id)
        return MoveAilment(data)

    async def fetch_move_battle_style(self, name_or_id) -> MoveBatteStyle:
        data = await self._fetch("move-battle-style", name_or_id)
        return MoveBatteStyle(data)

    async def fetch_move_category(self, name_or_id) -> MoveCategory:
        data = await self._fetch("move-category", name_or_id)
        return MoveCategory(data)

    async def fetch_move_damage_class(self, name_or_id) -> MoveDamageClass:
        data = await self._fetch("move-damage-class", name_or_id)
        return MoveDamageClass(data)

    async def fetch_move_learn_method(self, name_or_id) -> MoveLearnMethod:
        data = await self._fetch("move-learn-method", name_or_id)
        return MoveLearnMethod(data)

    async def fetch_move_target(self, name_or_id) -> MoveTarget:
        data = await self._fetch("move-target", name_or_id)
        return MoveTarget(data)

    async def fetch_nature(self, name_or_id) -> Nature:
        data = await self._fetch("nature", name_or_id)
        return Nature(data)

    async def fetch_pal_park_area(self, name_or_id) -> PalParkArea:
        data = await self._fetch("pal-park-area", name_or_id)
        return PalParkArea(data)

    async def fetch_pokeathlon_stat(self, name_or_id) -> PokeathlonStat:
        data = await self._fetch("pokeathlon-stat", name_or_id)
        return PokeathlonStat(data)

    async def fetch_pokedex(self, name_or_id) -> Pokedex:
        data = await self._fetch("pokedex", name_or_id)
        return Pokedex(data)

    async def fetch_pokemon(self, name_or_id) -> Pokemon:
        data = await self._fetch("pokemon", name_or_id)
        return Pokemon(data)

    async def fetch_pokemon_color(self, name_or_id) -> PokemonColor:
        data = await self._fetch("pokemon-color", name_or_id)
        return PokemonColor(data)

    async def fetch_pokemon_form(self, name_or_id) -> PokemonForm:
        data = await self._fetch("pokemon-form", name_or_id)
        return PokemonForm(data)

    async def fetch_pokemon_habitat(self, name_or_id) -> PokemonHabitat:
        data = await self._fetch("pokemon-habitat", name_or_id)
        return PokemonHabitat(data)

    async def fetch_pokemon_shape(self, name_or_id) -> PokemonShape:
        data = await self._fetch("pokemon-shape", name_or_id)
        return PokemonShape(data)

    async def fetch_pokemon_species(self, name_or_id) -> PokemonSpecies:
        data = await self._fetch("pokemon-species", name_or_id)
        return PokemonSpecies(data)

    async def fetch_region(self, name_or_id) -> Region:
        data = await self._fetch("region", name_or_id)
        return Region(data)

    async def fetch_stat(self, name_or_id) -> Stat:
        data = await self._fetch("stat", name_or_id)
        return Stat(data)

    async def fetch_super_contest_effect(self, name_or_id) -> SuperContestEffect:
        data = await self._fetch("super-contest-effect", name_or_id)
        return SuperContestEffect(data)

    async def fetch_type(self, name_or_id) -> NaturalGiftType:
        data = await self._fetch("type", name_or_id)
        return NaturalGiftType(data)

    async def fetch_natural_gift_type(self, name_or_id) -> NaturalGiftType:
        data = await self._fetch("type", name_or_id)
        return NaturalGiftType(data)

    async def fetch_version(self, name_or_id) -> Version:
        data = await self._fetch("version", name_or_id)
        return Version(data)

    async def fetch_version_group(self, name_or_id) -> VersionGroup:
        data = await self._fetch("version-group", name_or_id)
        return VersionGroup(data)
