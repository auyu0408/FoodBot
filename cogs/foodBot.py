import discord
from discord import app_commands
from discord.app_commands import Choice

from core.classes import Cog_Extension
from foodAPI.foodAPI import FoodAPI

from collections import defaultdict
import datetime
from typing import Dict


class FoodBot(Cog_Extension):
    # Create a API system for each user
    apis = defaultdict(FoodAPI)

    # Set location
    @app_commands.command(name="set_location", description="設定目前位置")
    async def set_location(self, interaction: discord.Interaction, location: str):
        user = interaction.user.name
        self.apis[user].set_location(location=location)
        await interaction.response.send_message(f"目前位置: {location}")

    # New set price budget
    class budget(discord.ui.View):
        def __init__(self, user, apis: Dict[str, FoodAPI]):
            super().__init__()
            self.user = user
            self.apis = apis

        @discord.ui.button(label="低", style=discord.ButtonStyle.gray)
        async def low(self, interaction: discord.Interaction, button: discord.ui.Button):
            if "低" in self.apis[self.user].get_price_budget():
                button.style = discord.ButtonStyle.gray
                self.apis[self.user].remove_price_budget(1)
            else:
                button.style = discord.ButtonStyle.primary
                self.apis[self.user].add_price_budget(1)
            await interaction.response.edit_message(view=self)
            # await interaction.response.send_message(f"價格範圍:{self.apis[self.user].get_price_budget()}")
            # await interaction.followup.send(f"價格範圍:{self.apis[self.user].get_price_budget()}")

        @discord.ui.button(label="中", style=discord.ButtonStyle.gray)
        async def medium(self, interaction: discord.Interaction, button: discord.ui.Button):
            if "中" in self.apis[self.user].get_price_budget():
                button.style = discord.ButtonStyle.gray
                self.apis[self.user].remove_price_budget(2)
            else:
                button.style = discord.ButtonStyle.primary
                self.apis[self.user].add_price_budget(2)
            await interaction.response.edit_message(view=self)
            # await interaction.response.send_message(f"價格範圍:{self.apis[self.user].get_price_budget()}")
            # await interaction.followup.send(f"價格範圍:{self.apis[self.user].get_price_budget()}")

        @discord.ui.button(label="高", style=discord.ButtonStyle.gray)
        async def high(self, interaction: discord.Interaction, button: discord.ui.Button):
            if "高" in self.apis[self.user].get_price_budget():
                button.style = discord.ButtonStyle.gray
                self.apis[self.user].remove_price_budget(3)
            else:
                button.style = discord.ButtonStyle.primary
                self.apis[self.user].add_price_budget(3)
            await interaction.response.edit_message(view=self)
            # await interaction.response.send_message(f"價格範圍:{self.apis[self.user].get_price_budget()}")
            # await interaction.followup.send(f"價格範圍:{self.apis[self.user].get_price_budget()}")

    @app_commands.command(name="set_price_budget", description="設定價格範圍")
    async def set_price_budget(self, interaction: discord.Interaction):
        user = interaction.user.name
        self.apis[user].reset_price_budget()
        view = self.budget(user, self.apis)
        embed = discord.Embed(
            title="請設定價格範圍",
            description="價格範圍包括: 低、中、高\n灰色代表未選擇\n藍色代表已選擇",
            color=discord.Color.blue(),
            timestamp=datetime.datetime.now()
        )
        await interaction.response.send_message(embed=embed, view=view)
    
    # Get price budget
    @app_commands.command(name="get_price_budget", description="取得價格範圍")
    async def get_price_budget(self, interaction: discord.Interaction):
        user = interaction.user.name
        await interaction.response.send_message(f"價格範圍: {self.apis[user].get_price_budget()}")

    # new add food preference
    class food_preference(discord.ui.View):
        def __init__(self, user, apis: Dict[str, FoodAPI]):
            super().__init__()
            self.user = user
            self.apis = apis

        @discord.ui.button(label="漢堡", style=discord.ButtonStyle.gray)
        async def hamburger(self, interaction: discord.Interaction, button: discord.ui.Button):
            if "漢堡" in self.apis[self.user].get_food_preference():
                button.style = discord.ButtonStyle.gray
                self.apis[self.user].remove_food_preference(177)
            else:
                button.style = discord.ButtonStyle.primary
                self.apis[self.user].add_food_preference(177)
            await interaction.response.edit_message(view=self)
            # self.apis[self.user].add_food_preference(177)
            # await interaction.response.send_message(f"食物偏好:{self.apis[self.user].get_food_preference()}")

        @discord.ui.button(label="牛排", style=discord.ButtonStyle.gray)
        async def steak(self, interaction: discord.Interaction, button: discord.ui.Button):
            if "牛排" in self.apis[self.user].get_food_preference():
                button.style = discord.ButtonStyle.gray
                self.apis[self.user].remove_food_preference(1211)
            else:
                button.style = discord.ButtonStyle.primary
                self.apis[self.user].add_food_preference(1211)
            await interaction.response.edit_message(view=self)
            # self.apis[self.user].add_food_preference(1211)
            # await interaction.response.send_message(f"食物偏好:{self.apis[self.user].get_food_preference()}")

        @discord.ui.button(label="麵食", style=discord.ButtonStyle.gray)
        async def noodle(self, interaction: discord.Interaction, button: discord.ui.Button):
            if "麵食" in self.apis[self.user].get_food_preference():
                button.style = discord.ButtonStyle.gray
                self.apis[self.user].remove_food_preference(201)
            else:
                button.style = discord.ButtonStyle.primary
                self.apis[self.user].add_food_preference(201)
            await interaction.response.edit_message(view=self)
            # self.apis[self.user].add_food_preference(201)
            # await interaction.response.send_message(f"食物偏好:{self.apis[self.user].get_food_preference()}")

        @discord.ui.button(label="素食", style=discord.ButtonStyle.gray)
        async def vegetarian(self, interaction: discord.Interaction, button: discord.ui.Button):
            if "素食" in self.apis[self.user].get_food_preference():
                button.style = discord.ButtonStyle.gray
                self.apis[self.user].remove_food_preference(186)
            else:
                button.style = discord.ButtonStyle.primary
                self.apis[self.user].add_food_preference(186)
            await interaction.response.edit_message(view=self)
            # self.apis[self.user].add_food_preference(186)
            # await interaction.response.send_message(f"食物偏好:{self.apis[self.user].get_food_preference()}")

        @discord.ui.button(label="便當", style=discord.ButtonStyle.gray)
        async def convenient(self, interaction: discord.Interaction, button: discord.ui.Button):
            if "便當" in self.apis[self.user].get_food_preference():
                button.style = discord.ButtonStyle.gray
                self.apis[self.user].remove_food_preference(1215)
            else:
                button.style = discord.ButtonStyle.primary
                self.apis[self.user].add_food_preference(1215)
            await interaction.response.edit_message(view=self)
            # self.apis[self.user].add_food_preference(1215)
            # await interaction.response.send_message(f"食物偏好:{self.apis[self.user].get_food_preference()}")

        @discord.ui.button(label="飲料", style=discord.ButtonStyle.gray)
        async def drink(self, interaction: discord.Interaction, button: discord.ui.Button):
            if "飲料" in self.apis[self.user].get_food_preference():
                button.style = discord.ButtonStyle.gray
                self.apis[self.user].remove_food_preference(181)
            else:
                button.style = discord.ButtonStyle.primary
                self.apis[self.user].add_food_preference(181)
            await interaction.response.edit_message(view=self)
            # self.apis[self.user].add_food_preference(181)
            # await interaction.response.send_message(f"食物偏好:{self.apis[self.user].get_food_preference()}")

        @discord.ui.button(label="甜點", style=discord.ButtonStyle.gray)
        async def dessert(self, interaction: discord.Interaction, button: discord.ui.Button):
            if "甜點" in self.apis[self.user].get_food_preference():
                button.style = discord.ButtonStyle.gray
                self.apis[self.user].remove_food_preference(176)
            else:
                button.style = discord.ButtonStyle.primary
                self.apis[self.user].add_food_preference(176)
            await interaction.response.edit_message(view=self)
            # self.apis[self.user].add_food_preference(176)
            # await interaction.response.send_message(f"食物偏好:{self.apis[self.user].get_food_preference()}")

    @app_commands.command(name="set_food_preference", description="設定食物偏好")
    async def set_food_preference(self, interaction: discord.Interaction):
        user = interaction.user.name
        self.apis[user].reset_food_preference()
        view = self.food_preference(user, self.apis)
        embed = discord.Embed(
            title="請選擇食物偏好",
            description="食物種類包括: 漢堡、牛排、麵食、素食、便當、飲料、甜點\n灰色代表未選擇\n藍色代表已選擇",
            color=discord.Color.blue(),
            timestamp=datetime.datetime.now()
        )
        await interaction.response.send_message(embed=embed, view=view)

    # Reset food preference
    # @app_commands.command(name="reset_food_preference", description="重設食物偏好")
    # async def reset_food_preference(self, interaction: discord.Interaction):
    #     user = interaction.user.name
    #     self.apis[user].reset_food_preference()
    #     await interaction.response.send_message(f"食物偏好: {self.apis[user].get_food_preference()}")
    
    # Get food preference
    @app_commands.command(name="get_food_preference", description="取得食物偏好")
    async def get_food_preference(self, interaction: discord.Interaction):
        user = interaction.user.name
        await interaction.response.send_message(f"食物偏好: {self.apis[user].get_food_preference()}")

    ## Get resturaunts
    #@app_commands.command(name="get_resturaunts", description="取得附近餐廳")
    #async def get_resturaunts(self, interaction: discord.Interaction):
    #    user = interaction.user.name
    #    ls = self.apis[user].get_restaurants()
    #    await interaction.response.send_message(ls)

    # Recommend a resturaunt
    @app_commands.command(name="recommend", description="建議一間餐廳")
    async def recommend(self, interaction: discord.Interaction):
        user = interaction.user.name
        resturaunt = self.apis[user].recommend()
        if resturaunt == "無":
            await interaction.response.send_message(f"沒有符合條件的餐廳")
        await interaction.response.send_message(f"要不要吃: {resturaunt}")

    # Show setting
    @app_commands.command(name="show_setting", description="使用者的搜尋設定")
    async def show_setting(self, interaction: discord.Interaction):
        user = interaction.user.name
        fs = self.apis[user].get_food_preference()
        ps = self.apis[user].get_price_budget()
        await interaction.response.send_message(f'{user} 的食物偏好: {fs}\n{user} 的預算: {ps}')


async def setup(bot):
    await bot.add_cog(FoodBot(bot))
