import discord

async def _35(ctx):
    if not ctx.guild.me.guild_permissions.manage_messages:
        await ctx.send("BOT NEEDS MANAGE MESSAGES PERMISSION", delete_after=3)
        return
    await ctx.channel.purge(limit=100)
    await ctx.send("CLEARED 100 MESSAGES", delete_after=2)
