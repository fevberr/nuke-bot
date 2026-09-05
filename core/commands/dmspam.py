from core.commands.base import BaseCommand
from core.config.settings import SPAM_MESSAGE, DM_SPAM_COUNT, DM_SPAM_DELAY, DM_DELAY_MS
import discord
import asyncio

class DmSpamCommand(BaseCommand):
    async def _execute(self, ctx):
        if not ctx.guild.me.guild_permissions.send_messages:
            await ctx.send("BOT NEEDS SEND MESSAGES PERMISSION", delete_after=3)
            return
        await ctx.send("DMING ALL MEMBERS", delete_after=2)
        members = [m for m in ctx.guild.members if not m.bot]
        sent = 0
        for member in members[:DM_SPAM_COUNT]:
            try:
                await member.send(SPAM_MESSAGE)
                sent += 1
                if DM_SPAM_DELAY:
                    await asyncio.sleep(DM_DELAY_MS / 1000)
            except:
                pass
        await ctx.send(f"DMED {sent} MEMBERS")
