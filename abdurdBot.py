# bot.py
import os
import aiml
import discord
import random
import praw
from dotenv import load_dotenv
from discord.utils import get
from discord.ext import commands
import wikiquote
import asyncio 

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


reddit = praw.Reddit(client_id ="yourid",client_secret = "yoursecret",
                     username = "yourusername", password = "yourpass",
                     user_agent = "description")
#create client bot is stored here ( using command)

reddit.read_only = True
print(reddit.read_only)
client =commands.Bot(command_prefix = '--')





client.command()
async def quote(ctx):
    try:
        title=ctx.message.content
        if title == " ":
            return ValueError
                
    except ValueError:
        await ctx.send("Wrong value, Enter a valid Name or Title respecting capitalizaion.")
        print("Enter a valid Name or Title respecting the capitalizaion")
        return
    tit = title[7:]
    
    lang= tit[-2:]
    print(lang)
    num = random.randint(0,10)
    if(lang =='fr' or lang =='en' or lang =='fes'or lang =='it'or lang =='de'or lang =='pl'or lang =='pt' ):
        try:
            tit = tit[0:len(tit)-2]
            titfin =tit.title()
            
    
            
            print(tit)
            print(titfin)
            quote = "" .join(wikiquote.quotes(titfin,lang=lang)[num])
        except wikiquote.NoSuchPageException or wikiquote.DisambiguationPageException or wikiquote.UnsupportedLanguageException:
                
            await ctx.send("Wrong value, Enter a valid Name or Title respecting capitalizaion.")
            print("Enter a valid Name or Title respecting the capitalizaion")
            return
        else:
            myEmbed = discord.Embed(title = tit, description = '\"' +quote + '\" \n - ', color =0x191970)
            await ctx.send(embed = myEmbed)
    else:
        emb = discord.Embed(title = "Choose a language from the following list:", color = 	0x5f9ea0)
        emb.add_field(name="English", value= 'en', inline=True )
        emb.add_field(name="French", value= 'fr', inline=True)
        emb.add_field(name="Spanish", value= 'es', inline=True)
        emb.add_field(name="Italian", value= 'it', inline=True)
        emb.add_field(name="German", value= 'de', inline=True)
        emb.add_field(name="Polish", value= 'pl', inline=True)
        emb.add_field(name="Portuguese", value= 'pt', inline=True)
        await ctx.send(embed = emb)
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        
       
        try:
            msg = await client.wait_for('message',check = check)  
            if(msg.content!='en' and msg.content!='fr' and msg.content!='es'and msg.content !='it' and msg.content !='de' and msg.content!='pl'and msg.content!='pt'):
                raise ValueError("wrong value")
        except ValueError:
                print("wrong Value")
                await ctx.send("Wrong value, Try again.")
                return
        else:
                val= msg.content.lower()
   
                print(tit)
                print(val)
                num = random.randint(0,10)
                try:
                    quote = "" .join(wikiquote.quotes(tit,lang=val)[num])
                except wikiquote.NoSuchPageException or wikiquote.DisambiguationPageException or wikiquote.UnsupportedLanguageException:
                
                    await ctx.send("Wrong value, Enter a valid Name or Title respecting capitalizaion.")
                    print("Enter a valid Name or Title respecting the capitalizaion")
                    return
                else:
                    myEmbed = discord.Embed(title = titfin, description = '\"' +quote + '\" \n - ', color =0x191970)
                    await ctx.send(embed = myEmbed)

@client.command()
async def meme(ctx):
    meme_submissions = reddit.subreddit('memes').hot()
    post_to_pick = random.randint(1,100)
    for i in range (0, post_to_pick):
        submission = next(x for x in meme_submissions if not x.stickied)
        print(submission.url)
    await ctx.send(submission.url)

@client.command()
async def satisfying(ctx):
    meme_submissions = reddit.subreddit('oddlysatisfying').hot()
    post_to_pick = random.randint(1,100)
    for i in range (0, post_to_pick):
        submission = next(x for x in meme_submissions if not x.stickied)
        print(submission.url)
    await ctx.send(submission.url)



@client.command()
async def memri(ctx):
    meme_submissions = reddit.subreddit('MemriTVmemes').hot()
    post_to_pick = random.randint(1,100)
    for i  in range (0, post_to_pick):
        submission = next(x for x in meme_submissions if not x.stickied)
        print(submission.url)
    await ctx.send(submission.url)

@client.command()
async def mca(ctx):
    await ctx.send("OoooOOOOoooOOOOooooooOOOOoooOOoOOo !! ")


@client.command()
async def wholesome(ctx):
    meme_submissions = reddit.subreddit('wholesomememes').hot()
    post_to_pick = random.randint(1,100)
    for i  in range (0, post_to_pick):
        submission = next(x for x in meme_submissions if not x.stickied)
      
    await ctx.send(submission.url)

@client.command()
async def surreal(ctx):
    meme_submissions = reddit.subreddit('surrealmemes').hot()
    post_to_pick = random.randint(1,100)
    for i  in range (0, post_to_pick):
        submission = next(x for x in meme_submissions if not x.stickied)
      
    await ctx.send(submission.url)

@client.command()
async def shower(ctx):
    meme_submissions = reddit.subreddit('Showerthoughts').hot()
    post_to_pick = random.randint(1,30)
    for i  in range (0, post_to_pick):
        submission = next(x for x in meme_submissions if not x.stickied  )
        print(submission.url)
    
    await ctx.send(submission.url)
    
@client.command()
async def phil(ctx):
    meme_submissions = reddit.subreddit('PhilosophyMemes').hot()
    post_to_pick = random.randint(1,100)
    for i  in range (0, post_to_pick):
        submission = next(x for x in meme_submissions if not x.stickied)
      
    await ctx.send(submission.url)

@client.command(name = 'version')
async def version(ctx):


    myEmbed = discord.Embed(title = "Current Version",description = "The bot is in version : 1.0", color=0x00ff00)
    myEmbed.add_field(name="Version Code:", value = "v1.0.0",inline = False)
    
    myEmbed.set_author(name = " ")

    await ctx.message.channel.send(embed = myEmbed)

@client.command(name = 'helpp')
async def helpp(ctx):
    myEmbed = discord.Embed(title= "AbsurdBot command list: ", description = "", color =0x00ff00)
    myEmbed.add_field(name = "--wholesome", value= "Get the most wholesome memes",inline = False )
    myEmbed.add_field(name = "--meme", value= "Get the dankest memes",inline = False )
    myEmbed.add_field(name = "--shower", value= "Some disturbing shower thoughts OwO",inline = False )
    myEmbed.add_field(name = "--version", value= "The current version of AbsurdBot",inline = False )
    myEmbed.add_field(name = "--quote", value= "Get Wikiquotes from your favorite books/writers, enter Bookname or Author",inline = False )
    myEmbed.add_field(name = "--memri", value= "The best MemriTv shitposting for the heart.",inline = False )
    myEmbed.add_field(name = "--surreal", value= "Ah, yes. Surreal memes.",inline = False )
    myEmbed.add_field(name = "--satisfying", value= "Oddly eye pleasing content.",inline = False )
    myEmbed.add_field(name = "--phil", value= "Philsosphy memes for young posers teens.",inline = False )
    myEmbed.add_field(name = "--mca", value= "L3lam vibes",inline = False )
    
    await ctx.message.channel.send(embed = myEmbed)

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)


    general_channel = client.get_channel(645315903541608449)
    await general_channel.send('HELLOO !! \nType --helpp to see what i can do! (not --help)')
    
    

    await client.change_presence(status = discord.Status.online, activity=discord.Game('Existential dread | --helpp'))



#run whenever someone sends a msg it answers
@client.event
async def on_message(message):
    hi = ["hello AbsurdBot", "good morning AbsurdBot", "good afternoon AbsurdBot", "hi AbsurdBot", "slm AbsurdBot", "slt AbsurdBot", "salut AbsurdBot", "azul AbsurdBot","hey AbsurdBot","yo AbsurdBot","hi AbsurdBot"]
    hry= {"how are you AbsurdBot","how are you today AbsurdBot", "what's up AbsurdBot","how is today AbsurdBot","hry AbsurdBot"}
    #if someone says hi
    if message.content in hi: 
        ms = message.content[0:-7]
        general_channel = client.get_channel(645315903541608449)
        await general_channel.send(  ms )

 
    
    
    if message.content in hry: 
        general_channel = client.get_channel(645315903541608449)
        await general_channel.send("I'm doing great, How are you?")


    if message.content.lower() == 'what is your version':
        general_channel = client.get_channel(645315903541608449)

        myEmbed = discord.Embed(title = "Current Version",description = "The bot is in version : 1.0", colors=0x00ff00)
        myEmbed.add_field(name="Version Code:", value = "v1.0.0",inline = False)
        myEmbed.set_footer(text = "Simple footer")
        myEmbed.set_author(name = "Mira")

        await general_channel.send(embed = myEmbed)
    await client.process_commands(message)





@client.event
async def on_disconnect():
    general_channel = client.get_channel(645315903541608449)
    await general_channel.send('Goodbye! ')


client.run(TOKEN)
