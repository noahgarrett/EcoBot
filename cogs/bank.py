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

    @commands.command()
    async def give(self, ctx, amt, member: discord.Member):
        server = ctx.guild.id
        user = ctx.author.id
        reciever = member.id
        try:
            balance =  await db.check_balance(server, user)
            if int(balance) >= int(amt):
                if int(amt) < 0:
                    await ctx.send('You cannot give someone a negative amount of money..')
                else:
                    update_balance = await db.give_money(server, user, reciever, amt)
                    if update_balance:
                        await ctx.send(f'Successfully gave {member.mention} **${amt}**')
                    else:
                        await ctx.send('Error')
            else:
                await ctx.send(f'You do not have enough money for this transaction. Current balance is: **${balance}**')
        except Exception as e:
            await ctx.send(e)



def setup(client):
    client.add_cog(Bank(client))