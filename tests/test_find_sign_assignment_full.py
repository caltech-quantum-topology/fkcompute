from __future__ import annotations

from fkcompute.domain.braid.states import BraidStates
from fkcompute.inversion.api import find_sign_assignment_full
from fkcompute.inversion.permutations import iter_perms_rot_closed, perm_to_signs


def _canon(signs: dict[int, list[int]], n_components: int) -> tuple[tuple[int, ...], ...]:
    return tuple(tuple(int(s) for s in signs.get(c, ())) for c in range(n_components))


def test_find_sign_assignment_full_dedupes_multicycle_candidates(monkeypatch) -> None:
    braid = [1, -1, -2]
    braid_states = BraidStates(braid)

    calls: list[int] = []

    def _ok_check_sign_assignment(degree: int, relations: list, braid_states: object, weight=None):
        calls.append(int(degree))
        return {"ok": True}

    monkeypatch.setattr(
        "fkcompute.inversion.api.check_sign_assignment",
        _ok_check_sign_assignment,
    )

    got = find_sign_assignment_full(braid, degree=7)

    expected: set[tuple[tuple[int, ...], ...]] = set()
    for perm in iter_perms_rot_closed(braid):
        signs = perm_to_signs(perm, braid)
        braid_states.strand_signs = signs
        braid_states.compute_matrices()
        assert braid_states.validate()
        expected.add(_canon(signs, braid_states.n_components))

    got_keys = {_canon(result.sign_assignment or {}, braid_states.n_components) for result in got}
    assert got_keys == expected
    assert len(calls) == len(expected)
