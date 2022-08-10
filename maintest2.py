from http import client
import discord
from discord.ext import commands
import youtube_dl

Token = ''
client = commands.Bot(command_prefix = '.')

players = {}

@client.event
async def on_ready():
    print('Bot online.')

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnet()

@client.command(pass_context=True)
async def play(ctx,url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()

@client.command(pass_context=True)
async def pause(ctx):
    id = ctx.messgae.server.id
    players[id].pause()

@client.command(pass_context=True)
async def stop(ctx):
    id = ctx.messgae.server.id
    players[id].stop()

@client.command(pass_context=True)
async def resume(ctx):
    id = ctx.messgae.server.id
    players[id].resume()

client.run(T)    