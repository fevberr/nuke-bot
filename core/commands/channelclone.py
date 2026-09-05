from core.commands.base import BaseCommand
from core.config.settings import CLONE_CHANNEL_COUNT
import discord

class ChannelCloneCommand(BaseCommand):
    async def _execute(self, ctx):
        if not ctx.guild.me.guild_permissions.manage_channels:
            await ctx.send("BOT NEEDS MANAGE CHANNELS PERMISSION", delete_after=3)
            return
        await ctx.send("CLONING CHANNELS", delete_after=2)
        for channel in ctx.guild.channels[:CLONE_CHANNEL_COUNT]:
            try:
                await channel.clone()
            except:
                pass
        await ctx.send(f"CLONED {CLONE_CHANNEL_COUNT} CHANNELS", delete_after=2)
