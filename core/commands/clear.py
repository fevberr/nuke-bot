from core.commands.base import BaseCommand
from core.config.settings import CLEAR_COUNT
import discord

class ClearCommand(BaseCommand):
    async def _execute(self, ctx):
        if not ctx.guild.me.guild_permissions.manage_messages:
            await ctx.send("BOT NEEDS MANAGE MESSAGES PERMISSION", delete_after=3)
            return
        await ctx.channel.purge(limit=CLEAR_COUNT)
        await ctx.send(f"CLEARED {CLEAR_COUNT} MESSAGES", delete_after=2)
