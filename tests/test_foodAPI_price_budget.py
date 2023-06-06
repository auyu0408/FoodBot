import unittest

from tests.test_foodAPI import TestFoodAPI


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
        with self.assertRaises(ValueError):
            self.bot.add_price_budget('無限')

    def test_remove_price_budget(self):
        self.bot.price_budget = {1, 2, 3}

        expected = {1, 2}
        ret = self.bot.remove_price_budget(3)
        self.assertEqual(ret, expected)

        with self.assertRaises(ValueError):
            self.bot.remove_price_budget(123)

    def test_reset_price_budget(self):
        ret = self.bot.reset_price_budget()
        self.assertEqual(ret, set())

    def test_get_price_budget(self):
        expected = '低'
        ret = self.bot.get_price_budget()
        self.assertEqual(ret, expected)

        self.bot.price_budget = {1, 2}
        expected = '低 中'
        ret = self.bot.get_price_budget()
        self.assertEqual(ret, expected)

        self.bot.price_budget = set()
        expected = '無'
        ret = self.bot.get_price_budget()
        self.assertEqual(ret, expected)

    def test_set_food_preference(self):
        expected = {186, 201, 1215}
        ret = self.bot.set_food_preference({201, 186, 1215})
        self.assertEqual(ret, expected)

        expected = {176, 181}
        ret = self.bot.set_food_preference({176, 181})
        self.assertEqual(ret, expected)

        expected = {1211}
        ret = self.bot.set_food_preference({1211})
        self.assertEqual(ret, expected)

        with self.assertRaises(ValueError):
            self.bot.set_food_preference({123})
        with self.assertRaises(ValueError):
            self.bot.set_food_preference({1211, 201, 156})

        with self.assertRaises(TypeError):
            self.bot.set_food_preference(123)
        with self.assertRaises(TypeError):
            self.bot.set_food_preference('A string')

    def test_reset_food_preference(self):
        ret = self.bot.reset_food_preference()
        self.assertEqual(ret, set())

    def test_add_food_preference(self):
        self.bot.reset_food_preference()

        expected = {201}
        ret = self.bot.add_food_preference(201)
        self.assertEqual(ret, expected)

        expected = {186, 201}
        ret = self.bot.add_food_preference(186)
        self.assertEqual(ret, expected)

        expected = {186, 201, 1215}
        ret = self.bot.add_food_preference(1215)
        self.assertEqual(ret, expected)

        with self.assertRaises(ValueError):
            self.bot.add_food_preference(1364)
        with self.assertRaises(ValueError):
            self.bot.add_food_preference('A string')


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
