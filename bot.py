import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

class CoffeeBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix = "/",
            intents=intents
        )

    async def setup_hook(self):
        await self.load_extension("cogs.coffee")
        await self.tree.sync()
        print("Slash commands synced")

bot = CoffeeBot()

@bot.event
async def on_ready():
    print(f"☕ Logged in as {bot.user}")

bot.run(TOKEN)