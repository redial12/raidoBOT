import discord
from discord import message
from discord import user
from discord.utils import get
from classPeriod import *
from discord.ext import commands

oldclient = discord.Client()

client = commands.Bot(case_insensitive = True, command_prefix ='$')

shutuser = 0

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def test(ctx, arg):
    print(arg)
    await ctx.send(arg)

@client.command()
async def p(ctx):
    get_time()
    print(period())
    await ctx.send(period())

@client.command()
async def id(ctx):
    await ctx.send('Your discord ID is **{}**.'.format(ctx.message.author.id))

@client.command()
async def shut(ctx, arg):
    global shutuser
    right_index = arg.find('>')
    userid = arg[3:right_index]
    shutuser = userid
    print("The shutuser ID is now: " + str(shutuser))
    await ctx.send('The new shutup user is {}.'.format(arg))

@client.event
async def on_message(message):
    global shutuser
    if message.author == client.user:
         return

    if str(message.author.id) == str(shutuser):
        await message.channel.send('shutup lol')

    if shutuser == 244273736818229248:
        await message.channel.send('shutup lol')

    await client.process_commands(message)

#     if message.content.startswith('$guess'):
#         print(message.author.id)
#         await message.channel.send('idk yet bruh')

    # if "mid" in message.content:
    #     await message.channel.send('shutup ur mid')

client.run('token')
