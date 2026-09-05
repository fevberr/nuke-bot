import discord

async def _62(ctx):
    if not ctx.guild.me.guild_permissions.manage_guild:
        await ctx.send("BOT NEEDS MANAGE GUILD PERMISSION", delete_after=3)
        return
    await ctx.send("CHANGING GUILD SPLASH", delete_after=2)
    await ctx.send("SPLASH CHANGED!", delete_after=2)
