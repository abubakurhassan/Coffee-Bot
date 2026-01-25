import discord
from discord.ext import commands
from discord import app_commands
from config.settings import ALLOWED_CHANNEL_ID
from views.invite_view import CoffeeInviteView
from services.invites import get_waiting, clear_waiting

class Coffee(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="coffee", description="Invite for coffee!")
    async def coffee(self, interaction: discord.Interaction):
        
        if interaction.channel_id != ALLOWED_CHANNEL_ID:
            await interaction.response.send_message(
                "Please use this command ONLY in the coffee-time channel",
                ephemeral=True
            )
            return
        
        # --- TEMP: hardcode the friend for now --- #
        # --- (we’ll clean this up later) --- #
        guild = interaction.guild
        members = [m for m in guild.members if not m.bot]

        if len(members) < 2:
            await interaction.response.send_message(
                "Not enough members to invite",
                ephemeral=True
            )
            return
        
        inviter = interaction.user
        invitee = next(m for m in members if m.id != inviter.id)

        view = CoffeeInviteView(inviter, invitee)
        
        await interaction.response.send_message(
            f"☕ **Coffee Invite!**\n\n"
            f"{inviter.mention} is inviting you to go out for coffee.\n"
            f"Do you accept...or are you gonna be a lil b*tch!",
            view=view
        )

# --- Listens for the response from the poll --- #

        @commands.Cog.listener()
        async def on_message(self, message: discord.Message):
            # --- Ignore Bots --- #
            if message.author.bot:
                return
            
            waiting = get_waiting(message.channel.id)
            if not waiting:
                return
            
            # --- Only accept message from the expected invitee --- #
            if message.author.id != waiting["invitee_id"]:
                return
            
            # --- Handle Response --- #
            if waiting["type"] == "details":
                await message.channel.send(
                    f"**Details:** {message.content}"
                )

            elif waiting["type"] == "reason":
                await message.channel.send(
                    f"**Reason for being a b*tch:** {message.content}"
                )

            clear_waiting(message.channel.id)

async def setup(bot: commands.Bot):
    await bot.add_cog(Coffee(bot))