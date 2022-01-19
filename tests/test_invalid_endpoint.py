import aiopoke
import pytest


@pytest.mark.asyncio
async def test_invalid_endpoint(client: aiopoke.AiopokeClient):
    with pytest.raises(ValueError):
        await client.get_egg_group(1234)

    with pytest.raises(ValueError):
        await client.get_egg_group("invalid")

    assert client.http.inexistent_endpoints == ["egg-group/1234", "egg-group/invalid"]
