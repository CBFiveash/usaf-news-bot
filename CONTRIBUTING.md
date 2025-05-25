# Contributing to USAF News Bot

Thank you for your interest in contributing! 🎖️  
The goal of this bot is to keep Airmen and enthusiasts up to date with the latest USAF-related news from trusted sources like AirForceTimes and AF.mil.

## How You Can Help

We welcome contributions of all kinds:

- 🧠 Feature suggestions
- 🐛 Bug fixes
- 📝 Documentation improvements
- 🧪 Tests or refactoring
- 🤖 New feed integrations

## Getting Started

1. **Fork the repository**
2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR-USERNAME/usaf-news-bot.git
   cd usaf-news-bot
   ```
3. **Install dependencies**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
4. **Create a `.env` file with your bot token and feed URLs:**
    ```bash
    DISCORD_TOKEN=your_discord_token
    DISCORD_CHANNEL_ID=your_channel_id
    AIR_FORCE_TIMES_RSS=https://...
    AF_MIL_RSS=https://...
    ```
## Contributing Guidelines
- Follow [PEP8](https://peps.python.org/pep-0008/) for Python code.
- Use clear, concise commit messages (e.g., Add AF.mil embed support).
- Write comments where the logic isn't immediately obvious.
- Run and test your changes before submitting a PR.

## Submitting Pull Requests (PR)
1. **Push your changes to a new branch:**
    ```bash
    git checkout -b feature/my-cool-idea
    git push origin feature/my-cool-idea
    ```
2. **Open a pull request on GitHub against the main branch.**
3. **Describe your changes and link any related issues.**

## Code of Conduct
Be respectful, kind, and constructive. We're all here to learn and improve.

---

**Fly, fight, and code on. 💻✈️**