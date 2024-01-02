import discord
from discord.ext import commands

Token = ''

bot = commands.Bot(command_prefix="=")
@bot.event
async def on_ready():
    print("Bot is ready")
    bot.load_extension("music")

bot.run(Token)
