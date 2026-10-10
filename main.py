from dotenv import load_dotenv
import os
import logging
import discord
from rich.console import Console
from rich.logging import RichHandler
from rich.theme import Theme

theme = Theme({
    "logging.level.info": "bold cyan",
    "logging.level.warning": "bold yellow",
    "logging.level.error": "bold red",
    "logging.level.debug": "dim green",
})

load_dotenv()
bot = discord.Bot()
console = Console(highlight=False, theme=theme)
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[
        RichHandler(
            console=console,
            show_path=False,
            highlighter=None,
            rich_tracebacks=True,
            log_time_format="[%X]")]
)

log = logging.getLogger("cortex")

@bot.event
async def on_ready():
    log.info(f'logged in as ur goat {bot.user}')

@bot.slash_command(name="ping", description="pong")
async def hello(ctx: discord.ApplicationContext):
    latency_ms = round(bot.latency * 1000) # wallahi im lowkey tuff????
    await ctx.respond(f"pong! latency: {latency_ms}ms")
    log.info(f"ping command used by {ctx.author} in {ctx.guild.name}")

@bot.slash_command(name="reverse_message", description="reverses a message")
async def reverse_message(ctx: discord.ApplicationContext, message: str):
    reversed_message = ''.join(reversed(message))
    await ctx.respond(f"reversed message: {reversed_message}")
    log.info(f"reverse_message command used by {ctx.author} in {ctx.guild.name}")
    
bot.run(os.getenv("DISCORD_TOKEN"))