import discord
from discord.ext import tasks, commands

import DaBaby
from DaBaby import *

class AbstractResponses(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.__last_member = None

    async def handle_messages(message):
        await AbstractResponses.replies(message)
        await AbstractResponses.reactions(message)
        await AbstractResponses.no(message)

    async def replies(message):
        content = message.content.lower()
        for key in reply_list:
            if key in content:
                await message.reply(reply_list[key])

    async def reactions(message):
        content = message.content.lower()
        for key in react_list:
            if key in content:
                await message.add_reaction(react_list[key])

    async def no(message):
        content = message.content.lower()
        if "no " in content or "no" in content[:2]:
            await message.add_reaction(❤️)

react_list = {
        "this!":                "<:this:823714994424250368>",
        "fax":                  "<:Fax:816331584999391262>",
        "dababy":               "<:dababy:827036898504736788>",
        "cactus":               "🌵",
        }

reply_list = {
        "thisdge":      "https://cdn.discordapp.com/attachments/189827180610453505/822571054773174282/unknown.png",
        "salaander":    "salaander"
        }
