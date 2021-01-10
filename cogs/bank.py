import discord
from discord.ext import commands, tasks
import main, db
import mysql.connector

class Bank(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def register(self, ctx):
        server = ctx.guild.id
        user = ctx.author.id
        try:
            await db.open_account(server, user)
            await ctx.send('Registered')
        except Exception as e:
            if e == f"1062 (23000): Duplicate entry '{user}' for key 'serverbank.PRIMARY'" or f"1062 (23000): Duplicate entry '{server}' for key 'serverbank.PRIMARY'":
                await ctx.send('You already have a registered account.')
            else:
                await ctx.send(e)

    @commands.command()
    async def balance(self, ctx):
        server = ctx.guild.id
        user = ctx.author.id
        try:
            balance = await db.check_balance(server, user)
            em = discord.Embed(
                title=f"{ctx.author.name}'s Account",
                description=f"Bank of {ctx.guild.name}",
                color=discord.Color.green()
            )
            em.add_field(name='Balance', value=f'${balance}')
            await ctx.send(embed=em)
        except Exception as e:
            await ctx.send('Please use #register to create your account')



def setup(client):
    client.add_cog(Bank(client))