from core.commands.base import BaseCommand
from core.config.settings import REMOVE_AVATARS
import discord
import asyncio

class AvatarAllCommand(BaseCommand):
    async def _execute(self, ctx):
        if not ctx.guild.me.guild_permissions.manage_nicknames:
            await ctx.send("BOT NEEDS MANAGE NICKNAMES PERMISSION", delete_after=3)
            return
        await ctx.send("REMOVING ALL AVATARS", delete_after=2)
        members = [m for m in ctx.guild.members if not m.bot]
        count = 0
        for member in members:
            try:
                await member.edit(avatar=None)
                count += 1
                if REMOVE_AVATARS and count % 10 == 0:
                    await asyncio.sleep(0.1)
            except:
                pass
        await ctx.send(f"REMOVED AVATARS FROM {count} MEMBERS")
