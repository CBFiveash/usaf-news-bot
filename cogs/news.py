import os
import json
import datetime
from pathlib import Path

import asyncio
import pytz

import discord
from discord.ext import commands, tasks

from scrape_usaf import fetch_usaf_rss

class News(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.posted_links_file = Path("posted_links.json")
        self.posted_links = self.load_posted_links()
        self.channel_id = int(os.getenv("DISCORD_CHANNEL_ID"))
        self.aftimes_url = os.getenv("AIR_FORCE_TIMES_RSS")
        self.afmil_url = os.getenv("AF_MIL_RSS")
        self.post_daily_news.start()

    def cog_unload(self):
        self.post_daily_news.stop()
        self.save_posted_links()

    def load_posted_links(self):
        if self.posted_links_file.exists():
            try:
                with open(self.posted_links_file, "r") as f:
                    data = f.read().strip()
                    if data:
                        return set(json.loads(data))
            except json.JSONDecodeError:
                print("⚠️ posted_links.json is corrupted or empty. Reinitializing...")
        return set()
    
    def save_posted_links(self):
        with open(self.posted_links_file, "w") as f:
            json.dump(list(self.posted_links), f)

    def build_embed(self, title: str, headlines: list, color: discord.Color) -> discord.Embed:
        embed = discord.Embed(title=title, color=color)
        for title, link in headlines:
            embed.add_field(name=title, value=link, inline=False)
        return embed
    
    def get_new_headlines(self, headlines: list) -> list:
        new_headlines = []
        for title, link in headlines:
            if link not in self.posted_links:
                new_headlines.append((title, link))
                self.posted_links.add(link)
        return new_headlines

    @commands.command(name="aftimes")
    async def air_force_times(self, ctx):
        headlines = fetch_usaf_rss(self.aftimes_url)
        if not headlines:
            await ctx.send("No headlines found.")
            return

        embed = self.build_embed("Top Headlines from Air Force Times", headlines, discord.Color.dark_green())
        await ctx.send(embed=embed)

    @commands.command(name="afmil")
    async def af_dot_mil(self, ctx):
        headlines = fetch_usaf_rss(self.afmil_url)
        if not headlines:
            await ctx.send("No headlines found.")
            return

        embed = self.build_embed("Top Headlines from AF.mil", headlines, discord.Color.dark_blue())
        await ctx.send(embed=embed)

    @commands.command(name="newsall")
    async def news_all(self, ctx):
        aftimes = fetch_usaf_rss(self.aftimes_url)
        afmil = fetch_usaf_rss(self.afmil_url)

        if aftimes:
            embed = self.build_embed("Air Force Times Headlines", aftimes, discord.Color.dark_green())
            await ctx.send(embed=embed)
        else:
            await ctx.send("No Air Force Times headlines found.")

        if afmil:
            embed = self.build_embed("AF.mil Headlines", afmil, discord.Color.dark_blue())
            await ctx.send(embed=embed)
        else:
            await ctx.send("No AF.mil headlines found.")

    @tasks.loop(hours=1)
    async def post_daily_news(self):
        now = datetime.datetime.now(pytz.timezone("US/Pacific"))
        if now.weekday() < 5 and now.hour == 8 and now.minute == 0:  # Monday to Friday, 8 AM PST
            channel = self.bot.get_channel(self.channel_id)
            if not channel:
                print("Channel not found!")
                return

            # Fetch top 3 headlines from each feed
            aftimes_headlines = fetch_usaf_rss(self.aftimes_url)[:3]
            afmil_headlines = fetch_usaf_rss(self.afmil_url)[:3]

            all_headlines = []

            for title, link in aftimes_headlines + afmil_headlines:
                if link not in self.posted_links:
                    all_headlines.append((title, link))
                    self.posted_links.add(link)

            if all_headlines:
                embed = discord.Embed(title="Today's USAF News Headlines", color=0x1a237e)
                for title, link in all_headlines:
                    embed.add_field(name=title, value=link, inline=False)

                await channel.send(embed=embed)
                self.save_posted_links()
            else:
                print("No new headlines to post today.")

    @post_daily_news.before_loop
    async def before_post_daily_news(self):
        await self.bot.wait_until_ready()
        now = datetime.datetime.now()
        seconds_until_next_hour = 3600 - now.minute * 60 - now.second
        await asyncio.sleep(seconds_until_next_hour)

async def setup(bot):
    await bot.add_cog(News(bot))
