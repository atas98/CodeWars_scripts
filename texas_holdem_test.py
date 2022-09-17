import unittest
from texas_holdem import hand


class TestTexasHoldem(unittest.TestCase):

    def test_nothing(self):
        self.assertEqual(
            hand(["K♠", "A♦"], ["J♣", "Q♥", "9♥", "2♥", "3♦"]),
            ("nothing", ["A", "K", "Q", "J", "9"]),
        )

    def test_pair(self):
        self.assertEqual(
            hand(["K♠", "Q♦"], ["J♣", "Q♥", "9♥", "2♥", "3♦"]),
            ("pair", ["Q", "K", "J", "9"]),
        )

    def test_two_pair(self):
        self.assertEqual(
            hand(["K♠", "J♦"], ["J♣", "K♥", "9♥", "2♥", "3♦"]),
            ("two pair", ["K", "J", "9"]),
        )

    def test_three_of_kind(self):
        self.assertEqual(
            hand(["4♠", "9♦"], ["J♣", "Q♥", "Q♠", "2♥", "Q♦"]),
            ("three-of-a-kind", ["Q", "J", "9"]),
        )

    def test_straight(self):
        self.assertEqual(
            hand(["Q♠", "2♦"], ["J♣", "10♥", "9♥", "K♥", "3♦"]),
            ("straight", ["K", "Q", "J", "10", "9"]),
        )

    def test_flush(self):
        self.assertEqual(
            hand(["A♠", "K♦"], ["J♥", "5♥", "10♥", "Q♥", "3♥"]),
            ("flush", ["Q", "J", "10", "5", "3"]),
        )

    def test_full_house(self):
        self.assertEqual(
            hand(["A♠", "A♦"], ["K♣", "K♥", "A♥", "Q♥", "3♦"]),
            ("full house", ["A", "K"]),
        )

    def test_four_of_a_kind(self):
        self.assertEqual(
            hand(["2♠", "3♦"], ["2♣", "2♥", "3♠", "3♥", "2♦"]),
            ("four-of-a-kind", ["2", "3"]),
        )

    def test_straight_flush(self):
        self.assertEqual(
            hand(["8♠", "6♠"], ["7♠", "5♠", "9♠", "J♠", "10♠"]),
            ("straight-flush", ["J", "10", "9", "8", "7"]),
        )

    def test_flush_more_cards(self):
        self.assertEqual(
            hand(['Q♦', '9♠'], ['9♦', '8♦', '2♦', '10♦', '7♦']),
            ('flush', ['Q', '10', '9', '8', '7']),
        )

    def test_four_of_a_kind_split(self):
        self.assertEqual(
            hand(['6♣', '6♥'], ['10♦', '2♠', '5♥', '6♦', '6♠']),
            ('four-of-a-kind', ['6', '10']),
        )

    def test_two_pair_sequence(self):
        self.assertEqual(
            hand(['A♦', 'J♣'], ['Q♠', '4♦', '9♣', '9♠', '4♠']),
            ('two pair', ['9', '4', 'A']),
        )


if __name__ == '__main__':
    unittest.main()
