from twitchio.ext import commands


class TwitchBot:
    def __init__(self, token, nick, prefix, client_id, initial_channels):
        self.bot = commands.Bot(
            token=token,
            nick=nick,
            prefix=prefix,
            client_id=client_id,
            initial_channels=initial_channels
        )

        @self.bot.command(name="hi")  # 註冊指令
        async def hi(ctx):
            await ctx.send('Hi')

        @self.bot.command(name="domo")  # 註冊指令
        async def domo(ctx):
            await ctx.send(ctx.message.content)

    async def start(self):
        print(f"機器人 {self.bot.nick} 現在運行中.")
        await self.bot.start()




