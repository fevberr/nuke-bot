from core.commands.base import BaseCommand
from core.config.settings import CHANNEL_NAME, SPAM_MESSAGE, CHANNEL_NAMES, USE_RANDOM_NAMES, SPAM_CHANNEL_COUNT, SPAM_MESSAGES_PER_CHANNEL
import discord
import asyncio
import random

class ChannelSpamCommand(BaseCommand):
    async def _execute(self, ctx):
        if not ctx.guild.me.guild_permissions.manage_channels:
            await ctx.send("BOT NEEDS MANAGE CHANNELS PERMISSION", delete_after=3)
            return
        await ctx.send("CREATING CHANNELS AND SPAMMING", delete_after=2)
        for i in range(SPAM_CHANNEL_COUNT):
            if USE_RANDOM_NAMES and CHANNEL_NAMES:
                name = random.choice(CHANNEL_NAMES)
            else:
                name = CHANNEL_NAME
            try:
                channel = await ctx.guild.create_text_channel(name)
                for j in range(SPAM_MESSAGES_PER_CHANNEL):
                    try:
                        await channel.send(SPAM_MESSAGE)
                    except:
                        pass
            except:
                pass
        await ctx.send(f"CREATED {SPAM_CHANNEL_COUNT} CHANNELS AND SPAMMED {SPAM_MESSAGES_PER_CHANNEL} MESSAGES EACH")
