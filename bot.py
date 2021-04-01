# Import discord.py library
import discord
from discord.ext import tasks, commands

# import classes
import AbstractResponses
from AbstractResponses import *
import Gifs
from Gifs import *
import OneLiners
from OneLiners import *

# gets client object from discord.py
bot = commands.Bot(command_prefix='~')

# Get discord token
import os
from dotenv import load_dotenv
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_DEV_TOKEN")

@bot.listen('on_message')
async def abstractListener(message):
    if not message.author.bot:
        await AbstractResponses.handle_messages(message)

# Register cogs
bot.add_cog(AbstractResponses(bot))
bot.add_cog(Gifs(bot))
bot.add_cog(OneLiners(bot))

# execute bot with token
bot.run(DISCORD_TOKEN)
