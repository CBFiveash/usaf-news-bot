import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

async def load_extensions():
    try:
        await bot.load_extension("cogs.news")
        print("🔌 Loaded extension: cogs.news")
    except Exception as e:
        print(f"❌ Failed to load extension: {e}")

async def main():
    async with bot:
        await load_extensions()
        await bot.start(DISCORD_TOKEN)

import asyncio
asyncio.run(main())
