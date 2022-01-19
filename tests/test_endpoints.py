import asyncio

import aiopoke
import pytest
from aiopoke.utils.resource import Resource


@pytest.mark.asyncio
async def test_endpoints(client: aiopoke.AiopokeClient):
    tasks = [
        client.get_ability(2),
        client.get_berry(2),
        client.get_berry_flavor(2),
        client.get_berry_firmness(2),
        client.get_characteristic(2),
        client.get_contest_effect(2),
        client.get_contest_type(2),
        client.get_egg_group(2),
        client.get_encounter_condition(2),
        client.get_encounter_condition_value(2),
        client.get_encounter_method(2),
        client.get_evolution_chain(2),
        client.get_evolution_trigger(2),
        client.get_gender(2),
        client.get_generation(2),
        client.get_growth_rate(2),
        client.get_item(2),
        client.get_item_attribute(2),
        client.get_item_category(2),
        client.get_item_fling_effect(2),
        client.get_item_pocket(2),
        client.get_language(2),
        client.get_location(2),
        client.get_location_area(2),
        client.get_machine(2),
        client.get_move(2),
        client.get_move_ailment(2),
        client.get_move_battle_style(2),
        client.get_move_category(2),
        client.get_move_damage_class(2),
        client.get_move_learn_method(2),
        client.get_move_target(2),
        client.get_nature(2),
        client.get_pal_park_area(2),
        client.get_pokeathlon_stat(2),
        client.get_pokedex(2),
        client.get_pokemon(2),
        client.get_pokemon_color(2),
        client.get_pokemon_form(2),
        client.get_pokemon_habitat(2),
        client.get_pokemon_shape(2),
        client.get_pokemon_species(2),
        client.get_region(2),
        client.get_stat(2),
        client.get_super_contest_effect(2),
        client.get_type(2),
        client.get_version(2),
        client.get_version_group(2),
    ]

    responses = await asyncio.gather(*tasks)
    for response in responses:
        assert isinstance(response, Resource)
