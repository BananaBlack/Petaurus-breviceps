# 11/25/2020 botbot main file

# modules
from discord.ext import commands
import asyncpg
import os
import json

bot = commands.Bot(command_prefix='~', case_insensitive=True, owner_id=305731416812158979)
bot.remove_command('help')

bot.path = os.path.join(os.path.split(os.path.abspath(__file__))[0], 'utils/utils.json') #bullshit
with open(bot.path, 'r') as f:
  bot.utils = json.load(f)

extensions = (
    'cogs.utility',
)

async def create_db_pool():
  bot.db = await asyncpg.create_pool(database="postgres", user="postgres", password=" ")

  if __name__ == '__main__':
    for extension in extensions:
      try:
        bot.load_extension(extension)
      except Exception as error:
        print(f'{extension} cannot be loaded. [{error}]')

bot.loop.run_until_complete(create_db_pool)

bot.run(bot.utils["TOKEN"])