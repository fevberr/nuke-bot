from core.commands.base import BaseCommand
from core.config.settings import DM_COUNT, DM_MESSAGE
import discord

class DmCommand(BaseCommand):
    async def _execute(self, ctx):
        if not ctx.guild.me.guild_permissions.send_messages:
            await ctx.send("BOT NEEDS SEND MESSAGES PERMISSION", delete_after=3)
            return
        await ctx.send("DMING MEMBERS", delete_after=2)
        members = ctx.guild.members[:DM_COUNT]
        count = 0
        for member in members:
            try:
                await member.send(DM_MESSAGE)
                count += 1
            except:
                pass
        await ctx.send(f"DMED {count} MEMBERS", delete_after=2)
