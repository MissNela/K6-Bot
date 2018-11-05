import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
from intertools import cycle
import time

my_token = 'NTA5MDA2MDAzMjk2MDEwMjcx.DsHgZQ.MOa_hcp69bsEshVw__up8_lkc3M'

client = commands.Bot(command_prefix = 'K!')
client.remove_command('help')

@client.event
async def on_ready():
    print('The bot is online and connected with Discord.')

#Help command

@client.command(pass_context=True)
async def help():
    embed = discord.Embed(
        title = "Help",
        description = """
        Here is everything I could find.
        ``ping``
        Bot řekne Pong

        """,
        color = discord.Color.dark_blue()
)
    await client.say(embed=embed)
  
#ping will say Pong!

@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.content.startswith('Ping'):
        await client.send_message(message.channel, ':ping_pong: Pong! :ping_pong:')
    
client.run(my_token)
