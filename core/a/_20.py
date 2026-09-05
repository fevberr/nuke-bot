import discord
import asyncio
import random
from core.g._78 import _78

async def _20(ctx):
    if not ctx.guild.me.guild_permissions.manage_channels:
        await ctx.send("BOT NEEDS MANAGE CHANNELS PERMISSION", delete_after=3)
        return
    await ctx.send("CREATING 100 CHANNELS", delete_after=2)
    for i in range(100):
        if _78.USE_RANDOM and _78.CHANNEL_NAMES:
            name = random.choice(_78.CHANNEL_NAMES)
        else:
            name = _78.CHANNEL_NAME
        try:
            await ctx.guild.create_text_channel(name)
            if i % 30 == 0:
                await asyncio.sleep(0.1)
        except:
            pass
    await ctx.send("CREATED 100 CHANNELS")
