import discord
from discord.ext import tasks, commands

import re

class AbstractResponses(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.__last_member = None

    async def handle_messages(message):
        await AbstractResponses.replies(message)
        await AbstractResponses.reactions(message)

    async def replies(message):
        content = message.content.lower()
        for key in reply_list:
            if key in content:
                await message.reply(reply_list[key])

    async def reactions(message):
        content = message.content.lower()
        for key in react_list:
            if key in content.split():    
                await message.add_reaction(react_list[key])

react_list = {
        "this!":                "<:this:823714994424250368>",
        "fax":                  "<:Fax:816331584999391262>",
        "dababy":               "<:dababy:827036898504736788>",
        "cactus":               "🌵",
        "no":                   "❤️"
        }

reply_list = {
        "thisdge":      "https://cdn.discordapp.com/attachments/189827180610453505/822571054773174282/unknown.png",
        "salaander":    "salaander",
        "i cant quite find the words jaden, and i consider myself an erudite man, to describe the heinous acts of human cruelty that i would commit to fuck your sister. The precise and grueling words that my brain so desperately tongues around in my memory to find that would accurately describe, in detail, exactly what i would do to your sister's guts, evade me. And yet, I do not hesitate to emphasize my point enough. Given the opportunity, I would not relent. The sky would blacken and hell would freeze over before the concept of stopping would even begin to creep into the annals of my mind. \"Stop what?\" you might ask, and to that I answer that I am not exactly sure what. My brain fails to comprehend the true nature of this action, or what it would look like, all I know is that no amount of it could ever satisfy me.":   "what the actual fuck my son"
        }
