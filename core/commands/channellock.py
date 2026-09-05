from core.commands.base import BaseCommand
from core.config.settings import LOCK_BATCH
import discord
import asyncio

class ChannelLockCommand(BaseCommand):
    async def _execute(self, ctx):
        if not ctx.guild.me.guild_permissions.manage_channels:
            await ctx.send("BOT NEEDS MANAGE CHANNELS PERMISSION", delete_after=3)
            return
        await ctx.send("LOCKING ALL CHANNELS", delete_after=2)
        count = 0
        for channel in ctx.guild.channels:
            try:
                overwrite = channel.overwrites_for(ctx.guild.default_role)
                overwrite.send_messages = False
                await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
                count += 1
                if count % LOCK_BATCH == 0:
                    await asyncio.sleep(0.1)
            except:
                pass
        await ctx.send(f"LOCKED {count} CHANNELS")
