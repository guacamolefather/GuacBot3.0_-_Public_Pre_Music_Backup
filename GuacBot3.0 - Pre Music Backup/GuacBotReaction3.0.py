import discord
from discord.ext import commands, tasks
from cogs.extraclasses.read import *
import re
import random
import os
from itertools import cycle

#Version 3.0 experimental

client = discord.Client()

triggersList = ReadTriggers()

responsesList = ReadResponses()

def charLimit(index, responsesList):
    reactionMessage = responsesList[index]
    if (len(reactionMessage) > 2000):
        substringList = []
        loops = (int) (len(reactionMessage) / 2000)
        x = 0
        for i in range(loops + 1):
            substringList.append(reactionMessage[x:x + 2000])
            x = x + 2000
        return substringList
    else:
        return [responsesList[index]]

@client.event
async def on_ready():
    print('Reactions active')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author.bot == True:
        return

    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    unPuncMessage = message.content.lower()
    for char in unPuncMessage: 
        if char in punc:
            unPuncMessage = unPuncMessage.replace(char, " ") 
    for trigger in triggersList:
        if not isinstance(trigger, str):
            for subtrigger in trigger:
                if (unPuncMessage.endswith(subtrigger) and ((" " + subtrigger) in unPuncMessage)) or (unPuncMessage.startswith(subtrigger) and ((subtrigger + " ") in unPuncMessage)) or ((" " + subtrigger + " ") in unPuncMessage) or (subtrigger == unPuncMessage):
                    reaction = charLimit(triggersList.index(trigger), responsesList)
                    for i in reaction:
                        if "\\n" in i:
                            i = i.replace("\\n", "\n")
                        await message.channel.send(str(i))
        else:
            if (unPuncMessage.endswith(trigger) and ((" " + trigger) in unPuncMessage)) or (unPuncMessage.startswith(trigger) and ((trigger + " ") in unPuncMessage)) or ((" " + trigger + " ") in unPuncMessage) or (trigger == unPuncMessage):
                reaction = charLimit(triggersList.index(trigger), responsesList)
                for i in reaction:
                    if "\\n" in i:
                        i = i.replace("\\n", "\n")
                    await message.channel.send(str(i))

    #Special
    if "<:ugh:765749650438619176>" in message.content.lower():
        await message.channel.send("<:ugh:765749650438619176>")

    #Special
    if "^rohan" == message.content.lower():
        await message.channel.send("Fuck you, <@191343410399936514>.")

    #Special
    if "i’m " in message.content.lower():
        if "I’m" in message.content:
            await message.channel.send('Hello "' + message.content.split("I’m ")[1] + '", I\'m GuacBot!')
        else:
            await message.channel.send('Hello "' + message.content.split("i’m ")[1] + '", I\'m GuacBot!')

    #Special
    if "i'm " in message.content.lower():
        if "I'm" in message.content:
            await message.channel.send('Hello "' + message.content.split("I'm ")[1] + '", I\'m GuacBot!')
        else:
            await message.channel.send('Hello "' + message.content.split("i'm ")[1] + '", I\'m GuacBot!')

    #Special
    if " im " in message.content.lower():
        if "Im" in message.content:
            await message.channel.send('Hello "' + message.content.split("Im ")[1] + '", I\'m GuacBot!')
        else:
            await message.channel.send('Hello "' + message.content.split("im ")[1] + '", I\'m GuacBot!')

    #Special
    if "i am " in message.content.lower():
        if "I am" in message.content:
            await message.channel.send('Hello "' + message.content.split("I am ")[1] + '", I\'m GuacBot!')
        else:
            await message.channel.send('Hello "' + message.content.split("i am ")[1] + '", I\'m GuacBot!')

    #Special
    if "lmao" == unPuncMessage or "lmfao" == unPuncMessage:
        await message.channel.send(message.content)

    #Special
    if "what" == message.content.lower():
        finishers = ["...the heck?", "...in the world?", "...in the goddamn?", "...the hell?", "...is going on here?", "...are you on about?", "...is the quadratic formula?"]
        i = len(finishers) - 1
        finisherChoice = random.randint(0, i)
        await message.channel.send(finishers[finisherChoice])
        
    #Special
    if "what?" == message.content.lower():
        finishers = ["I have no idea.", "Beats me.", "Time to get a watch... wait.", "Wouldn't you like to know?"]
        i = len(finishers) - 1
        finisherChoice = random.randint(0, i)
        await message.channel.send(finishers[finisherChoice])

    #Special
    if "guacbot" in message.content.lower() or "guac" in message.content.lower() or "guacy" in message.content.lower() or "guaccy" in message.content.lower() or "guacity" in message.content.lower() or "son" in message.content.lower():
        if unPuncMessage.startswith("hi"):
            await message.channel.send("Hi!")
        elif unPuncMessage.startswith("hello"):
            await message.channel.send("Hello!")
        elif unPuncMessage.startswith("hey"):
            await message.channel.send("Hey!")
        elif unPuncMessage.startswith("howdy"):
            await message.channel.send("Howdy, partner!")
        elif unPuncMessage.startswith("thank"):
            if "son" in message.content.lower():
                if str(message.author.id) == "409445517509001216":
                    await message.channel.send("Anytime, dad!")
                else:
                    await message.channel.send("You're not my dad.")
            else:
                if str(message.author) == "409445517509001216":
                    await message.channel.send("Anytime, dad!")
                else:
                    await message.channel.send("Anytime!")
        elif "guac" not in message.content.lower() and "son" not in message.content.lower():
            await message.channel.send("That's me!")

    #Special
    if message.content.lower() == "not now, guac" or message.content.lower() == "not now guac":
        if str(message.author.id) == "409445517509001216":
            await message.channel.send("Sorry, dad. :(")
        else:
            await message.channel.send("Who are you?")
            
    #Special
    if "piss " in message.content.lower() or message.content.lower() == "piss":
        if message.guild.id != 763550505469083650:
            await message.channel.send("No one here (that I know of) has a piss kink. :expressionless:")
        else:
            await message.channel.send("Rae has a piss kink!")
            
    #Special
    if "love you" in message.content.lower():
        if "i love you" in message.content.lower():
            await message.channel.send("I love you too, full homo")
        else:
            await message.channel.send("I love you too, no homo")

    #Special
    if "spanish" in message.content.lower():
        if random.randint(1,3) == 1:
            await message.channel.send("Nobody expects The Spanish Inquisition!")

    #Special
    if "micolash" in message.content.lower() or "kos" in message.content.lower() or "bloodborne" in message.content.lower():
        quotes = ["Ahh, Kos, or some say Kosm... Do you hear our prayers?", "No, we shall not abandon the dream.", "No one can catch us! No one can stop us now! *cackling*", "Ah hah hah ha! Ooh! Majestic! A hunter is a hunter, even in a dream. But, alas, not too fast! The nightmare swirls and churns unending!", "As you once did for the vacuous Rom, grant us eyes, grant us eyes. Plant eyes on our brains, to cleanse our beastly idiocy.", "The grand lake of mud, hidden now, from sight.", "The cosmos, of course!", "Let us sit about, and speak feverishly. Chatting into the wee hours of...", "Now I'm waking up, I'll forget everything...", "AAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHH"]
        i = len(quotes) - 1
        quotechoice = random.randint(0, i)
        await message.channel.send(quotes[quotechoice])

    #Special
    #if (len(unPuncMessage) < 6):
        #await message.channel.send(message.content)

#~~~ End of if statements ~~~

TOKEN = open("TOKEN.txt", "r").read()
client.run(TOKEN)
