import discord
from discord.ext import tasks, commands

gif_list = {
        "general":          "img/general.gif",
        "gifs":             "img/gifs.gif",
        "milkwar":          "img/milkwar.gif",
        "minecraftserver":  "img/minecraftserver.gif",
        "minishield":       "img/minishield.gif",
        "mori":             "img/mori.gif",
        "stadia":           "img/stadia.gif",
        "weebwill":         "img/weebwill.gif",
        "ballsitch":        "img/ballsitch.gif",
        "this":             "img/this.gif",
        "ryuuko":           "img/ryuuko.gif"
        }

class Gifs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.__last_member = None

    @commands.command()
    async def gif(self, ctx, gif):
        await ctx.send(file=discord.File(gif_list[gif]))
