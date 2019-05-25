import unittest
from algorithm.others.coin_change_2 import coin_exchange_top_down


class Test(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(coin_exchange_top_down([10, 20, 50, 100], 100), 11)
        self.assertEqual(coin_exchange_top_down([10, 20, 50, 100], 20), 2)
        self.assertEqual(coin_exchange_top_down([10, 20, 50, 100], 30), 2)
        self.assertEqual(coin_exchange_top_down([10, 20, 50, 100], 50), 4)

    def test_value(self):
        self.assertRaises(TypeError, coin_exchange_top_down, [10, 20, 50, 100], 10.5)