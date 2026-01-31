import discord
from services.invites import set_waiting, clear_waiting

class CoffeeInviteView(discord.ui.View):
    def __init__(self, inviter: discord.Member, channel_id: int):
        super().__init__(timeout=3600)
        self.inviter = inviter
        self.invitee = None
        self.channel_id = channel_id
    
    @discord.ui.button(label="Yes! ☕", style=discord.ButtonStyle.success)
    async def accept(self, interaction: discord.Interaction, button: discord.ui.Button):
        
        self.invitee = interaction.user
        
        # --- Only the invited person can click --- #
        if self.invitee == self.inviter:
            await interaction.response.send_message(
                f"{self.inviter.mention} What are you stupid? Trying to accept your own invite...go touch some grass!",
                ephemeral=True
            )
            self.invitee = None  # Reset since inviter can't be invitee
            return
        
        # Disable buttons after someone responds
        for item in self.children:
            item.disabled = True
        
        #clear waiting status
        clear_waiting(self.channel_id)

        # Update the message with disabled buttons
        await interaction.response.edit_message(view=self)
        
        # Send the follow-up message
        await interaction.followup.send(
            f"Awesome {self.invitee.mention}, anything you wanna add?"
        )
    
    @discord.ui.button(label="No! 🤨", style=discord.ButtonStyle.danger)
    async def decline(self, interaction: discord.Interaction, button: discord.ui.Button):
        
        self.invitee = interaction.user
        
        # --- Only the invited person can click --- #
        if self.invitee == self.inviter:
            await interaction.response.send_message(
                f"Really? Saying no to yourself? Have some self-respect!",
                ephemeral=True
            )
            self.invitee = None  # Reset since inviter can't be invitee
            return
        
        # Disable buttons after someone responds
        for item in self.children:
            item.disabled = True

        # Clear waiting status
        clear_waiting(self.channel_id)
        
        # Update the message with disabled buttons
        await interaction.response.edit_message(view=self)
        
        # Send the follow-up message
        await interaction.followup.send(
            "No?! Why? WHY? I guess you dont love me no more."
        )


    
    async def on_timeout(self):
        # Disable buttons when timeout occurs
        for item in self.children:
            item.disabled = True

            clear_waiting(self.channel_id)






        # # --- Only the invited person can click --- #
        # if interaction.user.id != self.invitee.id:
        #     await interaction.response.send_message(
        #         "Really? Saying no to yourself? Have some self-respect!",
        #         ephemeral=True
        #     )
        #     return
        
        # set_waiting(
        #     channel_id=interaction.channel_id,
        #     invitee_id=self.invitee.id,
        #     wait_type="reason"
        # )

        # await interaction.response.send_message(
        #     "No?! Why? WHY? I guess you dont love me no more."
        # )

        # self.stop() # --- Stops listening for button clicks --- #