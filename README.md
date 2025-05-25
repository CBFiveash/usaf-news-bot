# USAF News Discord Bot

A lightweight Discord bot that fetches and shares the latest United States Air Force news from two sources:
- [Air Force Times](https://www.airforcetimes.com)
- [AF.mil Official News](https://www.af.mil)

## 🚀 Features

- `/aftimes` — Get the 5 latest headlines from Air Force Times.
- `/afmil` — Get the 5 latest headlines from AF.mil.
- Embeds with article title, link, and image (when available).
- Cleanly grouped results for better readability.

## 🛠️ Prerequisites

- Python 3.9+
- A Discord bot token (https://discordpy.readthedocs.io/en/stable/discord.html)
- Access to a Discord server where you can add the bot

*(Optional)* **ONLY if you want to containerize**
- [Docker](https://docs.docker.com/get-started/get-docker/) installed
- [Docker Compose](https://docs.docker.com/compose/) for simplified orchestration

### Installation
```bash
git clone https://github.com/yourusername/usaf-news-bot.git
cd usaf-news-bot
```

### Environment Variables

Create a `.env` file with the following:

```bash
DISCORD_TOKEN=your_discord_bot_token_here
DISCORD_CHANNEL_ID=your_channel_id
AIR_FORCE_TIMES_RSS=[INSERT RSS URL]
AF_MIL_RSS=[INSERT RSS URL]
```

## ⚙️ Local Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run the Bot Locally
```bash
python bot.py
```

## 🐳 Running with Docker 
1. **Create a `.dockerignore`**
    ```bash
    venv/
    __pycache__/
    *.pyc
    .env
    ```

2. **Build the Docker iamge**
    ```bash
    docker build -t usaf-news-bot .
    ```

4. **Docker Compose using [docker-compose.yml](./docker-compose.yml)** 
    ```bash
    docker compose up --build -d
    ```

### 🤝 Contributing
See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines on reporting issues, suggesting features, and submitting pull requests.

### 📄 License 
This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.


--- 

**`Made with ❤️ by CBFiveash`**