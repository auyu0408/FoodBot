import unittest

from test_foodAPI import TestFoodAPI


class TestFoodPreference(TestFoodAPI):
    def test_reset_food_preference(self):
        self.bot.reset_food_preference()
        self.assertEqual(self.bot.food_preference, set())

    def test_set_food_preference(self):
        food_list = {'a', 'b', 'c'}
        ret = self.bot.set_food_preference(food_list)
        self.assertEqual(ret, food_list)

    def test_add_food_preference(self):
        food_list = set(self.bot.food_preference)
        food_list.add('牛排')
        ret = self.bot.add_food_preference('牛排')
        self.assertEqual(ret, food_list)

        food_list.add('速食')
        ret = self.bot.add_food_preference('速食')
        self.assertEqual(ret, food_list)

    def test_remove_food_preference(self):
        food_list = set(self.bot.food_preference)
        food_list.remove('麵食')
        ret = self.bot.remove_food_preference('麵食')
        self.assertEqual(ret, food_list)

    def test_get_food_preference(self):
        food_list = set(self.bot.food_preference)
        ret = self.bot.get_food_preference()
        expected = str(food_list).strip("\{\}").replace("\'", "")
        self.assertEqual(ret, expected)


if __name__ == '__main__':
    unittest.main()
