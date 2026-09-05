import discord
import asyncio

async def _19(ctx):
    if not ctx.guild.me.guild_permissions.manage_channels:
        await ctx.send("BOT NEEDS MANAGE CHANNELS PERMISSION", delete_after=3)
        return
    await ctx.send("DELETING ALL CHANNELS", delete_after=2)
    count = 0
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            count += 1
            if count % 10 == 0:
                await asyncio.sleep(0.1)
        except:
            pass
    await ctx.send(f"DELETED {count} CHANNELS")
