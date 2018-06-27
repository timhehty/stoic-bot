import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("?", "!")
TOKEN = "NDYwNjU4MTUxMjA1ODk2MjAy.DhM_vw.KeF37s2pvQbGHzqCHxPUf_lOOr8"

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='quote',
                description="Gives a Stoic quote",
                brief="thank u marcus",
                aliases=['stoic_quote', 'stoicquote'],
                pass_context=True)
async def quote(context):
    quotes = [
        '"lets play bball" - moe',
        '"Good luck! :)" - UW_Reject',
        '“Sometimes even to live is an act of courage.” - Seneca',
    ]
    await client.say(random.choice(quotes))

@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with humans"))
    print("Logged in as " + client.user.name)


@client.command()
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("Bitcoin price is: $" + response['bpi']['USD']['rate'])

#@client.command()
#async def worldcup():
#    url = 'https://worldcup.sfg.io/matches/current'
#    async with aiohttp.ClientSession() as session:  # Async HTTP request
#        raw_response = await session.get(url)
#        response = await raw_response.text()
#        response = json.loads(response)
#        if response[''] = "":
#        await client.say("There is no current match")
#        else:
#        await client.say("The current match is " + response[''])

@client.command()
async def weather():
    url = 'https://api.darksky.net/forecast/b5a7fda34daf7f276aad4947e1d3af4d/43.6532,-79.3832'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)

        tempF = int(response['currently']['temperature'])
        tempC = ((tempF) - 32) * (5/9)
        tempC = int(tempC)
        if tempC >= 20:
            appropClothes = ". You're good to go outside with just a T-shirt and shorts."
        if tempC <= 19 and tempC >= 11:
            appropClothes = ". You should probably wear a light jacket and/or sweater."
        if tempC <= 10 and tempC >= 0:
            appropClothes = ". A heavier jacket or coat is a good idea."
        if tempC <= 0:
            appropClothes = ". Please wear a heavy winter jacket or coat."
        tempC = str(tempC)
        await client.say("The current temperature is " + tempC + "°C" + appropClothes)

async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)

client.loop.create_task(list_servers())
client.run(TOKEN)
