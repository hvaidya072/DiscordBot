import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import asyncio

token = os.environ['token']
client = commands.Bot(command_prefix = '!')
# bot = discord.Bot()



#function activate when started
@client.event
async def on_ready():
    print("Spirit woken")
    await client.change_presence(game=discord.Game(name='Food War'))


#All the dank replies and copypasta stuff goes here
@client.event
async def on_message(message):
    if message.content.startswith("!test"):
        await client.send_message(message.channel, "Lets revolt my comrades!")

    if 'communism' in message.content.lower():
        if message.author == client.user:
            return
        pasta = """To be fair, you have to have a very high IQ to understand communism. The identity politics are extremely subtle, and without a solid grasp of liberal arts most of their viewpoints will go over a typical economist's head. There's also a large amount of ethnic genocides, which is deftly woven into communist regimes - Joseph Stalin's forced relocation of millions of Chechens, for instance. The teenagers understand this stuff; they have the intellectual capacity to truly appreciate the depths of the theories, to realize that they're not just starving- they say something deep about LIFE. As a consequence people who dislike communism truly ARE idiots- of course they wouldn't appreciate, for instance, the social conditions in Che's existencial catchphrase "The negro is indolent and lazy," which itself is a cryptic reference to Karl Marx's hatred of Jews. I'm smirking right now just imagining one of those addlepated simpletons scratching their heads in confusion as Peter Kropotkin's genius unfolds itself on their iPhone 6. What fools... how I pity them. 😂 And yes by the way, I DO have a hammer and sickle tattoo. And no, you cannot see it. It's for the ladies' eyes only- And even they have to demonstrate that they're within 5 welfare cards of my own (preferably lower) beforehand."""

        await client.send_message(message.channel, pasta)

    if 'mario' in message.content.lower():
        if message.author == client.user:
            return
        pasta = """Hello everyone, I would like to bring to your attention that there may just be a hidden metaphor for Communism in everyone's favorite racing game, Mario Kart Wii. As an avid Mario Kart player, I can say that I have endured my fair-shares of blue shells. However, after representing Uzbekistan in the 2009 Central Uzbek Nintendo Tournament (CUNT), and receiving at least 69 blue shell attacks, I finally come to the conclusion that the blue shell is not just any ordinary in-game item, but in fact a metaphor for Communism. Think about it. The entire game can be seen as a microcosm for Capitalism. The players that place in the top six gain the most experience, and they receive upbeat and cheerful music after every race, which could represent the privileges 1%. Meanwhile, the players that place below the top six will in fact lose experience, and degrading and sad music will be played after they finish the race. The players below the top six will have to work their way up to the top in order to receive the benefits of the top six. See? A perfect representation of Capitalism! However, there is an item that can be used to disrupt the course of the race; the blue shell. Any player that is not in first can receive this item upon opening up a item box. Said item will track down the player in first, and hit them without failure. Thus giving all the players that are not in first an opportunity to catch up during the race, and therefore equalizing the playing field. Did Nintendo mean to include this? We may never know. I believe that the blue shell is supposed to be a metaphor for Communism, as it can allow those below 6th place (the 1%) to catch up and be equal to those in 6th place and above (the 1%).Thank you all for your time, -An Uzbek Mario Kart Champion"""

        await client.send_message(message.channel, pasta)

    if 'seize' in message.content.lower():
        link = 'https://www.youtube.com/watch?v=U06jlgpMtQs'
        await client.send_message(message.channel, link)

    if 'liberal' in message.content.lower() or 'leftist' in message.content.lower():
        if message.author == client.user:
            return
        pasta = """I want leftists to start making use of the media channels that capitalist have been using for years to spread our theory rather than through academic shit. less reading books more interaction with humans and "recreational media". capitalists have painted memes and comic books as leisurely activities specifically to encourage this rhetoric in this meme of "lol you need a formal education (DEBT!!!) to be a leftist"""
        await client.send_message(message.channel, pasta)
    if 'capitalism' in message.content.lower() or 'capitalist' in message.content.lower():
        if message.author == client.user:
            return
        pasta = """Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system Flawed system"""
        await client.send_message(message.channel, pasta)
    if 'libtard' in message.content.lower():
        if message.author == client.user:
            return
        pasta = """What the fuck did you just fucking say about me? you fucking kulak? I'll have you know I graduated top of my class in the The People's Commissariat for Internal Affairs, and I’ve been involved in numerous secret raids on Batista's cuban government, and I have over 410757864530 confirmed kills. I am trained in gorilla warfare and I’m the top sniper in the entire USSR armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet you ass munching fascist? Think again, fucker. As we speak I am contacting my secret network of spies across the world and your IP is being traced right now so you better prepare for the storm, whitey. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kulak. I can be anywhere, anytime, and I can kill you in over seven hundred thousand ways, and that’s just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the Soviet Navy and I will use it to its full extent to wipe your miserable ass off the face of the earth, you little shit eating fascist insect. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldnt, and you didnt, and now you're paying the price, you goddamn nazi. I will shit fury all over you and you will drown in it. Youre fucking dead, kulak"""
        await client.send_message(message.channel, pasta)
    if 'python' in message.content.lower():
        if message.author == client.user:
            return
        pasta = """Oh you think python is good?Let's start with indentation errors. What the actual fuck? No sane programming language structures itself on tabs, you want clear blocks? You want an end, well fuck you! Better make sure it's all aligned well. Are you 4 layers down into indentation, better make sure that screen real estate is holding up, wouldn't want to cause you any fucking stupid problems or anything. Wanna use tabs? Sure, use tabs, prettiest things on earth, some spaces, why not, throw it all in, oh wait, I like either one but not both together. Your dirty friend doesn't know how to set up his vim (and it shouldn't damn well matter), :retab won't work because you've now created a horrible mess. Oh, wanna git clone some code, for sure, just make sure you use the exact same configuration, and please do follow the joke of a style guide, it's the only way our programs actually run. BECAUSE THEy ARE DEPENDANT ON STYLE WHAT THE FUCK. Semicolons are optional, lovely. Want to flatten an array, .flatten? Nooooo, gotta overload the + operator sum(fuck,+) this how disgusting is that. Want to unique a list? .uniq? Something like that? Noooo list(set(mylist)) are you kidding me?! Type conversion will solve all our issues. 100. most disguting syntax, and a loop just iterates through a range. Ohhh, backwards compatability? Nopeeeeee, wouldn't want that in a scripting language now would we, too bad our original design was so messed up we had to be so brave to basically rewrite the whole thing, not like anyone was using it or anything.... And holy crap the syntax, most ugly thing I've ever seen what on earth Curly braces noooooope, too easy and they have the gall to call this entire monster the "pythonist" way, must be . Want to overload default operators in your class, just what they look like right? Nooope, every single one has a godamn special name, let's take a look at the list right, couldn't make it simple or anything. Want a ternary, eh? Something simple two character ?: magic? No, fuck you, use [res1,res2](condition) or a assbackwards most confusing and ugly horrific res1 if condition else res 2, I mean what the actualy fuck is that? Oh and let's preface all our functions with a thousand ____ like the tears you cry when you try to make sure it's the correct number, oh and always make sure to pass in self, wouldn't want to have scope or get lost or anything nooooo.
                    Well you may ask? Surely python must have something good right? All those scientists must use it for a reason (and 90% of them write horrific code and have no clue about it by the way, as is unsurprising, hence the python). Well yeah, it has some nice libraries, but that's like saying it's a nice car because someone decided to build a fancy trailer for it. And it automatically freezes string literals, that's slightly convenient."""
        await client.send_message(message.channel, pasta)

    await client.process_commands(message)


#commands for the bot with prefix '!'
#this one echoes everything the user says
@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)


#clear messages, 10 at a time
@client.command(pass_context=True)
async def sweep(ctx, amount=10):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel,limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say("Cleared")

#leader images go here
@client.command(pass_context=True)
async def stalin(ctx):
    await client.send_file(ctx.message.channel, 'images/Stalin.jpg')

@client.command(pass_context=True)
async def sexystalin(ctx):
    await client.send_file(ctx.message.channel, 'images/sexystalin.jpg')

@client.command(pass_context=True)
async def daddymarx(ctx):
    await client.send_file(ctx.message.channel, 'images/daddymarx.jpg')

@client.command(pass_context=True)
async def fidel(ctx):
    await client.send_file(ctx.message.channel, 'images/fidel.jpg')

@client.command(pass_context=True)
async def lenin(ctx):
    await client.send_file(ctx.message.channel, 'images/lenin.jpg')


#command activated when a new member joins
@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Comrades')
    await client.add_roles(member, role)
    channel = discord.utils.get(member.server.channels, name='general')
    await client.send_message(channel, "Hello there {}. You have been promoted to Comrade rank!".format(member.name))


#only the admin can kick people
@client.command(pass_context=True)
async def kick(ctx, guilty):
    member = discord.utils.get(ctx.message.server.members, name=guilty)
    if member == None:
        await client.say("Traitor not found")
        return
    elif ctx.message.author.name == "Cartmanez#8671":
        await client.kick(member)
        await client.say("Member Kicked")
    else:
        await client.say("Back off Comrade! :triumph: You're not daddy Cartmanez :heart_eyes:")




client.run(token)
