import discord
from discord.ext import commands, tasks
import main, db, random
import mysql.connector

class Poker(commands.Cog):
    def __init__(self, client):
        self.client = client

    running = False
    @commands.command()
    async def create(self, ctx):
        # await ctx.message.guild.create_text_channel('High Rollers')
        channel = discord.utils.get(ctx.message.guild.channels, name='high-rollers')
        await channel.delete()

def setup(client):
    client.add_cog(Poker(client))