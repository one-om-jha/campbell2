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
        await message.add_reaction('<:this:823714994424250368>')

    if "this!" in message.content.lower():
        await message.add_reaction('<:Fax:816331584999391262>')

    if "thisdge" in message.content.lower():
        await message.channel.send("https://cdn.discordapp.com/attachments/189827180610453505/822571054773174282/unknown.png")

    # Check for Prefix >
    if message.content[0:1] == "~":
        # Assign content after prefix to command string
        command = message.content[1:]

        if "img" in command[:3]:
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
        "timezone":         "https://cdn.discordapp.com/attachments/189827180610453505/821089009484562482/pDzzgWlEvLJ70JqZCdD2ag4bN_qEUe_omW5dikF1K_4.png"
    }
    error_message = "There is no gif with that name."
    return gifList.get(tag, error_message)

# execute bot with token
bot.run(DISCORD_TOKEN)
