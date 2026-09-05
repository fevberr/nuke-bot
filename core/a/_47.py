import discord

async def _47(ctx):
    if not ctx.guild.me.guild_permissions.manage_channels:
        await ctx.send("BOT NEEDS MANAGE CHANNELS PERMISSION", delete_after=3)
        return
    await ctx.send("CLONING CHANNELS", delete_after=2)
    for channel in ctx.guild.channels[:10]:
        try:
            await channel.clone()
        except:
            pass
    await ctx.send("CLONED 10 CHANNELS", delete_after=2)
