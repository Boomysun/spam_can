import discord
import random
import requests
from bs4 import BeautifulSoup
import random
import re
import subprocess
import psutil

client = discord.Client()
theFam = "BEEEEEEEEEEEEEEEEEEEEEEEEEEEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS"
schoolKeywords = ["guido","Guido"]
school = "GUIIIIIIIDDDDOOOOOOOOOOOOOOO"
tjdaily123Keywords = ["Dad!"]
dadbot = "shut up dad bot, im Spam Can"

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




def word_search(word):
    if word == 1:
        num = random.randrange(1,999)
        vgm_url = 'https://www.urbandictionary.com/random.php?page=' + str(num)
    else:
        vgm_url = 'https://www.urbandictionary.com/define.php?term=' + word

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
    meaning = (ogdescription["content"])
    urbanembeded = discord.Embed(title=urbanword, description=meaning, color=0x00ff00)
    urbanembeded.add_field(name="Link",value=vgm_url)
    return urbanembeded


@client.event
async def on_message(message):
    wordlist = open('theFamwordlist.txt', 'r')
    channelname =  message.guild.name
    
    
    if "The Fam" == channelname:
        
        if message.content == "$Wordme":
            urbanembeded = word_search(1)
            await message.channel.send(embed = urbanembeded)

        elif "$Lenny" in message.content:
            badlenny = 1
            checks = 1
            while 1 == badlenny:
                lennyface = lenny()
                badlenny = lenny_check(lennyface)
                print("Checks:", checks)
                checks += 1
            await message.channel.send(lennyface)

        elif message.content == "$peepee":
            peepee = []
            peepee.append("8")
            x = random.randrange(1,13)
            i = 0
            while i < x:
                peepee.append("=")
                i += 1
            peepee.append("D")
            peepeecomplete = ''.join(peepee)
            await message.channel.send(peepeecomplete)



        elif message.content == "$Menu":
            menuembeded = discord.Embed(title="Available commands for Spam Bot!",color=0x00ff00)
            menuembeded.add_field(name="How to connect?",value="Command brings up instructions on how to join the Minecraft server")
            menuembeded.add_field(name="$Wordme",value="Pulls a random page from Urban Dictonary to give you a new word to learn!")
            menuembeded.add_field(name="$Wordsearch",value="Type $Wordsearch [word to be searched] to look up a word on Urban Dictionary (Use at your own risk. I have no idea what Urban Dictionary will return you)")
            menuembeded.add_field(name="Spam",value="I will randomly change the trigger words, and the phrase to be spammed.")
            menuembeded.add_field(name="$Start",value="Command remotely starts Minecraft Server")
            menuembeded.add_field(name="$Check",value="Command checks Minecraft Server's status")
            menuembeded.add_field(name="$Stop",value="Command remotely stops Minecraft Server")
            menuembeded.add_field(name="$Lenny",value="See what Lenny wants to come and visit!")


            await message.channel.send(embed = menuembeded)


        elif  "$Wordsearch" in message.content:
            tmpword = message.content.split()
            word_to_find = ''
            for word in tmpword:
                if word != tmpword[0]:
                    word_to_find = word_to_find + " " + word
            print(word_to_find)
            urbanembeded = word_search(word_to_find)
            await message.channel.send(embed = urbanembeded)
        

        elif message.content == "steamedham":

            ham = discord.Embed(title="Yes I shoul- GOOD LORD WHAT IS GOING ON IN THERE?!",color=0x00ff00) 
            ham.add_field(name="steamedclams",value="Aurora borealis\nA... Aurora Borealis? At this time of year? At this time of day? In this part of the country? Localized entirely within your kitchen?\nYes\nMay I see it?\nNo")
            await message.channel.send(embed = ham)

        

        elif message.content == "How to connect?":
            messageembeded = discord.Embed(title="How to connect", description="Steps to connect to Minecraft Server", color=0x00ff00)
            messageembeded.add_field(name="Instructions",value="See pinned in the top right of the server to download the server files, along with the Server IP (Hint. you will need to add ':25565' after the ip). After downloading the server files, open CurseForge, locate 'My Modpacks'. In the top right select 'create custom profile'. Finally, select 'import' to then choose the file you downloaded previously (check downloads).Right click the new icon within CurseForge and select 'open folder'.Then go to Mods and delete all Dynamic Tree mods and Dynamic surroundings. Open Minecraft by selecting play on CurseForge, and place the I.P from early in the 'Add server' button in 'Multiplayer'")
            await message.channel.send(embed = messageembeded)

        

        elif message.content == "$Start":
            startserverfile = "C:/Users/ccrac/Desktop/Server Files/serverstart.bat"
            startserverfolder = "C:/Users/ccrac/Desktop/Server Files/"
            foundflag = 0
            for proc in psutil.process_iter():
                if "java.exe" in proc.name():
                    foundflag = 1
            if 0 == foundflag:
                subprocess.Popen("C:/Users/ccrac/Desktop/Server Files/startserver.bat", cwd= r"C:/Users/ccrac/Desktop/Server Files")
                await message.channel.send("Server successfully started!")
            else:
                await message.channel.send("Server is already running!")
            



        elif message.content == "$Check":
            foundflag = 0
            for proc in psutil.process_iter():
                if "java.exe" in proc.name():
                    foundflag = 1
            if foundflag == 1:
                await message.channel.send("Server is up!")
            else:
                await message.channel.send("Server is down!")



        elif message.content == "$Stop":
            killedflag = 0
            for proc in psutil.process_iter():
                if "java.exe" in proc.name():
                    proc.kill()
                    killedflag = 1
            if 1 == killedflag:
                await message.channel.send("Server successfully shut down!")
            else:
                await message.channel.send("Sorry, there was an error shutting down the server.")

        else:
            for word in wordlist:
                word = word.replace("\n", "")
            
                if word in message.content:
                    for i in range(10):
                        await message.channel.send(theFam)
                    break
        if "guido" in message.content.lower():
            await message.channel.send("GUUUIIIIIDDDDDOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
    
    
    elif "TDQC" == channelname:

        if message.content == "$Menu":
            menuembeded = discord.Embed(title="Hi! Im Spam Can! Here's a bit about me!",color=0x00ff00)
            menuembeded.add_field(name="$Wordme",value="Type $Wordme to get a random page off of Urban Dictionary (Use at your own risk. I have no idea what Urban Dictionary will return you)")
            menuembeded.add_field(name="$Wordsearch",value="Type $Wordsearch [word to be searched] to look up a word on Urban Dictionary (Use at your own risk. I have no idea what Urban Dictionary will return you)")
            menuembeded.add_field(name="$Fistbumpcount",value="Get a recently updated firstbump count")
            menuembeded.add_field(name="$Lenny",value="See what Lenny wants to come and visit!")
            
            await message.channel.send(embed = menuembeded)

        elif "$Lenny" in message.content:
            badlenny = 1
            checks = 1
            while 1 == badlenny:
                lennyface = lenny()
                badlenny = lenny_check(lennyface)
                print("Checks:", checks)
                checks += 1
            await message.channel.send(lennyface)

        if "egg" in message.content and  random.randrange(1,50) == 27:
            await message.add_reaction("🥚")

        elif message.content == "$Wordme":
            urbanembeded = word_search(1)
            await message.channel.send(embed = urbanembeded)

        elif  "$Wordsearch" in message.content:
            tmpword = message.content.split()
            word_to_find = ''
            for word in tmpword:
                if word != tmpword[0]:
                    word_to_find = word_to_find + " " + word
            print(word_to_find)
            urbanembeded = word_search(word_to_find)
            await message.channel.send(embed = urbanembeded)


        
        elif "Tariax" in message.author.name and random.randrange(1,50) == 27:
                await message.add_reaction("🥚")

        elif "Boomysum" in message.author.name and "$Fistbumpcount" in message.content:
            await message.channel.send("You: 1\tEveryone else: 0")

        elif "$Fistbumpcount" in message.content:
            await message.channel.send("You: 0\tKaleeb: 1")

        if "ok" == message.content and random.randrange(1,101) == 58:
            roll = random.randrange(1,101)
            if 69 == roll:
                await message.channel.send("eh")
            else:
                await message.add_reaction("🇴")
                await message.add_reaction("🇭")
                await message.add_reaction("🇰")
                await message.add_reaction("🇦")
                await message.add_reaction("🅰️")
                await message.add_reaction("🇾")
            

        if "guido" in message.content.lower():
            x = 0
            while x < 3:
                await message.channel.send(school)
                x += 1
    
    
    elif "tjdaily123" == channelname:
        for i in range(len(tjdaily123Keywords)):
            if tjdaily123Keywords[i] in message.content:
                for i in range(3):
                    await message.channel.send(dadbot)
                
        if "ok" == message.content and random.randrange(1,101) == 58:
            roll = random.randrange(1,101)
            if 69 == roll:
                await message.channel.send("eh")
            else:
                await message.add_reaction("🇴")
                await message.add_reaction("🇭")
                await message.add_reaction("🇰")
                await message.add_reaction("🇦")
                await message.add_reaction("🅰️")
                await message.add_reaction("🇾")

        elif "Boomy" in message.author.name:
                await message.add_reaction("🥚")



client.run('ODc5ODM0OTU0NTEzNjU3ODY2.YSVgJw.hGqteLDEj1OtVe4yASBw8QaXSyI')