import unittest
from foodAPI.foodAPI import FoodAPI, price_to_str, food_to_str, food_name2id


# cuisine_dic = {177: "漢堡", 201: "麵食", 1215: "便當", 181: "飲料", 176: "甜點", 1211: "牛排", 186: "素食"}
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

    def test_price_to_str(self):
        expected = '低'
        ret = price_to_str({1})
        self.assertEqual(ret, expected)

        expected = '低 高'
        ret = price_to_str({1, 3})
        self.assertEqual(ret, expected)

        expected = '無'
        ret = price_to_str(set())
        self.assertEqual(ret, expected)

    def test_food_to_str(self):
        expected = '甜點'
        ret = food_to_str({176})
        self.assertEqual(ret, expected)

        expected = '漢堡 牛排'
        ret = food_to_str({177, 1211})
        self.assertEqual(ret, expected)

        expected = '無'
        ret = food_to_str(set())
        self.assertEqual(ret, expected)

    def test_food_name2id(self):
        expected = 1215
        ret = food_name2id('便當')
        self.assertEqual(ret, expected)

        expected = -1
        ret = food_name2id('我不是食物')
        self.assertEqual(ret, expected)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
