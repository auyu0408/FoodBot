import unittest

from test_foodAPI import TestFoodAPI
from test_foodAPI import DEFAULT


class TestFoodPreference(TestFoodAPI):
    def test_reset_food_preference(self):
        self.bot.reset_food_preference()
        self.assertEqual(self.bot.food_preference, set())

    def test_set_food_preference(self):
        food_list = set(DEFAULT.food_list)
        self.bot.set_food_preference(food_list)
        self.assertEqual(self.bot.food_preference, food_list)

    def test_add_food_preference(self):
        food_list = set(DEFAULT.food_list)
        food_list.add('牛排')
        self.bot.add_food_preference('牛排')
        self.assertEqual(self.bot.food_preference, food_list)

        food_list.add('速食')
        self.bot.add_food_preference('速食')
        self.assertEqual(self.bot.food_preference, food_list)

    def test_remove_food_preference(self):
        food_list = set(DEFAULT.food_list)
        food_list.remove('麵食')
        self.bot.remove_food_preference('麵食')
        self.assertEqual(self.bot.food_preference, food_list)

    def test_get_food_preference(self):
        ret = self.bot.get_food_preference()
        expected = str(DEFAULT.food_list).strip("\{\}").replace("\'", "")
        self.assertEqual(ret, expected)


if __name__ == '__main__':
    unittest.main()
