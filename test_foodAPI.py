import unittest
from foodAPI.foodAPI import FoodAPI


class Default():
    price_budget = (0, 10000)
    food_list = {'麵食', '便當'}
    longitude = 120.9955156241461
    latitude = 24.784065460221402
    location = ''


DEFAULT = Default()


class TestFoodAPI(unittest.TestCase):
    bot = FoodAPI()

    def setUp(self):
        self.bot.price_budget = DEFAULT.price_budget
        self.bot.food_preference = DEFAULT.food_list
        self.bot.longitude = DEFAULT.longitude
        self.bot.latitude = DEFAULT.latitude
        self.bot.location = DEFAULT.location


if __name__ == '__main__':
    unittest.main()
