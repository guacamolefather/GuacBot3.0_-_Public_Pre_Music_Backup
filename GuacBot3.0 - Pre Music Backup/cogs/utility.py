import discord
from discord.ext import commands, tasks
from cogs.extraclasses.read import *
import os
import datetime
import random
import subprocess
from itertools import cycle

class Utility(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def is_it_me(ctx):
        return ctx.author.id == 409445517509001216

    def admin(ctx):
        return ctx.author.id == 409445517509001216 or permissions_for(ctx.author).manage_guild

    @commands.Cog.listener()
    async def on_ready(self):
        print("Utility processes active.")

    @commands.command()
    @commands.check(is_it_me)
    async def utilitytest(self, ctx):
        await ctx.send('Utility extension cog works!')

    @commands.command()
    @commands.check(is_it_me)
    async def ping(self, ctx):
        await ctx.send('Latency: ' + str(round(self.bot.latency * 1000)) + 'ms.')

    @commands.command()
    async def avatar(self, ctx, *,  member : discord.Member=None):
        if (member == None):
            member = ctx.message.author
        memberAvatarUrl = member.avatar_url
        await ctx.send(memberAvatarUrl)
        
    @commands.command()
    async def profile(self, ctx): #, *, member : discord.Member=None):
        #if (member == None):
        member = ctx.message.author
        embed = discord.Embed(title=str(member), description="Member's statistics:", colour=discord.Color.purple(), url="https://www.youtube.com/watch?v=iik25wqIuFo")

        #Member's roles:
        member_roles = []
        fancy_roles_list = ""
        if (len(member.roles) > 1):
            raw_list = [role.mention for role in member.roles]
            raw_list.pop(0)
            for i in raw_list:
                member_roles.insert(0, i)
            for role in member_roles:
                fancy_roles_list = fancy_roles_list + "- " + role + "\n"
        else:
            fancy_roles_list = "None"
        embed.add_field(name="Role(s):",value=fancy_roles_list, inline=False)
        
        #How many channels member has access to:
        counter = 0
        for channel in ctx.guild.text_channels:
            if (channel.permissions_for(member).read_messages):
                counter = counter + 1
        embed.add_field(name="Channels:",value="Has access to " + str(counter) + " channels.",inline=False)

        embed.add_field(name="Messages sent:", value="at least 2?", inline=False)

        embed.add_field(name="Regular profile",value="This is the regular profile command. For the admin command, use #adminprofile (with admin priviledges).", inline=False)

        await ctx.send(embed=embed)

    @commands.command()
    async def reactions(self, ctx):
        triggers = ReadTriggers()
        fancyList = ""
        for i in triggers:
            if not isinstance(i, str):
                if fancyList.endswith(", "):
                    fancyList = fancyList + "("
                else:
                    fancyList = fancyList + ", ("
                for subtrigger in i:
                    if fancyList.endswith("("):
                        fancyList = fancyList + subtrigger
                    else:
                        fancyList = fancyList + ", " + subtrigger
                fancyList = fancyList + "), "
            else:
                if i == "409445517509001216":
                    fancyList = "@thememesareallreal"
                else:
                    if fancyList.endswith(", "):
                        fancyList = fancyList + i
                    else:
                        fancyList = fancyList + ", " + i
        await ctx.send(fancyList)

def setup(bot):
    bot.add_cog(Utility(bot))
