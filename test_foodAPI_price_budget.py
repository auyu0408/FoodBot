import unittest

from test_foodAPI import TestFoodAPI
from test_foodAPI import DEFAULT


class TestPriceBudget(TestFoodAPI):
    def test_add_price_budget(self):
        expected = {'低'}
        ret = self.bot.add_price_budget('低')
        self.assertEqual(ret, expected)

        expected = {'低', '中'}
        ret = self.bot.add_price_budget('中')
        self.assertEqual(ret, expected)

        expected = {'低', '中', '高'}
        ret = self.bot.add_price_budget('高')
        self.assertEqual(ret, expected)

    def test_reset_price_budget(self):
        ret = self.bot.reset_price_budget()
        self.assertEqual(ret, set())

    def test_get_price_budget(self):
        expected = self.bot.price_budget
        ret = self.bot.get_price_budget()

        for a, b in zip(ret, expected):
            self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()
