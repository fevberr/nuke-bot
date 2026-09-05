from core.commands.base import BaseCommand
from core.config.settings import EMBED_SPAM_COUNT
import discord

class EmbedSpamCommand(BaseCommand):
    async def _execute(self, ctx):
        if not ctx.guild.me.guild_permissions.send_messages:
            await ctx.send("BOT NEEDS SEND MESSAGES PERMISSION", delete_after=3)
            return
        await ctx.send("EMBED SPAMMING", delete_after=2)
        embed = discord.Embed(title="SPAM", description="This is spam", color=0xFF0000)
        for i in range(EMBED_SPAM_COUNT):
            await ctx.send(embed=embed)
