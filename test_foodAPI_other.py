import unittest
from unittest.mock import patch
from unittest.mock import Mock


from test_foodAPI import TestFoodAPI
from test_foodAPI import DEFAULT


class TestOther(TestFoodAPI):
    def test_set_location(self):
        longitude = DEFAULT.longitude
        latitude = DEFAULT.latitude
        location = DEFAULT.location

        self.bot.set_location(longitude=longitude, latitude=latitude)
        self.assertAlmostEqual(self.bot.longitude, longitude, delta=0.01)
        self.assertAlmostEqual(self.bot.latitude, latitude, delta=0.01)

        # self.bot.set_location(location=location)
        # self.assertEqual(self.bot.location, location)
        # self.assertEqual(self.bot.longitude, longitude)
        # self.assertEqual(self.bot.latitude, latitude)

    # need to mock send request
    # @patch('foodAPI.foodAPI.FoodAPI.send_request')
    # def test_get_resturaunts(self, mock_send_request: Mock):
    def test_get_resturaunts(self):
        print(self.bot.send_request())
        # mock_send_request.return_value ={
        #     "name" =
        # }
        # ret = self.bot.get_restaurants()
        # expected = {'李記', '魯肉飯', '鍋燒麵', '麥當勞', '牛排館'}
        # self.assertEqual(ret, expected)

    # def test_filter(self):
    #     # defaut food preference
    #     results = self.bot.get_restaurants()
    #     ls = self.bot.filter(results)
    #     excepted_ls = {'李記', '魯肉飯', '鍋燒麵'}
    #     self.assertEqual(ls, excepted_ls)

    #     # after adding food preference
    #     self.bot.add_food_preference('牛排')
    #     ls = self.bot.filter(results)
    #     excepted_ls = {'李記', '魯肉飯', '鍋燒麵', '牛排館'}
    #     self.assertEqual(ls, excepted_ls)

    # def test_recommend(self):
    #     results = self.bot.get_restaurants()
    #     ls = self.bot.recommend(results)
    #     excepted = '李記'
    #     self.assertEqual(ls, excepted)


if __name__ == '__main__':
    unittest.main()
