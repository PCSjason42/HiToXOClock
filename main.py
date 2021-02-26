import discord
from discord.ext import commands
import os
from decouple import config

bot = commands.Bot(command_prefix="p?")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="powered by discord.py"))
    print('We have logged in as {0.user}. Bot is ready.'.format(bot))

for i in os.listdir('./cogs'):
    if i.endswith('.py'):
        bot.load_extension(f'cogs.{i[:-3]}')
print('Extensions loaded!')

bot.run(config("TOKEN"), bot=False)