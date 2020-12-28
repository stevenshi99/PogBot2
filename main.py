import discord
import os
from dotenv import load_dotenv
from keep_alive import keep_alive

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
# if not TOKEN is None:
#     TOKEN = '';
client = discord.Client()
from discord.utils import find

@client.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'bots',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send('Hello {}! Press $help for a full list of commands'.format(guild.name))

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!mald'):
        await message.channel.send(file=discord.File('maldM.gif'))

    if message.content.startswith('!pbjt'):
        await message.channel.send(file=discord.File('pbjt.gif'))    

    if message.content.startswith('!help'):
        await message.channel.send('!hello - I will say hello back to you :kitty:\n!pbjt - epic pbjt gif\n!mald - malding emote gif\n!help - display this list again')

        
keep_alive()
client.run(TOKEN)