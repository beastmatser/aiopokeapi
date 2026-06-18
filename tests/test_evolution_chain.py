from aiopoke.objects.resources.evolutions.evolution_chain import EvolutionDetail


def _evolution_detail_payload():
    return {
        "base_form": None,
        "gender": None,
        "held_item": None,
        "item": {"name": "water-stone", "url": "https://pokeapi.co/api/v2/item/84/"},
        "known_move": None,
        "known_move_type": None,
        "location": None,
        "min_affection": None,
        "min_beauty": None,
        "min_damage_taken": None,
        "min_happiness": None,
        "min_level": None,
        "min_move_count": None,
        "min_steps": None,
        "near_special_rock": False,
        "needs_multiplayer": False,
        "needs_overworld_rain": False,
        "party_species": None,
        "party_type": None,
        "region": None,
        "relative_physical_stats": None,
        "time_of_day": "",
        "trade_species": None,
        "trigger": {
            "name": "use-item",
            "url": "https://pokeapi.co/api/v2/evolution-trigger/3/",
        },
        "turn_upside_down": False,
        "used_move": None,
    }


def test_evolution_detail_accepts_current_api_fields():
    detail = EvolutionDetail(**_evolution_detail_payload())

    assert detail.base_form is None
    assert detail.region is None
    assert detail.near_special_rock is False
