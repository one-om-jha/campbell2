import discord
from discord.ext import tasks, commands

class DaBaby(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.__last_member = None

    warned_users = []

    async def handle_messages(message: discord.Message):
        await DaBaby.less_gooo_chat(message)

    async def less_gooo_chat(message: discord.Message):
        if message.channel.name == "less-gooo" and not message.author.bot:
            if not DaBaby.has_less_gooo(message.content.lower()):
                await message.reply("Hi {0}, I noticed you posted a message withou    t saying LESS GOOO in the designated channel.".format(message.author.mention))

    async def name_guidelines(message: discord.Message):
        if message.author.id not in DaBaby.warned_users:
            if (not DaBaby.has_less_gooo(message.author.display_name.lower())
                    or "dababy" not in message.author.display_name.lower()):
                DaBaby.warned_users.append(message.author.id)
                await message.reply("Hi {0}, I noticed your name does not comply w    ith the dababy official discord naming rules. Please correct this obvous mistake.    ".format(message.author.mention))

    def has_less_gooo(content):
        return "le" in content and "go" in content
