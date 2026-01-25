import discord
from services.invites import set_waiting

class CoffeeInviteView(discord.ui.View):
    def __init__(self, inviter: discord.Member, invitee: discord.Member):
        super().__init__(timeout=3600)
        self.inviter = inviter
        self.invitee = invitee
        self.responded = False

    @discord.ui.button(label="Yes! ☕", style=discord.ButtonStyle.success)
    async def accept(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):
        
        # --- Only the invited person can click --- #
        if interaction.user.id == self.invitee.id:
            await interaction.response.send_message(
                f"{self.invitee.mention} What are you stupid? Trying to accept your own invite...go touch some grass!",
                ephemeral=True
            )
            return
        
        set_waiting(
            channel_id=interaction.channel_id,
            invitee_id=self.invitee.id,
            wait_type="details"
        )

        await interaction.response.send_message(
            f"Awesome {self.invitee.mention}, anything you wanna add?"
        )

        self.stop() # --- Stops listening for button clicks --- #

    @discord.ui.button(label="No! 🤨", style=discord.ButtonStyle.danger)
    async def decline(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):
        # --- Only the invited person can click --- #
        if interaction.user.id != self.invitee.id:
            await interaction.response.send_message(
                "Really? Saying no to yourself? Have some self-respect!",
                ephemeral=True
            )
            return
        
        set_waiting(
            channel_id=interaction.channel_id,
            invitee_id=self.invitee.id,
            wait_type="reason"
        )

        await interaction.response.send_message(
            "No?! Why? WHY? I guess you dont love me no more."
        )

        self.stop() # --- Stops listening for button clicks --- #