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

    # Check for Prefix >
    if message.content[0:1] == ">":
        # Assign content after prefix to command string
        command = message.content[1:]

        if command[:3] == "gif":
            tag = command[4:]
            await message.channel.send(file=discord.File(command_gif(tag)))


def command_gif(tag):
    gifList = {
        "general":          "img/general.GIF",
        "gifs":             "img/gifs.GIF",
        "milkwar":          "img/milkwar.GIF",
        "minecraftserver":  "img/minecraftserver.GIF",
        "minishield":       "img/minishield.GIF",
        "mori":             "img/mori.GIF",
        "stadia":           "img/stadia.GIF",
        "weebwill":         "img/weebwill.GIF",
        "ballsitch":        "img/ballsitch.GIF"
    }
    error_message = "There is no gif with that name."
    return gifList.get(tag, error_message)
    
# execute bot with token
bot.run(DISCORD_TOKEN)
