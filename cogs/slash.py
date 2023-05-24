import discord
from typing import Optional
from discord import app_commands
from discord.app_commands import Choice
from core.classes import Cog_Extension

class Slash(Cog_Extension):
    # name指令名稱，description指令敘述
    @app_commands.command(name = "hello", description = "Hello, world!")
    async def hello(self, interaction: discord.Interaction):
        # 回覆使用者的訊息
        await interaction.response.send_message("Hello, world!")

    # @app_commands.describe(參數名稱 = 參數敘述)
    # 參數: 資料型態，可以限制使用者輸入的內容
    @app_commands.command(name = "add", description = "計算相加值")
    @app_commands.describe(a = "輸入數字", b = "輸入數字")
    async def add(self, interaction: discord.Interaction, a: int, b: int):
        await interaction.response.send_message(f"Total: {a + b}")

    # 參數: Optional[資料型態]，參數變成可選，可以限制使用者輸入的內容
    @app_commands.command(name = "say", description = "大聲說出來")
    @app_commands.describe(name = "輸入人名", text = "輸入要說的話")
    async def say(self, interaction: discord.Interaction, name: str, text: Optional[str] = None):
        if text == None:
            text = "。。。"
        await interaction.response.send_message(f"{name} 說 「{text}」")

    # @app_commands.choices(參數 = [Choice(name = 顯示名稱, value = 隨意)])
    @app_commands.command(name = "order", description = "點餐機")
    @app_commands.describe(meal = "選擇餐點", size = "選擇份量")
    @app_commands.choices(
        meal = [
            Choice(name = "漢堡", value = "hamburger"),
            Choice(name = "薯條", value = "fries"),
            Choice(name = "雞塊", value = "chicken_nuggets"),
        ],
        size = [
            Choice(name = "大", value = 0),
            Choice(name = "中", value = 1),
            Choice(name = "小", value = 2),
        ]
    )
    async def order(self, interaction: discord.Interaction, meal: Choice[str], size: Choice[int]):
        # 獲取使用指令的使用者名稱
        customer = interaction.user.name
        # 使用者選擇的選項資料，可以使用name或value取值
        meal = meal.value
        size = size.value
        await interaction.response.send_message(f"{customer} 點了 {size} 號 {meal} 餐")
    
    # invite button
    class Invite(discord.ui.View):
        def __init__(self, inv: str):
            super().__init__()
            self.inv = inv
            self.add_item(discord.ui.Button(label='邀請機器人', url=self.inv))

        @discord.ui.button(label='邀請機器人', custom_id="invite_button", style=discord.ButtonStyle.blurple)
        async def invite(self, button: discord.ui.Button, interaction: discord.Interaction):
            print("button clicked")
            await interaction.response.send_message(str(self.inv))

    @app_commands.command(name = "invite", description = "邀請機器人")
    async def invite(self, interaction: discord.Interaction):
        inv = await interaction.channel.create_invite()
        await interaction.response.send_message("邀請機器人", view=self.Invite(str(inv)))

    # counter button
    class Counter(discord.ui.View):
        def __init__(self):
            super().__init__()

        @discord.ui.button(label='0', custom_id="counter_button", style=discord.ButtonStyle.primary)
        async def count(self, button: discord.ui.Button, interaction: discord.Interaction):
            value = int(button.label)
            value += 1
            button.label = str(value)
            await interaction.response.edit_message(view=self)
        

    @app_commands.command(name = "counter", description = "計數器")
    async def counter(self, interaction: discord.Interaction):
        await interaction.response.send_message('計數器', view=self.Counter())

async def setup(bot):
    await bot.add_cog(Slash(bot))