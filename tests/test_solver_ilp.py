from __future__ import annotations

import pytest

from fkcompute.domain.braid.states import BraidStates
from fkcompute.domain.constraints.reduction import full_reduce
from fkcompute.domain.constraints.symbols import Symbol, one
from fkcompute.solver.ilp import ilp, integral_bounded


def test_integral_bounded_accepts_bounded_integer_region() -> None:
    x = Symbol(1)

    assert integral_bounded([x, 3 - x], {x: 1})


def test_integral_bounded_rejects_infeasible_region() -> None:
    x = Symbol(1)

    assert not integral_bounded([(-1) - x], {x: 1})


def test_integral_bounded_rejects_unbounded_region() -> None:
    x = Symbol(1)

    assert not integral_bounded([x], {x: 1})


def test_integral_bounded_checks_every_coordinate() -> None:
    x = Symbol(1)
    y = Symbol(2)

    assert not integral_bounded([x, 2 - x, y], {x: 1, y: 1})


def test_integral_bounded_normalizes_negative_variables() -> None:
    x = Symbol(1)

    assert integral_bounded([x * -1, 3 + x], {x: -1})


def test_integral_bounded_supports_fractional_constants() -> None:
    x = Symbol(1)

    assert integral_bounded([x, 2.5 - x], {x: 1})


@pytest.mark.parametrize(
    ("constraints", "expected"),
    [
        ([], True),
        ([one], True),
        ([one * -1], False),
        ([one * -2], False),
    ],
)
def test_integral_bounded_handles_constant_only_systems(
    constraints: list[Symbol],
    expected: bool,
) -> None:
    assert integral_bounded(constraints, {}) is expected


@pytest.mark.parametrize(
    ("braid", "degree", "weight", "expected"),
    [
        (
            [1, 1, 1],
            3,
            None,
            """3,
1,
3,
1,1,1,1,1,1,
0,
0,0,0,0,0,0,
2.5,-1.0,
/
2,4,
/
0,0,
0,1,
0,1,
0,0,
0,1,
0,0,
0,0,
0,1,""",
        ),
        (
            [1, 1],
            3,
            None,
            """3,
2,
2,
1,1,1,1,
1,
0,1,1,0,
3.0,-1.0,
/
/
0,0,
0,1,
0,0,
0,1,
0,0,
0,1,""",
        ),
    ],
)
def test_ilp_output_is_unchanged(
    braid: list[int],
    degree: int,
    weight: int | None,
    expected: str,
) -> None:
    braid_states = BraidStates(braid)
    braid_states.generate_position_assignments()
    relations = full_reduce(braid_states.get_state_relations())

    assert ilp(degree, relations, braid_states, weight=weight) == expected
