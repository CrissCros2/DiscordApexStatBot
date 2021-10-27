import discord
import youtube_dl
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from discord import Member
import asyncio
import ffmpeg
from discord import Spotify

message = "A duck walks into a pub and orders a pint of beer and a ham sandwich. The barman looks at him and says, “hang on! You’re a duck.” “I see your eyes are working,” replies the duck. “And you can talk!” exclaims the barman. “I see your ears are working, too,” says the Duck. “Now if you don’t mind, can I have my beer and my sandwich please?” “Certainly, sorry about that” says the barman as he pulls the duck’s pint. “It ‘s just we don’t get many ducks in this pub.. What are you doing round this way?” “I’m working on the building site across the road,” explains the duck. “I’m a plasterer.” The flabbergasted barman cannot believe the duck and wants to learn more, but takes the hint when the duck pulls out a newspaper from his bag and proceeds to read it. So, the duck reads his paper, drinks his beer, eats his sandwich, bids the barman good day and leaves. The same thing happens for two weeks. Then one day the circus comes to town. The ringmaster comes into the pub for a pint and the barman says to him “you’re with the circus, aren’t you? Well, I know this duck that could be just brilliant in your circus. He talks, drinks beer, eats sandwiches, reads the newspaper and everything!” “Sounds marvelous,” says the ringmaster, handing over his business card. “Get him to give me a call.” So the next day when the Duck comes into the pub the barman says, “hey Mr. Duck, I reckon I can line you up with a top job, paying really good money.” “I’m always looking for the next job,” says the duck. “Where is it?” “At the circus,” says the barman. “The circus?” repeats the duck. “That’s right,” replies the barman. “The circus?” the duck asks again. “With the big TENT?” “Yeah,” the barman replies. “With all the animals who live in CAGES, and performers who live in CARAVANS?” says the duck. “Of course,” the barman replies. “And the tent has CANVAS sides and a big canvas roof with a hole in the middle?” persists the duck. “That’s right!”. The duck shakes his head in amazement,"
punchline = " and says .. What the fuck would they want with a plasterer??"
x = 10
y = 10

with open("apexwins.txt") as textFile:
    wins = [line.split() for line in textFile]
with open("apexduos.txt") as textFile:
    duos = [line.split() for line in textFile]
with open("apextrios.txt") as textFile:
    trios = [line.split() for line in textFile]
with open("apexnumofwins.txt") as textFile:
    numofwins = [line.split() for line in textFile]

#Chris = 0
#Simon = 1
#Jo Jo = 2
#Dylan = 3
#Izzy = 4
#Jon = 5
#Aaron = 6
#Oana = 7
#Nick = 8

def link(text):
    text = text.lower()
    x = 10
    if text == "chris":
        x = 0
    elif text == "simon":
        x = 1
    elif text == "joseph":
        x = 2
    elif text == "dylan":
        x = 3
    elif text == "izzy":
        x = 4
    elif text == "jon":
        x = 5
    elif text == "aaron":
        x = 6
    elif text == "oana":
        x = 7
    elif text == "nick":
        x = 8
    return x

async def statusChange(message):
    text = str(message.author)
    auth = ""
    for n in range(0,len(text)-5):
        auth = auth + text[n]
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=auth))

intents = discord.Intents().all()
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Content'))  
              
@bot.command()                                                                   
async def duck(ctx):
    duck = message[0]
    words = message.split()
    initial = str("A ")
    mess = await ctx.send(initial)
    for n in range(1,len(words)):
        duck = duck + " " + words[n]
        if n % 5 == 0:
            await mess.edit(content=duck)
    await mess.edit(content=duck)
    await ctx.send(punchline)

@bot.command()
async def test(ctx):
    try:
        author = ctx.message.author
        channel = author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(executable="C:\\Users\\chris\\OneDrive\\Desktop\\ApexStatBot\\ffmpeg.exe", source="duck.mp3"))
        while vc.is_playing():
            await asyncio.sleep(1)
        vc.stop()
        server = ctx.message.guild.voice_client
        await server.disconnect()
        await statusChange(ctx.message)
    except:
        return
        
@bot.command()    
async def MOO(ctx):
    try:
        author = ctx.message.author
        channel = author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(executable="C:\\Users\\chris\\OneDrive\\Desktop\\ApexStatBot\\ffmpeg.exe", source="MOOOO.mp3"))
        while vc.is_playing():
            await asyncio.sleep(1)
        vc.stop()
        server = ctx.message.guild.voice_client
        await server.disconnect()
        await statusChange(ctx.message)
    except:
        return
    
@bot.command()         
async def BIRT(ctx):
    try:
        author = ctx.message.author
        channel = author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(executable="C:\\Users\\chris\\OneDrive\\Desktop\\ApexStatBot\\ffmpeg.exe", source="BIRT.mp3"))
        while vc.is_playing():
            await asyncio.sleep(1)
        vc.stop()
        server = ctx.message.guild.voice_client
        await server.disconnect()
        await statusChange(ctx.message)
    except:
        return

@bot.command()                                                                   
async def barney(ctx):
    try:
        author = ctx.message.author
        dontplay = False
        channel = author.voice.channel
        for x in range(0,len(channel.members)):
            if str(channel.members[x]) == "IzxyEcho#5245":
                dontplay = True
        if dontplay == False:
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio(executable="C:\\Users\\chris\\OneDrive\\Desktop\\ApexStatBot\\ffmpeg.exe", source="Barney_Song_Backwards.mp3"))
        while vc.is_playing():
            await asyncio.sleep(1)
        vc.stop()
        server = ctx.message.guild.voice_client
        await server.disconnect()
        await statusChange(ctx.message)
    except:
        return
    
@bot.command()
async def duowin(ctx):
    cmd = ctx.message.content.split()[0].replace("$duowin","")
    if len(ctx.message.content.split()) > 2 and len(ctx.message.content.split()) < 4:
        parameters = ctx.message.content.split()[1:]
        text = str(parameters[0])
        x = link(text)
        text = str(parameters[1])
        y = link(text)
            
        if x == y:
            await ctx.send("No you dingus!")
        elif x == 10 or y == 10:
            await ctx.send("names are invalid")
        else:
            wins[x][y] = int(wins[x][y]) + 1
            wins[y][x] = int(wins[y][x]) + 1
            duos[x][y] = int(duos[x][y]) + 1
            duos[y][x] = int(duos[y][x]) + 1
            numofwins[0][x] = int(numofwins[0][x]) + 1
            numofwins[0][y] = int(numofwins[0][y]) + 1
            f = open("apexduos.txt", "w")
            for m in range(0,9):
                line = ""
                for n in range(0,9):
                    line = line + str(duos[n][m])
                    line = line + " "
                line = line + "\n"
                f.write(line)
            f.close()

            f = open("apexwins.txt", "w")
            for m in range(0,9):
                line = ""
                for n in range(0,9):
                    line = line + str(wins[n][m])
                    line = line + " "
                line = line + "\n"
                f.write(line)
            f.close()
            
            f = open("apexnumofwins.txt", "w")
            line = ""
            for n in range(0,9):
                line = line + str(numofwins[0][n])
                line = line + " "
            f.write(line)
            f.close()
            await ctx.send("Win added successfully")
            await statusChange(ctx.message)
            
    else:
        await ctx.send("invalid command")
        
@bot.command()             
async def triowin(ctx):
    cmd = ctx.message.content.split()[0].replace("$triowin","")
    if len(ctx.message.content.split()) > 3 and len(ctx.message.content.split()) < 5:
        parameters = ctx.message.content.split()[1:]
        text = str(parameters[0])
        x = link(text)
        text = str(parameters[1])
        y = link(text)
        text = str(parameters[2])
        z = link(text)

        if x == y or x == z or y == z:
            await ctx.send("No you dingus!")
        elif x == 10 or y == 10:
            await ctx.send("names are invalid")
        else:
            wins[x][y] = int(wins[x][y]) + 1
            wins[y][x] = int(wins[y][x]) + 1
            wins[x][z] = int(wins[x][z]) + 1
            wins[z][x] = int(wins[z][x]) + 1
            wins[z][y] = int(wins[z][y]) + 1
            wins[y][z] = int(wins[y][z]) + 1

            trios[x][y] = int(trios[x][y]) + 1
            trios[y][x] = int(trios[y][x]) + 1
            trios[x][z] = int(trios[x][z]) + 1
            trios[z][x] = int(trios[z][x]) + 1
            trios[z][y] = int(trios[z][y]) + 1
            trios[y][z] = int(trios[y][z]) + 1

            
            numofwins[0][x] = int(numofwins[0][x]) + 1
            numofwins[0][y] = int(numofwins[0][y]) + 1
            numofwins[0][z] = int(numofwins[0][y]) + 1
            f = open("apextrios.txt", "w")
            for m in range(0,9):
                line = ""
                for n in range(0,9):
                    line = line + str(trios[n][m])
                    line = line + " "
                line = line + "\n"
                f.write(line)
            f.close()

            f = open("apexwins.txt", "w")
            for m in range(0,9):
                line = ""
                for n in range(0,9):
                    line = line + str(wins[n][m])
                    line = line + " "
                line = line + "\n"
                f.write(line)
            f.close()
            
            f = open("apexnumofwins.txt", "w")
            line = ""
            for n in range(0,9):
                line = line + str(numofwins[0][n])
                line = line + " "
            f.write(line)
            f.close()
            await ctx.send("Win added successfully")
            await statusChange(ctx.message)
            
    else:
        await ctx.send("invalid command")
        
@bot.command()             
async def duoswith(ctx):
    cmd = ctx.message.content.split()[0].replace("$duoswith","")
    if len(ctx.message.content.split()) > 2 and len(ctx.message.content.split()) < 4:
        parameters = ctx.message.content.split()[1:]
        if parameters[1] == parameters[0]:
            await message.channel.send("No you dingus!")
        else:
            text1 = str(parameters[0])
            x = link(text1)
            text2 = str(parameters[1])
            y = link(text2)
            if x == 10 or y == 10:
                await ctx.send("Invalid names")
            else:
                num = duos[x][y]
                line = text1.capitalize() + " and " + text2.capitalize() + " have " + num + " duo wins together"
                await ctx.send(line)
                await statusChange(ctx.message)
        
    else:
        await ctx.send("invalid command")
@bot.command()  
async def trioswith(ctx):
    cmd = ctx.message.content.split()[0].replace("$trioswith","")
    if len(ctx.message.content.split()) > 2 and len(ctx.message.content.split()) < 4:
        parameters = ctx.message.content.split()[1:]
        if parameters[1] == parameters[0]:
            await ctx.send("No you dingus!")
        else:
            text1 = str(parameters[0])
            x = link(text1)
            text2 = str(parameters[1])
            y = link(text2)
            if x == 10 or y == 10:
                await ctx.send("Invalid names")
            else:
                num = trios[x][y]
                line = text1.capitalize() + " and " + text2.capitalize() + " have " + num + " trio wins together"
                await ctx.send(line)
                await statusChange(ctx.message)  
    else:
        await ctx.send("invalid command")
@bot.command()                 
async def winswith(ctx):
    cmd = ctx.message.content.split()[0].replace("$winswith","")
    if len(ctx.message.content.split()) > 2 and len(ctx.message.content.split()) < 4:
        parameters = ctx.message.content.split()[1:]
        if parameters[1] == parameters[0]:
            await message.channel.send("No you dingus!")
        else:
            text1 = str(parameters[0])
            x = link(text1)
            text2 = str(parameters[1])
            y = link(text2)
            if x == 10 or y == 10:
                await ctx.send("Invalid names")
            else:
                num = wins[x][y]
                line = text1.capitalize() + " and " + text2.capitalize() + " have " + str(num) + " wins together"
                await ctx.send(line)
                await statusChange(ctx.message)  
    else:
        await ctx.send("invalid command")
        
@bot.command()     
async def loggedwins(ctx):
    cmd = ctx.message.content.split()[0].replace("$winswith","")
    if len(ctx.message.content.split()) > 1 and len(ctx.message.content.split()) < 3:
        parameters = ctx.message.content.split()[1:]
        text1 = str(parameters[0])
        x = link(text1)
        if x == 10 :
                await ctx.send("Invalid names")
        else:
            num = numofwins[0][x]
            line = text1.capitalize() + " has " + str(num) + " wins stored by this bot" 
            await ctx.send(line)
            await statusChange(ctx.message)
    else:
        await ctx.send("invalid command")

bot.remove_command('help')        
@bot.command()       
async def help(ctx):
    cmd = ctx.message.content.split()[0].replace("$helps","")
    if len(ctx.message.content.split()) > 1 and len(ctx.message.content.split()) < 3:
        await statusChange(ctx.message)
        parameters = ctx.message.content.split()[1:]
        if str(parameters[0]) == "duowin":
            await ctx.send("Takes two players and credits them with a win. Format: $duowin [name1] [name2]")
        elif str(parameters[0]) == "triowin":
            await ctx.send("Takes three players and credits them with a win. Format: $triowin [name1] [name2] [name3]")
        elif str(parameters[0]) == "duoswith":
            await ctx.send("Takes two players and says how many duo wins they have together. Format: $duoswith [name1] [name2]")
        elif str(parameters[0]) == "trioswith":
            await ctx.send("Takes two players and says how many trio wins they have together. Format: $trioswith [name1] [name2]")
        elif str(parameters[0]) == "winswith":
            await ctx.send("Takes two players and says how many wins they have together. Format: $winswith [name1] [name2]")
        elif str(parameters[0]) == "loggedwins":
            await ctx.send("Takes one player and says how many of their wins are tracked. Formate: $numofwins [name1]")
        elif str(parameters[0]) == "MOO":
            await ctx.send("Take a guess you ball bag")
        else:
            await ctx.send("Invalid command")
    else:
        await ctx.send("Commands: $duowin $triowin $duoswith $trioswith $winswith $loggedwins $MOO")
        await ctx.send("For each command write $help [command] without the dollar sign")
        await ctx.send("Names: Chris Simon Joseph Dylan Izzy Jon Aaron Oana Nick")
        await statusChange(ctx.message)


bot.run('[Bot Token Here]')
