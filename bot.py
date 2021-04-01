# Import discord.py library
import discord
from discord.ext import tasks, commands

# gets client object from discord.py
bot = commands.Bot(command_prefix='~')

# Get discord token
import os
from dotenv import load_dotenv
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


# Commands

@bot.command()
async def gif(ctx, arg):
    gif_list = {
            "general":      "img/general.gif",
            "gifs":             "img/gifs.gif",
            "milkwar":          "img/milkwar.gif",
            "minecraftserver":  "https://media.discordapp.net/attachments/809112873665953793/809209556097433610/image2.gif",
            "minishield":       "img/minishield.gif",
            "mori":             "img/mori.gif",
            "stadia":           "https://media.discordapp.net/attachments/809112873665953793/809209650208571463/image0.gif",
            "weebwill":         "https://media.discordapp.net/attachments/809112873665953793/809209555623739412/image1.gif",
            "ballsitch":        "img/ballsitch.gif",
            "this":             "img/this.gif"
            }
    await ctx.send(gif_list.get(arg);

# execute bot with token
bot.run(DISCORD_TOKEN)
