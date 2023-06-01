import unittest

from test_foodAPI import TestFoodAPI


class TestPriceBudget(TestFoodAPI):
    def test_add_price_budget(self):
        expected = {1}
        ret = self.bot.add_price_budget(1)
        self.assertEqual(ret, expected)

        expected = {1, 2}
        ret = self.bot.add_price_budget(2)
        self.assertEqual(ret, expected)

        expected = {1, 2, 3}
        ret = self.bot.add_price_budget(3)
        self.assertEqual(ret, expected)

        with self.assertRaises(ValueError):
            self.bot.add_price_budget(123)
            self.bot.add_price_budget('無限')

    def test_reset_price_budget(self):
        ret = self.bot.reset_price_budget()
        self.assertEqual(ret, set())

    def test_get_price_budget(self):
        expected = '低 '
        ret = self.bot.get_price_budget()
        self.assertEqual(ret, expected)


if __name__ == '__main__':
    unittest.main()
