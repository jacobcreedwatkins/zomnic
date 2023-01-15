import discord
import os
import sys
from discord.ext import commands
import typing
import requests
from dotenv import load_dotenv
import json

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Bot(intents=intents)
load_dotenv()

TOKEN = os.getenv('ZOMNIC_TOKEN')
if not TOKEN:
    print('ERROR: Token var is missing: ZOMNIC_TOKEN')
    sys.exit(-1)



@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

## insert request info here
@bot.command()
async def summary(ctx, battletag: str):
    player_id = battletag
    player_url = f"https://overfast-api.tekrop.fr/players/{player_id}/summary"
    player_resp = requests.get(player_url)
    print(player_resp.json)


    await ctx.respond(player_resp)

bot.run(TOKEN)











