import discord
from discord import app_commands

from core.classes import Cog_Extension
from foodAPI import FoodAPI

class FoodBot(Cog_Extension):
    api = FoodAPI()

    @app_commands.command(name = "get resturaunts", description = "取得附近餐廳")
    async def get_resturaunts(self, interaction: discord.Interaction):
        ls = self.api.get_resturaunts()
        await interaction.response.send_message(ls)

async def setup(bot):
    await bot.add_cog(FoodBot(bot))