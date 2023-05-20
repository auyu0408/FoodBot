import unittest
from unittest.mock import Mock
from unittest.mock import patch
from foodBot import FoodBot

default_price_budget = (0, 10000)
default_food_preference = ['麵食', '便當']
default_longitude = 120.9955156241461
default_latitude = 24.784065460221402
default_location = ''

class TestFoodBot(unittest.TestCase):
    bot = FoodBot()
    
    def setUp(self):
        self.bot.price_budget = default_price_budget
        self.bot.food_preference = default_food_preference
        self.bot.longitude = default_longitude
        self.bot.latitude = default_latitude
        self.bot.location = default_location

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
        self.assertEqual(out, 'Invalid command, illegal format, lack of "".')

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

        # valid input, lower bound < 0, convert lower bound to zero
        self.bot.set_price_budget(-5, 200)
        self.assertEqual(self.bot.price_budget, (0, 200))

        # invalid input, upper bound < lower bound
        self.assertRaises(ValueError, self.bot.set_price_budget, 200, 0)

        # invalid input, upper bound < 0
        self.assertRaises(ValueError, self.bot.set_price_budget, 0, -5)

        # invalid input, wrong type
        self.assertRaises(TypeError, self.bot.set_price_budget, 'a', 200)
        self.assertRaises(TypeError, self.bot.set_price_budget, 0, 'a')
        self.assertRaises(TypeError, self.bot.set_price_budget, 'a', 'a')


    def test_set_food_preference(self):
        food_list = ['牛排', '速食']
        self.bot.set_food_preference(food_list)
        self.assertEqual(self.bot.food_preference, food_list)


    def test_add_food_preference(self):
        food_list = ['牛排', '速食'] + ['牛排']
        self.bot.add_food_preference('牛排')
        self.assertEqual(self.bot.food_preference, food_list)

        food_list = food_list + ['速食']
        self.bot.add_food_preference('速食')
        self.assertEqual(self.bot.food_preference, food_list)


    def test_remove_food_preference(self):
        food_list = default_food_preference.remove('麵食')
        self.bot.remove_food_preference('麵食')
        self.assertEqual(self.bot.food_preference, food_list)

    def test_get_food_preference(self):
        self.assertEqual(self.bot.get_food_preference(), default_food_preference)


    def test_set_location(self):
        longitude = 120.1
        latitude = 25.1
        location = '交大'

        self.bot.set_location(longitude = longitude, latitude = latitude)
        self.assertEqual(self.bot.longitude, longitude)
        self.assertEqual(self.bot.latitude, latitude)

        self.bot.set_location(location = location)
        self.assertEqual(self.bot.location, location)


    def test_get_resturaunts(self):
        ls = self.bot.get_resturaunts()
        excepted_ls = ['李記', '魯肉飯', '鍋燒麵', '麥當勞', '牛排館']
        self.assertEqual(ls, excepted_ls)

    def test_filter(self):
        # defaut food preference
        results = self.bot.get_resturaunts()
        ls = self.bot.filter(results)
        excepted_ls = ['李記', '魯肉飯', '鍋燒麵']
        self.assertEqual(ls, excepted_ls)

        # after adding food preference
        self.bot.add_food_preference('牛排')
        ls = self.bot.filter(results)
        excepted_ls = ['李記', '魯肉飯', '鍋燒麵', '牛排館']
        self.assertEqual(ls, excepted_ls)

    def test_recommend(self):
        results = self.bot.get_resturaunts()
        ls = self.bot.recommend(results)
        excepted = '李記'
        self.assertEqual(ls, excepted)


def sutie_food_preference():
    suite = unittest.TestSuite()
    suite.addTest(TestFoodBot('test_set_food_preference'))
    suite.addTest(TestFoodBot('test_add_food_preference'))
    suite.addTest(TestFoodBot('test_remove_food_preference'))
    suite.addTest(TestFoodBot('test_get_food_preference'))
    return suite

def sutie_get_recommend():
    suite = unittest.TestSuite()
    suite.addTest(TestFoodBot('test_set_location'))
    suite.addTest(TestFoodBot('test_get_resturaunts'))
    suite.addTest(TestFoodBot('test_filter'))
    suite.addTest(TestFoodBot('test_recommend'))
    return suite

def suite_other():
    suite = unittest.TestSuite()
    suite.addTest(TestFoodBot('test_set_price_budget'))
    suite.addTest(TestFoodBot('test_user_input'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(sutie_food_preference())
    runner.run(sutie_get_recommend())
    runner.run(suite_other())
    
    # unittest.main()
