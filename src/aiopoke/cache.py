from typing import Any, Awaitable, Callable, Dict, Optional, Union, TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    from .aiopoke_client import AiopokeClient

X = TypeVar("X")


# cache decorator
def cache(endpoint: str) -> Callable[[Callable[["AiopokeClient", Union[str, int]], X]], Callable[["AiopokeClient", Union[str, int]], X]]:
    def decorator(func: Callable[["AiopokeClient", Union[str, int]], X]) -> Callable[["AiopokeClient", Union[str, int]], X]:
        async def call(client: "AiopokeClient", name_or_id: Union[str, int]) -> X:
            cached_item: Optional[X] = client._cache.get(f"{endpoint}_{name_or_id}")
            if cached_item is not None:
                return cached_item

            obj: X = await func(client, name_or_id)  # type: ignore
            client._cache.put(endpoint, obj)
            return obj

        return call  # type: ignore
    return decorator


class Cache:
    _cache: Dict[str, Any]
    _aliases: Dict[str, str]

    def __init__(self) -> None:
        self._cache = {}
        self._aliases = {}

    def get(self, name: str):
        cached_object = self._cache.get(name)
        if cached_object is not None:
            return cached_object

        cached_object_value = self._aliases.get(name)
        if cached_object_value is not None:
            cached_object_key = name.split("_")[0] + "_" + cached_object_value
            return self._cache[cached_object_key]

        return None

    def put(self, endpoint: str, obj: Any):
        self._cache[f"{endpoint.replace('-', '_')}_{obj.id_}"] = obj
        if hasattr(obj, "name"):
            self._aliases[f"{endpoint}_{obj.name}"] = str(obj.id_)

    def is_cached(self, obj: Any) -> bool:
        return obj in self._cache.values()
