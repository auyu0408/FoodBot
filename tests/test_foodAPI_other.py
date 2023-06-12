import unittest
from unittest.mock import patch
from unittest.mock import Mock


from tests.test_foodAPI import TestFoodAPI
from tests.test_foodAPI import DEFAULT


import requests


def mocked_requests_get(*args, **kwargs):
    res = requests.Response()
    res.status_code = requests.codes.not_found
    return res


class TestOther(TestFoodAPI):
    def test_set_location(self):
        longitude = DEFAULT.longitude
        latitude = DEFAULT.latitude
        location = DEFAULT.location

        self.bot.set_location(longitude=longitude, latitude=latitude)
        self.assertAlmostEqual(self.bot.longitude, longitude, delta=0.01)
        self.assertAlmostEqual(self.bot.latitude, latitude, delta=0.01)

        self.bot.set_location(location='交通大學')
        self.assertAlmostEqual(
            self.bot.longitude, 120.98202608068497, delta=0.1)
        self.assertAlmostEqual(self.bot.latitude, 24.7914804453823, delta=0.01)

    def test_get_restaurants(self):
        ret = self.bot.get_restaurants()
        self.assertIsNot(ret, [])

        with self.assertRaises(TypeError):
            self.bot.set_food_preference('Invalid food')
        ret = self.bot.get_restaurants()
        self.assertNotEqual(ret, [])

        with patch('foodAPI.foodAPI.requests.get', side_effect=mocked_requests_get) as fake_api:
            fakeapi = TestFoodAPI()
            expected = []
            ret = fakeapi.bot.get_restaurants()
            self.assertEqual(ret, expected)

    def test_filter(self):
        pass

    def test_recommend(self):
        ret = self.bot.recommend()
        self.assertIsNot(ret, [])

        with self.assertRaises(ValueError):
            self.bot.add_food_preference('Invalid food')
        # with self.assertRaises(IndexError):
        ret = self.bot.recommend()
        self.assertIsNot(ret, [])

        self.bot.reset_food_preference()
        ret = self.bot.recommend()
        self.assertEqual(ret, '無')


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
