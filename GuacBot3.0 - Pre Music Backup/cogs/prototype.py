import discord
from discord.ext import commands, tasks
import os
import datetime
import random
import subprocess
from itertools import cycle


def charLimit(longString):
    if (len(longString) > 2000):
        substringList = []
        loops = (int) (len(longString) / 2000)
        x = 0
        for i in range(loops + 1):
            substringList.append(longString[x:x + 2000])
            x = x + 2000
        return substringList
    else:
        return [longString]

class Prototype(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def is_it_me(ctx):
        return ctx.author.id == 409445517509001216

    def admin(ctx):
        return ctx.author.guild_permissions.manage_guild or ctx.author.id == 409445517509001216

    @commands.Cog.listener()
    async def on_ready(self):
        print('Prototype processes active.')

    @commands.command()
    @commands.check(is_it_me)
    async def prototypetest(self, ctx):
        await ctx.send('Prototype extension cog works!')

    @commands.command()
    @commands.check(is_it_me)
    async def testembed(self, ctx):
        embed = discord.Embed(title="Suck my left nut", description="Give me your animosity.", colour=discord.Color.purple(), url="https://www.youtube.com/watch?v=iik25wqIuFo")
        embed.add_field(name="Why?",value="I am an awful human being and all I want in return is recognition for my evil manner, so click the title of this embed.", inline=False)
        embed.add_field(name="Alternate link:", value="https://www.thisworldthesedays.com/hateme2.html", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.check(is_it_me)
    async def thinkbee(self, ctx):
        slicedBeeMovie = []
        async with ctx.typing():
            beemovie = open("beemovie.txt", "r").read()
            slicedBeeMovie = charLimit(beemovie)
        for chunk in slicedBeeMovie:
            await ctx.send(chunk)
        
def setup(bot):
    bot.add_cog(Prototype(bot))
