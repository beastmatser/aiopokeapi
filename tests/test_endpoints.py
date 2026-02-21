import asyncio
import json
from random import choice

import pytest

import aiopoke
from aiopoke.utils.resource import Resource


@pytest.mark.asyncio
async def test_endpoints(client: aiopoke.AiopokeClient):
    file = open("tests/items.json")
    items = json.load(file)

    tasks = [
        client.get_ability(choice(items["ability"])),  #
        client.get_berry(choice(items["berry"])),
        client.get_berry_flavor(choice(items["berry-flavor"])),
        client.get_berry_firmness(choice(items["berry-firmness"])),
        client.get_characteristic(choice(items["characteristic"])),
        client.get_contest_effect(choice(items["contest-effect"])),
        client.get_contest_type(choice(items["contest-type"])),
        client.get_egg_group(choice(items["egg-group"])),
        client.get_encounter_condition(choice(items["encounter-condition"])),
        client.get_encounter_condition_value(
            choice(items["encounter-condition-value"])
        ),
        client.get_encounter_method(choice(items["encounter-method"])),
        client.get_evolution_chain(choice(items["evolution-chain"])),
        client.get_evolution_trigger(choice(items["evolution-trigger"])),
        client.get_gender(choice(items["gender"])),
        client.get_generation(choice(items["generation"])),
        client.get_growth_rate(choice(items["growth-rate"])),
        client.get_item(choice(items["item"])),  #
        client.get_item_attribute(choice(items["item-attribute"])),
        client.get_item_category(choice(items["item-category"])),
        client.get_item_fling_effect(choice(items["item-fling-effect"])),
        client.get_item_pocket(choice(items["item-pocket"])),
        client.get_language(choice(items["language"])),
        client.get_location(choice(items["location"])),
        client.get_location_area(choice(items["location-area"])),
        client.get_machine(choice(items["machine"])),
        client.get_move(choice(items["move"])),
        client.get_move_ailment(choice(items["move-ailment"])),
        client.get_move_battle_style(choice(items["move-battle-style"])),
        client.get_move_category(choice(items["move-category"])),
        client.get_move_damage_class(choice(items["move-damage-class"])),
        client.get_move_learn_method(choice(items["move-learn-method"])),
        client.get_move_target(choice(items["move-target"])),
        client.get_nature(choice(items["nature"])),
        client.get_pal_park_area(choice(items["pal-park-area"])),
        client.get_pokeathlon_stat(choice(items["pokeathlon-stat"])),
        client.get_pokedex(choice(items["pokedex"])),
        client.get_pokemon(choice(items["pokemon"])),  #
        client.get_pokemon_color(choice(items["pokemon-color"])),
        client.get_pokemon_form(choice(items["pokemon-form"])),
        client.get_pokemon_habitat(choice(items["pokemon-habitat"])),
        client.get_pokemon_shape(choice(items["pokemon-shape"])),
        client.get_pokemon_species(choice(items["pokemon-species"])),
        client.get_region(choice(items["region"])),
        client.get_stat(choice(items["stat"])),
        client.get_super_contest_effect(choice(items["super-contest-effect"])),
        client.get_type(choice(items["type"])),
        client.get_version(choice(items["version"])),
        client.get_version_group(choice(items["version-group"])),
    ]

    file.close()

    responses = await asyncio.gather(*tasks)
    for response in responses:
        assert isinstance(response, Resource)
