from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Coroutine,
    Dict,
    Optional,
    TypeVar,
    Union,
)

if TYPE_CHECKING:
    from aiopoke.aiopoke_client import AiopokeClient

U = TypeVar("U")


# cache decorator
def cache(
    endpoint: str,
) -> Callable[
    [Callable[["AiopokeClient", Union[str, int]], Coroutine[Any, Any, U]]],
    Callable[["AiopokeClient", Union[str, int]], Coroutine[Any, Any, U]],
]:
    def outer(
        coro: Callable[["AiopokeClient", Union[str, int]], Coroutine[Any, Any, U]]
    ) -> Callable[["AiopokeClient", Union[str, int]], Coroutine[Any, Any, U]]:
        async def inner(client: "AiopokeClient", name_or_id: Union[str, int]) -> U:
            cached_item: Optional[U] = client._cache.get(endpoint, name_or_id)

            if cached_item is not None:
                return cached_item

            obj: U = await coro(client, name_or_id)
            client._cache.put(endpoint, name_or_id, obj)
            return obj

        return inner

    return outer


BASE_CACHE: Dict[str, Dict[str, Any]] = {
    "ability": {},
    "berry": {},
    "berry-firmness": {},
    "berry-flavor": {},
    "characteristic": {},
    "contest-effect": {},
    "contest-type": {},
    "egg-group": {},
    "encounter-condition": {},
    "encounter-condition-value": {},
    "encounter-method": {},
    "evolution-chain": {},
    "evolution-trigger": {},
    "gender": {},
    "generation": {},
    "growth-rate": {},
    "item": {},
    "item-attribute": {},
    "item-category": {},
    "item-fling-effect": {},
    "item-pocket": {},
    "language": {},
    "location": {},
    "location-area": {},
    "machine": {},
    "move": {},
    "move-ailment": {},
    "move-battle-style": {},
    "move-category": {},
    "move-damage-class": {},
    "move-learn-method": {},
    "move-target": {},
    "nature": {},
    "pal-park-area": {},
    "pokeathlon-stat": {},
    "pokedex": {},
    "pokemon": {},
    "pokemon-color": {},
    "pokemon-form": {},
    "pokemon-habitat": {},
    "pokemon-shape": {},
    "pokemon-species": {},
    "region": {},
    "stat": {},
    "super-contest-effect": {},
    "type": {},
    "version": {},
    "version-group": {},
}


class Cache:
    cache: Dict[str, Dict[str, Any]] = BASE_CACHE

    def get(self, endpoint: str, id: Union[str, int]) -> Any:
        return self.cache[endpoint].get(str(id))

    def put(self, endpoint: str, id: Union[str, int], obj: Any) -> None:
        self.cache[endpoint][str(id)] = obj

    def has(self, endpoint: str, obj: Any) -> bool:
        return obj in self.cache[endpoint].values()
