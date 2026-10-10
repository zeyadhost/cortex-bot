import discord
from discord.ext import commands
import logging

log = logging.getLogger(__name__)

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @bot.slash_command(name="ping", description="pong")
        async def hello(ctx: discord.ApplicationContext) -> None:
            latency_ms = round(bot.latency * 1000) # wallahi im lowkey tuff????
            await ctx.respond(f"pong! latency: {latency_ms}ms")
            log.info(f"ping command used by {ctx.author} in {ctx.guild.name}")

def setup(bot: discord.Bot) -> None:
    bot.add_cog(Ping(bot))