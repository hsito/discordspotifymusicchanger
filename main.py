import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
token1 = os.getenv('DISCORD_TOKEN')



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
    # print(member)
    # print(before)
    # print(after)
    # print(after.channel)

    # if after.channel is not None:
    #         print('hi')
    #         await member.guild.system_channel.send(f"{member.display_name} has joined {after.channel.name}")
    if after.channel is not None and str(member) == "Nekotina#0608":
        print('nekotina has joined')
    else:
        print('nekotina has left')





client.run(token1)