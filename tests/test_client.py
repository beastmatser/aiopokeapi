import aiopoke
import pytest


@pytest.mark.asyncio
async def test_client(client: aiopoke.AiopokeClient):
    berry = await client.fetch_berry(1)

    assert hasattr(berry, "name")
    assert hasattr(berry, "id_")
