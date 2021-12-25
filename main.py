import discord
from classPeriod import *

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.id == 378635930875199498:
        await message.channel.send('shutup lol')

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$period'):
        get_time()
        print(period())
        await message.channel.send(period())

    if message.content.startswith('$repeat'):
        repeat_word = message.content[7:] 
        print(repeat_word)
        if repeat_word == '' or repeat_word == '':
            await message.channel.send('There is nothing to repeat!')
        else:
            await message.channel.send(repeat_word)

    if message.content.startswith('$guess'):
        print(message.author.id)
        await message.channel.send('idk yet bruh')

    if "mid" in message.content:
        await message.channel.send('shutup ur mid')

client.run('OTAxODkxMzc3MDAzMTM1MDY2.YXWdzA.xvwCTTyOW7rN8L2LDQfonYcTy6E')
