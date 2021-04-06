import discord
from discord.ext import tasks, commands

image_list = {
        "timezone": "https://cdn.discordapp.com/attachments/189827180610453505/828661635504799790/Time_Zones.jpg",
        "bitch":    "https://cdn.discordapp.com/attachments/189827180610453505/828983816144027648/image0.jpg"
        }

class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.__last_member = None

    @commands.command()
    async def img(self, ctx, img):
        await ctx.send(image_list.get(img))
