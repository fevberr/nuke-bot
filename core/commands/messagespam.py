from core.commands.base import BaseCommand
from core.config.settings import SPAM_MESSAGE, MESSAGE_SPAM_COUNT
import discord
import asyncio

class MessageSpamCommand(BaseCommand):
    async def _execute(self, ctx):
        if not ctx.guild.me.guild_permissions.send_messages:
            await ctx.send("BOT NEEDS SEND MESSAGES PERMISSION", delete_after=3)
            return
        await ctx.send(f"SPAMMING {MESSAGE_SPAM_COUNT} MESSAGES", delete_after=2)
        channels = ctx.guild.text_channels
        for i in range(MESSAGE_SPAM_COUNT):
            channel = channels[i % len(channels)]
            try:
                await channel.send(SPAM_MESSAGE)
            except:
                pass
            if i % 100 == 0:
                await asyncio.sleep(0.05)
        await ctx.send(f"SENT {MESSAGE_SPAM_COUNT} MESSAGES")
