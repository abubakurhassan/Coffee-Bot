# ☕ Coffee-Bot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Discord.py](https://img.shields.io/badge/discord.py-2.0%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A Discord bot that makes organizing coffee breaks effortless! Simply type "Coffee?" in your designated channel to send out an invitation with interactive Yes/No buttons.

[Features](#features) • [Installation](#installation) • [Configuration](#configuration) • [Usage](#usage) • [Contributing](#contributing)

</div>

---

## 📖 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Commands](#commands)
- [How It Works](#how-it-works)
- [Development](#development)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

---

## 🎯 Overview

Coffee-Bot is a lightweight Discord bot designed to streamline social interactions within your server. Whether you're working remotely or coordinating with teammates, this bot makes it easy to send out coffee invitations and track responses in real-time.

### Why Coffee-Bot?

- **Simple**: One message triggers the entire invitation system
- **Interactive**: Users respond with a single button click
- **Clean**: Auto-cleanup prevents channel clutter
- **Organized**: Track who's interested at a glance

---

## ✨ Features

- 🤖 **Simple Coffee Invitations** - Send invites with just "Coffee?" in the designated channel
- ✅ **Interactive Buttons** - Friends can accept or decline with button clicks
- 📊 **Real-time Updates** - See who's accepted/declined as responses come in
- ⏰ **Auto Cleanup** - Invites older than 1 hour are automatically removed
- 🔒 **Channel Restricted** - Works only in your designated coffee channel
- 🛡️ **Validation** - Users cannot accept or decline their own invites
- 🏗️ **Modular Architecture** - Clean separation of concerns with cogs, services, and views
- 💾 **Database Support** - Persistent storage for invite tracking
- ⚙️ **Configurable** - Easy configuration through environment variables

---

## 📋 Prerequisites

Before you begin, ensure you have the following:

- **Python 3.8 or higher** installed on your system
- A **Discord account** and a Discord server where you have administrative permissions
- A **Discord bot token** from the [Discord Developer Portal](https://discord.com/developers/applications)
- Basic knowledge of command line/terminal usage

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/abubakurhassan/Coffee-Bot.git
cd Coffee-Bot
```

### 2. Create a Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Copy the example environment file:

```bash
# Windows
copy .env.example .env

# macOS/Linux
cp .env.example .env
```

Edit the `.env` file with your configuration:

```env
DISCORD_TOKEN=your_bot_token_here
COFFEE_CHANNEL_ID=your_channel_id_here
```

---

## ⚙️ Configuration

### Getting Your Discord Bot Token

1. Navigate to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Click **"New Application"** and give it a meaningful name (e.g., "Coffee-Bot")
3. Go to the **"Bot"** section in the left sidebar
4. Click **"Add Bot"** and confirm
5. Under the bot's username, click **"Reset Token"** and copy the token
6. Paste the token in your `.env` file as `DISCORD_TOKEN`

**⚠️ Security Warning:** Never share your bot token publicly or commit it to version control!

### Getting Your Channel ID

1. Open Discord and enable Developer Mode:
   - **Desktop:** User Settings → Advanced → Enable Developer Mode
   - **Web:** User Settings → Appearance → Enable Developer Mode
2. Right-click on your desired coffee channel
3. Select **"Copy Channel ID"**
4. Paste the ID in your `.env` file as `COFFEE_CHANNEL_ID`

### Inviting the Bot to Your Server

1. In the Discord Developer Portal, go to **OAuth2 → URL Generator**
2. Select the following scopes:
   - `bot`
   - `applications.commands` (if using slash commands)
3. Select the following bot permissions:
   - Read Messages/View Channels
   - Send Messages
   - Manage Messages
   - Read Message History
   - Add Reactions
   - Use Slash Commands (optional)
4. Copy the generated URL and open it in your browser
5. Select your server and authorize the bot

### Required Bot Permissions

Ensure your bot has these permissions in the coffee channel:

| Permission | Required | Purpose |
|------------|----------|---------|
| View Channel | ✅ | To monitor messages |
| Send Messages | ✅ | To send invitations |
| Manage Messages | ✅ | To delete old invites |
| Read Message History | ✅ | To process past messages |
| Add Reactions | ✅ | For button interactions |

---

## 📁 Project Structure

```
Coffee-Bot/
│
├── cogs/                   # Discord.py Cogs (command modules)
│   └── ...                 # Individual feature modules
│
├── config/                 # Configuration files
│   └── ...                 # Settings and constants
│
├── database/               # Database models and handlers
│   └── ...                 # Database operations
│
├── services/               # Business logic layer
│   └── ...                 # Service classes
│
├── views/                  # Discord UI components
│   └── ...                 # Button views and modals
│
├── bot.py                  # Main bot entry point
├── requirements.txt        # Python dependencies
├── .env.example            # Example environment variables
├── .env                    # Your environment variables (gitignored)
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

### Architecture Overview

Coffee-Bot follows a modular architecture pattern:

- **Cogs**: Organize commands and event listeners into logical groups
- **Services**: Handle business logic and data operations
- **Views**: Manage Discord UI components (buttons, modals, etc.)
- **Database**: Persist invite data and user interactions
- **Config**: Centralize configuration and constants

---

## 💻 Usage

### Starting the Bot

1. Ensure your virtual environment is activated
2. Run the bot:

```bash
python bot.py
```

3. Wait for the confirmation message:
```
Coffee-Bot is ready!
Logged in as: Coffee-Bot#1234
```

### Sending a Coffee Invite

1. Navigate to your designated coffee channel
2. Type the trigger message:
```
coffee?
```

3. The bot will post an invitation message with interactive buttons:

```
☕ Coffee Time!

@YourName is inviting everyone for coffee!

React below to join:
[✅ Yes 🔥]  [❌ No 💔]
```

### Responding to Invites

Other users can respond by clicking one of the buttons:

- **✅ Yes 🔥** - Accept the coffee invitation
- **❌ No 💔** - Decline the invitation

The message updates in real-time to show responses:

```
☕ Coffee Time!

@YourName is inviting everyone for coffee!

✅ Going (2): @Alice, @Bob
❌ Can't make it (1): @Charlie
```

### Auto-Cleanup

Invitations are automatically deleted after 1 hour to keep the channel clean and relevant.

---

## 🎮 Commands

Currently, Coffee-Bot responds to natural language triggers rather than traditional commands:

| Trigger | Description | Channel |
|---------|-------------|---------|
| `coffee?` | Sends a coffee invitation | Coffee channel only |
| `coffee!` | Alternative trigger | Coffee channel only |
| `☕` | Emoji trigger (if enabled) | Coffee channel only |

*Note: The exact triggers may vary based on configuration. Check the cogs directory for current implementations.*

---

## 🔧 How It Works

### Flow Diagram

```
User types "coffee?"
        ↓
Bot detects message in coffee channel
        ↓
Creates invitation with interactive buttons
        ↓
Posts message in channel
        ↓
Stores invite in database
        ↓
Users click buttons to respond
        ↓
Bot updates message with responses
        ↓
Validates responses (users can't accept own invites)
        ↓
After 1 hour: Auto-delete invitation
```

### Technical Details

1. **Message Detection**: The bot listens for specific keywords in the configured channel
2. **Invite Creation**: When triggered, creates a Discord embed with button components
3. **Database Storage**: Stores invite metadata (creator, timestamp, message ID)
4. **Response Handling**: Uses Discord's interaction system to handle button clicks
5. **Validation**: Checks that users aren't responding to their own invitations
6. **Auto-Cleanup**: Background task runs periodically to remove old invites

---

## 👨‍💻 Development

### Setting Up for Development

1. Fork the repository
2. Clone your fork:
```bash
git clone https://github.com/YOUR_USERNAME/Coffee-Bot.git
```

3. Create a new branch:
```bash
git checkout -b feature/your-feature-name
```

4. Make your changes and test thoroughly
5. Commit your changes:
```bash
git commit -m "Add: your feature description"
```

6. Push to your fork:
```bash
git push origin feature/your-feature-name
```

7. Create a Pull Request

### Code Style

- Follow PEP 8 guidelines for Python code
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Comment complex logic
- Keep functions focused and single-purpose

### Testing

Before submitting a PR:

1. Test all bot features manually
2. Ensure no errors appear in the console
3. Verify button interactions work correctly
4. Check that auto-cleanup functions properly
5. Test with multiple users if possible

---

## 🐛 Troubleshooting

### Bot Doesn't Start

**Issue**: Bot fails to connect or start

**Solutions**:
- Verify your `DISCORD_TOKEN` in `.env` is correct
- Check that you've copied the token without extra spaces
- Ensure your bot hasn't been deleted in the Developer Portal
- Check your internet connection

### Bot Doesn't Respond to Messages

**Issue**: Bot is online but doesn't react to "coffee?"

**Solutions**:
- Confirm `COFFEE_CHANNEL_ID` matches your target channel
- Verify the bot has "Read Messages" permission in that channel
- Check that Message Content Intent is enabled in the Developer Portal
- Restart the bot after any permission changes

### Buttons Don't Work

**Issue**: Buttons appear but don't respond when clicked

**Solutions**:
- Ensure the bot has "Send Messages" permission
- Verify "Use External Emojis" permission if using custom emojis
- Check that the bot is running when buttons are clicked
- Look for error messages in the bot console

### Database Errors

**Issue**: Errors related to database operations

**Solutions**:
- Check that the `database/` directory exists
- Verify file permissions allow read/write
- Ensure SQLite is available (usually included with Python)
- Delete and recreate the database file if corrupted

### Permission Issues

**Issue**: Bot can't perform certain actions

**Solutions**:
- Review the bot's role in server settings
- Ensure the bot's role is higher than roles it needs to interact with
- Check channel-specific permission overrides
- Re-invite the bot with the correct permissions

### Common Error Messages

| Error | Cause | Solution |
|-------|-------|----------|
| `Forbidden` | Missing permissions | Check bot permissions |
| `NotFound` | Channel/message deleted | Verify channel ID |
| `HTTPException` | Rate limited | Reduce bot activity |
| `LoginFailure` | Invalid token | Check DISCORD_TOKEN |

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Ways to Contribute

- 🐛 Report bugs by opening an issue
- 💡 Suggest new features or improvements
- 📝 Improve documentation
- 🔧 Submit pull requests with fixes or features
- ⭐ Star the repository to show support

### Contribution Guidelines

1. **Check existing issues** before creating a new one
2. **Describe bugs clearly** with steps to reproduce
3. **Propose features** with use cases and benefits
4. **Follow code style** guidelines
5. **Test your changes** thoroughly
6. **Update documentation** for new features

### Pull Request Process

1. Ensure your code follows the project's style
2. Update the README if you're adding features
3. Test all functionality before submitting
4. Provide a clear description of changes
5. Link any related issues

---

## 📄 License

This project is licensed under the **MIT License**. See below for details:

```
MIT License

Copyright (c) 2024 Abubakur Hassan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 💬 Support

Need help? Here's how to get support:

### Documentation

- Read through this README thoroughly
- Check the [Troubleshooting](#troubleshooting) section
- Review the code comments and docstrings

### Community Support

- **Issues**: [Open an issue](https://github.com/abubakurhassan/Coffee-Bot/issues) on GitHub
- **Discussions**: Start a discussion for questions and ideas
- **Pull Requests**: Submit improvements and fixes

### Discord.py Resources

- [Discord.py Documentation](https://discordpy.readthedocs.io/)
- [Discord Developer Portal](https://discord.com/developers/docs)
- [Discord.py Discord Server](https://discord.gg/dpy)

---

## 🎉 Acknowledgments

- Built with [discord.py](https://github.com/Rapptz/discord.py) library
- Inspired by the need for better team coordination
- Thanks to all contributors and users!

---

## 🗺️ Roadmap

Planned features and improvements:

- [ ] Add slash command support
- [ ] Implement custom coffee locations
- [ ] Add scheduling for future coffee breaks
- [ ] Create stats dashboard (most active users, etc.)
- [ ] Support multiple coffee channels
- [ ] Add reminder notifications
- [ ] Implement coffee preferences tracking
- [ ] Create admin commands for configuration
- [ ] Add internationalization support

---

<div align="center">

**Happy coffee inviting! ☕**

Made with ❤️ by [Abubakur Hassan](https://github.com/abubakurhassan)

If you found this project helpful, consider giving it a ⭐!

[Report Bug](https://github.com/abubakurhassan/Coffee-Bot/issues) · [Request Feature](https://github.com/abubakurhassan/Coffee-Bot/issues) · [Contribute](https://github.com/abubakurhassan/Coffee-Bot/pulls)

</div>
