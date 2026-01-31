import discord
from discord.ext import commands
from discord import app_commands
from config.settings import ALLOWED_CHANNEL_ID
from views.invite_view import CoffeeInviteView
from services.invites import get_waiting, clear_waiting, set_waiting

class Coffee(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="coffee", description="Invite for coffee!")
    async def coffee(self, interaction: discord.Interaction):

        # --- Check if its the right channel --- #
        if interaction.channel_id != ALLOWED_CHANNEL_ID:
            await interaction.response.send_message(
                "Please use this command ONLY in the coffee-time channel",
                ephemeral=True
            )
            return
        
        # --- Check for active invites --- #
        waiting = get_waiting(interaction.channel_id)
        if waiting:
            await interaction.response.send_message(
                f"There's already an active coffee invite! Wait for it to finish first.",
                ephemeral=True
            )
        
        inviter = interaction.user

        # --- Mark this channel as having an active invite --- #
        set_waiting(interaction.channel_id, inviter.id)

        view = CoffeeInviteView(inviter = inviter, channel_id=interaction.channel_id)

        await interaction.response.send_message(
            f"☕ **Coffee Invite!**\n\n"
            f"{inviter.mention} is inviting you to go out for coffee.\n"
            f"Do you accept...or are you gonna be a lil b*tch!",
            view=view
        )

async def setup(bot):
    await bot.add_cog(Coffee(bot))
