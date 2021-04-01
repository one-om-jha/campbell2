# Import discord.py library
import discord

# gets client object from discord.py
bot = discord.Client()

# Get discord token
import os
from dotenv import load_dotenv
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# How this works! (for future me)
# utilizes discord.py
# https://discordpy.readthedocs.io/en/latest/

# Event Listeners - indicated by @bot.event
# on_ready()    - bot online
# on_message()  - detects message sent in channel

# on_message()
# returns Message object when message is detected
# https://discordpy.readthedocs.io/en/latest/api.html#message

dababy_reminders = []

# Event Listener - Bot Online
@bot.event
async def on_ready():
    print("Campbell 2 is online.")

# Event Listener - New Message Detected
@bot.event
async def on_message(message):
    if message.content == "hi campbell":
        await message.channel.send("hello")

    if "fax" in message.content.lower():
        await message.add_reaction('<:Fax:816331584999391262>')

    if "this!" in message.content.lower():
        await message.add_reaction('<:this:823714994424250368>')
    
    if "thisdge" in message.content.lower():
        await message.channel.send("https://cdn.discordapp.com/attachments/189827180610453505/822571054773174282/unknown.png")

# DaBaby
    if message.channel.name == 'less-gooo' and ("le" not in message.content.lower() or "go" not in message.content.lower()) and not message.author.bot:
        await message.channel.send("Hi {0}, I noticed you posted a message without saying LESS GOOO in the designated channel.".format(message.author.mention))

    if message.channel.name == 'dababy_discussion' and and message.author.id not in dababy_reminders and ("le" not in message.author.display_name.lower() or "go" not in message.author.display_name.lower())  and message.author != bot.user:
        dababy_reminders.append(message.author.id)
        await message.channel.send("Hi {0}, I noticed your name does not comply with the dababy official discord naming rules. Please correct this obvous mistake.".format(message.author.mention))

    if ("le" in message.content.lower() and "go" in message.content.lower()) or "dababy" in message.content.lower():
        await message.add_reaction('<:dababy:827036898504736788>')

    # Check for Prefix >
    if message.content[0:1] == "~":
        # Assign content after prefix to command string
        command = message.content[1:]

        if "img" in command[:3] or "gif" in command[:3]:
            tag = command[4:]
            await message.channel.send(file=discord.File(command_gif(tag)))

        if "flex" in command[:4]:
            reply = "{1} got caught flexing in {2} by {0}. Bitch.".format(message.author.mention, message.mentions[0].mention, message.guild.name)
            await message.channel.send(reply)

        if "sus" in command[:3]:
            reply = "{0}, ayo son? wtf.".format(message.mentions[0].mention)
            await message.channel.send(reply)

def command_gif(tag):
    gifList = {
        "general":          "img/general.gif",
        "gifs":             "img/gifs.gif",
        "milkwar":          "img/milkwar.gif",
        "minecraftserver":  "img/minecraftserver.gif",
        "minishield":       "img/minishield.gif",
        "mori":             "img/mori.gif",
        "stadia":           "img/stadia.gif",
        "weebwill":         "img/weebwill.gif",
        "ballsitch":        "img/ballsitch.gif",
        "this":             "img/this.gif"
    }
    error_message = "There is no gif with that name."
    return gifList.get(tag, error_message)

# execute bot with token
bot.run(DISCORD_TOKEN)
