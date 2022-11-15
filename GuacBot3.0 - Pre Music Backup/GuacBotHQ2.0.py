import discord
import asyncio
import time
import os
import subprocess
import random
import re
from discord.ext import commands, tasks
from itertools import cycle

#Version 2.0 experimental
bot = commands.Bot(command_prefix = '#', case_insensitive=True, activity=discord.Game("Only legends see this."))

@bot.event
async def on_ready():
    os.system('cls')
    print("Main bot processes active.")
    change_status.start()

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("That isn't a command, buddy.")

def is_it_me(ctx):
    return ctx.author.id == 409445517509001216

@bot.command()
@commands.check(is_it_me)
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'Extension "{extension}" loaded!')

@load.error
async def load_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please choose what cog to load.')

@bot.command()
@commands.check(is_it_me)
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Extension "{extension}" unloaded!')

@unload.error
async def unload_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please choose what cog to unload.')

@bot.command()
@commands.check(is_it_me)
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'Extension "{extension}" reloaded!')

@reload.error
async def reload_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please choose what cog to reload.')

@bot.command()
@commands.check(is_it_me)
async def die(ctx):
    await ctx.send("Goodbye, father.")
    await bot.change_presence(activity=discord.Game("Goodbye."))
    ta.kill()
    r.kill()
    os.system('cls')
    quit()

@bot.command()
@commands.check(is_it_me)
async def restart(ctx):
    await ctx.send("Restarting!")
    ta.kill()
    r.kill()
    subprocess.Popen(["python", "GuacBotHQ2.0.py"])
    quit()

@bot.command()
@commands.check(is_it_me)
async def puppet(ctx):
    ta.kill()
    os.system('cls')
    p = subprocess.Popen(["python", "GuacBotPuppet.py"])
    await asyncio.sleep(300)
    isDead = p.poll()
    if (isDead == None):
        p.kill()
    os.system('cls')
    ta.Popen(["python", "GuacBotTerminalAnimation.py"])

#Load cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py') and not filename.startswith("_"):
        bot.load_extension(f'cogs.{filename[:-3]}')

#Status loop
def NewOrder():
    statusorder = []
    indices = list(random.sample(range(len(possiblestatuses)), len(possiblestatuses)))
    for i in indices:
        statusorder.append(possiblestatuses[i])
    return statusorder

possiblestatuses = ['you like a damn fiddle', 'with your butt', 'with fire', 'with anime tiddy',
                    'with knives', 'ROBLOX DEATH RUN', 'Shrek 5 in HD', 'alone :(',
                    'Fortnite in Area 51', 'with some rope', 'with your heart ;)',
                    'Minecraft Hunger Games', 'dead', 'with the dark arts', 'with the bois', 'nothing...',
                    'with myself', "a tune on the world's smallest violin", "RealLife.exe", "a prank on you",
                    "Discord... what did you expect?", "with needles", "with a hammer", "SONIC.exe"]

status = cycle(NewOrder())
@tasks.loop(seconds=300)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))

#Open other GuacBot pieces
r = subprocess.Popen(["python", "GuacBotReaction3.0.py"])
ta = subprocess.Popen(["python", "GuacBotTerminalAnimation.py"])

#Start bot with token in text file
TOKEN = open("TOKEN.txt", "r").read()
bot.run(TOKEN)
