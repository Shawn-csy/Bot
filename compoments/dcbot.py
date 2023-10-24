import discord
from discord.ext import commands
import json
from test import astr, randomspin
import random

class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(command_prefix="%", intents=intents)
        self.add_commands()
        self.add_listeners()

    def add_commands(self):
        @self.command()
        async def 抽籤(ctx):
            for i in randomspin():
                await ctx.send(i)

        @self.command()
        async def 擲骰(ctx, dice: str):
            try:
                num_dice, num_sides = map(int, dice.split('D'))
                if num_dice <= 0 or num_sides <= 0:
                    await ctx.send("請輸入有效的骰子參數。")
                    return
                rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
                total = sum(rolls)
                await ctx.send(
                    f"投擲 {num_dice} 個 {num_sides} 面骰的結果為: {', '.join(map(str, rolls))}，總和為 {total}")
            except Exception as e:
                await ctx.send("ERROR， 格式是 %擲骰 2D6")

        with open('./stastic/memeurl.json', 'r', encoding='utf-8') as json_file:
            commands_data = json.load(json_file)
            for command_name, image_url in commands_data.items():
                self.add_dynamic_command(command_name, image_url)

        # 添加星座命令
        self.add_astro_commands()

    def add_dynamic_command(self, command_name, image_url):
        # 创建动态命令
        @self.command(name=command_name)
        async def dynamic_command(ctx):
            await ctx.send(image_url)

    def add_astro_commands(self):
        astro = ['牡羊座', '金牛座', "雙子座", '巨蟹座', '獅子座', '處女座', '天秤座', '天蠍座', '射手座', '魔羯座', '水瓶座', '雙魚座']
        for i in astro:
            self.add_astro_command(i)

    def add_astro_command(self, sign):
        @self.command(name=sign)
        async def astro_command(ctx):
            data = astr(sign)
            for j in data:
                await ctx.send(j)

    def add_listeners(self):
        @self.event
        async def on_ready():
            print(f"目前登入身份 --> {self.user}")
