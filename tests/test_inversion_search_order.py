from __future__ import annotations

from fkcompute.inversion.search import _free_signs_from_rank


def _fmt(signs: list[int]) -> str:
    return "".join("+" if sign == 1 else "-" for sign in signs)


def test_free_signs_from_rank_n4_prefix() -> None:
    got = [_fmt(_free_signs_from_rank(i, 4)) for i in range(6)]

    assert got == ["++++", "+++-", "++-+", "+-++", "-+++", "++--"]


def test_free_signs_from_rank_orders_by_negative_count_then_numeric() -> None:
    total = 1 << 6
    prev = None

    for rank in range(total):
        signs = _free_signs_from_rank(rank, 6)
        bits = [0 if sign == 1 else 1 for sign in signs]
        key = (sum(bits), int("".join(str(bit) for bit in bits), 2))
        if prev is not None:
            assert prev <= key
        prev = key
