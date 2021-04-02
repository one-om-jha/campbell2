import discord
from discord.ext import tasks, commands

class petty(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.__last_member = None

    @commands.command()
    async def channels(self, ctx):
        for guild in self.bot.guilds:
            for channel in guild.channels:
                print(channel.name + ": " + str(channel.id))
        await ctx.send("Done!")

    @commands.command()
    async def plsmod(self, ctx):
        channel = self.bot.get_channel(692181473645559940)
        await channel.send("through me, om is mod")
