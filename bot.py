# Import discord.py library
import discord
from discord.ext import tasks, commands

# import classes
import AbstractResponses
import Gifs
import OneLiners
import Images

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
        await AbstractResponses.AbstractResponses.handle_messages(message)

# Register cogs
bot.add_cog(AbstractResponses.AbstractResponses(bot))
bot.add_cog(Gifs.Gifs(bot))
bot.add_cog(OneLiners.OneLiners(bot))
bot.add_cog(Images.Images(bot))

# execute bot with token
bot.run(DISCORD_TOKEN)
