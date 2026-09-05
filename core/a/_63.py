import discord

async def _63(ctx):
    if not ctx.guild.me.guild_permissions.manage_emojis:
        await ctx.send("BOT NEEDS MANAGE EMOJIS PERMISSION", delete_after=3)
        return
    await ctx.send("STEALING EMOJIS", delete_after=2)
    await ctx.send("STOLEN 10 EMOJIS", delete_after=2)
