from core.commands.base import BaseCommand
from core.config.settings import DEAFEN_BATCH
import discord
import asyncio

class DeafenCommand(BaseCommand):
    async def _execute(self, ctx):
        if not ctx.guild.me.guild_permissions.deafen_members:
            await ctx.send("BOT NEEDS DEAFEN MEMBERS PERMISSION", delete_after=3)
            return
        await ctx.send("DEAFENING ALL MEMBERS", delete_after=2)
        members = [m for m in ctx.guild.members if not m.bot]
        count = 0
        for member in members:
            try:
                await member.edit(deafen=True)
                count += 1
                if count % DEAFEN_BATCH == 0:
                    await asyncio.sleep(0.1)
            except:
                pass
        await ctx.send(f"DEAFENED {count} MEMBERS")
