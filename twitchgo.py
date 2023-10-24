from compoments.twitch import TwitchBot
from decouple import config
import asyncio

# 要跟DC同時開才能用的爛BOT
async def main():
    twbot = TwitchBot(
        token=config('TW_ACCESS_TOKEN'),
        nick="twitchbot",
        prefix="!",
        client_id=config("TW_CLIENT_ID"),
        initial_channels=["booostman"]
    )
    await twbot.start()

asyncio.run(main())