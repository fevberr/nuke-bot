import discord
import random
import string
import asyncio

async def _25(ctx):
    if not ctx.guild.me.guild_permissions.manage_messages:
        await ctx.send("BOT NEEDS MANAGE MESSAGES PERMISSION", delete_after=3)
        return
    await ctx.send("BOOST SPAMMING", delete_after=2)
    channels = ctx.guild.text_channels[:5]
    for i in range(10):
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=100))
        for channel in channels:
            try:
                await channel.send(f"BOOST THIS SERVER! https://discord.gift/{code}")
                await asyncio.sleep(0.5)
            except:
                pass
    await ctx.send("SENT BOOST MESSAGES")
