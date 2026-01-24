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

# --- Store active invites --- #
active_invites = {}

# --- Discord Client Setup --- #
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

# --- Create Discord Client --- #
client = discord.Client(intents=intents)


class CoffeeButtons(View):
    def __init__(self, inviter_id):
        super().__init__(timeout=None)
        self.inviter_id = inviter_id

    @discord.ui.button(label="Yes 🔥", style=discord.ButtonStyle.grey, custom_id="yes_button")
    async def yes_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id == self.inviter_id:
            await interaction.response.send_message("You cannot accept your own coffee invite!", ephemeral=True)
            return
        
        await interaction.response.edit_message(
            content=f"{interaction.message.content}\n✅ {interaction.user.mention} accepted! Send details about time/place.",
            view=None
        )

        if interaction.message.id in active_invites:
            del active_invites[interaction.message.id]

    @discord.ui.button(label="No 💔", style=discord.ButtonStyle.grey, custom_id="no_button")
    async def no_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id == self.inviter_id:
            await interaction.response.send_message("You cannot decline your own coffee invite!", ephemeral=True)
            return
        
        await interaction.response.edit_message(
            content=f"{interaction.message.content}\n❌ {interaction.user.mention} said no...why would you do that?",
            view=None
        )

        if interaction.message.id in active_invites:
            del active_invites[interaction.message.id]

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    
    if message.channel.id != COFFEE_CHANNEL_ID:
        return
    
    content = message.content.strip()

    if content.lower() == "coffee?":
        await message.delete()

        view = CoffeeButtons(message.author.id)
        invite_msg = await message.channel.send(
            content=f"{message.author.mention} is inviting you for coffee!",
            view=view
        )

        active_invites[invite_msg.id] = {
            "inviter": message.author.id,
            "timestamp": datetime.now()
        }
        return

    await message.delete()
    warning_msg = await message.channel.send(
        f"{message.author.mention}, you can only send \"Coffee?\" to invite someone."
    )
    await asyncio.sleep(5)
    await warning_msg.delete()

async def cleanup_old_invites():
    await client.wait_until_ready()
    while not client.is_closed():
        now = datetime.now()
        to_delete = []


        for msg_id, data in active_invites.items():
            if now - data["timestamp"] > timedelta(hours=1):
                to_delete.append(msg_id)

        for msg_id in to_delete:
            del active_invites[msg_id]

        await asyncio.sleep(3600)

# --- Add setup_hook to client --- #
async def setup_hook():
    client.loop.create_task(cleanup_old_invites())

client.setup_hook = setup_hook

if __name__ == "__main__":
    client.run(TOKEN)