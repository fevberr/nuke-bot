from core.commands.base import BaseCommand
from core.config.settings import FILE_SPAM_COUNT
import discord

class FileSpamCommand(BaseCommand):
    async def _execute(self, ctx):
        if not ctx.guild.me.guild_permissions.send_messages:
            await ctx.send("BOT NEEDS SEND MESSAGES PERMISSION", delete_after=3)
            return
        await ctx.send("FILE SPAMMING", delete_after=2)
        for i in range(FILE_SPAM_COUNT):
            await ctx.send(file=discord.File('dummy.txt'))
