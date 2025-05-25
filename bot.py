import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from scrape_usaf import fetch_usaf_rss

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
AIR_FORCE_TIMES_RSS = os.getenv("AIR_FORCE_TIMES_RSS")
AF_MIL_RSS = os.getenv("AF_MIL_RSS")
DISCORD_CHANNEL_ID = os.getenv("DISCORD_CHANNEL_ID")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

def build_embeds(headlines, source):
    color = 0x1f8b4c if source == "AFT" else 0x00308F
    footer = "USAF News Bot • Air Force Times : Your Air Force RSS Feed " if source == "AFT" else "USAF News Bot • AF.mil : CSAF RSS Feed"

    embeds = []
    for title, link in headlines:
        embed = discord.Embed(title=title, url=link, color=color)
        embed.set_footer(text=footer)
        embeds.append(embed)
    return embeds

@bot.command(name="aftimes")
async def air_force_times(ctx):
    headlines = fetch_usaf_rss(AIR_FORCE_TIMES_RSS)
    if not headlines:
        await ctx.send("No headlines found.")
        return
    for embed in build_embeds(headlines, source="AFT"):
        await ctx.send(embed=embed)

@bot.command(name="afmil")
async def af_dot_mil(ctx):
    headlines = fetch_usaf_rss(AF_MIL_RSS)
    if not headlines:
        await ctx.send("No headlines found.")
        return
    for embed in build_embeds(headlines, source="AFM"):
        await ctx.send(embed=embed)

bot.run(DISCORD_TOKEN)