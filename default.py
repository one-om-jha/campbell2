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
        num_fax = message.content.lower().count("fax")
        if num_fax > 3:
            num_fax = 3
        for x in range(num_fax):
            await message.channel.send(file=discord.File("img/fax.png"))
    
    if "this!" in message.content.lower():
        await message.channel.send("https://cdn.discordapp.com/attachments/189827180610453505/821394282677403658/Screenshot_20210310-215818_Snapchat.jpg")

    # Check for Prefix >
    if message.content[0:1] == ">":
        # Assign content after prefix to command string
        command = message.content[1:]

        if command[:3] == "gif":
            tag = command[4:]
            await message.channel.send(file=discord.File(command_gif(tag)))

        if "timezone" in command.lower():
            await message.channel.send("https://cdn.discordapp.com/attachments/189827180610453505/821089009484562482/pDzzgWlEvLJ70JqZCdD2ag4bN_qEUe_omW5dikF1K_4.png")

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
        "ballsitch":        "img/ballsitch.gif"
    }
    error_message = "There is no gif with that name."
    return gifList.get(tag, error_message)
    
# execute bot with token
bot.run(DISCORD_TOKEN)
