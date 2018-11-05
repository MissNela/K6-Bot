import discord
from diecord.ext import commands
from discord.ext.commands import bot
import asyncio
from intertools import cycle
import time

my_token = 'NTA5MDA2MDAzMjk2MDEwMjcx.DsHgZQ.MOa_hcp69bsEshVw__up8_lkc3M'

client = commands.Bot(command_prefix: 'K!')
client.remove_command('help')

@client.event
async def on_ready():
    print('The bot is ready and online!)

#Help command

@client.command(pass_context=True)
async def help():
    embed = discord.Embed(
        title = "Help",
        description = """
        Here is everything I could find.
        ``ping``
        The bot will say Pong!
        """,
        color = discord.Color.dark_blue()
)
    await client.say(embed=embed)
  
#ping will say Pong!

@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.content.starts_with("ping")
    await client.say(":ping_pong: Pong! :ping_pong:")
    
client.run(my_token)
