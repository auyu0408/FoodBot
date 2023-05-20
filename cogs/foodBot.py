import discord
from discord import app_commands

from core.classes import Cog_Extension
from include.foodAPI import FoodAPI

from collections import defaultdict

class FoodBot(Cog_Extension):
    apis = defaultdict(FoodAPI)

    @app_commands.command(name = "get_resturaunts", description = "取得附近餐廳")
    async def get_resturaunts(self, interaction: discord.Interaction):
        ls = self.api.get_resturaunts()
        await interaction.response.send_message(ls)

    @app_commands.command(name = "show_setting", description = "使用者的搜尋設定")
    async def show_setting(self, interaction: discord.Interaction):
        user = interaction.user.name
        ls = self.apis[user].get_food_preference()
        await interaction.response.send_message(f'{user} 的食物偏好: {ls}')

    # async def set_price_budget(self, interaction: discord.Interaction, min, max):
    #     self.api.set_price_budget(min, max)
    #     await interaction.response.send_message("設定成功")

    

async def setup(bot):
    await bot.add_cog(FoodBot(bot))