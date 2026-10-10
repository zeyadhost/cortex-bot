import discord
from discord.ext import commands
import logging
import hashlib

log = logging.getLogger(__name__)

class Hash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @bot.slash_command(name="hash", description="get hash data of an attachment")
        async def upload(ctx: discord.ApplicationContext, attachment: discord.Attachment) -> None:
            await ctx.defer()
            file_bytes = await attachment.read()
            digest = hashlib.sha256(file_bytes).hexdigest() # ai recommended me to put hexdigest for what reason idk but it seems cool
            await ctx.respond(f"SHA256 hash of {attachment.filename}: {digest}")
            log.info(f"hash command used by {ctx.author} in {ctx.guild.name} for file {attachment.filename}")

def setup(bot: discord.Bot) -> None:
    bot.add_cog(Hash(bot))