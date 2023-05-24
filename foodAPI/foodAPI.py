import json
import requests
import random
from bs4 import BeautifulSoup

random.seed(0)

def change_location(location):
    URL = "https://www.google.com/maps/place?q=" + location
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, "html.parser")
    text = soup.prettify()#將部份資料轉成html形式
    initial_pos = text.find(";window.APP_INITIALIZATION_STATE")#尋找;window.APP_INITIALIZATION_STATE所在位置
    pos = text[initial_pos+36:initial_pos+85] #存取經緯鍍在的地方，ex.3610.8245986264596,121.43077076500904,25.175396183906233
    line = tuple(pos.split(','))
    num1 = float(line[1])
    num2 = float(line[2])
    return (num1, num2)

class FoodAPI:
    def __init__(self):
        self.price_budget = set()
        self.food_preference = set()
        self.longitude = 120.9955156241461
        self.latitude = 24.784065460221402
        self.location = ''
        self.restaurants = []

        with open('./foodAPI/config.json') as f:
            config = json.load(f)
            self.data = config['data'][0]
            self.headers = config['headers'][0]

    def build_data(self):
        self.data['longitude'] = self.longitude
        self.data['latitude'] = self.latitude
        self.data['budget'] = self.price_budget
        self.data['cuisine'] = set()

        return
    
    def send_request(self):
        url = 'https://disco.deliveryhero.io/listing/api/v1/pandora/vendors'
        self.build_data()
        r = requests.get(url=url, params=self.data, headers=self.headers)
        if r.status_code == requests.codes.ok:
            result = r.json()
            restaurants = result['data']['items']
            return restaurants
        else:
            print('請求失敗')
            return []

    def add_price_budget(self, budget):
        self.price_budget.add(budget)
        return self.price_budget

    def reset_price_budget(self):
        self.price_budget = set()
        return self.price_budget

    def get_price_budget(self):
        if len(self.price_budget) == 0:
            return "無"
        else:
            return str(self.price_budget).strip("\{\}").replace("\'", "")

    def reset_food_preference(self):
        self.food_preference = set()
        return self.food_preference

    def set_food_preference(self, food_list):
        self.food_preference = food_list
        return self.food_preference

    def add_food_preference(self, food):
        self.food_preference.add(food)
        return self.food_preference

    def remove_food_preference(self, food):
        self.food_preference.remove(food)
        return self.food_preference

    def get_food_preference(self):
        if len(self.food_preference) == 0:
            return "無"
        else:
            return str(self.food_preference).strip("\{\}").replace("\'", "")

    def set_location(self, longitude = 0, latitude = 0, location = ''):
        self.longitude =longitude
        self.latitude = latitude
        (long, lat) = change_location(location) #把location轉經緯度
        self.longitude =long
        self.latitude = lat

    def get_restaurants(self):
        self.restaurants = self.send_request()
        name = []
        for restautant in self.restaurants:
            name.append(restautant['name'])
        return name

    def filter(self):
        name = []
        restaurants = self.restaurants
        self.restaurants = []
        for restaurant in restaurants:
            flag = 0
            for cuisine in restaurant['cuisines']:
                for preference in self.food_preference:
                    if cuisine['name'] == preference:
                        flag = 1
                        break
            if flag:
                name.append(restaurant['name'])
                self.restaurants.append(restaurant)
        return name

    def recommend(self):
        max = len(self.restaurants)
        num = random.randint(0,max)
        return self.restaurants[num]['name']