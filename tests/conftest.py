import aiopoke
import pytest


@pytest.fixture
async def client():
    async with aiopoke.AiopokeClient() as _client:
        yield _client
