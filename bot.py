import discord
from discord.ext import commands

Token = 'OTg5ODg3ODIwMTY2NDc5ODgz.GUPR1c.VN8cDjXERI1KEbsK5eHp8vc0LRtUuKiTuJgWcs'

bot = commands.Bot(command_prefix="=")
@bot.event
async def on_ready():
    print("Bot is ready")
    bot.load_extension("music")

bot.run(Token)