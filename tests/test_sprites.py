import os

import pytest

import aiopoke


@pytest.mark.asyncio
async def test_sprites(client: aiopoke.AiopokeClient):
    pokemon = await client.get_pokemon(25)
    sprites = pokemon.sprites

    await sprites.back_default.save()
    assert "back_25.png" in os.listdir()
    assert sprites.back_default.client == client

    os.remove("back_25.png")
