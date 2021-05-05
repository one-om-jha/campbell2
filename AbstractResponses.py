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
        "i cant quite find the words jaden, and i consider myself an erudite man,":   "what the actual fuck my son",
        "yes ma'am":    "https://cdn.discordapp.com/attachments/431240474188316672/837663670674522132/Screenshot_20210427-170307_Snapchat.png",
        "what if my birthday cake is like a mcyt dnf basori knightxhornet septiplier hamilton": "what the actual fuck" 
        }
