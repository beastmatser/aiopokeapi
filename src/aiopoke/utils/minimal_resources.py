from dataclasses import field
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Coroutine,
    Dict,
    Generic,
    Optional,
    TypeVar,
    Union,
)

from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.aiopoke_client import AiopokeClient

T = TypeVar("T")


class Url(Resource, Generic[T]):
    url: str
    id: int
    endpoint: str

    _client: Optional["AiopokeClient"] = field(default=None, repr=False)

    def __init__(self, url: str) -> None:
        self.url = url

        self.id = int(self.url.split("/")[-2])
        self.endpoint = self.url.split("/")[-3]

    @property
    def client(self) -> Optional["AiopokeClient"]:
        if hasattr(self, "_client"):
            return self._client
        return None

    @classmethod
    def link(cls, client):
        cls._client = client

    async def fetch(self, *, client: Optional["AiopokeClient"] = None) -> T:
        client = self.client or client
        if client is None:
            raise ValueError(
                "A client must be provided, if you create your own instances of this class"
            )

        build_map: Dict[str, Callable[[Union[str, int]], Coroutine[Any, Any, Any]]] = {
            "ability": client.get_ability,
            "berry": client.get_berry,
            "berry-firmness": client.get_berry_firmness,
            "berry-flavor": client.get_berry_flavor,
            "characteristic": client.get_characteristic,
            "contest-effect": client.get_contest_effect,
            "contest-type": client.get_contest_type,
            "egg-group": client.get_egg_group,
            "encounter-condition": client.get_encounter_condition,
            "encounter-condition-value": client.get_encounter_condition_value,
            "encounter-method": client.get_encounter_method,
            "evolution-chain": client.get_evolution_chain,
            "evolution-trigger": client.get_evolution_trigger,
            "gender": client.get_gender,
            "generation": client.get_generation,
            "growth-rate": client.get_growth_rate,
            "item": client.get_item,
            "item-attribute": client.get_item_attribute,
            "item-category": client.get_item_category,
            "item-fling-effect": client.get_item_fling_effect,
            "item-pocket": client.get_item_pocket,
            "language": client.get_language,
            "location": client.get_location,
            "location-area": client.get_location_area,
            "machine": client.get_machine,
            "move": client.get_move,
            "move-ailment": client.get_move_ailment,
            "move-battle-style": client.get_move_battle_style,
            "move-category": client.get_move_category,
            "move-damage-class": client.get_move_damage_class,
            "move-learn-method": client.get_move_learn_method,
            "move-target": client.get_move_target,
            "nature": client.get_nature,
            "pal-park-area": client.get_pal_park_area,
            "pokeathlon-stat": client.get_pokeathlon_stat,
            "pokedex": client.get_pokedex,
            "pokemon": client.get_pokemon,
            "pokemon-color": client.get_pokemon_color,
            "pokemon-form": client.get_pokemon_form,
            "pokemon-habitat": client.get_pokemon_habitat,
            "pokemon-shape": client.get_pokemon_shape,
            "pokemon-species": client.get_pokemon_species,
            "region": client.get_region,
            "stat": client.get_stat,
            "super-contest-effect": client.get_super_contest_effect,
            "type": client.get_type,
            "version": client.get_version,
            "version-group": client.get_version_group,
        }

        obj: T = await build_map[self.endpoint](self.id)
        return obj


class MinimalResource(Url[T]):
    name: str
    url: str
    id: int
    endpoint: str

    def __init__(self, name: str, url: str) -> None:
        super().__init__(url=url)
        self.name = name
