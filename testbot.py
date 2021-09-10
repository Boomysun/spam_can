import pickle
from os import pipe
from sys import stdout
from typing import DefaultDict
from discord_components import component
from discord_components.component import Select, SelectOption
from discord import guild, message
import discord
from discord_components import ActionRow, Button, ButtonStyle, ComponentsBot
import time
import random
import requests
from bs4 import BeautifulSoup
import re
import subprocess
import psutil

bot = ComponentsBot(command_prefix = "$")

def word_search(word_original):
    """Creates URL for Urban Dictionary.com to pull a 1. Random word or 2. searched word

    Args:
        word_original (1 or str): Pass a 1 if you want a random page. Otherwise, pass a string

    Returns:
        discord.embeded: this is the embeded message ready to be sent
    """
    if word_original == 1:
        num = random.randrange(1,999)
        vgm_url = 'https://www.urbandictionary.com/random.php?page=' + str(num)
    else:
        vgm_url = 'https://www.urbandictionary.com/define.php?term=' + word_original
    print(vgm_url)
    html_text = requests.get(vgm_url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    attrs = {
        'href': re.compile(r'\.mid$')
    }
    for link in soup.find_all('a'):
        if "/define.php?term=" in link.get('href'):
            urbanword = link.get('href');urbanword = urbanword[17:];urbanword = urbanword.replace('%20',' ')         
            break
    ogdescription= soup.find("meta", property="og:description")
    print(ogdescription)
    meaning = (ogdescription['content'])
    urbanembeded = discord.Embed(title=urbanword, description=meaning, color=0x00ff00)
    urbanembeded.add_field(name="Link",value=vgm_url)
    return urbanembeded

def lenny():
    """Pulls random Lenny face from len.html (I think is the name of it).

    Returns:
        str: Lenny's face
    """
    f = open('len.html','r', encoding='utf-8')
    lines = f.readlines()
    x = 0
    y = random.randrange(1,101)
    leny = ''
    nolen = 0
    for line in lines:
        if "super-fancy-text-lenny-face" in line:
            x += 1
            if x == y:
                leny = line
                nolen = 0
                break
            else:
                nolen = 1
    x = 1
    y = 3
    leny = leny.split(">")
    for i in leny:
        if x == y:
            leny = i
            break
        x += 1
    x = 0
    y = 5
    while x != y:
        leny = leny[:-1]
        x += 1
    print(leny)
    return leny

def lenny_check(lenny):
    """Checks to make sure lenny is suitable to be sent to a discord

    Args:
        lenny (str): Lenny in question

    Returns:
        int: returns a 1 if the lenny is no good or 0 if he is
    """
    x = 0
    badlenny = 0
    while x < len(lenny):
        if any(char.isdigit() for char in lenny):
            badlenny = 1
        x += 1
    return badlenny

def user_check(name_to_be_checked,coord_dict):
    for name in coord_dict:
        if name_to_be_checked == name:
            return 1
    return 0

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}!")
    try:
        pickle_in = open("coord.pickle","rb")
        coord_dict = pickle.load(pickle_in)
    except:
        coord_dict = {}
        pickle_out = open("coord.pickle","wb")
        pickle.dump(coord_dict,pickle_out)

@bot.command()
async def m (ctx):
    await Menu(ctx)

@bot.command()
async def Menu(ctx: discord.ext.commands.Context):
    if "TDQC" == ctx.guild.name:
        menuembeded = discord.Embed(title="Hi! Im Spam Can! Here's a bit about me!",color=0x00ff00)
        menuembeded.add_field(name="$Wordme",value="Type $Wordme to get a random page off of Urban Dictionary (Use at your own risk. I have no idea what Urban Dictionary will return you)")
        menuembeded.add_field(name="$Wordsearch",value="Type $Wordsearch [word to be searched] to look up a word on Urban Dictionary (Use at your own risk. I have no idea what Urban Dictionary will return you)")
        menuembeded.add_field(name="$Fistbumpcount",value="Get a recently updated firstbump count")
        menuembeded.add_field(name="$Lenny",value="See what Lenny wants to come and visit!")
        await ctx.channel.send(embed = menuembeded)
        
        await ctx.send(
            "Buttons!",
            components = [
                ActionRow(
                    Button(label="Word me",custom_id="wordme"),
                    Button(label="Lenny",custom_id="lenny"),
                    )
            ]
        )
        interaction = await bot.wait_for("button_click")
        print("interaction:",interaction.custom_id)
        if interaction.custom_id == "wordme":
            await Wordme(ctx)
        elif interaction.custom_id == "lenny":
            await Lenny(ctx)
        await interaction.respond(type=6)
    elif "The Fam" == ctx.guild.name:
        menuembeded = discord.Embed(title="Available commands for Spam Bot!",color=0x00ff00)
        menuembeded.add_field(name="How to connect?",value="Command brings up instructions on how to join the Minecraft server")
        menuembeded.add_field(name="$Wordme",value="Pulls a random page from Urban Dictonary to give you a new word to learn!")
        menuembeded.add_field(name="$Wordsearch",value="Type $Wordsearch [word to be searched] to look up a word on Urban Dictionary")
        menuembeded.add_field(name="Spam",value="I will randomly change the trigger words, and the phrase to be spammed.")
        menuembeded.add_field(name="$Start",value="Command remotely starts Minecraft Server")
        menuembeded.add_field(name="$Check",value="Command checks Minecraft Server's status")
        menuembeded.add_field(name="$Restart",value="Command will attempt to shut down the server, then start it again")
        menuembeded.add_field(name="$Stop",value="Command remotely stops Minecraft Server")
        menuembeded.add_field(name="$Lenny",value="See what Lenny wants to come and visit!")
        menuembeded.add_field(name="$Add",value="Add something to your notebook!")
        menuembeded.add_field(name="$Rem",value="Remove something to your notebook!")
        menuembeded.add_field(name="$Print",value="Print out all the entries to the notebook")



        await ctx.channel.send(embed = menuembeded)

        await ctx.send(
            "Click to choose:",
            components = [
                ActionRow(
                    Button(label="Word me",custom_id="wordme"),
                    Button(label="Lenny",custom_id="lenny"),
                    Button(label="Start",custom_id="start"),
                    Button(label="Check",custom_id="check"),
                    Button(label="Stop",custom_id="stop"),
                    
                ),
                ActionRow(
                    Button(label="Restart",custom_id="restart")
                )
            ]
        )
        interaction = await bot.wait_for("button_click")
        if interaction.custom_id == "wordme":
            await Wordme(ctx)
        elif interaction.custom_id == "lenny":
            await Lenny(ctx)
        elif interaction.custom_id == "start":
            await Start(ctx)
        elif interaction.custom_id == "check":
            await interaction.respond(type=6)
            await Check(ctx)
        elif interaction.custom_id == "stop":
            await Stop(ctx)
        elif interaction.custom_id == "restart":
            await Restart(ctx)
        await interaction.respond(type=6)
        
@bot.command()
async def Wordme(ctx):
    urbanembeded = word_search(1)
    await ctx.channel.send(embed = urbanembeded)

@bot.command()
async def Wordsearch(ctx):
    tmpword = ctx.message.content.split()
    word_to_find = ''
    for word in tmpword:
        if word != tmpword[0]:
            word_to_find = word_to_find + " " + word
    print(word_to_find)
    word_to_find = (word_to_find[1:])
    print(word_to_find)
    urbanembeded = word_search(word_to_find)
    await ctx.channel.send(embed = urbanembeded)

@bot.command()
async def Lenny(ctx):
    badlenny = 1
    checks = 1
    while 1 == badlenny:
        lennyface = lenny()
        badlenny = lenny_check(lennyface)
        print("Checks:", checks)
        checks += 1
    await ctx.channel.send(lennyface)

@bot.command()
async def Start(ctx: discord.ext.commands.Context):
    if ctx.guild.name != "The Fam":
        return
    foundflag = 0
    for proc in psutil.process_iter():
        if "java.exe" in proc.name():
            foundflag = 1
    if 0 == foundflag:
        await ctx.channel.send("Attempting to start server...")
        subprocess.Popen("G:/Minecraft/Server Files/startserver.bat", cwd= r"G:/Minecraft/Server Files")
        await ctx.channel.send("Server successfully started! ( Please give it a minute to fully start. You can click the 'Refresh' button on the Multiplayer screen to be sure!)")
    else:
        await ctx.channel.send("Server is already running!")

@bot.command()
async def Check(ctx):
    if ctx.guild.name != "The Fam":
        return
    foundflag = 0
    for proc in psutil.process_iter():
        if "java.exe" in proc.name():
            foundflag = 1
    if foundflag == 1:
        await ctx.channel.send("Server is up!")
    else:
        await ctx.channel.send("Server is down!")
    submenuembeded = discord.Embed(title="What would you like to do next?",color=0x00ff00)
    submenuembeded.add_field(name="$Start",value="Command remotely starts Minecraft Server")
    submenuembeded.add_field(name="$Restart",value="Command will attempt to shut down the server, then start it again")
    submenuembeded.add_field(name="$Stop",value="Command remotely stops Minecraft Server")
    await ctx.channel.send(embed = submenuembeded)
    await ctx.send(
        "Click to choose:",
        components = [
            ActionRow(
                Button(label="Start",custom_id="start"),
                Button(label="Restart",custom_id="restart"),
                Button(label="Stop",custom_id="stop")
                )
        ]
    )
    interaction = await bot.wait_for("button_click")
    if interaction.custom_id == "start":
        await Start(ctx)
    elif interaction.custom_id == "restart":
        await Restart(ctx)
    elif interaction.custom_id == "stop":
        await Stop(ctx)
    await interaction.respond(type=6)

@bot.command()
async def Stop(ctx):
    if ctx.guild.name != "The Fam":
        return
    killedflag = 0
    for proc in psutil.process_iter():
        if "java.exe" in proc.name():
            proc.kill()
            killedflag = 1
    if 1 == killedflag:
        await ctx.channel.send("Server successfully shut down!")
    else:
        await ctx.channel.send("Sorry, there was an error shutting down the server.")

@bot.command()
async def Restart(ctx):
    if ctx.guild.name != "The Fam":
        return
    killedflag = 0
    for proc in psutil.process_iter():
        if "java.exe" in proc.name():
            proc.kill()
            await ctx.channel.send("Found the server. Shutting it down...")
            time.sleep(3)
            killedflag = 1
    if killedflag != 1:
        await ctx.channel.send("Server not found!")
    await ctx.channel.send("Attempting to start the server.")
    await Start(ctx)

@bot.command()
async def Add(ctx):
    if "The Fam" != ctx.guild.name:
        return
    msg = str(ctx.message.content)
    msg = msg[5:]
    msg = msg.replace(" ","_")

    pickle_in = open("coord.pickle","rb")
    coord_dict = pickle.load(pickle_in)

    already_in_dict = user_check(ctx.message.author.name,coord_dict)
    if already_in_dict == 1:
        coord_dict[ctx.message.author.name].append(msg)
    else:
        coord_dict[ctx.message.author.name] = []
        await ctx.channel.send("Hey there! It seems this is your first time utilizing this feature. Glad to have you! Since this is your first time, I had to remember your name. So please just try again and ill put it in my noggin this time!")
    

    pickle_out = open("coord.pickle","wb")
    pickle.dump(coord_dict,pickle_out)

@bot.command()
async def Rem(ctx):
    if "The Fam" != ctx.guild.name:
        return
    msg = str(ctx.message.content)
    msg = msg[5:]
    msg = msg.replace(" ","_")

    pickle_in = open("coord.pickle","rb")
    coord_dict = pickle.load(pickle_in)
    in_dict = user_check(ctx.message.author.name,coord_dict)
    if in_dict == 1:
        try:
            coord_dict[ctx.message.author.name].remove(msg)
            await ctx.channel.send("Successfully removed: " + msg)
        except:
            await ctx.channel.send("Failed removed: " + msg)
    pickle_out = open("coord.pickle","wb")
    pickle.dump(coord_dict,pickle_out)

@bot.command()
async def Print(ctx):
    if "The Fam" != ctx.guild.name:
        return
    tmplist = []
    pickle_in = open("coord.pickle","rb")
    coord_dict = pickle.load(pickle_in)
    for key in coord_dict:
        await ctx.channel.send("User: " + key)
        for value in coord_dict[key]:
            await ctx.channel.send(str(value).replace("_", " "))

@bot.command()
async def Poll(ctx):
    msg = str(ctx.message.content)
    msg = msg[6:]
    poll = discord.Embed(title=msg,color=0x00ff00)
    final = await ctx.channel.send(embed = poll)
    await final.add_reaction("⬆️")
    await final.add_reaction("⬇️")
        

    






bot.run("ODc5ODM0OTU0NTEzNjU3ODY2.YSVgJw.fdULVb4hpq4HifjwfwuGcqX4qZ4")