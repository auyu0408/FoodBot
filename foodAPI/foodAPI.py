import json
import requests
import random
from bs4 import BeautifulSoup

random.seed(0)


def change_location(location):
    URL = "https://www.google.com/maps/place?q=" + location
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, "html.parser")
    text = soup.prettify()  # 將部份資料轉成html形式
    # 尋找;window.APP_INITIALIZATION_STATE所在位置
    initial_pos = text.find(";window.APP_INITIALIZATION_STATE")
    # 存取經緯鍍在的地方，ex.3610.8245986264596,121.43077076500904,25.175396183906233
    pos = text[initial_pos+36:initial_pos+85]
    line = tuple(pos.split(','))
    num1 = float(line[1])
    num2 = float(line[2])
    return (num1, num2)


price_dic = {1: "低", 2: "中", 3: "高"}


def price_to_str(_set):
    if len(_set) == 0:
        return "無"
    else:
        string = ""
        for i in _set:
            string += price_dic[i] + " "
        # return str(_set).strip("\{\}").replace("\'", "")
        return string.strip()


cuisine_dic = {177:'漢堡', 201:'麵食', 1215:'便當',
               181:'飲料', 176:'甜點', 1211:'牛排', 186:'素食'}


def food_to_str(_set):
    if len(_set) == 0:
        return "無"
    else:
        string = ""
        for i in _set:
            string += cuisine_dic[i] + " "
        # return str(_set).strip("\{\}").replace("\'", "")
        return string.strip()


def food_name2id(name: str) -> int:
    for key, value in cuisine_dic.items():
        if value == name:
            return key
    return -1


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
        self.data['cuisine'] = self.food_preference

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
        if price_dic.get(budget) == None:
            raise(ValueError)
        self.price_budget.add(budget)
        return self.price_budget

    def reset_price_budget(self):
        self.price_budget = set()
        return self.price_budget

    def get_price_budget(self):
        return price_to_str(self.price_budget)

    def reset_food_preference(self):
        self.food_preference = set()
        return self.food_preference

    def set_food_preference(self, food_list):
        if type(food_list) != type(set()):
            raise(TypeError)
        if any(cuisine_dic.get(x) == None for x in food_list):
            raise(ValueError)
        self.food_preference = food_list
        return self.food_preference

    def add_food_preference(self, food):
        if cuisine_dic.get(food) == None:
            raise(ValueError)
        self.food_preference.add(food)
        return self.food_preference

    def remove_food_preference(self, food):
        if food in self.food_preference:
            self.food_preference.remove(food)
        return self.food_preference

    def get_food_preference(self):
        return food_to_str(self.food_preference)

    def set_location(self, longitude=0, latitude=0, location=''):
        self.longitude = longitude
        self.latitude = latitude
        (long, lat) = change_location(location)  # 把location轉經緯度
        self.longitude = long
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
                    if cuisine['name'] == cuisine_dic[preference]:
                        flag = 1
                        break
            if flag:
                name.append(restaurant['name'])
                self.restaurants.append(restaurant)
        return name

    def recommend(self):
        self.restaurants = self.send_request()
        max = len(self.restaurants)
        num = random.randint(0, max)
        return self.restaurants[num]['name']
