
MAX_PRICE = 10000

class FoodAPI:
    def __init__(self):
        self.price_budget = (0, MAX_PRICE)
        self.food_preference = []
        self.longitude = 0
        self.latitude = 0
        self.location = ''

    def set_price_budget(self, min, max):
        pass

    def set_food_preference(self, food_list):
        pass

    def add_food_preference(self, food):
        pass

    def remove_food_preference(self, food):
        pass

    def get_food_preference(self):
        pass

    def set_location(self, longitude = 0, latitude = 0, location = ''):
        pass

    def get_resturaunts(self):
        return ['李記', '魯肉飯', '鍋燒麵', '麥當勞', '牛排館']

    def filter(self, resturaunts):
        pass

    def recommend(self):
        pass