import discord
from discord.ui import Button, View
from datetime import datetime, timedelta
from dotenv import load_dotenv
import asyncio
import os

# --- Load environment variables --- #
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
COFFEE_CHANNEL_ID = int(os.getenv('COFFEE_CHANNEL_ID'))

