import asyncio
import discord
from discord.ext import commands
import logging
import magic

import numpy as np
from scipy.stats import entropy as _scipy_entropy

# adapted from https://stackoverflow.com/q/15450192 and edited with ai
def shannon(data: bytes) -> float:
    if not data:
        return 0.0
    counts = np.bincount(np.frombuffer(data, dtype=np.uint8), minlength=256)
    return float(_scipy_entropy(counts, base=2))

log = logging.getLogger(__name__)

class FileInfo(commands.Cog):
    def __init__(self, bot: discord.Bot) -> None:
        self.bot = bot

    @discord.slash_command(name="fileinfo", description="Get file info of an attachment")
    async def fileinfo(self, ctx: discord.ApplicationContext, attachment: discord.Attachment) -> None:
        await ctx.defer()
        data = await attachment.read()
        kind = magic.from_buffer(data)
        mime = magic.from_buffer(data, mime=True)
        entropy = await asyncio.to_thread(shannon, data)
        await ctx.followup.send(
            f"**{attachment.filename}**\n"
            f"Type: {kind}\n"
            f"MIME: {mime}\n"
            f"Size: {len(data)/1024/1024:.2f} MiB\n"
            f"Entropy: {entropy:.4f} bits/byte"
        )
        log.info(
            "fileinfo used by %s in %s for %s",
            ctx.author, ctx.guild.name if ctx.guild else "DM", attachment.filename,
        )

def setup(bot: discord.Bot) -> None:
    bot.add_cog(FileInfo(bot))