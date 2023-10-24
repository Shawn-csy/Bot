import discord
from discord.ext import commands
import json
from test import astr, randomspin
import random
from decouple import config


# intents要求機器人的權限
intents = discord.Intents.all()
# command_prefix 是前綴符號
bot = commands.Bot(command_prefix="%", intents=intents)

'''各種梗圖'''
with open('tehe.json', 'r', encoding='utf-8') as json_file:
    commands_data = json.load(json_file)

for command_name, image_url in commands_data.items():
    @bot.command(name=command_name)
    async def dynamic_command(ctx, url=image_url):
        await ctx.send(url)

'''星座'''
astro = ['牡羊座', '金牛座', "雙子座", '巨蟹座', '獅子座', '處女座', '天秤座', '天蠍座', '射手座', '魔羯座',
         '水瓶座', '雙魚座', ]
for i in astro:
    @bot.command(name=i)
    async def dynamic_command(ctx, data=astr(i)):
        for j in data:
            await ctx.send(j)

'''抽籤'''


@bot.command()
async def 抽籤(ctx):
    for i in randomspin():
        await ctx.send(i)


'''擲骰'''


@bot.command()
async def 擲骰(ctx, dice: str):
    try:
        # 解析命令參數
        num_dice, num_sides = map(int, dice.split('D'))

        # 檢查擲骰參數是否有效
        if num_dice <= 0 or num_sides <= 0:
            await ctx.send("請輸入有效的骰子參數。")
            return

        # 擲骰並計算總和
        rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
        total = sum(rolls)

        # 發送結果到Discord
        await ctx.send(f"投擲 {num_dice} 個 {num_sides} 面骰的結果為: {', '.join(map(str, rolls))}，總和為 {total}")
    except Exception as e:
        await ctx.send("發生錯誤，請使用正確的格式，例如：%擲骰 2D6")


@bot.event
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")


bot.run(config('dc_token'))
