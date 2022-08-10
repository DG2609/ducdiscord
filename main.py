import discord
from discord.ext import commands

improt music

cogs = [music]

client = commands.Bot(command_prefix='?',intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run("OTg5ODg3ODIwMTY2NDc5ODgz.GS-MEN.cLgmUk2j_MBlhZOvdptesTXy92IQGLVf6U1uVU")