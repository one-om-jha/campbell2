import discord
from discord.ext import tasks, commands
import io
import aiohttp
import random

image_list = {
        "timezone": "https://cdn.discordapp.com/attachments/189827180610453505/828661635504799790/Time_Zones.jpg",
        "bitch":    "https://cdn.discordapp.com/attachments/189827180610453505/828983816144027648/image0.jpg",
        "ratio":    "https://cdn.discordapp.com/attachments/189827180610453505/829712330166108230/D7E51CD2-2758-4251-9F9A-6824143CDB9F.JPG",
        "mugiwtf":  "https://cdn.discordapp.com/attachments/189827180610453505/829712550874185749/04F934DE-6F85-4DFB-88F8-7A629F2F77C7.JPG"
        }

class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.__last_member = None

    @commands.command()
    async def img(self, ctx, img):
        await ctx.send(image_list.get(img))

    @commands.command()
    async def horse(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://thishorsedoesnotexist.com') as resp:
                if resp.status != 200:
                    return await ctx.send("Could not get file...")
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'horse.jpg'))

    @commands.command()
    async def waifu(self, ctx):
        num = random.randint(1,99999)
        url = "https://www.thiswaifudoesnotexist.net/example-{0}.jpg".format(num)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    return await ctx.send("Could not get file...")
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'waifu.jpg'))

    @commands.command()
    async def art(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://thisartworkdoesnotexist.com') as resp:
                if resp.status != 200:
                    return await ctx.send("Could not get file...")
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'art.jpg'))
