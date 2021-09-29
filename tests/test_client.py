import aiopoke
import pytest


@pytest.mark.asyncio
async def test_client(client: aiopoke.AiopokeClient):
    berry = await client.fetch_berry(1)
    berry_flavor = await berry.flavors[0].flavor.fetch()

    assert hasattr(berry, "name")
    assert hasattr(berry, "id_")
    assert isinstance(berry_flavor, aiopoke.BerryFlavor)
