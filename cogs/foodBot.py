import discord
from discord import app_commands
from discord.app_commands import Choice

from core.classes import Cog_Extension
from include.foodAPI import FoodAPI

from collections import defaultdict

class FoodBot(Cog_Extension):
    # Create a API system for each user
    apis = defaultdict(FoodAPI)

    # Set location
    @app_commands.command(name = "set_location", description = "設定目前位置")
    async def set_location(self, interaction: discord.Interaction, location: str):
        user = interaction.user.name
        self.apis[user].set_location(location)
        await interaction.response.send_message(f"目前位置:{self.apis[user].get_location()}")

    # Set price budget
    @app_commands.command(name = "set_price_budget", description = "設定價格範圍")
    async def set_price_budget(self, interaction: discord.Interaction, min: int, max: int):
        user = interaction.user.name
        self.apis[user].set_price_budget(min, max)
        await interaction.response.send_message(f"價格範圍:{self.apis[user].get_price_budget()}")

    # Add food preference
    @app_commands.command(name = "add_food_preference", description = "設定食物偏好")
    @app_commands.describe(food = "輸入食物名稱")
    @app_commands.choices(
        food = [
            Choice(name = "漢堡", value = "漢堡"),
            Choice(name = "麵食", value = "麵食"),
            Choice(name = "速食", value = "速食"),
            Choice(name = "飯類", value = "飯類"),
            Choice(name = "飲料", value = "飲料"),
            Choice(name = "甜點", value = "甜點")
        ]
    )
    async def add_food_preference(self, interaction: discord.Interaction, food: str):
        user = interaction.user.name
        self.apis[user].add_food_preference(food)
        await interaction.response.send_message(f"食物偏好:{self.apis[user].get_food_preference()}")

    # Reset food preference
    @app_commands.command(name = "reset_food_preference", description = "重設食物偏好")
    async def reset_food_preference(self, interaction: discord.Interaction):
        user = interaction.user.name
        self.apis[user].reset_food_preference()
        await interaction.response.send_message(f"食物偏好:{self.apis[user].get_food_preference()}")

    # Get resturaunts
    @app_commands.command(name = "get_resturaunts", description = "取得附近餐廳")
    async def get_resturaunts(self, interaction: discord.Interaction):
        ls = self.api.get_resturaunts()
        await interaction.response.send_message(ls)
        
    # Recommend a resturaunt
    @app_commands.command(name = "recommend", description = "建議一間餐廳")
    async def recommend(self, interaction: discord.Interaction):
        resturaunt = self.api.recommend()
        await interaction.response.send_message(f"要不要吃:{resturaunt}")

    # Show setting
    @app_commands.command(name = "show_setting", description = "使用者的搜尋設定")
    async def show_setting(self, interaction: discord.Interaction):
        user = interaction.user.name
        ls = self.apis[user].get_food_preference()
        await interaction.response.send_message(f'{user} 的食物偏好: {ls}')
    

async def setup(bot):
    await bot.add_cog(FoodBot(bot))