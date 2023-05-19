import unittest
from unittest.mock import Mock
from unittest.mock import patch
from foodBot import FoodBot

class TestFoodBot(unittest.TestCase):
    def setUp(self):
        self.bot = FoodBot()
        pass

    def tearDown(self):
        pass

    def test_user_input(self):
        # invalid command, not exist command
        input = ['/asdf']
        valid, out= self.bot.user_input(input)
        self.assertEqual(valid, False)
        self.assertEqual(out, 'Invalid command, the command not exist.')

        # invalid command, illegal argument
        input = ['/set_location']
        valid, out= self.bot.user_input(input)
        self.assertEqual(valid, False)
        self.assertEqual(out, 'Invalid command, illegal argument.')

        # invalid command, illegal format
        input = ['asdf']
        valid, out= self.bot.user_input(input)
        self.assertEqual(valid, False)
        self.assertEqual(out, 'Invalid command, illegal format, lack of "\\".')

        # help
        input = ['/help']
        valid, out = self.bot.user_input(input)
        command_list = ['help', 'set_location', 'get_resturaunts', 'search_food']
        self.assertEqual(valid, True)
        self.assertEqual(out, command_list)

    def test_set_price_budget(self):
        # valid input
        self.bot.set_price_budget(0, 200)
        self.assertEqual(self.bot.price_budget, (0, 200))

        # valid input, upper bound is inf
        self.bot.set_price_budget(0, -1)
        self.assertEqual(self.bot.price_budget, (0, -1))

        # valid input, lower bound < 0, convert lower bound to zero
        self.bot.set_price_budget(-5, 200)
        self.assertEqual(self.bot.price_budget, (0, 200))

        # invalid input, upper bound < lower bound
        self.assertRaises(ValueError, self.bot.set_price_budget, 200, 0)

        # invalid input, wrong type
        self.assertRaises(TypeError, self.bot.set_price_budget, 'a', 200)
        self.assertRaises(TypeError, self.bot.set_price_budget, 0, 'a')
        self.assertRaises(TypeError, self.bot.set_price_budget, 'a', 'a')


    def test_set_food_preference(self):
        food_list = ['麵', '飯']
        self.bot.set_food_preference(food_list)
        self.assertEqual(self.bot.food_preference, food_list)


    def test_add_food_preference(self):
        self.bot.add_food_preference('麵')
        self.assertEqual(self.bot.food_preference, ['麵'])

        self.bot.add_food_preference('飯')
        self.assertEqual(self.bot.food_preference, ['麵', '飯'])


    def test_remove_food_preference(self):
        self.bot.add_food_preference('麵')
        self.bot.add_food_preference('飯')
        self.bot.remove_food_preference('麵')
        self.assertEqual(self.bot.food_preference, ['飯'])


    def test_get_food_preference(self):
        food_list = ['麵', '飯']
        self.bot.set_food_preference(food_list)
        self.assertEqual(self.bot.get_food_preference(), food_list)


    def test_get_resturaunts(self):
        ls = self.bot.get_resturaunts()
        excepted_ls = ['c', '肯德基', '摩斯漢堡', '漢堡王']
        self.assertEqual(ls, excepted_ls)


    def test_set_location(self):
        longitude = 120.1
        latitude = 25.1
        location = '交大'

        self.bot.set_location(longitude = longitude, latitude = latitude)
        self.assertEqual(self.bot.longitude, longitude)
        self.assertEqual(self.bot.latitude, latitude)

        self.bot.set_location(location = location)
        self.assertEqual(self.bot.location, location)


    def test_search_food(self):
        ls = self.bot.search_food('義大利麵')
        excepted_ls = ['A', 'B', 'C', 'D']
        self.assertEqual(ls, excepted_ls)


def sutie_food_preference():
    suite = unittest.TestSuite()
    suite.addTest(TestFoodBot('test_set_food_preference'))
    suite.addTest(TestFoodBot('test_add_food_preference'))
    suite.addTest(TestFoodBot('test_remove_food_preference'))
    suite.addTest(TestFoodBot('test_get_food_preference'))
    return suite

if __name__ == '__main__':
    unittest.main()
