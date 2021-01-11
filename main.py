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

## Help Command ##
@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(
        title='EcoBot v0.0.1',
        description='Use #help <command> for extended information on a command',
        color=discord.Color.orange()
    )
    em.add_field(name='Bank', value='`register\n` `balance`', inline=True)
    em.add_field(name='Transactions', value='`give`', inline=True)
    em.add_field(name='Gambling', value='`coinflip`', inline=True)

    await ctx.send(embed=em)

@help.command()
async def register(ctx):
    em = discord.Embed(
        title='$register',
        description="Registers you to your server's EcoBot database",
        color=discord.Color.orange()
    )
    em.add_field(name='Syntax', value='`$register`')
    await ctx.send(embed=em)

@help.command()
async def balance(ctx):
    em = discord.Embed(
        title='$balance',
        description="Check your account balance",
        color=discord.Color.orange()
    )
    em.add_field(name='Syntax', value='`$balance`')
    await ctx.send(embed=em)

@help.command()
async def give(ctx):
    em = discord.Embed(
        title='$give',
        description="Give a selected user money from your account",
        color=discord.Color.orange()
    )
    em.add_field(name='Syntax', value='`$give <amount> <@user>`')
    em.add_field(name='Note', value='`<@user> = a tagged discord member`', inline=False)
    await ctx.send(embed=em)

@help.command()
async def coinflip(ctx):
    em = discord.Embed(
        title='$coinflip',
        description="Gamble the against the odds with heads or tails",
        color=discord.Color.orange()
    )
    em.add_field(name='Syntax', value='`$coinflip <heads/tails> <bet_amount>`')
    await ctx.send(embed=em)

## Runs Bot ##
client.run(ecobot)