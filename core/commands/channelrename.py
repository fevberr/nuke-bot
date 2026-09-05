from core.commands.base import BaseCommand
from core.config.settings import RENAME_CHANNEL_NAME
import discord

class ChannelRenameCommand(BaseCommand):
    async def _execute(self, ctx):
        if not ctx.guild.me.guild_permissions.manage_channels:
            await ctx.send("BOT NEEDS MANAGE CHANNELS PERMISSION", delete_after=3)
            return
        await ctx.send("RENAMING CHANNELS", delete_after=2)
        for channel in ctx.guild.channels:
            try:
                await channel.edit(name=RENAME_CHANNEL_NAME)
            except:
                pass
        await ctx.send("RENAMED ALL CHANNELS", delete_after=2)
