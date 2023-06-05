import unittest

from test_foodAPI import TestFoodAPI
from foodAPI.foodAPI import price_to_str, food_to_str, food_name2id


class TestHelper(TestFoodAPI):
    def test_price_to_str(self):
        expected = '低'
        ret = price_to_str({1})
        self.assertEqual(ret, expected)

        expected = '低 高'
        ret = price_to_str({1, 3})
        self.assertEqual(ret, expected)

        expected = '無'
        ret = price_to_str(set())
        self.assertEqual(ret, expected)

    def test_food_to_str(self):
        expected = '甜點'
        ret = food_to_str({176})
        self.assertEqual(ret, expected)

        expected = '漢堡 牛排'
        ret = food_to_str({177, 1211})
        self.assertEqual(ret, expected)

        expected = '無'
        ret = food_to_str(set())
        self.assertEqual(ret, expected)

    def test_food_name2id(self):
        expected = 1215
        ret = food_name2id('便當')
        self.assertEqual(ret, expected)

        expected = -1
        ret = food_name2id('我不是食物')
        self.assertEqual(ret, expected)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
