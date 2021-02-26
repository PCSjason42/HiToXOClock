import discord
from discord.ext import commands, tasks
from datetime import datetime
import pytz
import time

class Hi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Started!")
        while True:
            nowMin = datetime.now(pytz.timezone("Hongkong")).minute
            if nowMin == 30:
                nowHour = datetime.now(pytz.timezone("Hongkong")).hour
                while True:
                    channel = self.bot.get_channel(795545262822260756)
                    nowHour += 1
                    if nowHour == 0:
                        nowHour = 12
                    elif nowHour < 13:
                        nowHour = nowHour
                    else:
                        nowHour = nowHour % 12
                    await channel.send(f"Hi to {nowHour} o'clock")
                    await channel.send("Hi")
                    time.sleep(3600)

def setup(bot):
    bot.add_cog(Hi(bot))
