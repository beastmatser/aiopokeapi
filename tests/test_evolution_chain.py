"""Regression tests for EvolutionDetail field name fixes.

Regression for https://github.com/beastmatser/aiopokeapi/issues/165
The PokeAPI returns ``base_form`` (a Pokemon reference) and ``region`` (a Region
reference), but the original ``EvolutionDetail`` class expected
``base_form_id`` and ``region_id`` and was missing several newer fields
(``evolved_form``, ``is_default``, ``near_special_rock``, ``version_group``).
"""

from typing import Any
from typing import Dict

import pytest

from aiopoke.objects.resources.evolutions.evolution_chain import (
    ChainLink,
    EvolutionChain,
    EvolutionDetail,
)


def _make_detail(**overrides: Any) -> Dict[str, Any]:
    """Build a minimally valid evolution-detail payload."""
    base: Dict[str, Any] = {
        "base_form": None,
        "evolved_form": None,
        "gender": None,
        "held_item": None,
        "is_default": True,
        "item": None,
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
        "trigger": {"name": "level-up", "url": "https://pokeapi.co/api/v2/evolution-trigger/1/"},
        "turn_upside_down": False,
        "used_move": None,
        "version_group": {
            "name": "red-blue",
            "url": "https://pokeapi.co/api/v2/version-group/1/",
        },
    }
    base.update(overrides)
    return base


def test_evolution_detail_accepts_base_form_field() -> None:
    """The API returns ``base_form``; the class must accept it (issue #165)."""
    payload = _make_detail(
        base_form={"name": "zigzagoon-galar", "url": "https://pokeapi.co/api/v2/pokemon/10174/"},
    )
    detail = EvolutionDetail(**payload)
    assert detail.base_form is not None
    assert detail.base_form.name == "zigzagoon-galar"


def test_evolution_detail_accepts_region_field() -> None:
    """The API returns ``region``; the class must accept it."""
    payload = _make_detail(
        region={"name": "hisui", "url": "https://pokeapi.co/api/v2/region/8/"},
    )
    detail = EvolutionDetail(**payload)
    assert detail.region is not None
    assert detail.region.name == "hisui"


def test_evolution_detail_accepts_evolved_form_field() -> None:
    payload = _make_detail(
        evolved_form={"name": "linoone-galar", "url": "https://pokeapi.co/api/v2/pokemon/10175/"},
    )
    detail = EvolutionDetail(**payload)
    assert detail.evolved_form is not None
    assert detail.evolved_form.name == "linoone-galar"


def test_evolution_detail_accepts_new_boolean_fields() -> None:
    payload = _make_detail(is_default=True, near_special_rock=False)
    detail = EvolutionDetail(**payload)
    assert detail.is_default is True
    assert detail.near_special_rock is False


def test_evolution_detail_accepts_version_group_field() -> None:
    payload = _make_detail()
    detail = EvolutionDetail(**payload)
    assert detail.version_group.name == "red-blue"


def test_evolution_detail_rejects_old_base_form_id_field() -> None:
    """The class should no longer accept the bogus ``base_form_id`` field."""
    payload = _make_detail(base_form_id=None)
    with pytest.raises(TypeError) as excinfo:
        EvolutionDetail(**payload)
    assert "base_form_id" in str(excinfo.value)


def test_chain_link_constructs_with_realistic_payload() -> None:
    detail_payload = _make_detail()
    link = ChainLink(
        evolution_details=[detail_payload],
        evolves_to=[],
        is_baby=False,
        species={"name": "eevee", "url": "https://pokeapi.co/api/v2/pokemon-species/133/"},
    )
    assert len(link.evolution_details) == 1
    assert link.species.name == "eevee"


def test_evolution_chain_constructs_with_full_payload() -> None:
    payload = {
        "baby_trigger_item": None,
        "id": 1,
        "chain": {
            "evolution_details": [_make_detail()],
            "evolves_to": [],
            "is_baby": False,
            "species": {
                "name": "bulbasaur",
                "url": "https://pokeapi.co/api/v2/pokemon-species/1/",
            },
        },
    }
    chain = EvolutionChain(**payload)
    assert chain.id == 1
    assert chain.baby_trigger_item is None
    assert chain.chain.species.name == "bulbasaur"


def test_minimal_payload_constructs_without_optional_relationships() -> None:
    """All previously-bogus fields accept None / falsy values."""
    payload = _make_detail()
    detail = EvolutionDetail(**payload)
    assert detail.base_form is None
    assert detail.evolved_form is None
    assert detail.region is None
    assert detail.item is None
    assert detail.held_item is None
