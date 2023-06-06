import unittest
from foodAPI.foodAPI import FoodAPI, food_name2id


# cuisine_dic = {177: '漢堡', 201: '麵食', 1215: '便當', 181: '飲料', 176: '甜點', 1211: '牛排', 186: '素食'}
class Default():
    price_budget = [1]
    f1 = food_name2id('麵食')
    f2 = food_name2id('便當')
    food_list = [f1, f2]
    longitude = 120.9955156241461
    latitude = 24.784065460221402
    location = ''


DEFAULT = Default()


class TestFoodAPI(unittest.TestCase):
    bot = FoodAPI()

    def setUp(self):
        self.bot.price_budget = set(DEFAULT.price_budget)
        self.bot.food_preference = set(DEFAULT.food_list)
        self.bot.longitude = DEFAULT.longitude
        self.bot.latitude = DEFAULT.latitude
        self.bot.location = DEFAULT.location


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
