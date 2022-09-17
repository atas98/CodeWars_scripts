#!/usr/bin/env python
# https://www.codewars.com/kata/524c74f855025e2495000262

from typing import Generator, List, Tuple
from collections import Counter
from itertools import islice, tee


CARD_RANKS: Tuple[str] = (
    "A",
    "K",
    "Q",
    "J",
    "10",
    "9",
    "8",
    "7",
    "6",
    "5",
    "4",
    "3",
    "2",
)


def window_iter(iterable, size) -> Generator[Tuple[str], None, None]:
    iterables = tee(iter(iterable), size)
    window = zip(*(islice(t, n, None) for n, t in enumerate(iterables)))
    yield from window


def sort_by_ranks(cards: List[str], exclude: Tuple[str] = tuple()) -> List[str]:
    return [
        card[:-1]
        for card in sorted(
            filter(lambda card: card[:-1] not in exclude, cards),
            key=lambda card: CARD_RANKS.index(card[:-1]),
        )
    ]


def _check_flash(cards: List[str]) -> Tuple[bool, List[str]]:
    suits: Counter[str] = Counter(card[-1] for card in cards)
    return (
        suits.most_common(1)[0][1] >= 5,
        [card for card in cards if card[-1] == suits.most_common(1)[0][0]],
    )


def _check_straight(cards: List[str]) -> Tuple[bool, List[str]]:
    card_ranks = set(card[:-1] for card in cards)
    rank_indices = sorted([CARD_RANKS.index(rank) for rank in card_ranks])
    for window in window_iter(rank_indices, 5):
        window = sorted(window)
        if window[0] == window[-1] - 4:
            return True, [CARD_RANKS[i] for i in window]
    return False, cards


def _check_pairs(cards: List[str]) -> Tuple[bool, List[Tuple[str, int]]]:
    pairs_count: Counter[str] = Counter(card[:-1] for card in cards)
    most_common: List[Tuple[str, int]] = pairs_count.most_common()
    return most_common[0][1] >= 2, [
        (card, amount) for card, amount in most_common if amount >= 2
    ]


def hand(hole_cards: List[str], community_cards: List[str]) -> Tuple[str, List[str]]:
    """
    Return the best poker hand and the cards that make it.

    Flash -> Straight -> Pairs -> Nothing

    Args:
        hole_cards (list): cards in hand
        community_cards (list): cards on the table

    Returns:
        Tuple[str, list]: hand name and card ranks that make it
    """
    cards: list[str] = hole_cards + community_cards
    is_flash, flash_cards = _check_flash(cards)
    if is_flash:
        is_straight, straight_cards = _check_straight(flash_cards)
        if is_straight:
            return "straight-flush", straight_cards
    is_pairs, pairs = _check_pairs(cards)
    if is_pairs and pairs and pairs[0][1] >= 4:
        four_card = pairs[0][0]
        return "four-of-a-kind", [
            four_card,
            sort_by_ranks(cards, exclude=(four_card,))[0],
        ]
    elif is_pairs and len(pairs) >= 2 and pairs[0][1] == 3 and pairs[1][1] == 2:
        three_card = pairs[0][0]
        two_card = pairs[1][0]
        return "full house", [three_card, two_card]
    elif is_flash:
        return "flush", sort_by_ranks(flash_cards)[:5]

    is_straight, straight_cards = _check_straight(cards)

    if is_straight:
        return "straight", straight_cards
    if is_pairs:
        pair_card = pairs[0][0]
        if pairs[0][1] == 3:
            return "three-of-a-kind", [
                pair_card,
                *sort_by_ranks(cards, exclude=(pair_card,))[:2],
            ]
        if len(pairs) >= 2 and pairs[0][1] == 2 and pairs[1][1] == 2:
            second_pair_card = pairs[1][0]
            return "two pair", [
                *sorted(
                    (pair_card, second_pair_card),
                    key=lambda card: CARD_RANKS.index(card),
                ),
                sort_by_ranks(cards, exclude=(pair_card, second_pair_card))[0],
            ]
        else:
            return "pair", [
                pair_card,
                *sort_by_ranks(cards, exclude=(pair_card,))[:3],
            ]
    else:
        return "nothing", sort_by_ranks(cards)[:5]
