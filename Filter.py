import discord
from discord.ext import tasks, commands


class Filter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.__last_member = None
        
        global words
        words = []

        with open('filter.txt') as f:
            for line in f:
                words.append(line[:-1])
        
        print(words)

    async def handle_messages(message):
        await Filter.profanityChecker(message)

    async def profanityChecker(message):
        content = message.content.lower().split()
        for word in words:
            if word in content:
                author = message.author.id
                await message.reply("Check #rules.")

    def load_words():
        with open('filter.txt') as f:
            for line in f:
                currentPlace = line[:-1]
                words.append(currentPlace)
