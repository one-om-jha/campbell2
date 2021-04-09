# Import discord.py library
import discord
from discord.ext import tasks, commands

# import classes
from AbstractResponses import AbstractResponses
from Gifs import Gifs
from OneLiners import OneLiners
from Images import Images
from Filter import Filter

# gets client object from discord.py
bot = commands.Bot(command_prefix='~')

# Get discord token
import os
from dotenv import load_dotenv
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

@bot.listen('on_message')
async def abstractListener(message):
    if not message.author.bot:
        await Filter.handle_messages(message)
        await AbstractResponses.handle_messages(message)

# Register cogs
bot.add_cog(AbstractResponses(bot))
bot.add_cog(Gifs(bot))
bot.add_cog(OneLiners(bot))
bot.add_cog(Images(bot))
bot.add_cog(Filter(bot))

# execute bot with token
bot.run(DISCORD_TOKEN)
