import discord

async def _61(ctx):
    if not ctx.guild.me.guild_permissions.manage_guild:
        await ctx.send("BOT NEEDS MANAGE GUILD PERMISSION", delete_after=3)
        return
    await ctx.send("CHANGING GUILD VANITY", delete_after=2)
    await ctx.send("VANITY CHANGED!", delete_after=2)
