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

battletag = discord.SlashCommandGroup("battletag", "player related commands by battletag")

@battletag.command()
async def summary(ctx, battletag: str):
    player_url = f"https://overfast-api.tekrop.fr/players/{battletag}/summary"
    headers = {'Accept': 'application/json'}
    auth = ('username', 'userpass')
    response = requests.get(player_url, headers=headers, auth=auth).json()
    

 
    '''
    request handling and json embed / output goes here. continue later
    '''

# you'll have to manually add the manually created Slash Command group
bot.add_application_command(battletag)

bot.run(TOKEN)
