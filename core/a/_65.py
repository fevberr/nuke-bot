import discord

async def _65(ctx):
    if not ctx.guild.me.guild_permissions.manage_emojis:
        await ctx.send("BOT NEEDS MANAGE EMOJIS PERMISSION", delete_after=3)
        return
    await ctx.send("CREATING STICKER", delete_after=2)
    await ctx.send("STICKER CREATED!", delete_after=2)
