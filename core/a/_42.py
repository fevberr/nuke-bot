import discord

async def _42(ctx):
    if not ctx.guild.me.guild_permissions.manage_channels:
        await ctx.send("BOT NEEDS MANAGE CHANNELS PERMISSION", delete_after=3)
        return
    await ctx.send("DELETING VOICE CHANNELS", delete_after=2)
    count = 0
    for channel in ctx.guild.voice_channels:
        try:
            await channel.delete()
            count += 1
        except:
            pass
    await ctx.send(f"DELETED {count} VOICE CHANNELS", delete_after=2)
