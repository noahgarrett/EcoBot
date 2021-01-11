import discord
from discord.ext import commands, tasks
import main

class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity=discord.Game("w/ Capitalism"))
        print("Bot is online.")
        print(f'Discord.PY Version: {discord.__version__}')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Please use #help for the correct arguments')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == 210801541219745792:
            await message.channel.send('Crump stfu')

def setup(client):
    client.add_cog(Events(client))