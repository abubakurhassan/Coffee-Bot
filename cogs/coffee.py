import discord
from discord.ext import commands
from discord import app_commands
from config.settings import ALLOWED_CHANNEL_ID
from views.invite_view import CoffeeInviteView
from services.invites import get_waiting, clear_waiting, set_waiting
from database.db import get_user_stats, get_all_interactions, get_leaderboard
from typing import Optional


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
            return
        
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

    # --- Adds these commands to your Coffee cog --- #

    @app_commands.command(name="coffee-stats", description="View your coffee statistics")
    async def coffee_stats(self, interaction: discord.Interaction, member: Optional[discord.Member] = None):
        member = member or interaction.user
        
        stats = get_user_stats(member.id)
        
        embed = discord.Embed(
            title=f"☕ Coffee Stats for {member.display_name}",
            color=discord.Color.orange()
        )
        
        embed.add_field(name="Invites Sent", value=stats['invites_sent'], inline=True)
        embed.add_field(name="Invites Accepted", value=stats['invites_accepted'], inline=True)
        embed.add_field(name="Invites Declined", value=stats['invites_declined'], inline=True)
        
        embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
        
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="coffee-history", description="View recent coffee interactions")
    async def coffee_history(self, interaction: discord.Interaction):
        interactions = get_all_interactions(limit=10)
        
        if not interactions:
            await interaction.response.send_message("No coffee interactions yet!")
            return
        
        embed = discord.Embed(
            title="☕ Recent Coffee Interactions",
            color=discord.Color.orange()
        )
        
        for inviter, invitee, response, timestamp in interactions:
            status = "✅ Accepted" if response == "accepted" else "❌ Declined"
            embed.add_field(
                name=f"{inviter} → {invitee}",
                value=f"{status} • {timestamp}",
                inline=False
            )
        
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="coffee-leaderboard", description="View coffee invite leaderboard")
    async def coffee_leaderboard(self, interaction: discord.Interaction):
        leaderboard = get_leaderboard()
        
        if not leaderboard:
            await interaction.response.send_message("No data yet!")
            return
        
        embed = discord.Embed(
            title="☕ Coffee Invite Leaderboard",
            description="Most active coffee inviters",
            color=discord.Color.gold()
        )
        
        medals = ["🥇", "🥈", "🥉"]
        for i, (name, count) in enumerate(leaderboard):
            medal = medals[i] if i < 3 else f"{i+1}."
            embed.add_field(
                name=f"{medal} {name}",
                value=f"{count} invites",
                inline=False
            )
        
        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Coffee(bot))
