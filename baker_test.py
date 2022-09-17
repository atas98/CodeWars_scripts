import unittest
from baker import cakes


class TestTexasHoldem(unittest.TestCase):

    def test_available(self):
        recipe = {"flour": 500, "sugar": 200, "eggs": 1}
        available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
        for _ in range(1000000):
            self.assertEquals(cakes(recipe, available), 2, 'example #1')

    def test_not_available(self):
        recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
        available = {"sugar": 500, "flour": 2000, "milk": 2000}
        for _ in range(1000000):
            self.assertEquals(cakes(recipe, available), 0, 'example #2')


if __name__ == '__main__':
    unittest.main()
