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

    
    def test_get_resturaunts(self):
        ls = self.bot.get_resturaunts()
        excepted_ls = ['麥當勞', '肯德基', '摩斯漢堡', '漢堡王']
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


    def test_user_input(self):
        # help
        input = ['/help']
        ret = self.bot.user_input(input)
        command_list = ['help', 'set_location', 'get_resturaunts', 'search_food']
        self.assertEqual(ret, command_list)

        # set location
        input = ['/set_location', '交大']
        ret = self.bot.user_input(input)
        self.assertEqual(ret, True)

        # invalid command
        input = ['/asdf']
        ret = self.bot.user_input(input)
        self.assertEqual(ret, False)

    def test_set_price_budget(self):
        min = 10
        max = 200

        self.bot.set_price_budget(min, max)
        self.assertEqual(self.bot.price_budget, (min, max))


if __name__ == '__main__':
    unittest.main()
