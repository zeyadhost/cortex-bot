import discord
from discord.ext import commands
import logging
import hashlib

log = logging.getLogger(__name__)


class Hash(commands.Cog):
    def __init__(self, bot: discord.Bot) -> None:
        self.bot = bot

    @discord.slash_command(name="hash", description="Get hash data of an attachment")
    async def upload(
        self,
        ctx: discord.ApplicationContext,
        attachment: discord.Attachment,
        algorithm: discord.Option(
            str, "hash algorithm to use",
            choices=["sha256", "md5", "sha1", "sha512"],
        ) = "sha256", # pyright: ignore[reportInvalidTypeForm]
    ) -> None:
        await ctx.defer()
        file_bytes = await attachment.read()
        digest = hashlib.new(algorithm, file_bytes).hexdigest()
        await ctx.followup.send(f"Hash of {attachment.filename}: `{digest}`")
        log.info(
            "hash used by %s in %s for %s",
            ctx.author, ctx.guild.name if ctx.guild else "DM", attachment.filename,
        )


def setup(bot: discord.Bot) -> None:
    bot.add_cog(Hash(bot))