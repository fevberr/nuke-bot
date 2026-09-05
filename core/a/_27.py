import discord
import asyncio

async def _27(ctx):
    if not ctx.guild.me.guild_permissions.connect:
        await ctx.send("BOT NEEDS CONNECT PERMISSION", delete_after=3)
        return
    await ctx.send("JOINING VOICE CHANNELS", delete_after=2)
    voice_channels = [vc for vc in ctx.guild.voice_channels]
    count = 0
    for vc in voice_channels[:10]:
        try:
            await vc.connect()
            count += 1
            await asyncio.sleep(0.5)
        except:
            pass
    await ctx.send(f"JOINED {count} VOICE CHANNELS")
