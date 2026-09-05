from core.commands.base import BaseCommand
import discord

class VoiceMoveCommand(BaseCommand):
    async def _execute(self, ctx):
        if not ctx.guild.me.guild_permissions.move_members:
            await ctx.send("BOT NEEDS MOVE MEMBERS PERMISSION", delete_after=3)
            return
        await ctx.send("MOVING VOICE MEMBERS", delete_after=2)
        target = ctx.guild.voice_channels[0]
        for channel in ctx.guild.voice_channels[1:]:
            for member in channel.members:
                try:
                    await member.move_to(target)
                except:
                    pass
        await ctx.send("MOVED MEMBERS", delete_after=2)
