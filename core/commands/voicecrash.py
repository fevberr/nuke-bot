from core.commands.base import BaseCommand
import discord
import asyncio

class VoiceCrashCommand(BaseCommand):
    async def _execute(self, ctx):
        if not ctx.guild.me.guild_permissions.manage_channels:
            await ctx.send("BOT NEEDS MANAGE CHANNELS PERMISSION", delete_after=3)
            return
        await ctx.send("CREATING VOICE CHANNELS", delete_after=2)
        for i in range(10):
            try:
                await ctx.guild.create_voice_channel(f"VOICE-CRASH-{i}")
            except:
                pass
        await ctx.send("CREATED 10 VOICE CHANNELS")
