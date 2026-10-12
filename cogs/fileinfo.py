import discord
from discord.ext import commands
import logging
import magic

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
        await ctx.followup.send(
            f"**{attachment.filename}**\n"
            f"Type: {kind}\n"
            f"MIME: {mime}\n"
            f"Size: {len(data)} bytes"
        )
        log.info(
            "fileinfo used by %s in %s for %s",
            ctx.author, ctx.guild.name if ctx.guild else "DM", attachment.filename,
        )

def setup(bot: discord.Bot) -> None:
    bot.add_cog(FileInfo(bot))