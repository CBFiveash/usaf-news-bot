# USAF News Discord Bot

A lightweight Discord bot that fetches and shares the latest United States Air Force news from two sources:
- [Air Force Times](https://www.airforcetimes.com)
- [AF.mil Official News](https://www.af.mil)

## Features

- `/aftimes` — Get the 5 latest headlines from Air Force Times.
- `/afmil` — Get the 5 latest headlines from AF.mil.
- Embeds with article title, link, and image (when available).
- Cleanly grouped results for better readability.

## Setup

### Prerequisites

- Python 3.9+
- A Discord bot token (https://discordpy.readthedocs.io/en/stable/discord.html)
- Access to a Discord server where you can add the bot

### Installation

```bash
git clone https://github.com/yourusername/usaf-news-bot.git
cd usaf-news-bot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file with the following:

```bash
DISCORD_TOKEN=your_discord_bot_token_here
DISCORD_CHANNEL_ID=your_channel_id
AIR_FORCE_TIMES_RSS=[INSERT RSS URL]
AF_MIL_RSS=[INSERT RSS URL]
```

### Run the Bot
```bash
python bot.py
```

### License 
This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.


`Made with ❤️ by CBFiveash`