import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
token1 = os.getenv('DISCORD_TOKEN')
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
redirect_uri = os.getenv('REDIRECT_URI')

scope = 'user-modify-playback-state'  # Specify the required scope(s) for controlling playback

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
intents.presences = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        print('hi')
        await message.channel.send('Hello!')

    # if message.content.startswith('$get_voice_channels'):
    #     await message.channel.send(message.guild.voice_channels)

@client.event
async def on_voice_state_update(member, before, after):

    if after.channel is not None and str(member) == "Nekotina#0608":
        print('nekotina has joined')
        sp.pause_playback()
    else:
        sp.start_playback()
        print('nekotina has left')





client.run(token1)