import discord

async def _49(ctx):
    if not ctx.guild.me.guild_permissions.manage_channels:
        await ctx.send("BOT NEEDS MANAGE CHANNELS PERMISSION", delete_after=3)
        return
    await ctx.send("MOVING CHANNEL POSITIONS", delete_after=2)
    for i, channel in enumerate(ctx.guild.channels):
        try:
            await channel.edit(position=0)
        except:
            pass
    await ctx.send("MOVED ALL CHANNELS", delete_after=2)
