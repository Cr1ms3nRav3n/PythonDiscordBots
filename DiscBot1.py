#!/usr/bin/python
#Script for Discord Bot to pull lmgtfy links and spam IT crowd quotes
#Version 1.0
#Author: Cr1ms3nRav3n

import discord
import requests
import json
import random
import urllib.parse
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
TOKEN = 'YourTokenHere'
GUILD = 'YourGuildHere'

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user.name} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    
#Quotes from IT crowd
@bot.command(name='ITCrowd')
async def ITCrowd(ctx):
        
        ITCrowd_Quotes = [
                "You best put seatbelts on your ears, Roy! 'Cause I'm gonna take them for the ride of their lives!",
                "Why are you giving me the secret signal to shut up?",
                "Oh, shut up, Dumpo, the elephant who got dumped!",
                "Prepare to put mustard on those words for you will soon be consuming them along with this slice of humble pie, that comes direct from the oven of shame, set at gas mark egg on your face!",
                "I feel trapped like a moth in a bath.",
                "Do you think you would die if you drank wee?"
                "I came  here to drink milk and kick ass...and I've just finished my milk.",
                "I want to go back to being weird. I like being weird. Weird is all I've got. That and my sweet style."
                "You think this is some kind of mother flipping joke? Mother flippers think everything is a mother flipping joke. Let me tell you, the jokey ain't no jokey sucker!"
                "I'm disabled",
                "A fire... at a Sea Parks?!?",
                "People... what a bunch of bastards!",
                "I'm not turning it up to eight Moss! It'll blow my cock off!",
                "If this was a human being, I'd shoot it in the face!",
                "If two grown men can't make a pervert happy for a few minutes in order to watch a film about zombies, then maybe we should all just move to Iran.",                
                "Have you tried turning it off and on again?",
                "You do know what a button is, don't you?",
                "My bottom is not a kissing post, sir!"
                "I'm a 32 year old IT-man who works in a basement. Yes, I do the whole Lonely Hearts thing!",
                "Oh, I'm very comfortable with my sexuality, I just don't want to be slapped in the face with their sexuality",
                "Unbelievable! Some idiot disabled his firewall, meaning all the computers on floor Seven are teeming with viruses, plus I've just had to walk all the way down the motherfudging stairs, because the lifts are broken again!",
                "You wouldn't steal a handbag. You wouldn't steal a car. You wouldn't steal a baby. You wouldn't shoot a policeman. And then steal his helmet. You wouldn't go to the toilet in his helmet. And then send it to the policeman's grieving widow. And then steal it again! Downloading films is stealing. If you do it, you will face the consequences.",
                "With all due respect John, I am the head of IT and I have it on good authority that if you type Google into Google, you can break the Internet. So please, no one try it, even for a joke.",
                "These toys may smell of wee, come the morn.",
                "Small people are not a race. This isn't Game of Thrones!"
        ]

            response = random.choice(ITCrowd_Quotes)
            await ctx.send(response)
                

@bot.command(name='lmgtfy')
async def lmgtfy(ctx, *, searchquery: str):
  
    await ctx.send('<https://lmgtfy.com/?iie=1&q={}>'
                   .format(urllib.parse.quote_plus(searchquery)))
bot.run(TOKEN)
