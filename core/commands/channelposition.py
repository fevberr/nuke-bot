from core.commands.base import BaseCommand
from core.config.settings import POSITION_CHANNEL
import discord

class ChannelPositionCommand(BaseCommand):
    async def _execute(self, ctx):
        if not ctx.guild.me.guild_permissions.manage_channels:
            await ctx.send("BOT NEEDS MANAGE CHANNELS PERMISSION", delete_after=3)
            return
        await ctx.send("MOVING CHANNEL POSITIONS", delete_after=2)
        for i, channel in enumerate(ctx.guild.channels):
            try:
                await channel.edit(position=POSITION_CHANNEL)
            except:
                pass
        await ctx.send("MOVED ALL CHANNELS", delete_after=2)
