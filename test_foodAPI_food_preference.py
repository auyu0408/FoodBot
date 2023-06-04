import unittest

from foodAPI import foodAPI
from test_foodAPI import TestFoodAPI


class TestFoodPreference(TestFoodAPI):
    def test_reset_food_preference(self):
        self.bot.reset_food_preference()
        self.assertEqual(self.bot.food_preference, set())

    def test_set_food_preference(self):
        food_list = {1211, 176, 1215}
        ret = self.bot.set_food_preference(food_list)
        self.assertEqual(ret, food_list)

    def test_add_food_preference(self):
        food_list = set(self.bot.food_preference)
        food_list.add(1211)
        ret = self.bot.add_food_preference(1211)
        self.assertEqual(ret, food_list)

        food_list.add(186)
        ret = self.bot.add_food_preference(186)
        self.assertEqual(ret, food_list)

    def test_remove_food_preference(self):
        food_list = set(self.bot.food_preference)
        f = foodAPI.food_name2id('麵食')
        food_list.remove(f)
        ret = self.bot.remove_food_preference(f)
        self.assertEqual(ret, food_list)

    def test_get_food_preference(self):
        ret = self.bot.get_food_preference()
        expected = self.bot.food_preference
        self.assertEqual(ret, expected)


if __name__ == '__main__':
    unittest.main()
