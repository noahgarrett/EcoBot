import discord
from discord.ext import commands, tasks
import main, db, random
import mysql.connector

class Gambling(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def coinflip(self, ctx, pick, bet_amt):
        server = ctx.guild.id
        user = ctx.author.id
        balance = await db.check_balance(server, user)
        h_picks = ['H', 'h', 'Heads', 'heads']
        t_picks = ['T', 't', 'Tails', 'tails']
        if int(balance) >= int(bet_amt):
            bot_pick = random.randint(0,1)
            if pick[0] == 'H' or pick[0] == 'h':
                pick = 0
                if pick == bot_pick:
                    winnings = int(bet_amt) * 2
                    update_balance = await db.increase_balance(server, user, winnings)
                    if update_balance:
                        await ctx.send(f'You won! Enjoy your **${winnings}**.')
                    else:
                        await ctx.send('Unknown Error. Unable to update your balance.')
                else:
                    losings = int(bet_amt)
                    update_balance = await db.decrease_balance(server, user, losings)
                    if update_balance:
                        await ctx.send(f'You lost! You are now down **${losings}**.')
                    else:
                        await ctx.send('Unknown Error. Unable to update your balance.')
            elif pick[0] == 'T' or pick[0] == 't':
                pick = 1
                if pick == bot_pick:
                    winnings = int(bet_amt) * 2
                    update_balance = await db.increase_balance(server, user, winnings)
                    if update_balance:
                        await ctx.send(f'You won! Enjoy your **${winnings}**.')
                    else:
                        await ctx.send('Unknown Error. Unable to update your balance.')
                else:
                    losings = int(bet_amt)
                    update_balance = await db.decrease_balance(server, user, losings)
                    if update_balance:
                        await ctx.send(f'You lost! You are now down **${losings}**.')
                    else:
                        await ctx.send('Unknown Error. Unable to update your balance.')
            else:
                await ctx.send('You must choose **heads** or **tails**')
        else:
            await ctx.send(f'You do not have enough money for this bet. Your current balance is: **${balance}**')


def setup(client):
    client.add_cog(Gambling(client))