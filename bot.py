# Import discord.py library
import discord
from discord.ext import tasks, commands

# gets client object from discord.py
bot = commands.Bot(command_prefix='~')

# Get discord token
import os
from dotenv import load_dotenv
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


# Commands

@bot.event()
async def on_message():
    # Run abstract reactions
    reactions(message)

    # Run abstract replies
    replies(message)

async def reactions(message: Message):
    react_list = {
            "fax":      "<:Fax:816331584999391262>",
            "this!":    "<:this:823714994424250368>",
            "dababy":   "<:dababy:827036898504736788>"
            }
    content = message.content.lower()
    for key in (key in react_list if key in content):
        await message.add_reaction(react_list.get(key))

async def replies(message: Message):
    reply_list = {
            "thisdge":      "https://cdn.discordapp.com/attachments/189827180610453505/822571054773174282/unknown.png"
            }
    content = message.content.lower()
    for key in (key in reply_list if key in content):
        await message.reply(reply_list.get(key))


@bot.command()
async def gif(ctx, gif):
    gif_list = {
            "general":      "img/general.gif",
            "gifs":             "img/gifs.gif",
            "milkwar":          "img/milkwar.gif",
            "minecraftserver":  "https://media.discordapp.net/attachments/809112873665953793/809209556097433610/image2.gif",
            "minishield":       "img/minishield.gif",
            "mori":             "img/mori.gif",
            "stadia":           "https://media.discordapp.net/attachments/809112873665953793/809209650208571463/image0.gif",
            "weebwill":         "https://media.discordapp.net/attachments/809112873665953793/809209555623739412/image1.gif",
            "ballsitch":        "img/ballsitch.gif",
            "this":             "img/this.gif"
            }
    await ctx.send(gif_list.get(gif);

@bot.command()
async def flex(ctx, mention: Member):
    reply = "{0.mention} got caught flexing in {1.name} by {0.mention}. Bitch.".format(mention, ctx.guild, ctx.author)
    await ctx.send(reply)

@bot.command()
async def sus(ctx, mention: Member):
    reply = "{0.mention} ayo son? wtf.".format(mention)
    await ctx.send(reply)

# execute bot with token
bot.run(DISCORD_TOKEN)
