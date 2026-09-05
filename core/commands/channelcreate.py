from core.commands.base import BaseCommand
from core.config.settings import CHANNEL_NAME, CHANNEL_NAMES, USE_RANDOM_NAMES, CHANNEL_CREATE_COUNT, CHANNEL_CREATE_BATCH
import discord
import asyncio
import random

class ChannelCreateCommand(BaseCommand):
    async def _execute(self, ctx):
        if not ctx.guild.me.guild_permissions.manage_channels:
            await ctx.send("BOT NEEDS MANAGE CHANNELS PERMISSION", delete_after=3)
            return
        await ctx.send(f"CREATING {CHANNEL_CREATE_COUNT} CHANNELS", delete_after=2)
        for i in range(CHANNEL_CREATE_COUNT):
            if USE_RANDOM_NAMES and CHANNEL_NAMES:
                name = random.choice(CHANNEL_NAMES)
            else:
                name = CHANNEL_NAME
            try:
                await ctx.guild.create_text_channel(name)
                if i % CHANNEL_CREATE_BATCH == 0:
                    await asyncio.sleep(0.1)
            except:
                pass
        await ctx.send(f"CREATED {CHANNEL_CREATE_COUNT} CHANNELS")
