import unittest
from unittest.mock import Mock
from unittest.mock import patch
from foodBot import FoodBot

class TestFoodBot(unittest.TestCase):
    bot = FoodBot()
    
    def setUp(self):
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
        excepted_ls = ['李記', '某麵館','肯德基', '摩斯漢堡', '漢堡王']
        self.assertEqual(ls, excepted_ls)

    def test_filter(self):
        self.bot.set_price_budget(0, 200)
        self.bot.set_food_preference(['麵', '飯'])
        self.bot.set_location(longitude = 120.1, latitude = 25.1)
        results = self.bot.get_resturaunts()
        ls = self.bot.filter(results)
        excepted_ls = ['李記', '某麵館']
        self.assertEqual(ls, excepted_ls)

    def test_recommend(self):
        self.bot.set_price_budget(0, 200)
        self.bot.set_food_preference(['麵', '飯'])
        self.bot.set_location(longitude = 120.1, latitude = 25.1)
        results = self.bot.get_resturaunts()
        ls = self.bot.recommend(results)
        excepted_ls = ['李記']
        self.assertEqual(ls, excepted_ls)


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
