import pytest

import aiopoke


@pytest.mark.asyncio
async def test_client(client: aiopoke.AiopokeClient):
    berry = await client.get_berry(1)
    berry_flavor = await berry.flavors[0].flavor.fetch()

    assert hasattr(berry, "name")
    assert hasattr(berry, "id")
    assert isinstance(berry_flavor, aiopoke.BerryFlavor)
