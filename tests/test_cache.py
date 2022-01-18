import pytest

import aiopoke


@pytest.mark.asyncio
async def test_cache(client: aiopoke.AiopokeClient):
    pokemon = await client.get_pokemon(5)
    encounter_condition = await client.get_encounter_condition(2)

    cache = client._cache
    assert cache.has("pokemon", pokemon)
    assert cache.has("encounter-condition", encounter_condition)

    move = await client.get_move(1)
    contest_effect = await move.contest_effect.fetch()

    assert isinstance(contest_effect, aiopoke.ContestEffect)
