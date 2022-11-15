import discord
from discord.ext import commands, tasks
import os
import datetime
import random
import subprocess
from itertools import cycle

class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def is_it_me(ctx):
        return ctx.author.id == 409445517509001216

    def admin(ctx):
        return ctx.author.guild_permissions.manage_guild or ctx.author.id == 409445517509001216

    @commands.Cog.listener()
    async def on_ready(self):
        print("Fun processes active.")

    @commands.command()
    @commands.check(is_it_me)
    async def funtest(self, ctx):
        await ctx.send('Fun extension cog works!')

    @commands.command(aliases=['8ball'])
    async def eightball(self, ctx, *, question="TBD (Try typing a question after the command)"):
        responses = ['Hmmmm.',
                     'Ask again.',
                     "It's possible.",
                     'Maybe.',
                     'Perhaps.',
                     'Not sure.',
                     'Uncertain.',
                     '(͡° ͜ʖ ͡°)',
                     'No clue.',
                     'Response hazy.']
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    @commands.command(aliases=['rd'])
    async def rolldice(self, ctx, sides=6, amount=1):
        diceList=[]
        for i in range(0, amount):
            diceList.append(random.randint(1,sides))
            i = i + 1
        await ctx.send("Your roll(s) are:  " + str(diceList))

    @commands.command()
    async def snap(self, ctx):
        snap = random.randint(0, 1)
        if snap == 0:
            await ctx.send("You survived, now go make use of the resources you have left and rebuild your world.")
        if snap == 1:
            await ctx.send("Sorry, little one, but you were sacrificed for the greater good.")

    @commands.command()
    async def rps(self, ctx, choice=""):
        botchoice = random.randint(0, 2)
        if botchoice == 0 and choice.lower() == "rock":
            await ctx.send("I chose rock!  It's a tie!")
        elif botchoice == 0 and choice.lower() == "paper":
            await ctx.send("I chose rock! You win!")
        elif botchoice == 0 and choice.lower() == "scissors":
            await ctx.send("I chose rock! I win!")
        elif botchoice == 1 and choice.lower() == "rock":
            await ctx.send("I chose paper!  I win!")
        elif botchoice == 1 and choice.lower() == "paper":
            await ctx.send("I chose paper! It's a tie!")
        elif botchoice == 1 and choice.lower() == "scissors":
            await ctx.send("I chose paper! You win!")
        elif botchoice == 2 and choice.lower() == "rock":
            await ctx.send("I chose scissors!  You win!")
        elif botchoice == 2 and choice.lower() == "paper":
            await ctx.send("I chose scissors! I win!")
        elif botchoice == 2 and choice.lower() == "scissors":
            await ctx.send("I chose scissors! It's a tie!")
        else:
            if botchoice == 0:
                await ctx.send("I chose rock!")
            elif botchoice == 1:
                await ctx.send("I chose paper!")
            elif botchoice == 2:
                await ctx.send("I chose scissors!")
            else:
                await ctx.send("You've royally screwed up")

    @commands.command(aliases=['bn'])
    async def bignumber(self, ctx):
        for i in range(0, random.randint(1, 1000)):
            i = i * random.randint(1, 1000)
        await ctx.send(i)

    @commands.command(aliases=['brn'])
    async def biggernumber(self, ctx):
        for i in range(1000, random.randint(1001, 1000000)):
            i = i * random.randint(1000, 1000000)
        await ctx.send(i)

    @commands.command(aliases=['bstn'])
    async def biggestnumber(self, ctx):
        for i in range(0, random.randint(1, 1000)):
            i = i ** random.randint(1, 1000)
        await ctx.send(i)

    @commands.command(hidden=True)
    async def secret(self, ctx):
        await ctx.channel.purge(limit=1)
        await ctx.send("SHH!!!", delete_after=3)

    @commands.command(aliases=['echo'])
    @commands.check(is_it_me)
    async def say(self, ctx, *, words: commands.clean_content):
        print(words)
        await ctx.channel.purge(limit=1)
        await ctx.send(words)

def setup(bot):
    bot.add_cog(Fun(bot))
