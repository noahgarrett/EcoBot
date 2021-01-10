import discord
from discord.ext import commands, tasks
from discord.utils import get
import asyncio, os, json
from constants.prefix import *
from constants.tokens import *


client = commands.Bot(command_prefix= ecobot_prefix)
client.remove_command('help')

## Cog Setup ##
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f'Loaded: {filename[:-3]}')

## Runs Bot ##
client.run(ecobot)