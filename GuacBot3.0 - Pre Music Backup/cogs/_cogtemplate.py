import discord
from discord.ext import commands, tasks
import os
import datetime
import random
import subprocess
from itertools import cycle
import json
import asyncio

class #(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('# processes active.')

    @commands.command()
    async def #test(self, ctx):
        await ctx.send('# extension cog works!')

def setup(client):
    client.add_cog(#(client))
