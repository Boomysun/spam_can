from discord_components import component
from discord_components.component import Select, SelectOption
from discord import guild, message
import discord
from discord_components import ActionRow, Button, ButtonStyle, ComponentsBot


import random
import requests
from bs4 import BeautifulSoup
import re
import subprocess
import psutil

bot = ComponentsBot(command_prefix = "$")

def word_search(word_original):
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
    x = 0
    badlenny = 0
    while x < len(lenny):
        if any(char.isdigit() for char in lenny):
            badlenny = 1
        x += 1
    return badlenny


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}!")


@bot.command()
async def button(ctx: discord.ext.commands.Context) -> None:
    print(ctx.guild.name)
    if "TDQC" == ctx.guild.name:
        await ctx.send(
            "Hello, World!",
            components = [
                Select(placeholder="Simple placeholder",
                options = [SelectOption(label="option 1",value="option 1"),
                            SelectOption(label="option 2",value="option 2")]
                )
            ],
        )
        interaction = await bot.wait_for("button_click", check = lambda i: i.custom_id == "button1")
        await interaction.send(content = "Button clicked!")

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
        menuembeded.add_field(name="$Wordsearch",value="Type $Wordsearch [word to be searched] to look up a word on Urban Dictionary (Use at your own risk. I have no idea what Urban Dictionary will return you)")
        menuembeded.add_field(name="Spam",value="I will randomly change the trigger words, and the phrase to be spammed.")
        menuembeded.add_field(name="$Start",value="Command remotely starts Minecraft Server")
        menuembeded.add_field(name="$Check",value="Command checks Minecraft Server's status")
        menuembeded.add_field(name="$Stop",value="Command remotely stops Minecraft Server")
        menuembeded.add_field(name="$Lenny",value="See what Lenny wants to come and visit!")
        await ctx.channel.send(embed = menuembeded)

        await ctx.send(
            "Click to choose:",
            components = [
                ActionRow(
                    Button(label="Word me",custom_id="wordme"),
                    Button(label="Lenny",custom_id="lenny"),
                    Button(label="Start",custom_id="start"),
                    Button(label="Check",custom_id="check"),
                    Button(label="Stop",custom_id="stop")
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
            await Check(ctx)
        elif interaction.custom_id == "stop":
            await Stop(ctx)
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
    startserverfile = "C:/Users/ccrac/Desktop/Server Files/serverstart.bat"
    startserverfolder = "C:/Users/ccrac/Desktop/Server Files/"
    foundflag = 0
    for proc in psutil.process_iter():
        if "java.exe" in proc.name():
            foundflag = 1
    if 0 == foundflag:
        subprocess.Popen("C:/Users/ccrac/Desktop/Server Files/startserver.bat", cwd= r"C:/Users/ccrac/Desktop/Server Files")
        await ctx.channel.send("Server successfully started!")
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

        





bot.run("ODc5ODM0OTU0NTEzNjU3ODY2.YSVgJw.6T7x41V7W0ETv-n-RYy9VhEsn8g")