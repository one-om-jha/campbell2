import discord
from discord.ext import tasks, commands

class OneLiners(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.__last_member = None

    @commands.command()
    async def flex(self, ctx, mention: discord.Member):
        reply = "{0.mention} got caught flexing in {1.name} by {0.mention}. Bitch.".format(mention, ctx.guild, ctx.author)
        await ctx.send(reply)

    @commands.command()
    async def sus(self, ctx, mention: discord.Member):
        reply = "{0.mention} ayo son? wtf.".format(mention)
        await ctx.send(reply)
