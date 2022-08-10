import discord
from discord import FFmpegPCMAudio
from discord import client
from discord.ext import commands
from youtube_dl import YoutubeDL
import requests


Token = 'OTg5ODg3ODIwMTY2NDc5ODgz.GUPR1c.VN8cDjXERI1KEbsK5eHp8vc0LRtUuKiTuJgWcs'

def search(query):
    with YoutubeDL({'format': 'bestaudio', 'noplaylist': 'true'}) as ydl:
        try:
            request.get(query)
        except:
            info = ydl.extract_info(f"ytsearch:{query}",download=False)['entries'][0]
        else:
            info = ydl.extract_info(query, download=False)
    return (info, info['formats'][0]['url'])

Client = commands.Bot(command_prefix=";")

@Client.command(name="Join",help="joins the channel the author is in",aliases=["join","J","j"])
async def Join(context):
  member_voice = context.author.voice
  if member_voice and member_voice.channel:
    if context.voice_client:
      await context.send("Bot already in a voice channel!")
    else:
      try:
        await member_voice.channel.connect()
        await context.send("Pé Hoa đã tới")
      except:
        await context.send("An error occured make sure you're in a voice channel!")

@Client.command(name="Leave",help="Leaves the channel the bot is currently in",aliases=["leave","L","l"])
async def Leave(context):
  member_voice = context.author.voice
  if member_voice and member_voice.channel:
    if context.voice_client:
      if member_voice.channel == context.voice_client.channel:
        try:
          if context.voice_client.is_playing():
            context.voice_client.stop()
            await context.voice_client.disconnect()
            await context.send("Disconneted")
          else:
            await context.voice_client.disconnect()
            await context.send("Disconneted")
        except:
          await context.send("An error occured")
      else:
        await context.send("You must be in the same voice channel as the bot")
    else:
      await context.send("Bot is not in a voice channel!")

@Client.command(name="Play",help="Plays a song",aliases=["play","P","p"])
async def play(context,*,query):
  member_voice = context.author.voice
  if member_voice and member_voice.channel:
    if context.voice_client:
      client_voice = context.voice_client
      video, source = search(query)
      await context.send(f"Now playing: {video['title']}")
      client_voice.play(FFmpegPCMAudio(source))
      client_voice.is_playing()
    else:
      await member_voice.channel.connect()
      client_voice = context.voice_client
      video, source = search(query)
      await context.send(f"Now playing: {video['title']}")
      client_voice.play(FFmpegPCMAudio(source))
      client_voice.is_playing()


@Client.event
async def on_ready():
  print("Bot is ready")
Client.run(Token)