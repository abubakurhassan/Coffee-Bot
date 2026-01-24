# ☕ Coffee-Bot

A Discord bot that makes it easy to invite friends for coffee! Simply type "Coffee?" in the designated channel to send out an invitation with Yes/No buttons.

## Features

- 🤖 **Simple Coffee Invitations**: Send coffee invites with a single message
- ✅ **Interactive Buttons**: Friends can accept or decline with button clicks
- ⏰ **Auto Cleanup**: Invites older than 1 hour are automatically cleaned up
- 🔒 **Channel Restricted**: Works only in the designated coffee channel
- 🛡️ **Validation**: Prevents users from accepting their own invites

## Prerequisites

- Python 3.8 or higher
- A Discord bot token (from the [Discord Developer Portal](https://discord.com/developers/applications))
- A Discord server and channel ID where the bot will operate

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/abubakurhassan/Coffee-Bot.git
   cd Coffee-Bot
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   ```
   
   Activate it:
   - **Windows**: `venv\Scripts\activate`
   - **macOS/Linux**: `source venv/bin/activate`

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Copy [.env.example](.env.example) to `.env`:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your credentials:
   ```
   DISCORD_TOKEN=your_bot_token_here
   COFFEE_CHANNEL_ID=your_channel_id_here
   ```

## Configuration

### Getting Your Discord Token

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give it a name
3. Go to the "Bot" section and click "Add Bot"
4. Copy the token under the bot's username
5. Paste it in your `.env` file as `DISCORD_TOKEN`

### Getting Your Channel ID

1. Enable Developer Mode in Discord (User Settings → Advanced → Developer Mode)
2. Right-click on your desired channel and select "Copy Channel ID"
3. Paste it in your `.env` file as `COFFEE_CHANNEL_ID`

### Bot Permissions

Make sure your bot has the following permissions in the target channel:
- Send Messages
- Read Messages/View Channels
- Manage Messages (to delete messages)

## Usage

1. **Start the bot**
   ```bash
   python main.py
   ```

2. **Send a coffee invite**
   
   In your designated coffee channel, type:
   ```
   coffee?
   ```

3. **Wait for responses**
   
   Other users will see a message with two buttons:
   - ✅ **Yes 🔥** - Accept the coffee invite
   - ❌ **No 💔** - Decline the invite

4. **View the result**
   
   The invite message will update to show who accepted or declined

## How It Works

- **Message Detection**: The bot listens for messages in the designated channel
- **Invite Creation**: When someone types `coffee?`, an invite message with interactive buttons is posted
- **Response Handling**: Users click buttons to accept or decline
- **Auto-Cleanup**: Invites expire after 1 hour and are automatically removed
- **Validation**: Users cannot accept or decline their own invites

## Project Structure

```
Coffee-Bot/
├── main.py              # Main bot script
├── requirements.txt     # Python dependencies
├── .env.example         # Example environment variables
├── .env                 # Your environment variables (not in git)
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## Dependencies

- **discord.py** - Discord API wrapper
- **python-dotenv** - Environment variable management

See [requirements.txt](requirements.txt) for full details.

## Troubleshooting

### Bot doesn't respond
- Check that your `DISCORD_TOKEN` is correct
- Verify the bot is in your Discord server
- Ensure the bot has the necessary permissions

### Bot doesn't see messages
- Confirm `COFFEE_CHANNEL_ID` matches your target channel
- Check that the bot has "Read Messages" permission in that channel

### Buttons don't work
- Make sure the bot has "Send Messages" and "Manage Messages" permissions
- The bot should be running when you click buttons

## Contributing

Feel free to submit issues or pull requests to improve the bot!

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please open an issue on the [GitHub repository](https://github.com/abubakurhassan/Coffee-Bot).

---

**Happy coffee inviting! ☕**
