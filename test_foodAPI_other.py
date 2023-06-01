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

    def test_get_resturaunts(self):
        ret = self.bot.get_restaurants()
        self.assertIsNot(ret, [])

        self.bot.set_food_preference('Invalid food')
        ret = self.bot.get_restaurants()
        self.assertEqual(ret, [])

    def test_filter(self):
        pass

    def test_recommend(self):
        ret = self.bot.recommend()
        self.assertIsNot(ret, [])

        self.bot.add_food_preference('Invalid food')
        with self.assertRaises(IndexError):
            ret = self.bot.recommend()


if __name__ == '__main__':
    unittest.main()
