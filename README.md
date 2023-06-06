# FoodBot 🍔 :fries:

This is a discord bot for choosing what to eat.

[![Unittest](https://github.com/auyu0408/FoodBot/actions/workflows/Unittest.yml/badge.svg)](https://github.com/auyu0408/FoodBot/actions/workflows/Unittest.yml) [![Coverage](https://github.com/auyu0408/FoodBot/blob/main/coverage.svg)](https://github.com/auyu0408/FoodBot/blob/main/coverage.svg)

## Set Up

### Prerequisites

- Python 3.10
- pipenv

### Step by step

1. Clone repo
```
$ git clone https://github.com/auyu0408/FoodBot.git
```

2. Install pipenv
```
$ pipenv install --python 3.10
```

3. Install Dependencies
```
$ sudo apt install build-essential libpython3-dev libdbus-1-dev
$ cd FoodBot
$ pip install -r requirements.txt
```

4. Change `config.ini.sample` into `config.ini`
```
$ cp config.ini.sample config.ini
```

5. Configure your Discord Bot token
![image](https://github.com/auyu0408/FoodBot/assets/73648626/167225af-76b4-417c-98a2-f4559a19e982)

6. Start the application
```
$ pipenv shell
$ python bot.py
```

7. Invite the bot into ypur discord server
