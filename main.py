from pathlib import Path
import os
os.environ["PATH"] = os.pathsep.join([
    os.path.join(os.path.dirname(__file__), ".venv", "Lib", "site-packages", "magic", "libmagic"),
    os.environ["PATH"],
])

import logging

from dotenv import load_dotenv
import discord
from rich.console import Console
from rich.logging import RichHandler
from rich.theme import Theme
from rich.highlighter import NullHighlighter

# from services.http import close_session

theme = Theme({
    "logging.level.info": "bold cyan",
    "logging.level.warning": "bold yellow",
    "logging.level.error": "bold red",
    "logging.level.debug": "dim green",
})

load_dotenv()

console = Console(highlight=False, theme=theme)
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[
        RichHandler(
            console=console,
            show_path=False,
            highlighter=NullHighlighter(),
            rich_tracebacks=True,
            log_time_format="[%X]",
        )
    ],
)

logging.getLogger("discord").setLevel(logging.WARNING)
logger = logging.getLogger("cortex")
logging.getLogger("cogs").setLevel(logging.INFO)

COGS_DIR = Path(__file__).parent / "cogs"


class Cortex(discord.Bot):
    async def on_ready(self) -> None:
        logger.info("logged in as %s", self.user)

    def discover_ext(self) -> None:
        for path in sorted(COGS_DIR.glob("*.py")):
            if path.name.startswith("_"):
                continue
            module = f"cogs.{path.stem}"
            try:
                self.load_extension(module)
                logger.info("loaded extension: %s", module)
            except Exception as exc:
                logger.error("failed to load %s: %s", module, exc)

    # async def close(self) -> None:
    #     await close_session()
    #     await super().close()


bot = Cortex()
bot.discover_ext()

if __name__ == "__main__":
    bot.run(os.environ["DISCORD_TOKEN"])