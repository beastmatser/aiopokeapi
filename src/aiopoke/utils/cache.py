from typing import Any
from typing import Callable
from typing import Coroutine
from typing import Dict
from typing import Optional
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union

if TYPE_CHECKING:
    from aiopoke.aiopoke_client import AiopokeClient

U = TypeVar("U")


# cache decorator
def cache(
    endpoint: str,
    coro: Callable[["AiopokeClient", Union[str, int]], Coroutine[Any, Any, U]],
) -> Callable[["AiopokeClient", Union[str, int]], Coroutine[Any, Any, U]]:
    async def wrapper(client: "AiopokeClient", name_or_id: Union[str, int]) -> U:
        cached_item: Optional[U] = client._cache.get(f"{endpoint}/{name_or_id}")

        if cached_item is not None:
            return cached_item

        obj: U = await coro(client, name_or_id)
        client._cache.put(f"{endpoint}/{name_or_id}", obj)
        return obj

    return wrapper


class Cache:
    cache: Dict[str, Any] = {}

    def get(self, id: Union[str, int]) -> Any:
        return self.cache.get(str(id))

    def put(self, id: Union[str, int], obj: Any) -> None:
        self.cache[str(id)] = obj

    def has(self, obj: Any) -> bool:
        return obj in self.cache.values()
